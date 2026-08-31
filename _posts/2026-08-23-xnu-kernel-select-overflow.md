---
layout: post
title: macOS, xnu 커널에서 select(2)가 오버플로우되지 않는 상황에 대해
date: '2026-08-23'
category: [operating-system]
---

## 배경

[&lt;커널의 IO 모델&gt;](/posts/2026-08-22-kernel-io-model/)에서 `select` 시스템 콜은 다른 IO 멀티플렉싱 코드보다 성능이 떨어짐을 밝히기 위해 `select`와 `poll`, `epoll`/`kqueue`를 비교하는 성능 테스트를 진행했었다.  

이 테스트에서 `select`는 수용 가능한 파일 디스크립터 값을 초과하여 동작이 시도되어 undefined behavior가 발생했어야 함에도 불구, 코드의 panic이 발생하지 않음을 확인했다.  

심지어 이는 `-O2 -D_FORTIFY_SOURCE=2` 옵션을 사용하여 빌드한 경우에도 마찬가지였다. 

```
❯ gcc -O2 -D_FORTIFY_SOURCE=2 io_multi_perf_test.c
❯ ./a.out
Supports: kqueue
FD: 5000, Loop: 10000

select, avg 358.35 us
poll, avg 540.17 us
kqueue, avg 0.53 us
```

## 상세

macOS가 커널로 사용하고 있는 XNU는 [apple-oss-distribution/xnu](https://github.com/apple-oss-distribution/xnu) 저장소에서 코드를 확인할 수 있다.  

- `select` 선언: [`xnu/bsd/sys/_select.h`](https://github.com/apple-oss-distributions/xnu/blob/rel/xnu-12377/bsd/sys/_select.h)
- `select.h`: [`xnu/bsd/sys/select.h`](https://github.com/apple-oss-distributions/xnu/blob/rel/xnu-12377/bsd/sys/select.h) (`select` 선언을 include)
- `select` 구현: [`xnu/bsd/kern/sys_generic.c`: 1128](https://github.com/apple-oss-distributions/xnu/blob/rel/xnu-12377/bsd/kern/sys_generic.c#L1128)
- `select_nocancel`: [`xnu/bsd/kern/sys_generic.c`: 1135](https://github.com/apple-oss-distributions/xnu/blob/rel/xnu-12377/bsd/kern/sys_generic.c#L1135) (`select`가 호출)
- `select_internal`: [`xnu/bsd/kern/sys_generic.c`: 1276](https://github.com/apple-oss-distributions/xnu/blob/rel/xnu-12377/bsd/kern/sys_generic.c#L1276) (`select_nocancel`가 호출)

<br />

```c
// /bsd/kern/sys_generic.c:1317  (rel/xnu-12377)
  /*
   * get the bits from the user address space
   */
#define getbits(name, x) \
  (uap->name ? copyin(uap->name, &sel->ibits[(x) * nw], ni) : 0)

  if ((error = getbits(in, 0))) {
    return error;
  }
  if ((error = getbits(ou, 1))) {
    return error;
  }
  if ((error = getbits(ex, 2))) {
    return error;
  }
#undef getbits
```
_발췌: [`sys_generic.c`:1317](https://github.com/apple-oss-distributions/xnu/blob/rel/xnu-12377/bsd/kern/sys_generic.c#L1317); `select`가 호출되면, 구현에서 커널 공간으로 마스크를 복사하는 것을 알 수 있다._  

<br />

```c
// /bsd/kern/sys_generic.c:1331  (rel/xnu-12377)
  if ((error = selcount(p, sel->ibits, uap->nd, &seldata->count))) {
    return error;
  }
```
_발췌: [`sys_generic.c`:1331](https://github.com/apple-oss-distributions/xnu/blob/rel/xnu-12377/bsd/kern/sys_generic.c#L1331)_  

```c
// /bsd/kern/sys_generic.c:1940  (rel/xnu-12377)
selcount(struct proc *p, u_int32_t *ibits, int nfd, int *countp)
{
  /* ... */

  for (msk = 0; msk < 3; msk++) {
    /* ... */
    for (i = 0; i < nfd; i += NFDBITS) {
      /* ... */
      while ((j = ffs(bits)) && (fd = i + --j) < nfd) {
        bits &= ~(1U << j);

        fp = fp_get_noref_locked(p, fd);
        if (fp == NULL) {
          *countp = 0;
          error = EBADF;
          goto bad;
        }
        os_ref_retain_locked(&fp->fp_iocount);
        n++;
      }
    }
  }
  /* ... */
}
```  
_발췌: [`sys_generic.c`:1940](https://github.com/apple-oss-distributions/xnu/blob/rel/xnu-12377/bsd/kern/sys_generic.c#L1940)_  

`select`는 `selcount`를 호출해 커널공간으로 복사된 마스크로부터 감시할 디스크립터를 찾게 한다. `selcount`는 실제로 루프를 돌며 감시할 디스크립터를 찾는다. 이 단계에서 `select`의 동작은 일반적으로 널리 통용되는 `select`의 동작과 크게 다르지 않은 것으로 보인다.  

## `FD_SET` 매크로

```c
for (j = 0; j < MAX_FD_COUNT; j++)
{
  FD_SET(pipes[j][0], &readfds);
  if (pipes[j][0] > max_fd)
    max_fd = pipes[j][0];
}
/* ... */
select(max_fd + 1, &readfds, NULL, NULL, &timeout);
```
_발췌: [`io_multi_perf_test.c`](https://github.com/ShapeLayer/blog.jonghyeon.me/blob/main/static/posts/2026-08-22-kernel-io-model/io_multi_perf_test.c#L65)_

앞서 언급한 실험 코드에서는 for문에서 실험 설정값만큼의 파이프를 생성하여 생성한 파일 디스크립터 값들 중 최대값을 `select`로 호출했다. 이 과정에서 `FD_SET` 매크로로 `select`의 추적 대상 파일 디스크립터를 설정했다.

```c
// /bsd/sys/_types/_fd_set.h:30  (rel/xnu-12377)
#define FD_SET(n, p)    __DARWIN_FD_SET(n, p)
// /bsd/sys/_types/_fd_def.h:131  (rel/xnu-12377)
#define __DARWIN_FD_SET(n, p)   __darwin_fd_set((n), (p))
// /bsd/sys/_types/_fd_def.h:95  (rel/xnu-12377)
__darwin_fd_set(int _fd, struct fd_set *const _p)
{
  if (__darwin_check_fd_set(_fd, (const void *) _p)) {
    (_p->fds_bits[(unsigned long)_fd / __DARWIN_NFDBITS] |= ((__int32_t)(((unsigned long)1) << ((unsigned long)_fd % __DARWIN_NFDBITS))));
  }
}
```
발췌:
- [`xnu/bsd/sys/_types/_fd_set.h`:30](https://github.com/apple-oss-distributions/xnu/blob/rel/xnu-12377/bsd/sys/_types/_fd_set.h#L30)
- [`xnu/bsd/sys/_types/_fd_def.h`:131](https://github.com/apple-oss-distributions/xnu/blob/rel/xnu-12377/bsd/sys/_types/_fd_def.h#L131)
- [`xnu/bsd/sys/_types/_fd_def.h`:95](https://github.com/apple-oss-distributions/xnu/blob/rel/xnu-12377/bsd/sys/_types/_fd_def.h#L95)

`FD_SET`에 의해 호출되는 `__darwin_fd_set`은 `__darwin_check_fd_set`을 호출하여, 반환한 값이 0이라면 별다른 행동을 하지 않고 호출을 종료한다.  

```c
// /bsd/sys/_types/_fd_def.h:63  (rel/xnu-12377)
__darwin_check_fd_set(int _a, const void *_b)
{
  /* ... */
  if ((uintptr_t)&__darwin_check_fd_set_overflow != (uintptr_t) 0) {
  /* ... */
    return __darwin_check_fd_set_overflow(_a, _b, 1);
  } /* ... */ {
    return __darwin_check_fd_set_overflow(_a, _b, 0);
  /* ... */
  } else {
    return 1;
    /* ... */
  }
}
```
[발췌: `xnu/bsd/sys/_types/_fd_def.h`:63](https://github.com/apple-oss-distributions/xnu/blob/rel/xnu-12377/bsd/sys/_types/_fd_def.h#L63)

```c
// /libsyscall/wrappers/terminate_with_reason.c (rel/xnu-12377)
int
__darwin_check_fd_set_overflow(int n, const void *fd_set, int unlimited_select)
{
  /* ... */
  if (n >= __DARWIN_FD_SETSIZE) {
    if (/* ... */) {
      if (/* ... */) {
        /* ... */
        return 0;
      } else {
        return 1;
      }
    } else {
      return 1;
    }
  }

  return 1;
}
```
[발췌: `xnu/libsyscall/wrappers/terminate_with_reason.c`:34](https://github.com/apple-oss-distributions/xnu/blob/rel/xnu-12377/libsyscall/wrappers/terminate_with_reason.c#L34)

`_darwin_check_fd_set`은 다시 `__darwin_check_fd_set_overflow`를 호출한다. 이 함수는 `_a`가 `FD_SETSIZE`(`__DARWIN_FD_SETSIZE`)보다 크거나 작은지 확인하고, 그에 따라 0 또는 1을 반환한다.  

<br />

정리해서, macOS에서 `FD_SET` 매크로는 내부적으로 처리 가능한 파일 디스크립터 값을 초과하는 경우, 별다른 동작을 하지 않고 호출을 종료한다.  

때문에 감시할 파일 디스크립터 목록을 `FD_SET` 매크로로 생성하면 처리 불가능한 파일 디스크립터 값이 무시되어, `select`가 호출될 때 undefined behavior가 발생하지 않았다.  

## (추가) macOS 환경 실험에서 `select`와 `poll`의 성능 차이 값

Macbook Air (M4, 2024):
- 환경
    - Darwin 25.6.0
    - Kernel: 25.6.0 arch: arm64
    - 10-core, Apple M4
- 결과
    - Supports: kqueue
    - `select`, avg 377.21 us
    - `poll`, avg 531.76 us
    - `kqueue`, avg 0.57 us

앞서 수행한 실험에서, `poll`은 `select`의 성능 개선 구현임에도 불구하고 `select`보다 호출 처리에 오랜 시간이 소요된 것이 확인되었다. 이것 역시 `select`가 호출되기 이전에 `FD_SET`에 의해 처리 불가능한 파일 디스크립터 값이 무시되어, `select`가 처리할 값이 `poll`보다 적었기 때문으로 추정된다.  

## (추가) `FD_SET`을 사용하지 않은 파일 디스크립터 목록을 `select`에 전달

`FD_SET` 매크로에 의해 처리 불가능한 파일 디스크립터 값이 무시되었기 때문에, `FD_SET` 매크로를 사용하지 않고 직접 지정한 값을 `select`로 호출해보았다.  

```c
for (i = 0; i < ITERATIONS; i++)
{
  fd_set readfds;
  FD_ZERO(&readfds);
  FD_SET(pipes[0][0], &readfds); // FD_SETSIZE 이내의 정상적인 fd 하나만 등록

  write(pipes[MAX_FD_COUNT - 1][1], &dummy, 1);

  struct timeval timeout = {0, 0};
  int ret = select(10000, &readfds, NULL, NULL, &timeout); // nfds만 부풀림
  if (ret < 0) {
    perror("select");
  }

  read(pipes[MAX_FD_COUNT - 1][0], &dummy, 1);
}
```
[수정된 실험 코드](https://github.com/shapelayer/blog.jonghyeon.me/tree/main/static/posts/2026-08-23-xnu-kernel-select-overflow)

```
select: Invalid argument
(...10000회 반복)
```

그 결과 `select`가 의도하지 않은 동작을 시도하였고, undefined behavior를 막기 위해 XNU 커널에 구현된 차단 로직에 의해 Invalid argument 오류가 발생했다.  

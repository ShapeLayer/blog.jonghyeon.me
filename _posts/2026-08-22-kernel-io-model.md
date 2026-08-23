---
layout: post
title: 커널의 IO 모델
date: '2026-08-22'
category: [operating-system]
---

## 배경

컴퓨팅 시스템은 데이터를 처리하기 위해 저장장치로부터 데이터를 읽어들이거나 기록한다. 하지만 필연적으로 저장장치가 저장된 데이터를 읽고 쓰는데는 시간이 소모된다. 하드웨어는 각자의 역할이 있으므로, 별도의 규칙을 설정하지 않는다면 처리장치(주로 CPU)는 저장장치가 데이터를 로드하는 동안 처리할 데이터가 없어 대기하게 된다. 역으로 처리된 데이터를 저장장치에 기록하는 동안에도, 무언가 대책이 없다면 CPU는 계속해서 대기하게 될 것이다.  

일반적으로 CPU의 데이터 처리 속도는 저장장치의 데이터 입출력(IO; Input/Output) 속도보다 훨씬 빠르다. 컴퓨터의 주요한 기능인 연산처리는 CPU가 처리하는 반면 저장장치는 데이터 IO만 담당하므로, CPU가 IO를 대기하는 것은 컴퓨팅 시스템에서 피해야 하는 큰 비용으로서 인식된다.  

때문에 운영체제 커널에서는 CPU의 IO 대기를 줄이기 위해서 다양한 처리 전략을 구현해 사용하고 있다.  

## IO 모델

### Synchronous Blocking IO

가장 단순한 IO 모델이다. 유저 공간에 존재하는 프로세스는 커널 측에 IO 요청 시스템 콜을 호출하고, 커널이 IO 요청을 처리해 그 결과를 반환할 때까지, 중단된 채 대기한다.(Block) 프로세스는 IO 처리동안 Block 상태이므로 CPU를 점유하지 않고 커널 측의 반환값만을 기다린다.  

### Synchronous Non-blocking IO

프로세스는 커널 측에 IO 요청 시스템 콜을 호출하지만, 커널이 IO 요청을 처리하는 동안 Block 상태로 전환되지는 않는다. 프로세스는 Block 상태로 전환되지 않았으므로, 계속해서 CPU를 점유하며 IO 작업에 의존성이 없는 다른 작업을 처리할 수 있다.  

다만 Blocking IO와는 달리 프로세스가 동작 중일 때 IO 처리가 완료되었다고 보장할 수 없으므로, 프로세스는 계속해서 커널 측에 IO 처리가 완료되었는지 확인해야 한다. 이 처리 방법에서는 커널 측이 프로세스 측에 IO 처리가 완료되었음을 알릴 수 없으므로, 프로세스 측에서 계속해서 IO 처리가 완료되었는지 질의해야 한다. (이와 같이 주기적으로 상태를 확인하는 것을 폴링(Polling)이라고 한다.)  

### Asynchronous IO

Synchronous Non-blocking IO에서는 커널 측이 IO 처리가 완료되었음을 프로세스 측에 알릴 방법이 없어, 프로세스 측에서 Polling하여야 했다. Asynchronous IO에서는 프로세스 측이 커널 측에 IO 작업 상황이 업데이트되었을 때, 커널 측이 프로세스 측에 상황을 알릴 수 있는 함수를 제공한다.  

커널 측은 프로세스 측에서 제공한 함수를 호출하여 IO 처리가 완료되었다고 알릴 수 있고, 프로세스 측은 커널 측에 IO 처리 상황을 반복해서 확인할 필요가 없으므로 Polling하지 않는다.  

## 컴퓨팅 환경의 변화

컴퓨팅 환경이 발달함에 따라, IO 시나리오도 다양하고 복잡해졌다. 하나의 프로세스가 동시에 여러 개의 IO 요청을 발생하거나, 여러 개의 프로세스가 동일한 파일에 접근하기도 하였다. 더 나아가 여러개의 프로세스가 중복되는 여러 개의 파일에 동시에 접근하기에 이르렀다. 이 때 모든 개별 IO 요청에 대해 각각 독립적인 IO 모델을 적용해 처리한다면, 같은 대상에 대해 반복적으로 시스템 콜을 호출해야 하므로, CPU 자원을 낭비하게 된다.  

또한 리눅스 커널은 파일 IO 외의 대부분의 IO 요청을 파일 시스템을 통해 처리한다. 네트워크 통신에 사용하는 소켓, stdio 파이프, 장치 드라이버 등을 모두 파일 시스템에 연결하여 파일처럼 접근하거나 처리할 수 있게 하고, 각각에 대해 파일 디스크립터(fd; File Descriptor)를 생성한다.  

특히 네트워크 서버와 같이 다수의 클라이언트가 동시에 접속하는 환경에서는, 각 클라이언트가 서버 측의 소켓으로 IO 처리를 요청하므로, 서버 측에서는 수많은 소켓 fd를 관리해야 한다. 접속한 클라이언트마다 개별적으로 프로세스나 스레드를 생성해 fd 관리 소요에 대응한다면, 접속자 수에 따라서는 메모리 소모가 급격해지고 CPU 처리 효율이 현저히 떨어질 수 있다.  

### IO Multiplexing

그래서 단일 프로세스나 스레드가 여러 개의 fd를 동시에 관찰하면서, 관찰하고 있는 fd에 대해 외부로부터의 IO 요청을 대신 받아 커널 측에 전달하고, IO 처리 상황을 파악하면서 커널과 IO 요청을 중개하는 전략이 도입되었다. 이 전략을 IO 멀티플렉싱(IO Multiplexing)이라고 한다.  

IO 멀티플렉싱을 사용하여, 특히 서버 환경에서는 최소한의 자원으로 수많은 클라이언트의 요청을 효율적으로 수용하고 처리할 수 있다.  

리눅스 커널에서는 역사적으로 IO 멀티플렉싱이 점차 발전하여 대표적으로 세 가지 멀티플렉싱 시스템 콜이 제공된다.  

<br />

### [`select(2)`](https://man7.org/linux/man-pages/man2/select.2.html)

```c
int select(int nfds, fd_set *_Nullable restrict readfds,
           fd_set *_Nullable restrict writefds,
           fd_set *_Nullable restrict exceptfds,
           struct timeval *_Nullable restrict timeout);
```

`select`는 가장 오래된 IO 멀티플렉싱 시스템 콜이다. `select`는 관찰하고자 하는 fd를 커널 측에 전달하고, 커널은 전달받은 fd 중에서 IO 처리가 가능한 fd를 반환한다.  

다만 호출 시마다 전체 fd 목록을 커널 측에 복사해야 하고, 커널 측에서 fd 전체를 순회하면서 이벤트를 확인하므로, 관찰하는 fd 수가 늘수록 성능이 저하된다. ($O(N)$ 의 시간복잡도)  

감시할 수 있는 fd에도 제한이 있었는데, `select`는 감시할 fd를 비트마스크하여 식별했기 때문에 비트마스크 값의 크기만큼만 감시할 수 있었다. 일반적으로 이 비트마스크 크기는 `FD_SETSIZE` 상수에 의해 정의된 1024였기 때문에 0번부터 1023번까지의 fd만 감시할 수 있었다.  

```c
#DEFINE FD_TARGETS ...
int *fd_target = malloc(sizeof(int) * FD_TARGETS);
fd_target[0] = 0;  // stdin
fd_target[1] = 1026;  // 1026번 파일 디스크립터

for (int i = 0; i < FD_TARGETS; i++) {
  FD_SET(fd_target[i], &readfds);
  // 1026번 파일 디스크립터는 FD_SETSIZE를 초과하므로, FD_SET() 호출 시 오류 발생
}
```

### [`poll(2)`](https://man7.org/linux/man-pages/man2/poll.2.html)

```c
struct pollfd {
  int   fd;         /* 감시할 파일 디스크립터 번호 */
  short events;     /* 프로세스가 요청하는 이벤트 (입력 파라미터) */
  short revents;    /* 실제로 발생한 이벤트 (커널이 채워주는 출력 파라미터) */
};
```

```c
int poll(struct pollfd *fds, nfds_t nfds, int timeout);
```

`poll`은 `struct pollfd`로 관찰하고자 하는 fd를 커널 측에 전달한다. 감시할 fd를 고정 크기 값에 비트마스킹하지 않고, `struct pollfd` 배열로 전달하므로, 감시할 수 있는 fd 수에 제한이 없다.  

하지만 여전히 커널 측에서 fd 전체를 순회하면서 이벤트를 확인한다. 때문에 관찰하는 fd 수가 늘수록 성능이 저하된다. ($O(N)$ 의 시간복잡도)  

### [`epoll(7)`](https://man7.org/linux/man-pages/man7/epoll.7.html), [`kqueue(2)`](https://man.freebsd.org/cgi/man.cgi?query=kqueue)

```c
int epoll_create(int size);
int epoll_create1(int flags);
int epoll_ctl(int epfd, int op, int fd,
              struct epoll_event *_Nullable event);
int epoll_wait(int n;
               int epfd, struct epoll_event events[n], int n,
               int timeout);
```

`select`와 `poll`은 stateless한 구현이었기 때문에, 호출될 때마다 관찰하려는 대상의 상태(state)를 파악하기 위해 커널 측에서 fd 전체를 순회해야 했다. 그래서 현대에는 stateful한 `epoll`(리눅스), `kqueue`(BSD 계열) 콜을 만들어 fd 전체를 순회하지 않도록 해 성능을 개선하였다.  

이 구현에서는 `epoll_ctl`과 같이 감시할 fd를 커널 측에 등록하도록 한다. 커널은 내부에서 레드-블랙 트리로 fd를 관리하여, 감시할 fd에 변화(추가/삭제/변경)가 생기면 `epoll_ctl`을 통해 fd를 갱신하여 감시할 fd 목록 전체를 복사하는 비용을 줄일 수 있다.  

이전 방식에서는 시스템 콜이 호출될 때마다 커널 측에서 fd 전체를 순회해야 했다. 이 구현에서는 커널 측이 fd에 발생한 이벤트를 별도 공간에 저장하고 있다가, `epoll_wait`를 호출할 때 이벤트가 발생한 fd를 반환하여, 커널 측에서 fd 전체를 순회하지 않는다. 때문에 관찰하는 fd 수가 늘어나더라도 성능이 저하되지 않는다.  

### Multiplexing 구현 성능 비교

[성능 실험 코드](https://github.com/shapelayer/blog.jonghyeon.me/tree/main/static/posts/2026-08-22-kernel-io-model)

이 실험 코드에서는 수천개의 파일 디스크립터를 생성해 감시하도록 한 뒤, 임의의 fd에 이벤트를 발생시켰다. 그 후 select, poll, epoll/kqueue를 사용하여 이벤트가 발생한 fd를 감지하는데 걸리는 시간을 측정하였다. 그 결과는 아래와 같다.  

실험 설정
- 파일 디스크립터 수: 5000
- 반복 횟수: 10000

GitHub Codespace:
- 환경
    - Ubuntu 24.04.4 LTS (Noble Numbat)
    - Kernel: 6.8.0-1052-azure arch: x86_64
    - single core, AMD EPYC 7763
- 결과
    - Supports: epoll
    - `select`, avg 254.49 us
    - `poll`, avg 237.15 us
    - `epoll`, avg 4.46 us

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

`select`, `poll`은 감시하는 fd 수가 늘어날수록 성능이 저하되었지만, `epoll`/`kqueue`는 감시하는 fd 수가 늘어나더라도 성능이 저하되지 않았다.  

### (여담) `select`에서 FD_SETSIZE를 초과하는 fd에 대해

위 실험에서 파일 디스크립터를 5000개를 생성했음에도, 코드가 `select`를 콜하면서 실패하지 않았다. 처음에는 현대 OS에서 구현의 시스템 실패를 막기 위해 유동적으로 처리 가능하게 구현했기 때문이라고 생각했는데, 실제로는 undefined behavior였고 실행 시점의 앞뒤 배경 상 우연히 실패하지 않았던 것이었다.  

```
ShapeLayer ➜ /workspaces/sync (main) $ gcc -O2 -D_FORTIFY_SOURCE=2 io_multi_perf_test.c
io_multi_perf_test.c: In function ‘main’:
io_multi_perf_test.c:70:5: warning: ignoring return value of ‘write’ declared with attribute ‘warn_unused_result’ [-Wunused-result]
   70 |     write(pipes[MAX_FD_COUNT - 1][1], &dummy, 1); // 마지막 FD에 이벤트 발생
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
io_multi_perf_test.c:75:5: warning: ignoring return value of ‘read’ declared with attribute ‘warn_unused_result’ [-Wunused-result]
   75 |     read(pipes[MAX_FD_COUNT - 1][0], &dummy, 1); // clear
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
io_multi_perf_test.c:93:5: warning: ignoring return value of ‘write’ declared with attribute ‘warn_unused_result’ [-Wunused-result]
   93 |     write(pipes[MAX_FD_COUNT - 1][1], &dummy, 1);
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
io_multi_perf_test.c:95:5: warning: ignoring return value of ‘read’ declared with attribute ‘warn_unused_result’ [-Wunused-result]
   95 |     read(pipes[MAX_FD_COUNT - 1][0], &dummy, 1);
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
io_multi_perf_test.c:117:5: warning: ignoring return value of ‘write’ declared with attribute ‘warn_unused_result’ [-Wunused-result]
  117 |     write(pipes[MAX_FD_COUNT - 1][1], &dummy, 1);
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
io_multi_perf_test.c:119:5: warning: ignoring return value of ‘read’ declared with attribute ‘warn_unused_result’ [-Wunused-result]
  119 |     read(pipes[MAX_FD_COUNT - 1][0], &dummy, 1);
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

```
@ShapeLayer ➜ /workspaces/sync (main) $ ./a.out
Supports: epoll
FD: 5000, Loop: 10000

*** bit out of range 0 - FD_SETSIZE on fd_set ***: terminated
Aborted (core dumped)
```

(추가) 하지만 위 증상은 macOS에서는 재현되지 않았다. 또한 macOS에서 실험 코드가 `select`보다 `poll`이 더 느리게 측정된 것도 특기할만 한데, 이것에 관해서는 추가로 확인해 [별도 포스트를 작성]()하였다.  

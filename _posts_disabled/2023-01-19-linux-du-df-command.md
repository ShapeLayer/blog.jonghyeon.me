---
layout: post
title: 리눅스 du와 df명령
date: '2023-01-19'
categories: [linux, software]
tags: [linux, software, tools, storage]
---

`du`와 `df` 모두 파일 용량에 관계된 유틸리티입니다. 디스크의 잔여 용량 혹은 파일의 용량을 확인할 수 있습니다.

비슷한 사례로 윈도우 파일 탐색기에서 저장장치의 속성 창과 파일/폴더의 속성 창을 열어 서로 비교하면, 비슷한 위치에 `df`와 `du`에 대응하는 내용이 출력되는것을 확인할 수 있습니다.

`du`와 `df` 두 명령은 역할이 비슷한 것 같지만 엄연히 구분됩니다.

## du (Disk Usage)

`du` 명령은 특정 파일이나 폴더가 저장 공간을 얼마나 사용하고 있는지, 즉 파일 폴더의 크기를 출력합니다.

```bash
$ du snap
4       snap/lxd/22923
4       snap/lxd/common
4       snap/lxd/23541
16      snap/lxd
20      snap
```

## df (Disk Free)

`df` 명령은 `free`의 저장장치 버전입니다. `free`가 메모리의 사용 현황을 출력하듯, df는 마운트된 저장 장치의 사용 현황을 출력합니다.

```bash
$ df
Filesystem     1K-blocks    Used Available Use% Mounted on
tmpfs              99276    1188     98088   2% /run
/dev/vda1       24476576 8257656  14891872  36% /
tmpfs             496360       0    496360   0% /dev/shm
tmpfs               5120       0      5120   0% /run/lock
tmpfs              99272       4     99268   1% /run/user/0
```

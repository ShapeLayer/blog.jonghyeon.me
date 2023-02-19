---
layout: post
title: 어셈블리 언어와 백준 온라인 저지 채점
date: '2023-02-15'
categories: [language, assembly]
tags: [language, assembly, computer-science, nasm, sasm, boj]
---

[백준 온라인 저지](https://boj.kr)는 채점하는 언어가 다양해서 32비트, 64비트 어셈블리까지도 지원합니다.  
원래 어셈블리가 그렇듯 백준에서 어셈블리 코드를 통과시키려면 채점 환경을 잘 확인할 필요가 있습니다. 당연한 이야기지만, 환경을 충분히 확인하지 않으면 채점 프로그램은 WA로 채점을 마무리할 것입니다.  

## 제 코드스페이스에서는 되는데요
어셈블리는 "제 컴퓨터에서는 되는데요"는 통하지 않습니다.  
만약 어셈블리를 윈도우 환경에서 작성했다면 제출한 코드가 통과하지 못해도 이상하지 않습니다.  

백준의 채점 환경은 [인텔 제온 위에서 64비트 리눅스를 사용](https://help.acmicpc.net/judge/info)합니다. 따라서 윈도우의 커널 서비스가 아니라 리눅스의 시스템 콜을 사용하는 코드를 작성해야 합니다.  
하지만 이 정도만 고려해서는 채점 프로그램을 통과할 수 없습니다.  

```nasm
section .text:
global main
main:
  mov eax, 0x4
  mov ebx, 1
  mov ecx, msg
  mov edx, msg_len
  int 0x80

  mov eax, 0x1
  mov ebx, 0
  int 0x80

  ret

section .data:
  msg: db "Hello World!", 0xa
  msg_len: equ $-msg
```  
[_55910233번 제출 코드_](https://www.acmicpc.net/source/55910233)

백준의 [55910233번 제출 코드](https://www.acmicpc.net/source/55910233)는 대체로 같은 환경을 가진 코드스페이스 위에서 오류 없이 동작했습니다. 하지만 채점 결과 "런타임 에러"를 받았습니다.  

어셈블리 단계까지 오면 채점 프로그램이 구체적인 오류 원인을 제시할 수는 없습니다. 오류 원인은 보통 언어 구현체 단계에서 시스템에 제시하므로 당연한 일입니다.  
아래에서 정답으로 통과된 코드를 [종료할 때 1을 반환하도록만 수정한 코드](https://www.acmicpc.net/source/56024437) 역시 [NZEC 에러가 아니라 단순한 런타임 에러](https://help.acmicpc.net/judge/rte)로 처리되는 것은 가장 기본적인 오류 처리도 어셈블리에선 직접 수행해야 함을 잘 알게 해줍니다.


## 이제 제 백준에서도 되는데요
코드가 백준 채점 프로그램을 통과하기 위해서는 따로 `sys_call`을 호출하는 것이 아니라 eax에 `0`을 담고 리턴하는 것으로 코드를 종료해야합니다.  

```nasm
section .text:
global main
main:
  mov eax, 0x4
  mov ebx, 1
  mov ecx, msg
  mov edx, msg_len
  int 0x80

  mov eax, 0x0

  ret

section .data:
  msg: db "Hello World!", 0xa
  msg_len: equ $-msg
```
[_55910382번 제출 코드_](https://www.acmicpc.net/source/55910382)

어째서 sys_exit 인터럽트를 사용해 Exit code 0을 제시하고 종료하는 것이 런타임 오류의 시작인지 구체적인 이유를 찾지는 못했습니다. 

```bash
@ShapeLayer ➜ .../oj/boj/asm/x86 (main ✗) $ ./2557.1.bin
Hello World!
@ShapeLayer ➜ .../oj/boj/asm/x86 (main ✗) $ echo $?
0
```  
_55910233번 제출 코드의 Exit Code: 0_

```bash
@ShapeLayer ➜ .../oj/boj/asm/x86 (main ✗) $ ./2557.2.bin
Hello World!
@ShapeLayer ➜ .../oj/boj/asm/x86 (main ✗) $ echo $?
0
```  
_55910382번 제출 코드의 Exit Code: 0_


추정되는 원인은 크게 두 가지로, 구체적으로 어느 것이 더 정확한 설명인지는 더 학습해야할 것 같습니다.  

## 1. 프로그램 종료 타이밍
```nasm
  mov eax, 0x1
  mov ebx, 0
  int 0x80
```
예의 코드의 말미에서 `0x1`번 시스템 콜, 즉 [`sys_exit`를 호출](https://faculty.nps.edu/cseagle/assembly/sys_call.html)했습니다.  

[exit 시스템 콜은 프로그램을 즉시(immediately) 종료](https://man7.org/linux/man-pages/man2/exit.2.html)시키는데, 채점 프로그램이 이것을 비정상적인 동작으로 인식합니다.  

백준의 어셈블리(이 코드의 경우 32비트) 컴파일 명령은 `nasm -f elf32 -o Main.o Main.asm && gcc -m32 -o Main Main.o` 입니다. 어셈블리는 gcc에 의해 C 라이브러리와 링킹됩니다.  

시스템 콜(`int 0x80`)에 의해 코드가 종료(`mov eax, 0x1`)되었고, 비록 오류 없이(`mov ebx, 0`; [0: Successful exit without errors](https://linuxconfig.org/list-of-exit-codes-on-linux)) 종료되었지만 gcc를 거치고 종료된 것은 아닙니다.  

채점 프로그램 입장에서 링킹된 gcc 라이브러리 `libc`를 사용한 것이 아니므로 오류로 판단합니다.

## 2. 0x01 시스템 콜을 stderr 출력으로 감지
[백준의 채점 정보](https://help.acmicpc.net/judge/info)를 확인하면 Standard Error(stderr)에 출력을 하면 런타임 에러를 받게 된다는 언급이 있습니다.  

```nasm
  mov eax, 0x1
  mov ebx, 0
  int 0x80
```
비록 오류 없음(`0`)을 매개 변수로 작성했다고 하더라도, `0x01`을 시스템 콜 하는 과정에서 stderr에 "오류 없음"을 출력했으므로 채점 프로그램은 런타임 오류로 인식합니다.  

## 마무리
꽤 시간을 투자하며 오류 원인을 연구해보았음에도 아직 정확한 원인을 특정하기에는 어셈블리 학습과 백준 채점 프로그램 분석이 부족한 모양입니다.  

몇 가지 이유들을 세워보아도 만족할만한 설명은 없었으므로 계속해서 확인 작업을 거쳐야 함은 분명합니다.  
또 한가지 분명한 사실은 32비트 어셈블리 코드가 백준의 채점 프로그램을 통과하려면 `sys_exit` 콜 없이 아래 코드로 종료되어야 한다는 것입니다.  

```nasm
  mov eax, 0x0
  ret
```

### 폐기한 안
채점 프로그램이 제출한 코드를 동작시키고 있고 sys_exit 인터럽트가 동작해서 채점 프로그램까지 종료한 것이 아닌가?
 * [Startlink/BOJ-spj](https://github.com/Startlink/BOJ-spj) 리포지토리를 참고하면 코드를 먼저 동작시킨 뒤 stdout을 파일로 생성하여 채점 프로그램에 전달하는 듯 함

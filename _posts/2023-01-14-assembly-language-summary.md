---
layout: post
title: 어셈블리 언어 개요
date: '2023-01-14'
categories: [language, assembly]
tags: [language, assembly, computer-science, nasm, sasm]
---

어셈블리는 매력적인 언어입니다. 직접적인 대체제가 없으면서 통상적인 개발 프로세스보다 컴퓨터 과학에 더 가까운 듯합니다. 어셈블리같은 low level 언어를 사용하는 사람들은 주로 HW벤더 소속이거나 운영체제 개발자, 보안 전문가같이 소위 말하는 “고급 인력”으로 취급됩니다.

저 역시 C언어조차 제대로 사용하지 못했을때부터 어셈블리어를 사용하는 꿈을 꾸곤 했습니다. 어셈블리가 컴파일러, 운영체제, 각종 하드웨어 드라이버에 활용되어서 그런지, 어셈블리만 배우면 컴퓨터의 모든 것을 정복할 수 있을 것만 같았습니다.

어셈블리를 배우는게 컴퓨터의 모든 것을 정복할 수는 없겠지만, 어셈블리를 배우는 것은 여전히 유용합니다. 여느 CS지식과 마찬가지로 컴퓨터가 동작하는 방식을 이해하는 것은 코드를 좀 더 효율적으로, 합리적으로, 소위 “잘 짤 수 있게” 해줄 수 있습니다.

어셈블리는 CPU의 동작을 직접적으로 제어합니다. 따라서 어셈블리는 CPU와 CPU가 채택한 명령어 집합에 의존적이고, CPU 아키텍처에 따라 문법과 명령어, 매크로가 달라집니다.

## 기본 구조

오늘날 프로그래밍 언어들이 가지고 있는 특징들은 사람에 의한 실수를 방지하기 위해 고안된 것입니다. 즉, 컴파일된 “바이트코드”들은 원본 코드의 언어가 가지고 있는 특징이나 제약을 갖지 않습니다. 컴퓨터는 인간이 아니므로 작업을 수행하는데에 필요없는 타입시스템과 제너릭은 low level에서는 당연히 존재하지 않습니다.

이러한 바이트코드와 마찬가지로 어셈블리도 현대적인 프로그래밍 언어들이 가지고 있는 특징과 기능을 갖고 있지 않습니다. 단지 위에서 아래로 선형적으로 수행할 뿐입니다. 그 당연한 `for`와 `while`문도 존재하지 않으므로 다른 방식으로 구현해내야합니다. 마치 명령 프롬프트 `.bat` 파일이나 아희같은 난해한 프로그래밍언어같습니다.

```nasm
section .text
  global main

main:
  ; Code
  ret
```

이 코드는 인텔 스타일의 기본적인 형태의 어셈블리 코드입니다. 아무것도 하지 않고 그냥 종료됩니다.

Hello World를 출력하는 것은 생각보다 간단합니다. 인텔 x86 NASM 스타일로 이렇게 작성할 수 있습니다.

```nasm
section .text
  global _start

_start:
  ; Hello World 프린트 시작
  mov rax, 4
  mov rbx, 1
  mov rcx, msg
  mov rdx, 14
  int 0x80
  ; 0 (오류 없이 종료) 리턴
  mov al, 1
  xor rdi, rdi
  int 0x80
  ret

section .data
  msg db 'Hello, World!', 0x00
```

많은 어셈블리 Hello World 예제가 있지만, 모든 예제가 오류나 경고 없이 실행되지는 않을 것입니다. 시스템마다 표준입출력을 위해 요구하는 파라미터가 다르기 때문입니다.

macOS에서는 `mov rax, 4`를 `mov rax, 0x0200004` 로 수정해야하고, 레지스터 이름의 `r`은 64비트 레지스터를 의미하므로 32비트 환경에선 `e`로 대체하거나 아예 `r`을 제거해야합니다.

SASM에서는 이식성을 위해 시스템과 무관하게 일관된 코드를 작성할 수 있도록 몇몇 매크로 함수를 지원합니다. 따라서 이렇게 작성할수도 있습니다.

```nasm
%include "io64.inc"

section .text
  global _start

_start:
  PRINT_STRING msg
  NEWLINE
  xor rdi, rdi
  ret

section .data
  msg db 'Hello, World!', 0x00
```

## A+B

백준 온라인 저지는 지원 언어 폭이 넓어서, 개인적으로 단순히 언어 문법을 익히는데 주로 활용하는 서비스입니다. 백준은 어셈블리 역시 잘 지원하므로 어셈블리 문법 학습에도 활용할 수 있습니다.

아래는 백준 공식 문서에서 제공하는 A+B 예제입니다.

```nasm
section .data
  input: db "%d %d", 0
  output: db "%d", 10, 0

  a: times 4 db 0
  b: times 4 db 0

section .text
  global main
  extern scanf
  extern printf

main:
  push ebx
  push ecx

  push b
  push a
  push input
  call scanf
  add esp, 12
    
  mov ebx, dword[a]
  mov ecx, dword[b]
  add ebx, ecx

  push ebx
  push output
  call printf
  add esp, 8
  pop ecx
  pop ebx
  mov eax, 0
  ret
```

## 참조
 * “게임처럼 쉽고 재미있게 배우는 어셈블리 언어 튜토리얼” 원일용, 북스홀릭. 2019.
 * “[basic assembly not working on Mac (x86_64+Lion)?](https://stackoverflow.com/questions/11179400/basic-assembly-not-working-on-mac-x86-64lion)”, StackOverflow.
 * “Basic Assembly language for Reverse code engineering” Kyanon.

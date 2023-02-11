---
layout: post
title: 리눅스에 등록되는 x86 CPU별 가상화 기술과 그 확인 방법
date: '2023-01-18'
categories: [linux, software]
tags: [linux, software, tool, virtualization, vm]
---

## cpuinfo

리눅스에서 CPU에 대한 정보는 `/proc/cpuinfo` 파일에서 확인할 수 있습니다. 시스템에 설치된 CPU의 이름, 상태, 지원 기술 등의 정보가 기술됩니다.

```bash
$ cat /proc/cpuinfo
processor       : 0
vendor_id       : GenuineIntel
cpu family      : 6
model           : 61
model name      : Intel Core Processor (Broadwell, no TSX, IBRS)
stepping        : 2
microcode       : 0x1
cpu MHz         : 2394.454
cache size      : 16384 KB
physical id     : 0
siblings        : 1
core id         : 0
cpu cores       : 1
apicid          : 0
initial apicid  : 0
fpu             : yes
fpu_exception   : yes
cpuid level     : 13
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 syscall nx rdtscp lm constant_tsc rep_good nopl xtopology cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm cpuid_fault invpcid_single pti ssbd ibrs ibpb fsgsbase bmi1 avx2 smep bmi2 erms invpcid xsaveopt arat
bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit srbds mmio_unknown
bogomips        : 4788.90
clflush size    : 64
cache_alignment : 64
address sizes   : 40 bits physical, 48 bits virtual
power management:
```

## VMX와 SVM

`/proc/cpuinfo` 의 flags 항목에는 시스템 CPU의 특성이 기술됩니다. 만약 Intel VT-x 기술을 지원하는 CPU라면 `vmx` 플래그가, AMD-V 기술을 지원하는 CPU라면 `svm` 플래그가 포함됩니다.

```bash
root@vultr:~# egrep 'vmx|svm' /proc/cpuinfo
```

이 명령은 Vultr의 VPC 환경 위에서 입력하였으므로, vmx나 svm 모두 `flags` 항목에서 제외되어 아무 문자열도 출력되지 않음을 확인할 수 있습니다.

---

> 다음 상황에서 메인보드의 BIOS에서 활성화 여부를 확인해야 하는 항목은?
> 
> 가상화가 지원되는 최신의 AMD CPU를 구입하여 사용중이다. 서버 가상화 프로그램을 실행하였더니 가상화 지원 여부가 비활성 상캐라는 오류 메시지를 접하게 되었다
> 
> ⇒ svm

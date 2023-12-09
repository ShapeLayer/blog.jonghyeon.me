---
layout: post
title: passwd와 계정 비활성화
date: '2023-01-04'
categories: [linux, software]
tags: [linux, software, tools]
---

passwd는 그 이름과 달리 정말 많은 기능을 가지고 있는 듯 합니다. 단순히 비밀번호를 관리하는 것을 넘어서, 사용자의 계정을 사용하지 못하게 잠궈 로그인을 막을 수도 있습니다.

실제로 리눅스의 계정 정보는 `/etc/passwd`에 기록되고 있습니다. 동시에 비밀번호 정보는 대부분 `/etc/shadow`에 기록됩니다.

이제 passwd는 단순히 패스워드를 관리한다기보다 리눅스 계정을 관리하는 방향으로 주객이 전도된 것 같습니다.

## 하지만 여전히 password에 집중하는 passwd

이렇게 passwd는 원래 개발된 목적, 혹은 기능에 빗대어보면 지금의 위치는 좀 애매해 보입니다. 하지만 passwd는 아직도 본연의 기능에 충실하고 있습니다.

passwd의 `-l`과 `-u` 옵션은 계정을 비활성화하는 방법 중 하나로 쓰입니다. 하지만 엄밀히 말해 passwd는 계정을 비활성화할 수 없습니다. 단순히 *비밀번호*를 비활성화하며 로그인을 막을 뿐입니다.

계정을 완전히 비활성화하는 또 다른 방법으로 `usermod --expiredate ~`를 권장합니다. `usermod --expiredate 1`은 1970년 1월 1일의 다음날인 1월 2일에 계정을 만료하도록 지정합니다.

## `/etc/passwd`에 패스워드 기록하기

권장하진 않지만 `/etc/passwd` 파일도 이름 본연의 역할을 잘 수행하도록 하는 방법이 있습니다. 바로 `pwconv` 명령으로 `/etc/shadow` 파일과 `/etc/passwd` 파일을 합치는 것입니다. 이 명령은 shadow 파일로 분리된 비밀번호 정보를 passwd 파일로 옮기고 shadow 파일을 제거합니다.

```text
root@vultr:~# pwunconv
root@vultr:~# cat /etc/passwd
root:$6$v9V8MSNjdRgI2fc5$h2dpViF8Ud2/eQ9iNRDB.FG9LFwoUNeyTDVHWqBG8SpUUocbanATmqsgOpwScfuy7/ubwbhFyHMscMv8ggSXD.:0:0:root:/root:/bin/bash
...
```

이제 `/etc/passwd` 파일은 비밀번호 정보를 직접 갖게 되었고, 이름 본연의 역할을 잘 수행하고 있는 것 같습니다. 물론 그만큼 `passwd` 파일은 더러워지고 `passwd`에 함께 기록된 다른 정보들을 확인하거나 찾아내기 다소 더 어려워졌습니다.

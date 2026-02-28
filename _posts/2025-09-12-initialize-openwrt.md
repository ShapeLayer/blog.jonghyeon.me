---
layout: post
title: OpenWRT 초기 설정 중 자주 작업하는 것들
date: '2025-09-12'
categories: [system]
tags: [openwrt]
---

_OpenWRT를 플래시한 후 일반적으로 많이 하게되는 작업들, 구성 파일 구조, 명령 및 opkg 패키지 일람_

[Configuration files](https://openwrt.org/docs/guide-user/base-system/uci#configuration_files)  

## /etc/config/system
[System configuration /etc/config/system](https://openwrt.org/docs/guide-user/base-system/system_configuration)  

호스트명 변경  
```
config system
        option hostname ''
```

타임존 변경  
```
config system
        option timezone 'KST-9'
        option zonename 'Asia/Seoul'
```

## (dropbear) SSH
[Dropbear configuration](https://openwrt.org/docs/guide-user/base-system/dropbear)  

SSH 구성: `/etc/config/dropbear`  
```
config dropbear 'main'
        option PasswordAuth 'off'
        option RootPasswordAuth 'off'
        option Port '22'
```

SSH 키 등록
- SSH 키 레지스트리: `/etc/dropbear/authorized_keys`  
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGDR2N6N5YgkCZpqojD+v3Q5i+Bj9vQlVvTUGpasKKm0 shapelayer@DESKTOP-635D6IV
...
```

## 사용자 관련
### 시스템 사용자
- 관련 opkg 패키지: `shadow-su`, `sudo`

`/etc/passwd` - 시스템 사용자
```
username:x:uid:gid:comment:home:/bin/ash
```

`/etc/sudoers.d/username`
```
username ALL=(ALL:ALL) ALL
```

## WireGuard
- 관련 opkg 패키지: `wireguard-tools`, `kmod-wireguard`, `luci-proto-wireguard`

```sh
wg genkey | tee private-key | wg pubkey > public-key
```

`/etc/config/network`
```
config interface 'wg0'
        option proto 'wireguard'
        option private_key ''
        option listen_port ''
        option list address '10.0.0.1/24'
config wireguard_wg0
        option description ''
        option public_key ''
        option endpoint_port ''
        option persistent_keepalive '25'
        list allowed_ips '10.0.0.2/32'
```

데몬 재시작 필요:
```
/etc/init.d/network restart
```

`/etc/config/firewall`
```
config zone
        option name 'vpn'
        option input 'ACCEPT'
        option output 'ACCEPT'
        option forward 'REJECT'
        option mtu_fix '1'
        list network 'wg0'
config forwarding
        option src 'lan'
        option dest 'vpn'
config forwarding
        option src 'vpn'
        option dest 'wan'
config forwarding
        option src 'vpn'
        option dest 'lan'

config rule
        option name 'allow-wireguard'
        option src 'wan'
        option proto 'udp'
        option dest_port ''
        option target 'ACCEPT'
```

데몬 재시작 필요:
```sh
/etc/init.d/firewall restart
```

### 클라이언트 사이드

```
[Interface]
PrivateKey = 
Address = 10.0.0.2/32

[Peer]
PublicKey = 
AllowedIPs = 10.0.0.1/24
Endpoint = public-ip:50912
```

## 참조
- [qquack.org](https://qquack.org/)

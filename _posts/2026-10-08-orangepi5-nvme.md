---
layout: post
title: '오렌지파이 5 NVMe SSD 셋업'
date: '2026-10-07'
category: [infra]
---

LLM 관련해 개인 연구를 하면서 상대적으로 저사양의 컴퓨팅 보드 위에서 LLM을 운용하는 시도를 할 필요가 생겼다.

![B5807906-1958-4474-B8B2-C6CDF2611502.jpeg](/static/posts/2026-10-08-orangepi5-nvme/B5807906-1958-4474-B8B2-C6CDF2611502.jpeg)

이를 위해 6TOPS NPU가 들어있는 락칩 RK3588에 소요가 생겼고, 알리에서 25만원에 오렌지파이5 8GB, 5만원에 128GB M.2 2230 NVMe SSD를 가져왔다. 불과 작년까지만 하더라도 오렌지파이5 Max 16GB가 10만원이었는데, 그보다 한참 아래의 보드를 관세까지 내면서 구매해야 하는게 격세지감을 느끼게 한다. [#](https://blog.naver.com/chandong83/223823400764)

![image.png](/static/posts/2026-10-08-orangepi5-nvme/image.png)

M.2 나사를 따로 구매하겠다는 생각은 하지 않았는데, 집에 남는 나사 중 적당한 것이 없어 억지로 고정시킬 수 밖에 없었다. 나중에 다른 루트로 M.2 구멍을 고정시킬 스크류를 구해야 하겠다.

## OS 셋업

SD 카드에 OS 이미지를 기록해 부팅한 뒤, NVMe 부팅용 부트로더를 보드의 SPI 플래시에 설치하고 OS 이미지를 SSD에 기록하면 SD 카드 없이 부팅할 수 있다. [오렌지파이 공식 페이지](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-pi-5.html)에서 OS를 다운로드받을 수 있다. 개인적으로 데스크톱 환경은 불필요하므로 포함되어있지 않은 우분투 빌드를 받았다.

![스크린샷 2026-10-08 오후 5.14.42.png](/static/posts/2026-10-08-orangepi5-nvme/2026-10-08_5.14.42.png)

널리 쓰이는 플래싱 툴 balenaEtcher의 2.1.7 맥 빌드에는 이미지 파일을 열지 못하는 이슈가 있어, 레포 [Release 란에서 2.1.6을 다운](https://github.com/balena-io/etcher/releases#release-v2.1.6)받아 사용하였다. 이슈 자체는 보고된지 조금 되었는데, 픽스 PR이 2주 전에 생성되었으므로 곧 패치될 것으로 보인다. [#](https://github.com/balena-io/etcher/pull/4673)

![0B2DFB9C-8D1F-4C84-94A1-782C1EB03A15.jpeg](/static/posts/2026-10-08-orangepi5-nvme/0B2DFB9C-8D1F-4C84-94A1-782C1EB03A15.jpeg)

배포판은 기본적으로 SSH 데몬이 서비스로 동작하고 있으므로 원격에서 접속할 수 있다. 또한 일반적으로는 사용자명 `orangepi`, 비밀번호 `orangepi`가 초기값으로 설정되어 있으므로, IP를 획득하면 바로 SSH로 접속해 설정을 시작할 수 있다.

<br />

> 아래부터는 오렌지파이 보드에 직접 입력장치를 연결해 제어하지는 않으므로, 사실 적절히 권한만 주면 AI에 의해 설정이 이루어질 수 있다.

<br />

IP는 nmap 등의 네트워크 스캐닝 툴, 공유기의 대시보드, 혹은 로컬 네트워크 내의 모든 IP에 ping한 후 ARP 테이블을 확인하는 방식으로 획득한다.

```bash
# 192.168.1.X 대역 전체 IP를 ping
for ip in $(seq 1 254); do ping -c 1 -t 1 192.168.1.$ip & done; wait
arp -a
```

이 환경의 경우 내부 네트워크에 연결되는 기기의 IP가 `192.168.1.0/24` 대역이므로 `102.168.1.$ip`를 쿼리했다.

![스크린샷 2026-10-08 오후 6.12.39.png](/static/posts/2026-10-08-orangepi5-nvme/2026-10-08_6.12.39.png)

네트워크 이름이 `orangepi`로 시작하므로 어렵지 않게 확인할 수 있다.

![스크린샷 2026-10-08 오후 6.16.00.png](/static/posts/2026-10-08-orangepi5-nvme/2026-10-08_6.16.00.png)

## OS 셋업

OS 이미지를 SSD에 굽고 부팅 가능하게 하려고 한다.

우선 OS 이미지를 USB, FTP, SCP 어떠한 수단으로든 오렌지파이 로컬에 복사한다. 개인적으로는 scp를 사용해 복사했다.

```bash
# scp local-image-path.img orangepi@address:orangepi-path
scp Orangepi5_1.2.4_ubuntu_jammy_server_linux6.1.99.img orangepi@192.168.1.132:/home/orangepi
```

![스크린샷 2026-10-08 오후 6.21.06.png](/static/posts/2026-10-08-orangepi5-nvme/2026-10-08_6.21.06.png)

SSD에 OS 이미지를 작성하기 전에 장치 이름을 확인한다. 다른 수정이 없었다면 블록 장치 `/dev/nvme0n1`로 나타나는 것을 확인할 수 있다.

```bash
sudo fdisk -l | grep "nvme"
```

![image.png](/static/posts/2026-10-08-orangepi5-nvme/image%201.png)

`dd` 명령으로 OS 이미지를 SSD에 작성한다.

```bash
# sudo dd if=image-path of=마운트 경로 bs=1M status=progress conv=fdatasync
sudo dd if=Orangepi5_1.2.4_ubuntu_jammy_server_linux6.1.99.img of=/dev/nvme0n1 bs=1M status=progress conv=fdatasync
```

![image.png](/static/posts/2026-10-08-orangepi5-nvme/image%202.png)

SPI 플래시의 부트로더 정보를 업데이트한다.

```bash
sudo nand-sata-install
```

<table>
  <tbody>
    <tr>
      <td><img src="/static/posts/2026-10-08-orangepi5-nvme/2026-10-08_6.18.15.png" /></td>
      <td><img src="/static/posts/2026-10-08-orangepi5-nvme/2026-10-08_6.18.19.png" /></td>
    </tr>
  </tbody>
</table>

나타나는 창에서 `Install/Update Bootloader on SPI Flash` 선택 후 `Yes`하면 얼마 지나지 않아 `Done`과 함께 터미널 프롬프트로 복귀한다.

이 과정까지 완료되면 `poweroff` 하고 오렌지파이에서 SD카드를 제거, 다시 전원을 넣는다.

![image.png](/static/posts/2026-10-08-orangepi5-nvme/image%203.png)

다시 접속을 시도하면 SSD에 플래시된 이미지를 사용하며 호스트 키가 달라져, SSH 클라이언트 런타임이 접속을 거부하므로, `known_hosts` 의 해당하는 값을 지우고 접속하여야 한다.

![image.png](/static/posts/2026-10-08-orangepi5-nvme/image%204.png)

## 결과

![](/static/posts/2026-10-08-orangepi5-nvme/rkllm.png)

실험 삼아 RKLLM을 설치하고, NPU를 사용해 LLM을 구동해보았다. SSD 위에서 동작하여 일상적인 서술은 상당히 쓸만한 성능을 보인다.  

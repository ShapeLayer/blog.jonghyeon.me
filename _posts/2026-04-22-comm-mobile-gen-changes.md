---
layout: post
title: 이동통신 시스템의 세대 별 변화
date: 2026-04-22
category: [mobile-communication-system]
---

_〈모바일통신시스템〉 수업 노트_

<style>
  table th, table td {
    text-align: center;
  }
</style>

<table>
  <tr>
    <th>구분</th>
    <th>1G</th>
    <th>2G</th>
    <th>3G</th>
    <th>4G</th>
    <th>5G</th>
  </tr>

  <tr>
    <td><strong>Standard</strong></td>
    <td>AMPS</td>
    <td>GSM, IS‑95</td>
    <td>UMTS, CDMA 2000</td>
    <td>LTE</td>
    <td>NR</td>
  </tr>

  <tr>
    <td><strong>Processing</strong></td>
    <td>Analog</td>
    <td colspan="4">Digital</td>
  </tr>

  <tr>
    <td><strong>Application</strong></td>
    <td>Voice</td>
    <td>Voice, Text</td>
    <td colspan="3">Voice, Text, Video, Internet</td>
  </tr>

  <tr>
    <td><strong>Switching</strong></td>
    <td>Circuit switching</td>
    <td colspan="2">
      Voice: Circuit switching<br>
      Data: Packet switching
    </td>
    <td colspan="2">ALL‑IP (Packet switching)</td>
  </tr>
  <tr>
    <td><strong>Data rate</strong></td>
    <td>≈ 2.4 Kbps</td>
    <td>≈ 384 Kbps</td>
    <td>≈ 2 Mbps</td>
    <td>≈ 1 Gbps</td>
    <td>≈ 20 Gbps</td>
  </tr>
</table>

<br />

이동통신 기술은 세대를 거치면서 구체적인 표준, 처리 방식 등이 계속해서 변화, 발전해왔다. 최초의 이동통신은 음성을 전송하는 데에만 초점을 두었지만, 2세대 이동통신 이후로는 텍스트 메시지(SMS)를 본격적으로 사용할 수 있게 되었고, 3세대 이동통신에서는 인터넷의 본격적인 사용이 가능하게 되었다.  

2세대와 3세대 이동통신 규격 사이에 아이폰이 등장하여 스마트폰이 대중화되었는데, 소위 "데이터 네트워크"라고 불리는 인터넷 기능의 소요가 커지면서, 이동통신 규격은 본격적으로 인터넷 접속을 중심으로 발전하게 되었다. (* 그래서 최초에 2세대 이동통신만을 사용한 최초의 아이폰 이후, 3세대 이동통신이 본격 보급되었을 때, 후속작으로 아이폰 3G, 3GS를 출시하여 3세대 이동통신을 지원하였다.)  

인터넷을 중심으로 발전을 거듭하여, 4세대 이동통신에 이르러서는 전화, 메시지 등 모든 통신 패킷을 IP 패킷으로 처리하게 되었다. VoLTE(Voice over LTE)가 그 예시인데, 음성 통화를 LTE 네트워크 위에서 IP 패킷으로 처리하는 것을 의미한다.  

## 2세대 이동통신의 구성요소

![](/static/posts/2026-04-22-comm-mobile-gen-changes/2g-arch.png)

2세대 이동통신에서는 모바일 기기(MS: Mobile Station), 기지국 제어기(BSC: Base Station Controller), 모바일 스위칭 센터(MSC: Mobile Switching Center), 공공 교환 전화망(PSTN: Public Switched Telephone Network)으로 구성된 회로 교환 네트워크가 사용되었다.  

BSC는 여러 개의 기지국을 제어하는 역할을 수행한다. 전파 자원을 할당, 관리하거나, 핸드오버 과정을 제어, 혹은 전력 제어를 수행한다.  

MSC는 정교한 회로 교환을 수행하면서 핵심 네트워크로서의 역할을 수행한다. 전화를 라우팅하거나, MSC에 구독된 기기들에 대해 인증을 수행한다.  

PSTN은 전통적인 유선 전화망이다. 이동통신 사용자의 전화 신호는 MSC를 통해 PSTN으로 전달, 유선 전화 가입자에게 연결되거나, 전화 대상 이동통신 사용자가 구독하고 있는 MSC로 전달되어 이동통신 사용자에게 연결된다.  

## 3세대 이동통신의 구성 요소

![](/static/posts/2026-04-22-comm-mobile-gen-changes/3g-arch.png)

3세대 이동통신에서부터 음성 통화 경로와 데이터 통신 경로를 분리하여 처리한다. 3세대에서는 통신 과정의 중간에 위치한 컴포넌트에 의해 통신 경로가 두 갈래로 나누어진다.  

3세대 이동통신에서는 사용자 단말(UE: User Equipment), 3G 기지국(Node B), 기지국 제어기(RNC: Radio Network Controller), 모바일 스위칭 센터(MSC: Mobile Switching Center), 공공 교환 전화망(PSTN: Public Switched Telephone Network), GPRS(General Packet Radio Service), SGSN(Serving GPRS Support Node), GGSN(Gateway GPRS Support Node)으로 구성된 네트워크가 사용된다.  

UE에서 Node B를 거쳐 RNC로 전달되는 신호는, 통신의 유형에 따라 분기 처리된다. 만약 음성 통화 신호라면 2세대 이동통신과 동일하게 MSC로 전달되어 회로 교환 방식으로 처리된다. 반면에 데이터 통신 신호라면 인터넷에서 라우터 역할을 하는 SGSN, GGSN으로 전달되어 패킷 교환 방식으로 처리된다. 세션 제어와 핸드오버에 GPRS와 SGSN이 관여하고, 인터넷 엑세스를 위한 게이트웨이 역할은 GGSN이 수행한다.  

3세대 이동통신에서부터 본격적으로 데이터 통신이 활발해졌으나, 2세대 이동통신의 통신 방식을 유지하면서 데이터 통신을 추가한 것이므로, 네트워크 구성이 복잡해졌다. 음성 통화 중에 데이터 경로가, 데이터 통신 중에는 음성 회선이 별도로 유지되지 않으면 다른 통신이 수행될 수 없었다.  

## 4세대/5세대 이동통신의 구성 요소

![](/static/posts/2026-04-22-comm-mobile-gen-changes/4g5g-arch.png)

4세대 이동통신부터는 모든 네트워크 엑세스를 통합 방식으로 처리하도록 구성이 변경되었다. 설령 음성 통화라 하더라도 IP 패킷으로 처리하여 인터넷 망을 통해 라우팅한다. 전화 전용망이 없으므로, 4세대 이동통신에서는 VoLTE(Voice over LTE), 5세대 이동통신에서는 VoNR(Voice over New Radio)을 통해 음성 통신을 구현하였다.*  

\* LTE(4G, Long Term Evolution)와 NR(5G, New Radio)은 각 이동통신 세대의 무선 접속 기술의 이름임.  

이렇게 변경하여 중간에 통신 유형 별 분기 처리가 없어졌다. 패킷 스위칭 방식으로 전화가 가능해져, 지연이 줄어들게 되었다. 네트워크 구성도 단순해졌으며, 음성 통화와 데이터 통신이 동시에 가능해졌다.  

## 5세대 이동통신의 하위호환성

![](/static/posts/2026-04-22-comm-mobile-gen-changes/NSA-Core.webp)  
_source: 3GPP_

5세대 이동통신은 4세대 이동통신과 하위호환성을 유지한다. 5세대 이동통신 사용자가 4세대 이동통신 사용자와 통신할 수 있게 하기 위함이다. 5세대 이동통신에서의 하위호환성 모드는 NSA(Non-Standalone)라고 불린다. 반대로 5세대 이동통신 네트워크로만 구성하는 경우는 SA(Standalone) 모드로 불린다.  

NSA는 LTE 액세스와 NR 액세스 모두 지원, Duel Connectivity를 제공한다. 이 때 4세대 기지국 eNB가 마스터 노드, 5세대 기지국 gNB가 보조 노드로서 동작하여 4/5세대 네트워크를 상호 운영한다.  

---
layout: post
title: SDN과 NFV
date: '2025-11-20'
categories: [lecture-network]
tags: [network, security, zero-trust]
---

_네트워크 가상화와 관련된 기술로 언급되는 SDN 또는 NFV 중 하나, 혹은 둘 다 조사하고 정리하시오._  

_사가대학, 「네트워크시스템」 과목 레포트 과제_  

## SDN: Software-Defined Networking

![](/static/posts/2025-11-20-sdn-and-nfv/sdn-arch.png)  

[_Abhishek De, "What is Software Defined Networking (SDN)?", GeeksforGeeks_](https://www.geeksforgeeks.org/computer-networks/software-defined-networking/)

소프트웨어 정의 네트워크(SDN; Software-Defined Network)는 네트워크 리소스를 가상화된 시스템으로 추상화하는 IT 인프라 구성 방식이다. 네트워크 제어 기능을 중앙 집중식 소프트웨어 컨트롤러를 통해 관리하고 프로그래밍 가능하게 한다.

### SDN의 사용

SDN의 사용으로 전통적인 인프라 제약 사항으로부터 벗어날 수 있다.

**네트워크 제어 평면(Control Plane)와 데이터 평면(Data Plane) 분리**

데이터 패킷의 전달 방법을 결정하는 네트워크 제어 평면을 소프트웨어 기반 컨트롤러에 중앙집중식으로 구현한다. 실제로 네트워크를 통해 데이터 패킷을 전달하는 데이터 전송 평면은 하드웨어 기반 네트워크 기기가 패킷 전달에만 집중하도록 간소화, 전문화된다. 다른 방식에서, 두 평면은 일반적으로 스위치, 라우터, 액세스 포인트와 같은 네트워크 장치 내에 통합되어 중앙집중식 제어가 불가능하다.
  
**중앙집중식 제어**

네트워크 정책 및 구성이 여러 네트워크 장치 전반에 분산되어 관리 소요가 큰 다른 방식과 달리, SDN은 중앙 컨트롤러에서 네트워크 정책과 구성을 관리하고 시행할 수 있다.

**비용 절감**  
SDN 인프라는 비용이 많이 드는 단일 목적 인프라가 아니라, 상용 서버에서 구동할 수 있기 때문에 하드웨어 네트워크 인프라에 비해 저렴하다. 단일 서버에서 여러 기능이 구동될 수 있으므로, 물리 하드웨어가 덜 필요하고, 리소스를 통합하여 물리적 공간, 전력 및 전체 비용을 절감할 수 있다.

**우수한 확장성 및 유연성**  

네트워크 인프라를 가상화하면 또 다른 상용 하드웨어를 추가하지 않아도, 원하는 대로 필요한 시기에 네트워크 리소스를 확장하거나 축소할 수 있다.

**프로그래밍 가능 및 자동화 친화적**  
SDN 관리자는 API를 사용하여 네트워크 정책과 구성을 정의할 수 있다. 이를 통해 네트워크 리소스의 동적 프로비저닝과 정책 기반 관리가 가능해, 요구 사항이 계속해서 변화하더라도 이에 맞춰 신속하게 배포, 대응이 가능하다.  

**관리 간소화**  
SDN은 숙련된 전문가가 아니어도 관리할 수 있게 구현하여, 전반적으로 운영하기 쉬운 인프라를 구축할 수 있다.  

### SDN의 구성

SDN의 아키텍처는 크게 세 가지 주요 계층으로 구성된다. 각 계층은 API를 통해 서로 상호작용한다.

#### 애플리케이션 계층 (Application Layer)

애플리케이션 계층은 SDN 아키텍처의 가장 상위에 위치하여, 네트워크 서비스와 애플리케이션이 실행되는 곳이다. 네트워크 관리 시스템(NMS), 클라우드 오케스트레이션 플랫폼, 보안 애플리케이션, 로드 밸런싱 서비스 등이 애플리케이션 계층에서 실행된다.

이 계층의 애플리케이션들은 네트워크 자원을 활용하여 특정한 목적을 달성하거나 사용자에게 서비스를 제공한다.

이 계층의 애플리케이션들은 Northbound API 통해 제어 계층과 상호작용한다. 이를 통해 네트워크 서비스 요청, 네트워크 정책 정의, 네트워크 토폴로지, 트래픽 흐름, 성능 메트릭에 대한 정보 검색을 수행할 수 있다.

이 API를 통해 네트워크 관리 작업을 프로그래밍할 수 있게 하여, 외부 시스템과 통합할 수 있다.

#### 제어 계층 (Control Layer / SDN Controller)

네트워크 전체의 중앙 집중식 제어를 담당한다. 구체적으로는 애플리케이션 계층의 요구사항을 인프라 계층의 실제 네트워크 장비에 대한 명령으로 변환한다.

토폴로지, 장비 상태, 트래픽 흐름 등 네트워크의 전체적인 상태를 파악하고, 최적의 네트워킹 경로를 계산하거나 정책을 적용하는 등의 결정을 내린다.

#### 인프라 계층 (Infrastructure Layer / Data Plane)

실제로 네트워크 트래픽을 처리하고 전달하는 네트워크 구현으로 구성된다. 이 계층의 장비들은 자체적인 제어 로직 대신 SDN 컨트롤러의 제어를 따른다.

Southbound API SDN 컨트롤러로부터 제어 명령을 수신하고, 자신의 상태 정보를 컨트롤러에 보고한다. 컨트롤러는 이 API를 통해 네트워크 기기를 프로그래밍하고, 네트워크 토폴로지와 상태 정보를 검색하거나, 링크 실패, 정체 등의 이벤트를 확인할 수 있다.

## NFV: Network Function Virtualization

![](/static/posts/2025-11-20-sdn-and-nfv/mano-in-nfv.png)  

[_Faisal, "A Beginner’s Guide to NFV MANO-Management & Orchestration"_](https://telcocloudbridge.com/blog/a-beginners-guide-to-nfv-management-orchestration-mano/)

네트워크 기능 가상화(NFV; Network Funciton Virtualization)는 네트워크를 구성하는 데 사용되는 하드웨어들의 기능을 소프트웨어로 구현한 방식을 의미한다. 구체적으로 라우터, 방화벽, 로드밸런서의 상용 하드웨어의 기능과 역할을 구현하는 것이다.

### NFV의 사용

NFV는 소프트웨어 구현이므로, 네트워크 기능을 사용하기 위해서 전용 하드웨어 장비나 온프레미스 환경을 필요로 하지 않는다. 일반 소프트웨어가 동작하는 것과 같이, 표준적인 PC 환경에서 운용할 수 있어, 인프라 비용을 절감하고 네트워크 시스템의 민첩성을 향상할 수 있다.

모든 네트워크 기능을 가상화할 수 있으므로, 서버의 성능 요구사항만 충족된다면 이들 기능을 모두 하나의 서버에서 운영하는 것이 가능하다. 물리 하드웨어가 덜 필요하게 되므로, 하드웨어를 사용할 때보다 자원을 통합할 수 있고, 물리적인 공간, 전력 소비, 하드웨어 구매와 유지보수에 소모되는 비용 등을 절감할 수 있다.

하드웨어 구현은 소프트웨어 구현보다 유동적이지 못하므로, 필요에 따라 유연하게 조정할 수 없다. NFV를 사용하면 새로운 네트워크 기능이 필요할 경우, 새 가상 머신(VM)을 실행하는 것으로 대응할 수 있고, 더 이상 필요하지 않으면 VM을 제거하는 것으로 정리할 수 있다. 구체적으로, 일순간 트래픽이 급증할 경우, 로드밸런서나 방화벽을 추가하여 네트워크의 중단을 방지할 수 있다.

### NFV의 구성

NFV는 주로 유럽 전기 통신 표준 협회(ETSI)가 제안한 NFV 아키텍처와 같은 구성으로 사용한다. 이 아키텍처는 가상 네트워크 기능(VNF; Virtual Network Function), 네트워크 기능 가상화 인프라(NFVI; Network Functions Virtualization Infrastructure), NFV 관리, 자동화 및 네트워크 오케스트레이션(NFV MANO; NFV Management, Automation and Network Orchestration)으로 구성된다.

#### 가상 네트워크 기능(VNF; Virtual Network Function)

VNF는 실제로 하드웨어를 대체하는 소프트웨어의 네트워크 기능 구현을 의미한다. 디렉토리 서비스, 라우터, 방화벽, 로드 밸런서 등의 네트워크 기능을 소프트웨어로 제공한다. 일반적으로 이러한 기능은 VM으로 패키지되어 NFVI 위에서 운용, 배포된다.

이전에는 단순히 내장된 소프트웨어 시스템을 애플리케이션으로부터 분리하여 VM으로 패키지하여 사용했기 때문에, 오히려 비효율적이고 관리와 유지보수가 어려웠다. 클라우드 환경이 널리 퍼지기 시작하면서, VNF를 경량화하고 수평적인 구성의 NFVI 클라우드를 채택해 표준 네트워크 아키텍처로 만들었다.

#### 네트워크 기능 가상화 인프라(NFVI; Network Functions Virtualization Infrastructure)

NFVI는 VNF를 실제로 실행하고 운영하는 데 필요한 물리적 및 가상화된 인프라를 의미한다. 이는 NFV 아키텍처의 기반이 되는 계층으로, VNF가 동작할 수 있는 환경을 제공한다.

NFVI는 주로 다음 세 가지 주요 구성 요소로 이루어진다:

**하드웨어 자원 (Hardware Resources)**

범용 서버(compute), 스토리지(storage), 네트워크 장비(network switches)와 같은 물리적인 컴퓨팅 자원이다. 이들은 VNF가 필요로 하는 CPU, 메모리, 디스크 공간, 네트워크 대역폭 등을 제공한다. 기존의 고가 전용 장비 대신, x86 아키텍처 기반의 표준 서버를 활용하여 비용 효율성을 높인다.

**가상화 계층 (Virtualization Layer)**

하드웨어 자원 위에 위치하며, 하이퍼바이저(Hypervisor) 또는 컨테이너 런타임(Container Runtime)과 같은 가상화 기술을 포함한다. 이 계층은 물리적 하드웨어 자원을 추상화하여 여러 개의 가상 머신(VM)이나 컨테이너를 생성하고 관리할 수 있도록 한다. 이를 통해 VNF는 특정 하드웨어에 종속되지 않고 유연하게 배치될 수 있으며, 자원의 격리 및 효율적인 활용이 가능하다.

**가상화된 자원 (Virtualized Resources)**

가상화 계층에 의해 생성되고 관리되는 가상 머신(VM), 가상 스토리지, 가상 네트워크 등의 자원이다. VNF는 이러한 가상화된 자원 위에서 독립적으로 실행되며, 필요에 따라 자원을 동적으로 할당받거나 해제할 수 있다.

NFVI의 핵심은 범용 하드웨어를 사용하여 네트워크 기능을 유연하게 배치하고 확장할 수 있는 환경을 제공하는 것이다. 이를 통해 통신 사업자나 기업은 특정 벤더의 고가 장비에 대한 의존도를 낮추고, 다양한 VNF를 효율적으로 통합 및 운영할 수 있게 된다. NFVI는 클라우드 컴퓨팅 환경과 유사하게 자원을 풀링(pooling)하고 가상화하여 VNF에게 제공함으로써, 유연성과 확장성을 극대화한다.

#### 관리, 자동화 및 네트워크 오케스트레이션(NFV MANO; NFV Management, Automation and Network Orchestration)

MANO는 NFV 인프라와 VNF의 라이프사이클 관리, 자동화, 그리고 네트워크 서비스 오케스트레이션을 위한 프레임워크를 의미한다. NFV 환경의 복잡성을 관리하고, 효율적인 운영을 가능하게 하는 핵심적인 제어 및 관리 계층이다. ETSI NFV MANO 아키텍처는 주로 다음 세 가지 기능적 블록으로 구성된다:

**NFV 오케스트레이터 (NFVO; NFV Orchestrator)**

네트워크 서비스의 전체 라이프사이클 관리를 담당한다. 이는 여러 VNF를 조합하여 하나의 네트워크 서비스를 정의하고, 이 서비스가 NFVI 상에 배포, 확장, 업데이트, 종료될 수 있도록 조정하는 역할을 한다. NFVO는 VNF 간의 연결 관계와 서비스 요구사항을 이해하고, VNF Manager와 VIM에 적절한 지시를 내린다. 예를 들어, 새로운 모바일 코어 네트워크 서비스를 배포할 때, NFVO는 필요한 VNF(예: MME, SGW, PGW)들을 식별하고, 이들이 적절한 순서로 NFVI에 배포되도록 조정한다.

**VNF 관리자 (VNFM; VNF Manager)**  

개별 VNF의 라이프사이클 관리를 담당한다. VNF의 인스턴스 생성, 업데이트, 스케일링(확장/축소), 종료 등을 제어한다. 또한 VNF의 성능 모니터링 및 장애 복구 기능도 수행하여 VNF가 안정적으로 운영되도록 보장한다. VNFM은 VNF의 특정 요구사항(예: 특정 OS 이미지, 최소 자원)을 이해하고, VIM과 협력하여 해당 VNF를 배포하고 관리한다.

**가상화 인프라 관리자 (VIM; Virtualized Infrastructure Manager)**  

NFVI의 물리적 및 가상화된 자원을 관리한다. 컴퓨팅, 스토리지, 네트워크 자원을 추상화하고, VNF가 필요로 하는 자원을 할당하며, 자원의 사용률을 모니터링한다. OpenStack, VMware vCloud Director 등이 VIM의 대표적인 예시이다. VIM은 NFVO 및 VNFM의 요청에 따라 자원을 프로비저닝하고, 자원 사용량 데이터를 제공하여 전체 시스템의 효율적인 운영을 돕는다.

<br />
MANO는 이러한 구성 요소들의 유기적인 연동을 통해 NFV 환경에서 네트워크 서비스의 자동화된 배포와 운영을 가능하게 한다. 이를 통해 서비스 프로비저닝 시간을 단축하고, 운영 비용을 절감하며, 네트워크의 민첩성과 유연성을 극대화할 수 있다. MANO는 NFV의 핵심 가치인 '소프트웨어 정의'를 실현하는 데 필수적인 역할을 하며, 5G와 같은 차세대 네트워크에서 요구되는 복잡한 서비스 체이닝(Service Chaining) 및 슬라이싱(Network Slicing) 구현의 기반이 된다.

## SDN과 NFV의 관계

SDN과 NFV는 모두 하드웨어로 구현된 네트워크 기능을 추상화한다. NFV는 SDN 소프트웨어를 실행할 인프라를 제공하는 방식으로 SDN을 지원할 수 있다.

SDN은 네트워크의 제어 평면과 데이터 평면을 분리하여 소프트웨어로 네트워크를 중앙 제어하는 데 초점이 맞춰져있고, NFV는 물리적 하드웨어 구현을 소프트웨어로 구현하는 데 초점이 맞춰져있다. 두 기능은 독립적으로도, 함께로도 사용할 수 있다.

# 참고 문헌
- Abhishek De, "What is Software Defined Networking (SDN)?", GeeksforGeeks, https://www.geeksforgeeks.org/computer-networks/software-defined-networking/
- Faisal, "A Beginner’s Guide to NFV MANO-Management & Orchestration", Telco Cloud Bridge, https://telcocloudbridge.com/blog/a-beginners-guide-to-nfv-management-orchestration-mano/
- IBM Think, "What Is Software-Defined Networking (SDN)?", IBM, https://www.ibm.com/think/topics/sdn

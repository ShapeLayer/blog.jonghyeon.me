---
layout: post
title: Six degree-of-freedom haptic rendering using voxel sampling 리뷰
date: 2026-07-11
categories: [paper]
tags: [paper, vr, haptics]
---

[McNeely, William A., Kevin D. Puterbaugh, and James J. Troy. "Six degree-of-freedom haptic rendering using voxel sampling." ACM SIGGRAPH 2005 Courses. 2005.](https://dl.acm.org/doi/10.1145/1198555.1198605)

〈가상현실〉 수업 참고자료

## 배경

[god-object](/posts/2026-07-02-paper-a-constraint-based-god-object-method-for-haptic-display)와 [proxy](/posts/2026-07-09-paper-the-haptic-display-of-complex-graphical-environments)를 다룬 연구에서는 햅틱 인터페이스 끝점의 위치 데이터만 렌더링에 사용했다. 따라서 3차원 공간에서의 병진 운동만 다루는 3자유도(3-DOF) 햅틱 렌더링을 수행했다. 그러나 물체는 병진 운동뿐 아니라 회전하기도 하여, 회전축 3개를 포함하는 6자유도(6-DOF) 처리에 대한 필요성이 제기되었다.  

6-DOF 렌더링은 3-DOF 렌더링보다 어렵다. 3-DOF에서는 장치 끝점 하나의 위치와 접촉 반작용 힘만 다루면 되지만, 6-DOF에서는 강체의 자세까지 고려해 물체 표면의 여러 접촉을 함께 처리하고, 각 접촉이 만드는 힘뿐 아니라 물체 중심에 대한 토크도 계산해야 한다.

<br />

이 연구에서는 항공기 유지보수와 조립 시뮬레이션을 구현하기 위해 6-DOF 렌더링이 고려되었다. 시뮬레이션을 구현하기 위해 이 연구의 햅틱 렌더링은 다음의 요구조건을 만족해야 한다.

1. 첫 충돌만 검출하는 것이 아니라, 접촉 및 근접 구간을 모두 찾아야 한다.
2. 접촉마다 힘과 토크를 계산하여 강체의 운동을 안정적으로 제어해야 한다.
3. 물체의 자세와 장면의 복잡도에 관계없이 1000 Hz 갱신을 유지해야 한다.
4. 선행 연구의 렌더링 과정에서 좁은 쐐기형 구멍에 물체를 밀어 넣을 때 발생하는 불안정성 문제와 같이, 기하학에서 비롯되는 불안정성을 제어해야 한다.

이 연구는 정밀도를 voxel 단위로 제한하는 대신, 복잡한 정적 장면과 하나의 강체 동적 물체를 안정적으로 처리하는 것을 목표로 한다. (예를 들어 공구 접근과 조립 공차에는 보통 0.5 inch 이상의 여유를 둔다. 이 상황에서는 voxel 크기만큼 물체를 분리할 수 있다.)  

## Voxmap + Point Shell

이 방법은 'Voxmap PointShell'이라고 명명되었다. 이 방법에서는 표현을 두 개 역할로 나눈다.  

| 대상 | 표현 | 역할 |
| :-: | :-: | -- |
| 정적 환경 (항공기 구조물 등) | voxmap (체적 점유 맵) | 공간을 free, surface, interior, proximity voxel로 표시 |
| 동적 물체 (공구·부품) | point shell (표면 점과 안쪽 법선) | 매 프레임 voxmap을 샘플링하여 충돌과 힘을 계산 |

동적 물체의 표면은 샘플 점으로 구성된 껍질로 표현하고, 정적 환경에 속하는 모든 물체는 하나의 voxmap으로 통합한다. (이 연구에서는 강체만 다루었기 때문에 재질별 구분이 필요하지 않았다.) voxmap을 사용하여 물체 쌍의 충돌을 계산할 때 발생하는 $O(N)$ 크기 비용도 피할 수 있다.  

이 방법에서는 다음과 같이 햅틱 렌더링을 처리한다.  

1. 전역 voxel 크기 $s$ 를 정한다.  
2. 정적 폴리곤 모델을 스캔 변환해 voxmap을 만든다.  
3. 동적 물체 표면 voxel 중심점들로 point shell을 만든다.  
4. 매 햅틱 프레임(1 ms)마다 point shell 각 점에서 voxmap을 샘플링한다.  
5. 침투·근접에 따른 penalty 힘을 합산해 알짜 힘과 토크를 구한다.  
6. virtual coupling 동역학으로 장치와 가상 물체를 연결해 힘을 출력한다.

계산 성능은 조작 물체의 노출 표면적, 즉 point shell 점 개수에 대략 선형으로 비례한다. 그래서 렌더 대상 전체의 삼각형 수에는 거의 영향을 받지 않는다.

## Tangent-plane force model

힘은 단순하게 계산하도록 설계하였다.  

point shell의 한 점이 표면, 즉 force field의 voxel 내부로 들어가면, 해당 voxel의 중심을 지나고 그 점의 법선과 같은 방향을 법선으로 갖는 평면(tangent plane)을 구성한다. 그 점에서 평면까지의 깊이 $d$ 에 비례하는 힘을 훅의 법칙(Hooke's Law)에 따라 적용한다.  

$$
F = K_{ff}\, d
$$

$K_{ff}$ 는 force field의 강성이다. 점이 평면 위 또는 평면 바깥에 있으면 힘은 0이다. 각 점에서 계산한 힘과 토크를 모두 합산하면 동적 물체에 작용하는 알짜 힘과 토크를 얻을 수 있다.  

> 접점 근처에서는 실제 두 표면이 서로 접한다. tangent-plane 모델은 이 국소 접평면을 동적 물체 쪽에서 미리 계산한 법선으로 근사한다.

이 방법은 정적 표면에서 법선을 매번 계산하거나 potential의 기울기를 구하지 않으므로 매우 빠르다. 다만 voxel 경계를 가로질러 미끄러질 때 힘 크기가 불연속적으로 변할 수 있다. 힘의 방향은 상대적으로 덜 불연속적이다.  

3-DOF 렌더링에서는 이러한 불연속이 치명적일 수 있지만, 6-DOF 렌더링에서는 여러 점을 동시에 샘플링 확률적으로 불연속을 완화했다.  

## 정확한 표면 침투를 막기: force-layer offset

| 값 | 이름 | 의미 |
| :-: | :-: | -- |
| 0 | Free space | 자유 공간 |
| 1 | Interior | 내부 |
| 2 | Surface | offset된 force field 표면 |
| 3 | Proximity | 표면의 free-space 이웃으로, 접근 감속에 사용 |

_연구에서 정의해 사용한 2비트 voxel 타입_

tangent-plane 모델만 사용하면 실제 폴리곤 표면이 voxel 크기만큼 서로 침투할 수 있다. 용도에 따라서는 이것을 허용할 수 있지만, 이 연구는 표면 교차 자체를 막으려고 했다.  

그래서 voxel들에 타입을 부여하고, 기하학적 표면 voxel에서 바깥쪽으로 2층 offset한 위치를 `2` = "force field 표면"으로 사용했다. point shell이 이 force field와 접촉하면, 실제 폴리곤 표면 사이에 최소한 voxel 크기만큼의 간격이 남도록 설계한다.  

![](/static/posts/2026-07-11-paper-six-degree-of-freedom-haptic-rendering-using-voxel-sampling/force-layer-offset.png)  

Voxel화의 마지막 단계에서는 proximity를 surface로 변환하고, 기존 surface를 interior로 변경하는 작업을 두 번 반복하여 offset을 만든다. 26개 이웃으로 값을 전파하므로, 얇은 가시(spike) 구조가 한 줄의 voxel 기둥으로만 남아 point shell이 그 사이를 비껴 통과하는 경우도 줄일 수 있다.  

## Voxel tree (고정 깊이 $2^{3N}$ -tree)

일반적인 octree는 탐색 깊이가 일정하지 않아 갱신 주기마다 계산 시간이 달라진다. 하지만 이 연구에서는 평균적인 속도보다 일정한 1000 Hz 갱신을 유지하는 것이 중요했다.  

따라서 이 연구에서는 깊이를 3레벨로 고정하고, 각각의 입방체 공간을 $2^{3N}$ 개로 분할하는 octree 일반화를 사용했다. $N=1$ 이면 고전적인 octree인 8-tree가 되지만, 실험 결과 이 연구의 희소한 형상에는 $N=3$, 즉 512-tree가 가장 높은 메모리 효율을 보였다.

- 최소 셀 크기 = leaf voxel 크기 $s$ (전역 정확도 상한)  
- 최대 셀 크기 = leaf 위쪽 3레벨로 제한하여 탐색 시간의 상한을 둠

이 방법은 정확도 손실을 테셀레이션 오차처럼, 일관된 수준으로 감수하고, 어느 자세에서도 갱신 시간이 크게 변하지 않도록 한다.

## 동역학: Virtual coupling과 6-DOF god-object

![](/static/posts/2026-07-11-paper-six-degree-of-freedom-haptic-rendering-using-voxel-sampling/virtual-coupling.png)  

출력은 임피던스, 즉 위치와 자세를 입력받아 힘과 토크를 출력하도록 한다. 장치와 가상 물체는 가상 스프링과 댐퍼로 연결했다. (이것을 virtual coupler 명명하였다.)  

개념적으로는 가상 환경 안에 햅틱 핸들의 가상 복사본을 두고, 이 복사본을 동적 물체와 6-DOF 스프링으로 연결한다.

$$
\begin{aligned}
\mathbf{F}_{\text{spring}} &= k_T \mathbf{d} - b_T \mathbf{v} \\
\boldsymbol{\tau}_{\text{spring}} &= k_R \boldsymbol{\theta} - b_R \boldsymbol{\omega}
\end{aligned}
$$

- $k_T, b_T$ : 병진 강성과 감쇠 계수
- $k_R, b_R$ : 회전 강성과 감쇠 계수. $\boldsymbol{\theta}$ 는 equivalent-axis 각이다.
- 수치 적분 시간 간격 $\Delta t = 1\,\text{ms}$ (1000 Hz)

동적 물체의 반영 질량은 장치의 관성에 더해지는 값이 약 12 g이 되도록 작게 설정했다. 회전 관성은 모든 방향에서 같다고 설정하여 체감 관성을 키우지는 않았다.  

### god-object 확장과 강성 클램프

force field 깊이인 반 voxel보다 스프링이 더 늘어나 물체를 밀어 넣지 못하도록, 스프링 힘을 변위 $\Delta s$ 의 절반 값으로 클램프한다.  

논문에서는 god-object를 일반화한 것이라고 설명한다. 다만 이 연구에서는 voxel로 처리하고 있으므로, 원래의 god-object처럼 표면에 엄밀하게 붙는 점은 아니다. 최대 반 voxel까지 침투할 수 있는 proxy에 가깝다고 볼 수 있다. 정확하게 제약 수식을 푸는 대신 penalty 힘으로 표면 제약을 근사적으로 만족시킨다.  

동시에 많은 점이 force field에 들어가면 합산된 강성이 지나치게 커져 고정 시간 간격 적분이 불안정해질 수 있다. 따라서 점과 voxel의 교차 개수 $N$에 따라 알짜 힘을 평균한다.  

$$
\mathbf{F}_{\text{Net}} =
\begin{cases}
\mathbf{F}_{\text{Total}} & N < 10 \\[4pt]
\dfrac{\mathbf{F}_{\text{Total}}}{N/10} & N \ge 10
\end{cases}
$$

토크에도 같은 방식을 적용한다. $N=10$ 이후에만 평균을 적용해, 작은 $N$에서 힘이 급격히 작아지지 않도록 한다.  

자유 공간에서는 모든 point shell 점이 free voxel에 있을 때, 스프링 힘이 남아 있더라도 장치에 힘과 토크를 0으로 출력한다. 이렇게 처리하면 장치의 전원이 꺼진 상태와 유사한 자유 공간 감각을 제공할 수 있다.  

### Pre-contact braking force

정지 상태의 접촉을 기준으로 한 클램프만으로는 빠른 충돌에서 운동량 때문에 force field를 통과할 수 있다. 따라서 표면 바깥의 proximity voxel에서는 점이 접근할 때만 속도를 줄이는 제동 힘을 적용한다.

점 $i$ 의 안쪽 법선을 $\hat{n}_i$, 속도를 $\mathbf{v}_i$ 라고 할 때, 점이 접근하는 조건 $\hat{n}_i \cdot \hat{v}_i < 0$ 일 때 다음의 힘 $F_i$ 를 적용한다.  

$$
\mathbf{F}_i = -b\, (\mathbf{v}_i \cdot \hat{n}_i)\,\hat{n}_i
$$

감쇠 계수 $b$는 병진 운동 에너지 성분을 한 햅틱 주기 안에 소산하도록 휴리스틱하게 설정한다. 점이 표면에서 멀어질 때에는 힘이 0이므로, 표면이 "끈적이는" 감각을 만들지 않는다.

이 방법으로는 한 햅틱 주기 안에 proximity 영역, 혹은 얇은 물체 전체를 건너뛰면 제동과 충돌을 감지하지 못한다.(tunnelling) 긴 물체가 빠르게 회전하면 끝점의 속도가 특히 커진다. 논문에서는 점의 속도가 $s/\Delta t$ 를 넘지 않도록 선속도와 각속도를 제한하는 방안을 제안했다.  

## god-object / proxy와의 관계

이 연구에서는 god-object와 proxy를 다룬 앞선 두 연구와 다음과 같은 차이가 있었다.  

| | God-object (Zilles) | Proxy (Ruspini) | Voxel sampling (이 논문) |
| :-: | :-: | :-: | :-: |
| 자유도 | 3-DOF 점 | 3-DOF 점과 반경 | 6-DOF 강체 |
| 가상 접촉 상태 | 표면에 붙는 점 | 질량이 없는 구와 configuration space | point shell 전체 |
| 제약 처리 | 능동 평면과 라그랑주 승수 | 제약 평면 최적화 | penalty force field와 voxel |
| 장면 복잡도 | 비교적 단순한 강체 | 복잡한 그래픽 환경 | 수십만 폴리곤의 정적인 환경 |
| 정확도 | 표면 기하 기준 | 표면 + force shading | voxel 스케일 |
| 표면 속성 | 추가 계층이 필요함 | proxy를 통해 마찰, 점성, 강성, 질감 표현 | 단단한 강체 force field만을 다룸 |

이들 연구는, 실제로는 장치 끝점이 표면을 뚫고 들어가더라도, 가상 환경에는 물체를 두고 스프링 힘으로써 계산하여 침투하지 않도록 역방향 힘을 장치에 전달한다는 점에서 공통점이 있다.  

이 연구에서는 제약을 해석적으로 풀지 않고, 미리 voxmap을 생성해 1kHz 샘플링 목표를 달성했다는 데에서 선행 연구와 차이점이 있다.  

## 마무리

이 연구는 voxel로 샘플링해 6-DOF 햅틱 렌더링을 구현했다. 정적 환경은 하나의 voxmap으로 표현하고 동적 물체는 point shell로 표현했다. 

핵심적인 개선은 god-object와 proxy가 제시한 "가상 접촉 상태와 스프링 피드백"을 "복잡한 정적 물체에서의 6-DOF 조작"으로 확장했다는 것이다. 대신 정밀도는 voxel 해상도에 제한되었고, tunnelling, 쐐기 문제, 비수동성은 완전히 해결하지 못하고 경험적으로 관리하게 되었다. 

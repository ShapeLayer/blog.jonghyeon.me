---
layout: post
title: 기하 변환을 사용하여 화상 처리
date: 2025-11-14
category: [image-processing]
---

_〈화상정보처리〉 수업 노트_

화상에는 크게 두 종류의 정보가 담겨 있다. 하나는 피사체의 배치, 형상, 움직임을 나타내는 좌표 정보이고, 다른 하나는 재질, 표면 상태, 색채, 반사율, 방사율 등의 물리적 특성 정보이다. 동화상을 포함하면 화상은 3차원 공간 내(시간까지 포함하면 4차원)의 정보를 담게 된다. 이번 강의에서는 그 중 좌표 정보와 관련된 화상 처리 기법, 즉 기하 변환(幾何変換; Geometric Transformation)을 다룬다.

## 화상의 좌표계

3차원 공간의 좌표계에는 왼손 좌표계와 오른손 좌표계가 있다. 화상 처리에서는 오른손 좌표계를 사용하는데, 이는 카메라나 모니터의 래스터 주사(raster scan) 순서를 따르기 위해서이다. 일반적인 수학의 직교 좌표계는 왼손계이지만, 화상 처리에서는 좌상단을 원점으로 두고 오른쪽, 아래 방향을 양의 방향으로 삼는 오른손계를 사용한다.

## 기본 변환

### 평행 이동

물체의 방향이나 크기를 바꾸지 않고 위치만 이동시키는 조작을 평행 이동(平行移動; Translation)이라 한다. 점 $(x, y)$를 $(\Delta x, \Delta y)$만큼 이동시키면 변환 후의 좌표 $(x', y')$는 다음과 같다.

$$
\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} x \\ y \end{pmatrix} + \begin{pmatrix} \Delta x \\ \Delta y \end{pmatrix}
$$

### 축척 (확대, 축소)

물체의 위치나 방향을 바꾸지 않고 크기만 변화시키는 조작을 축척(縮尺; Scaling)이라 한다. 축척률 $K$가 1보다 크면 확대, $0 \le K < 1$이면 축소이다. 원점을 중심으로 한 축척의 행렬 형식은 다음과 같다.

$$
\begin{pmatrix} x' \\ y' \end{pmatrix} = K \begin{pmatrix} x \\ y \end{pmatrix}
$$

### 회전

물체의 크기나 형상을 바꾸지 않고 방향만 변화시키는 조작을 회전(回転; Rotation)이라 한다. 회전각 $\theta$는 반시계 방향을 양으로 정의한다. 원점을 중심으로 한 회전의 행렬 형식은 다음과 같다.

$$
\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}
$$

## 동차 좌표 (Homogeneous Coordinates)

위의 세 가지 기본 변환을 살펴보면, 축척과 회전은 행렬의 곱으로 표현되지만 평행 이동만은 벡터의 합으로 표현된다는 문제가 있다. 이 불일치를 해소하기 위해 동차 좌표(同次座標; Homogeneous Coordinates)를 사용한다.

동차 좌표는 2차원 점 $(x, y)$를 3차원 벡터 $(\omega x,\ \omega y,\ \omega)$로 표현하는 방법으로, 일반적으로 $\omega = 1$을 사용한다. 즉 점 $(x, y)$는 $(x, y, 1)$로 표현된다.

동차 좌표를 이용하면 축척, 회전, 평행 이동을 모두 $3 \times 3$ 행렬의 곱으로 통일하여 표현할 수 있다.

$$
\begin{pmatrix}x' \\ y' \\ 1 \end{pmatrix} = \begin{pmatrix} K & 0 & 0 \\ 0 & K & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ 1 \end{pmatrix}
$$

_축척 계산_

<br />

$$
\begin{pmatrix} x' \\ y' \\ 1 \end{pmatrix} = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ 1 \end{pmatrix}
$$

_회전 계산_

<br />

$$
\begin{pmatrix} x' \\ y' \\ 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & \Delta x \\ 0 & 1 & \Delta y \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ 1 \end{pmatrix}
$$

_평행 이동 계산_

## 종횡비와 스큐

축척 변환을 X축 방향과 Y축 방향에 각각 다른 비율 $P$, $Q$로 적용하면 종횡비를 변경할 수 있다.

$$
\begin{pmatrix} x' \\ y' \\ 1 \end{pmatrix} = \begin{pmatrix} P & 0 & 0 \\ 0 & Q & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ 1 \end{pmatrix}
$$

스큐(Skew) 변환은 한 축의 크기에 비례하여 다른 축 방향으로 기울이는 변환이다. X 방향 스큐와 Y 방향 스큐 각각의 변환 행렬은 다음과 같다.

$$
\begin{pmatrix} 1 & \alpha & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$

_$X$ 방향 스큐_

<br />

$$
\begin{pmatrix} 1 & 0 & 0 \\ \beta & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$

_$Y$ 방향 스큐_

## 합성 사상 (Composite Transformation)

복수의 변환을 순서대로 적용하는 것을 합성 사상이라 한다. 동차 좌표를 사용하면 각 변환 행렬의 곱으로 합성 변환 행렬을 한 번에 구할 수 있다.

$$\begin{pmatrix} x' \\ y' \\ 1 \end{pmatrix} = A_4 A_3 A_2 A_1 \begin{pmatrix} x \\ y \\ 1 \end{pmatrix}$$

주의할 점은 행렬 곱셈의 순서가 변환의 순서와 역순으로 배치된다는 것이다. 즉 가장 먼저 적용되는 변환 행렬이 가장 오른쪽에 위치한다.

### 유클리드 변환 (Euclidean Transformation)

회전과 평행 이동만을 조합한 변환이다. 물체의 형상과 크기가 보존되며, 미지 계수는 4개이다. 플랫베드형 이미지 스캐너에서 발생하는 기하 왜곡을 보정하는 데 주로 사용된다.

$$\begin{pmatrix} x' \\ y' \\ 1 \end{pmatrix} = \begin{pmatrix} a & -b & e \\ b & a & d \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ 1 \end{pmatrix}$$

### 헬머트 변환 (Helmert Transformation)

유클리드 변환에 전체 축척 변환을 추가한 것으로, 상사 변환(Similarity Transformation)이라고도 한다. 미지 계수는 4개이며, 복사기에서 발생하는 기하 왜곡 보정에 사용된다.

### 어파인 변환 (Affine Transformation)

헬머트 변환에 종횡비 변환과 스큐를 추가한 것으로, 임의의 평행사변형을 다른 임의의 평행사변형으로 변환할 수 있다. 미지 계수는 6개이다.

$$\begin{pmatrix} x' \\ y' \\ 1 \end{pmatrix} = \begin{pmatrix} a' & b' & c' \\ d' & e' & f' \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ 1 \end{pmatrix}$$

### 사영 변환 (Projective Transformation)

투시 변환(Perspective Transformation) 또는 호모그래피 변환(Homography Transformation)이라고도 한다. 임의의 사각형을 다른 임의의 사각형으로 변환할 수 있으며, 미지 계수는 9개이다. 액정 프로젝터로 스크린에 투영할 때 수행하는 사다리꼴 보정도 이 변환의 일종이다.

$$\begin{pmatrix} x' \\ y' \\ 1 \end{pmatrix} = \begin{pmatrix} h_{11} & h_{12} & h_{13} \\ h_{21} & h_{22} & h_{23} \\ h_{31} & h_{32} & h_{33} \end{pmatrix} \begin{pmatrix} x \\ y \\ 1 \end{pmatrix}$$

## 변환 계수의 산출

어파인 변환을 예로 들면, 변환 계수를 구하기 위해서는 화상 내에서 동일 직선 위에 있지 않은 3점의 변환 전후 좌표 쌍(대응 제어점 쌍)을 선정하여 연립 방정식을 풀면 된다. 실용적으로는 화상 전체를 포함하는 큰 삼각형을 설정하는 방법, 다수의 대응 제어점 쌍에서 계수의 평균을 구하는 방법, 화상을 작은 삼각형 영역으로 분할하여 각각에서 계수를 추정하는 방법 등 다양한 접근이 사용된다.

## 디지털 화상의 기하 변환 시 발생하는 문제

연속적인 좌표계를 다루는 수학적 변환을 이산적인 격자점으로 구성된 디지털 화상에 적용하면 문제가 발생한다. 예를 들어 화상을 확대하면 변환 후의 좌표가 원래 화소가 존재하지 않는 격자점 사이에 오는 경우가 생기고, 임의의 각도로 회전하면 대부분의 화소가 격자점 위에 정확히 오지 않는다. 또한 축소 시에는 여러 화소 중 어느 것을 선택해야 할지가 모호해진다.

이처럼 기하 변환의 결과가 디지털 화상의 격자점 좌표와 일치하지 않는 경우, 원래의 연속 화상을 가정하여 다시 표본화를 수행하는 처리를 리샘플링(Resampling; 재표본화)이라 한다.

## 리샘플링 기법

주요 리샘플링 기법으로는 다음 다섯 가지가 있다.

**최근방법(Nearest Neighbor)**

변환 후의 좌표에서 가장 가까운 격자점의 화소값을 그대로 할당하는 방법으로, 소수부를 절사(切捨て)하여 처리한다. 연산이 단순하고 고속이지만, 확대 시 블록 노이즈가 발생하기 쉽다.

<br />

**쌍일차법(Bi-Linear)**

변환 후의 좌표를 둘러싸는 4개의 인접 화소값을 일차 선형 보간하는 방법이다. 먼저 X 방향으로 일차 보간을 행한 뒤, 그 결과를 Y 방향으로 다시 일차 보간하여 2차원으로 확장한다. 확대 계열의 처리에 최적이다.

<br />

**쌍삼차 보간법(Bi-Cubic)**

주변 16개 화소를 사용하여 3차 함수로 보간하는 방법이다. 여기서 사용되는 함수 $h(t)$는 Sinc 함수를 3차까지의 테일러 전개로 근사한 3차 함수이며, 계수 $a$는 통상 $-0.7 \sim -2$ 범위의 값을 사용한다. 처리 속도가 느리고 확대 시에 다소 흐림이 발생할 수 있다.

<br />

**면적 평균법(Area Averaging)**

변환 후의 화소 영역에 대응하는 원본 화소들의 가중 평균을 취하는 방법으로, 축소 계열의 처리에 최적이다.

<br />

**란치오스 보간법(Lanczos Interpolation)**

Sinc 함수를 란치오스 창 함수로 제한한 필터를 이용하는 고품질 보간 방법이다.

세 가지 대표적인 기법의 결과를 비교하면, 최근방법은 처리 속도가 빠르지만 계단 현상이 두드러지고, 쌍일차법은 부드럽지만 다소 흐림이 생기며, 쌍삼차 보간법은 가장 자연스러운 결과를 주지만 연산 비용이 높다.

## 고차 기하 보정

복사기, 스캐너, 디지털 카메라에서 발생하는 기하 왜곡은 일반적으로 앞서 설명한 어파인 변환이나 사영 변환의 범위 내에서 보정이 가능하다. 그러나 특수한 렌즈를 사용하거나, 기류가 불안정한 상태에서 드론, 항공기로 촬영할 때 발생하는 왜곡은 이보다 복잡한 고차 기하 왜곡으로 분류된다.

OpenCV에는 체커보드 패턴을 이용하여 카메라의 렌즈 왜곡을 교정하는 함수가 내장되어 있어, 방사형 왜곡이나 접선 방향 왜곡을 포함한 카메라 내부 파라미터를 추정하고 보정하는 처리를 간편하게 구현할 수 있다.

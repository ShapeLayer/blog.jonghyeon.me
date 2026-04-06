---
layout: post
title: 전파와 전파의 발생
date: 2026-04-06
category: [mobile-communication-system]
---

_〈모바일통신시스템〉 수업 노트_

## 전파

전파는 전파법에 의해 "인공적 매개물 없이 공간에 전달하는 3000GHz보다 낮은 주파수의 전자파"로 정의된다. 가시광선 범위 바깥의 빛이므로 사람이 직접 전파를 확인하는 것은 어렵지만, 맥스웰 방정식에 의해 전파의 존재가 예언, 헤르츠의 실험에 의해 전파를 포착하게 되면서 전파의 실재를 확인하게 되었다.  

90도의 위상 차이를 갖는 전계와 자계가 시간적인 변화에 따라 파동이 발생하는 것을 전자파, 혹은 전자기파로 정의한다. 전기장과 자기장의 파형 진행 방향이 상호 직각이라는 데에서, "TEM(Transverse Electromagnetic)파로 전파된다"고 표현한다.  

전자파의 전달 속도 $v_p$ 는 빛의 속도 $c$, 유전 상수 $\varepsilon_r$ 을 사용하여 다음과 같이 정의된다:  

$$
\begin{aligned}
c &= 3 \times 10^8 \text{m/s} \\
v_p &= \frac{c}{\sqrt{\varepsilon_r}}
\end{aligned}
$$

다만 전파를 활용하는 실제 환경은 자유공간이 아니므로, 현실에서의 전자파의 전달 속도는 이와 같지는 않다.  

## 안테나

어떤 도선에 교류 전류를 흘리면, 맥스웰 방정식에 의해 주변 공간에 시간에 따라 변하는 전기장과 자기장이 생성된다.  

안테나는 이것을 이용하여 전자기파를 방사, 확산시킴으로써, 무선 통신을 구현한다. 때문에 안테나를 만드는 데 있어서 주요한 논의는 전파를 효율적으로 확산시키고 흡수시키는 데 방점을 둔다.  

전파의 파장 $\lambda$ 은 전파의 속도 $C = 3 \times 10^8 \text{m/sec}$ 와 주파수 $f$ (Hz)에 대해서, 다음과 같이 정의된다:  

$$
\lambda = \frac{C}{f}
$$

안테나의 길이는 일반적으로 $\frac{1}{2} \lambda$, $\frac{1}{4} \lambda$ 를 최적의 길이로 간주한다.  

900MHz 대역을 사용하는 셀룰러, 1.8GHz 대역을 사용하는 PCS, 2GHz 대역을 사용하는 IMT2000 환경을 가정할 때, 각각 다음과 같이 계산할 수 있다. $L$ 은 안테나의 길이이다.  

$$
\begin{aligned}
\lambda_\text{Cellular} &= \frac{c_\text{Cellular}}{f_\text{Cellular}} = \frac{3 \times 10^8}{9 \times 10^8} \approx 33.3\text{cm} \\
L_\text{Cellular} &= \frac{33.3}{4} \text{cm} = 8.325 \text{cm} \\
\end{aligned}
$$

$$
\begin{aligned}
\lambda_\text{PCS} &= \frac{c_\text{PCS}}{f_\text{PCS}} = \frac{3 \times 10^8}{18 \times 10^8} \approx 16.6\text{cm} \\
L_\text{PCS} &= \frac{16.6}{4} \text{cm} = 4.15 \text{cm} \\
\end{aligned}
$$

$$
\begin{aligned}
\lambda_\text{IMT2000} &= \frac{c_\text{IMT2000}}{f_\text{IMT2000}} = \frac{3 \times 10^8}{20 \times 10^8} \approx 15\text{cm} \\
L_\text{IMT2000} &= \frac{15}{4} \text{cm} = 3.75 \text{cm} \\
\end{aligned}
$$

일반적인 안테나의 최적 길이는 파장의 상수배수이므로, 주파수가 커질 수록 안테나 길이가 줄어드는 경향이 있음을 알 수 있다.  

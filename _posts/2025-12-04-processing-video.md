---
layout: post
title: 동화상 처리
date: 2025-12-04
category: [image-processing]
---

_〈화상정보처리〉 수업 노트_

통상적인 화상은 3차원 공간을 2차원 평면에 투영한 것으로, 특정 시각의 상태를 포착한 스냅샷이다. 동화상은 이러한 스냅샷 화상을 일정한 시간 간격으로 연속 취득하여 구성된다. 애니메이션처럼 정지화상을 이어 붙여 연속 재생하는 경우나, 팬(pan), 틸트(tilt)와 같이 카메라의 시점을 이동시키며 촬영하는 경우도 동화상의 일종으로 간주된다.

## 동화상 처리의 기본 방식

동화상에 대한 화상 처리는 크게 세 가지 방식으로 분류된다.

A. 정지화상 처리 결과를 합성하는 방식  
여러 장의 정지화상 각각에 처리를 적용한 뒤, 그 결과를 다시 이어 붙여 동화상을 구성한다.

B. 비디오에서 프레임을 추출하여 처리 후 재합성하는 방식  
비디오 파일에서 각 프레임을 추출하고, 정지화상 처리를 거친 뒤 처리된 프레임들을 다시 동화화하는 방식이다. 기존의 정지화상 처리 기법을 동화상에 그대로 적용할 수 있다는 점에서 범용적으로 활용된다.

C. 프레임 간 연산을 수행하는 방식  
인접한 프레임들 사이의 차이를 계산하는 등, 시간적 변화에 주목한 처리를 수행하는 방식이다. 움직임 검출처럼 동화상에 고유한 처리에 적합하다.

## Python + OpenCV를 이용한 동화상 처리

### 웹카메라 화상 취득

Python과 OpenCV를 조합하면 웹카메라로부터 실시간 화상을 취득하여 처리할 수 있다. `cv2.VideoCapture(0)`으로 카메라 장치를 열고, 루프 내에서 `cap.read()`를 호출하면 프레임을 순차적으로 읽어올 수 있다. 아래 코드는 취득한 화상을 절반 크기로 리사이즈하여 표시하는 기본 예제이다.

```python
import cv2

def main():
    cap = cv2.VideoCapture(0)  # 카메라 번호는 환경에 따라 다를 수 있음
    while True:
        ret, im = cap.read()
        h = im.shape[0]  # 화상의 높이
        w = im.shape[1]  # 화상의 너비
        resize = cv2.resize(im, (w // 2, h // 2))
        cv2.imshow("Camera Test", resize)
        # ESC 키가 눌리면 종료
        if cv2.waitKey(10) == 27:
            cap.release()
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()
```

이미 파일로 저장된 동화상을 처리하려면, `cv2.VideoCapture(0)` 대신 `cv2.VideoCapture('test.avi')`와 같이 파일 경로를 지정하면 된다.

### 프레임 간 차분을 이용한 움직임 검출

프레임 간 연산의 대표적인 응용이 프레임 간 차분(frame difference)에 의한 움직임 검출이다. 연속된 세 프레임 사이의 절댓값 차분을 구하고, 두 차분의 논리곱(AND)을 취함으로써 일시적인 노이즈가 아닌 지속적인 변화 영역만을 추출한다. 차분값이 임곗값보다 큰 화소를 흰색으로 표시하여 움직임 마스크 화상을 생성하고, 미디안 블러로 노이즈를 저감한다.

```python
import cv2
import numpy as np

def flame_sub(im1, im2, im3, th, blur):
    d1 = cv2.absdiff(im3, im2)
    d2 = cv2.absdiff(im2, im1)
    diff = cv2.bitwise_and(d1, d2)
    mask = diff > th  # 차분이 임곗값보다 크면 True
    im_mask = np.empty((im1.shape[0], im1.shape[1]), np.uint8)
    im_mask[mask] = 255  # True 화소(변화 위치)를 흰색으로 표시
    im_mask = cv2.medianBlur(im_mask, blur)  # 노이즈 저감
    return im_mask

if __name__ == '__main__':
    cam = cv2.VideoCapture(0)
    im1 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    im2 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    im3 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    while True:
        im_fs = flame_sub(im1, im2, im3, 5, 7)
        cv2.imshow("Input", im2)
        cv2.imshow("Motion Mask", im_fs)
        im1 = im2
        im2 = im3
        im3 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
        if cv2.waitKey(10) == 27:  # ESC 키로 종료
            cv2.destroyAllWindows()
            break
```

## Haar-like 특징량 기반 캐스케이드 분류기를 이용한 얼굴 인식

캐스케이드 분류기(Cascade Classifier)는 여러 식별기를 단계적으로 조합한 분류기이다. 모든 식별기가 정해라고 판단한 경우에만 최종적으로 정해로 분류된다. 각 식별기는 오검출(정답을 오답으로 판단)이 발생하지 않도록 설계되어 있으며, 초기 단계에서 대다수의 비해당 영역을 신속히 기각할 수 있어 처리 속도가 빠르다.

Haar-like 특징량은 화상 내 두 인접 영역의 평균 휘도 차이를 기준으로 산출되는 특징량이다. 이를 이용한 식별기를 캐스케이드 구조로 조합하면 효율적으로 얼굴을 검출할 수 있다.

OpenCV에는 미리 학습된 Haar-like 분류기 파일(XML 형식)이 내장되어있다. 이것을 이용하면 간단한 코드로 얼굴과 눈을 검출할 수 있다.

```python
import cv2

face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = img[y: y + h, x: x + w]
        face_gray = gray[y: y + h, x: x + w]
        eyes = eye_cascade.detectMultiScale(face_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.imshow('video image', img)
    if cv2.waitKey(10) == 27:  # ESC 키로 종료
        break

cap.release()
cv2.destroyAllWindows()
```

얼굴 영역은 파란색(BGR: 255, 0, 0), 눈 영역은 초록색(0, 255, 0)의 사각형으로 표시된다. `detectMultiScale`의 `scaleFactor`와 `minNeighbors` 파라미터를 조정함으로써 검출 정밀도와 속도 사이의 균형을 조율할 수 있다.

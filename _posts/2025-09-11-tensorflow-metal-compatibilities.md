---
layout: post
title: tensorflow-metal 패키지의 버전별 tensorflow 호환성
date: '2025-09-11'
categories: [system]
tags: [python, machine-learning, tensorflow, tensorflow-metal, macos]
---

## 도입

하위 호환성이 다소 포기된 몇몇 소프트웨어들은 의존성을 엄격히 관리해야 하게 된다. 설령 의존성을 갖는 소프트웨어라고 할지라도, 버전, 빌드에 따라서 제대로 동작하지 않는다.  

지난 학기에서는 &lt;분산시스템&gt; 과목에서 하둡, Hive, HBase, 그리고 Spark를 설정하면서 이 의존성 문제를 절실히 겪었다.  

<br />

텐서플로우도 최초 환경 설정 과정에서 의존성 문제로 시간을 잡아먹는다.  

사실 최근에는 많이 개선되었다. 하지만 맥 환경에서는 GPU 가속을 위해 텐서플로우 개발자들의 손이 닿지 않은 `tensorflow-metal` 확장도 사용해야 하게 되는데, 이쪽 방면은 아직도 문제 해결이 요원하다.  

<br />

![](/static/posts/2025-09-11-tensorflow-metal-compatibilities/pypi-description-compatibilities-table.png)

이번에 맥북을 초기화하고 다시 환경을 잡으면서, [PyPI `tensorflow-metal` 레포 디스크립션의 호환성 표](https://pypi.org/project/tensorflow-metal/)가 실제와 조금 맞지 않는다는 것을 확인했다.  

그래서 호환성 표에 근거하여 직접 여러 버전 조합의 호환성을 검증했다.

<br />

이 작업은 단순히 패키지 설치 후 임포트와 [공식 문서에서의 검증 코드](https://developer.apple.com/metal/tensorflow-plugin/)를 실행하여 프로그램 중단이 없는지 확인하는 것이다.  

또한 호환성 문제가 정말 패키지 간의 문제인지 엄밀하게 검증하지는 않았다. 문제가 확인된 패키지 조합이 정말 대응 버전이 아니기 때문으로 간주하고, 표면적으로 나타나는 예외와 함수 콜스택 그대로를 받아들여도 되는지는 보장하지 못한다.

맥북을 초기화하였어도 발견된 문제가 운영체제에 의해 발생했을 가능성, 패키지 내부 라이브러리가 특정한 하드웨어에서 문제가 발생할 가능성을 완전히 배제하지는 않았다는 의미이다.

## 검증 결과

![](/static/posts/2025-09-11-tensorflow-metal-compatibilities/neofetch.png)  

실행 환경
- MacBook Air (M1, 2020)
- Apple M1 (8코어 CPU, 7코어 GPU, 16GB RAM)
- macOS Sequoia 15.6.1 24G90

<style>
  .content-table th, 
  .content-table td {
    text-align: center;
    vertical-align: middle;
  }
</style>

<p style="text-align: right;"><i>2025-09-12 (금) 기준</i></p>

<table class="table content-table">
  <thead>
    <tr>
      <th>Python</th>
      <th>Tensorflow</th>
      <th>Tensorflow-Metal</th>
      <th>Supports<sup>*</sup></th>
      <th>Import</th>
      <th>Verify</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="19">3.10<sup>**</sup></td>
      <td rowspan="2">2.20.0</td>
      <td>1.2.0</td>
      <td>⚠️</td>
      <td>❌ <sup>1</sup></td>
      <td>-</td>
    </tr>
    <tr>
      <td>1.1.0</td>
      <td>⚠️</td>
      <td>❌ <sup>1</sup></td>
      <td>-</td>
    </tr>
    <tr>
      <td rowspan="2">2.19.0</td>
      <td>1.2.0</td>
      <td>⚠️</td>
      <td>✅</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>1.1.0</td>
      <td>⚠️</td>
      <td>❌<sup>2</sup></td>
      <td>-</td>
    </tr>
    <tr>
      <td>2.18.0</td>
      <td>1.1.0</td>
      <td>✅</td>
      <td>❌<sup>2</sup></td>
      <td>-</td>
    </tr>
    <tr>
      <td>2.17.0</td>
      <td>1.1.0</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>2.16.0rc</td>
      <td>1.1.0</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>2.15.0</td>
      <td>1.1.0</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>2.14.0</td>
      <td>1.1.0</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
    </tr>
    <tr>
      <td rowspan="2">2.13.0</td>
      <td>1.1.0</td>
      <td>❌</td>
      <td>✅</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>1.0.0</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>2.12.0</td>
      <td>1.0.0</td>
      <td>❌</td>
      <td>✅</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>2.12.0</td>
      <td>0.8.0</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
    </tr>
    <tr>
      <td rowspan="2">2.11.0</td>
      <td>0.8.0</td>
      <td>❌</td>
      <td>❌<sup>3</sup></td>
      <td>-</td>
    </tr>
    <tr>
      <td>0.7.0</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌<sup>4</sup></td>
    </tr>
    <tr>
      <td rowspan="2">2.10.0</td>
      <td>0.7.0</td>
      <td>❌</td>
      <td>❌<sup>5</sup></td>
      <td>-</td>
    </tr>
    <tr>
      <td>0.6.0</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
    </tr>
    <tr>
      <td rowspan="2">2.9.0</td>
      <td>0.6.0</td>
      <td>❌</td>
      <td>✅</td>
      <td>❌<sup>6</sup></td>
    </tr>
    <tr>
      <td>0.5.0</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
    </tr>
  </tbody>
</table>

<sup>*</sup> PyPI `tensorflow-metal` 프로젝트 디스크립션의 [호환성 표](https://pypi.org/project/tensorflow-metal/)에 표기된 호환 여부.  
⚠️ 표기는 `tensorflow-metal==1.1.0`의 비고란에 `Fixes compatibility with 2.18+ TF versions`으로 표기되어, 공식적인 호환 여부가 모호한 것임.

<sup>**</sup> Python 3.10 (Python 3.10.18 Jun 5 2025 [Clang 14.0.6])

<sup>***</sup> 아래 traceback에서의 `/opt/miniconda3/envs/metal`는 miniconda3로 생성한 가상환경이다. 의존성 관리는 `python -m pip ...`로 수행하였다.  

<br />

<style>
  .rouge-code pre {
    white-space: pre-wrap !important;
    word-break: break-all !important;
    overflow: auto !important;
  }
</style>

<sup>1</sup> <code>Library not loaded: @rpath/_pywrap_tensorflow_internal.so</code>

```
tensorflow.python.framework.errors_impl.NotFoundError: dlopen(/opt/miniconda3/envs/metal/lib/python3.10/site-packages/tensorflow-plugins/libmetal_plugin.dylib, 0x0006): Library not loaded: @rpath/_pywrap_tensorflow_internal.so
  Referenced from: <D2EF42E3-3A7F-39DD-9982-FB6BCDC2853C> /opt/miniconda3/envs/metal/lib/python3.10/site-packages/tensorflow-plugins/libmetal_plugin.dylib
  Reason: tried: '/opt/miniconda3/envs/metal/lib/python3.10/site-packages/tensorflow-plugins/../_solib_darwin_arm64/_U@local_Uconfig_Utf_S_S_C_Upywrap_Utensorflow_Uinternal___Uexternal_Slocal_Uconfig_Utf/_pywrap_tensorflow_internal.so' (no such file), '/opt/miniconda3/envs/metal/lib/python3.10/site-packages/tensorflow-plugins/../_solib_darwin_arm64/_U@local_Uconfig_Utf_S_S_C_Upywrap_Utensorflow_Uinternal___Uexternal_Slocal_Uconfig_Utf/_pywrap_tensorflow_internal.so' (no such file), '/opt/miniconda3/envs/metal/bin/../lib/_pywrap_tensorflow_internal.so' (no such file)
```

<br />

<sup>2</sup> <code>Symbol not found: __ZN3tsl8internal10LogMessageC1EPKcii</code>

```
tensorflow.python.framework.errors_impl.NotFoundError: dlopen(/opt/miniconda3/envs/metal/lib/python3.10/site-packages/tensorflow-plugins/libmetal_plugin.dylib, 0x0006): Symbol not found: __ZN3tsl8internal10LogMessageC1EPKcii
  Referenced from: <D2EF42E3-3A7F-39DD-9982-FB6BCDC2853C> /opt/miniconda3/envs/metal/lib/python3.10/site-packages/tensorflow-plugins/libmetal_plugin.dylib
  Expected in:     <300F849B-E9A8-3BDA-B8D9-C6617800789D> /opt/miniconda3/envs/metal/lib/python3.10/site-packages/tensorflow/python/_pywrap_tensorflow_internal.so
```

<br />

<sup>3</sup> <code>symbol not found in flat namespace '_TF_GetInputPropertiesList'</code>

```
tensorflow.python.framework.errors_impl.NotFoundError: dlopen(/opt/miniconda3/envs/metal/lib/python3.10/site-packages/tensorflow-plugins/libmetal_plugin.dylib, 0x0006): symbol not found in flat namespace '_TF_GetInputPropertiesList'
```

<br />

<sup>4</sup> <code>Node: 'StatefulPartitionedCall_212'
could not find registered platform with id: 0x106170d30</code>

```
W tensorflow/core/framework/op_kernel.cc:1830] OP_REQUIRES failed at xla_ops.cc:418 : NOT_FOUND: could not find registered platform with id: 0x106170d30
```

```
tensorflow.python.framework.errors_impl.NotFoundError: Graph execution error:

Detected at node 'StatefulPartitionedCall_212' defined at (most recent call last):

(...)

Node: 'StatefulPartitionedCall_212'
could not find registered platform with id: 0x106170d30
	 [[{{node StatefulPartitionedCall_212}}]] [Op:__inference_train_function_23355]
```

<br />

<sup>5</sup> <code>symbol not found in flat namespace '__ZN3tsl8internal10LogMessage16VmoduleActivatedEPKci'</code>

```
tensorflow.python.framework.errors_impl.NotFoundError: dlopen(/opt/miniconda3/envs/metal/lib/python3.10/site-packages/tensorflow-plugins/libmetal_plugin.dylib, 0x0006): symbol not found in flat namespace '__ZN3tsl8internal10LogMessage16VmoduleActivatedEPKci'
```

<br />

<sup>6</sup> <code>segmentation fault python3</code>

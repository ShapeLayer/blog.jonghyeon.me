---
layout: post
title: 전남대학교 AI 8종의 사용 방법에 관하여
date: '2026-08-21'
category: [ai-product]
---

전남대학교에서는 다른 학교와 마찬가지로 학생들에게 [유료 인공지능 사용권을 제공](https://news.kbs.co.kr/news/pc/view/view.do?ncd=8432968)하고 있고, 심지어 다른 학교에 비해 훨씬 빠르게 제공하기 시작했다. 하지만 주요한 프론티어 랩과 직접 계약을 맺지 않고, 서드파티로부터 리셀 계약을 맺어 공급하고 있기 때문에, 다소 생소하거나 불편함을 느끼는 학생들이 많다.  

![](/static/posts/2026-08-21-how-to-use-cnu-ai8types/everytime-finding-user.png)  

한동안은 프론트엔드에 이슈가 있어 스트림 도중에 세션이 중단되어 다시 복구되지 않는 이슈도 있어, [학교에서 제공하는 방식이 효과를 보지 못하고 있다는 기사](https://www.gjdream.com/news/articleView.html?idxno=670478)가 발행되거나, 학내 언론에서 실사용자를 찾는 공지를 내보내기도 했다.  

그래서 아직도 대부분의 학생들은 자체적으로 AI를 구독해 사용하고 있을 것으로 보인다.  

## 사용사례

하지만 나는 학교에서 제공하는 쿼터를 매월 거의 전부 사용하고 있다.  

![](/static/posts/2026-08-21-how-to-use-cnu-ai8types/api-key.png)  

학교의 AI 공급자는 API를 제공하고 있고, [자체 규격의 API](https://hello.timelygpt.co.kr/api/v2/chat/sdk) 외에도 [OpenAI Compatible한 OpenRouter 프록시](https://github.com/timely-hub/timely-gpt-sdk/blob/master/OPENAI_SDK_GUIDE.md)를 제공하고 있다. 문서에 언급되어있듯, 오픈라우터의 모든 모델을 사용할 수 있는 것은 아니지만, 주요한 프론티어 모델들은 전부 사용할 수 있다. 심지는 Max 플랜이 있어야 하는 페이블5나, 많은 쿼터를 필요로 하는 아스트라도 쿼터 내에서 자유롭게 사용할 수 있다. (사용하는 사람이 적으니, 쿼터도 크게 잡혀서 만족스럽게 사용할 수 있었다.)  

<br />

따라서 OpenAI Compatible API를 지원하는 코딩 에이전트 클라이언트를 학교가 제공하는 AI 모델들에 연결해 사용할 수 있다. Codex, 클로드 코드, 오픈코드 등 모두 예외 없이 연결해 사용할 수 있다.  

- [Codex 연결 방법](https://docs.modelstudio.console.alibabacloud.com/en/model-studio/codex)

링크한 가이드는 알리바바 클라우드 모델 스튜디오의 것인데, 중국 모델 제공자들은 오픈AI, 앤트로픽 등의 퍼스트파티 전용 클라이언트의 수정하는 방법을 공식적으로 잘 정리해두어 참조해두었다. 실제로 엔드포인트 링크와 API 키만 바꾸면 바로 연결해 사용할 수 있다.  

### Kilo Code

![](/static/posts/2026-08-21-how-to-use-cnu-ai8types/kilo-settings.png)  

하지만 개인적으로는 Kilo Code와 Open Code에 연결해 사용하고 있다. 이들의 특징은 오픈라우터 외에도 프로바이더를 여러개 연결할 수도, 신규 출시하는 모델을 연결하기도, 모델을 전환하기도 쉽다는 점이다.  

![](/static/posts/2026-08-21-how-to-use-cnu-ai8types/kilo-model-selector.png)  

<br />

![](/static/posts/2026-08-21-how-to-use-cnu-ai8types/kilo-typst.png)  

그래서 Kilo Code로 학교 제공 AI를 연결해, 발표 자료를 Typst로 작성, 디자인이나 반복 적, 혹은 노동 집약적인 작업을 AI 편에 맡기는 식으로 활용하게 되었다.  

이렇게 되니, 보고서, 과제, 발표자료 작성 등을 전부 코드 에디터에서 작업하고, 코드 에디터 확장 프로그램 판 Kilo Code, 혹은 Open Code를 에디터의 터미널 패널에서 실행하고 있다.  

## 연동・사용 방법

1. AI 클라이언트를 설치한다. 아래의 첫 안을 추천한다.  
    1. (권장) [Visual Studio Code(vscode)](https://code.visualstudio.com/)를 설치하고, Kilo Code 익스텐션을 설치: vscode를 설치한 후, [vscode 마켓플레이스에서 Kilo Code를 설치한다.](https://marketplace.visualstudio.com/items?itemName=kilocode.Kilo-Code)  
    2. Open Code를 설치해 연결
    3. Codex, 클로드 코드 등 프론티어 랩의 클라이언트의 설정값을 직접 수정

![](/static/posts/2026-08-21-how-to-use-cnu-ai8types/timely-apikey.png)  

2. 학교에서 제공하는 AI 서비스의 설정에서 「연동 키 관리」 항목을 찾아 키를 발급받는다.  

![](/static/posts/2026-08-21-how-to-use-cnu-ai8types/kilo-customprovider.png)  

3. 설치한 클라이언트의 설정에서 Provider 항목을 찾는다.  
    Kilo Code의 경우 Providers 탭의 하단에 Custom Provider를 추가할 수 있다.  

![](/static/posts/2026-08-21-how-to-use-cnu-ai8types/kilo-config-model.png)

4. 프로바이더를 설정한다. 
    - 중요한 설정
        - Provider API (혹은 API Type): `OpenAI Compatible`
        - Base URL (혹은 API URL, Endpoint): `https://hello.timelygpt.co.kr/api/v2/chat/bridge/openai`
        - API Key (혹은 Access Token): 2번 과정에서 발급받은 키
    - 그 외에 Provider ID, Display Name 등은 프로그램이 내부적으로 사용하거나, 사용자에게 보여주는 이름 등이므로 적절히 설정해도 문제없다.  
    - Kilo Code의 경우, "중요한 설정"의 세 값이 정확히 입력되면 자동으로 사용 가능한 모델을 불러와 어떤 모델을 활성화할 것인지 설정하도록 되어있다. `Add # model(s)`하여 사용할 모델을 추가하여 설정을 마무리한다.  
    ![](/static/posts/2026-08-21-how-to-use-cnu-ai8types/kilo-add-models.png)  
        - Kilo Code의 경우, 나중에 새로운 모델이 업데이트되었을 때, 이 설정 화면에서 새로 추가된 모델이 자동으로 추가할 모델 목록에 나타나는 것을 확인할 수 있다.
        - 자동으로 사용 가능한 모델 목록에 추가되지는 않아서, 직접 선택해 Add하기 전까지는 사용할 수 없다. (모델이 지나치게 많아, 자동으로 모델들을 사용 가능 모델 목록에 추가하면, 모델을 선택할 때마다 불편을 초래할 수 있어, 이 과정은 수동으로 진행하도록 되어있다.)

5. 설정을 마치면 vscode의 경우에는 좌측 탭에 확장 프로그램의 아이콘을 통해 AI 클라이언트를 사용할 수 있다.  

### 추가 팁

대개의 작업은 vscode에 확장 프로그램을 설치해 수행하는 것으로, 앞 작업의 효과를 더욱 볼 수 있다.  

1. 원고, 줄글 텍스트 등을 작성할 때는 vscode에서 `.txt`, `.md` 파일로 작성하고 있다.
    - 워드, 한컴 등의 조판 시스템과는 달리 텍스트에 스타일이 적용되지 않으므로, 작업하는 도중에 폰트나 크기 문제로 골머리를 앓지 않는다.
2. 보고서, PPT 등을 작성할 때는 Typst(`.typ` 파일)로 작성하고 있다.
    - 취향에 따라서는 LaTeX 등 TeX(`.tex`) 계열로 작성해도 된다.  
    - 대부분의 서식은 AI를 통해 Typst 등으로 변환 가능하다. Typst는 소정의 문법만 따르면 충분한 퀄리티의 보고서나 발표 자료를 만들어낸다.
    - [vscode용 Typst 프리뷰](https://marketplace.visualstudio.com/items?itemName=myriad-dreamin.tinymist) 확장을 설치해 미리보기하며 작업할 수 있다.  
        ![](/static/posts/2026-08-21-how-to-use-cnu-ai8types/kilo-typst.png)  
        예: Kilo Code(좌), Typst 파일(중), 슬라이드 프리뷰(우)
3. 코드 에디터이므로 당연히 프로그램 작성에 사용할 수 있다. 또한 로컬의 터미널을 이용할 수 있으므로 (혹은 언어 런타임 익스텐션을 추가해) 컴파일이나 디버그 과정도 AI 편에 제어시킬 수 있다.  

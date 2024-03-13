---
layout: post
title: 2024 상반기 전남대학교 PIMM 알고리즘 파티를 반성하며
date: '2024-03-13'
categories: [review]
tags: [review, project, baekjoon, contest, algorithm]
---

안녕하세요, [&lt;2024 상반기 전남대학교 PIMM 알고리즘 파티&gt;](https://www.acmicpc.net/contest/view/1247) 대회(24년 대회, 핌파티)의 총괄을 맡은 박종현<sup>belline0124</sup>입니다. 이번 대회도 잘 마무리되어서 진심으로 기쁩니다. 특히 저번 대회보다 조금 "우당탕탕"하게 준비한 부분이 있어 조금 불안했는데 정말 다행입니다.

## 시작

24년 대회는 23년 대회를 마무리하고 얼마 지나지 않아 준비하기 시작했습니다. 23년 대회보다 목표를 높게 잡았기 때문에 최대한 준비 기간을 길게 가져가고자 했습니다.

- 23년 대회의 자체 에디토리얼 빌더(turbo-waffle, tw)의 성능 개선
- 아레나 대회로 개최
- 대회 운영비용 최적화
- 대회 운영 워크플로우 최적화, 내부 표준화, 시스템화
- 23년 대회보다 넓은 스펙트럼의 문제셋

**turbo-waffle의 성능 개선**

24년 대회에서도 tw를 계속해서 사용할 생각이었기 때문에, 수 주에 걸쳐 tw를 개선하기 위한 R&D를 수행해보았습니다. 하지만 tw가 충분하지 못한 여건 아래에서 만들어졌기 때문에 개선해야할 점이 한둘이 아니었고, 계획을 변경하다가 가성비 문제로 결국 계획을 드랍하게 되었습니다.

**핌파티 TF 최적화**

동아리 내 핌파티 TF는 꽤 위태롭게 운영되고 있습니다. 고정적인 외부 지원도 없는데다, 출제진, 검수진의 개인 후원으로 운영됩니다. 

23년 대회는 일종의 버킷리스트 느낌이었으므로 출제진 모두들 기꺼이 개인 후원에 큰 돈을 투자했지만 이제는 상황이 다릅니다. 최소한 저부터 대회 자체에 대한 애정이 꽤 식었으니까요. 더 나아가 총괄 업무에서 손을 떼는 것도 고려하고 있었습니다.

그래서 대회 추진 예산도, 운영 워크플로우도 최적화하고 간소화해야했습니다. 제가 없어도 TF가 굴러갈 수 있도록 문서화, 내부 표준화, 동아리 차원의 시스템화를 해야했습니다.

아니면 핌파티 자체가 그만 굴러가도록 놓아줘도 되지만, 그건 아무래도 가슴이 조금 아팠습니다.

**아레나 대회로 개최**

아레나 대회로 개최는 대부분의 백준 대회 TF들의 목표일 것이라고 생각합니다. 아레나 개최로 얻는 효용도 크고, 더 재밌을 것 같고, 뭔가 더 멋지고.. 저 역시도 교내에 대회 홍보할 때 대회 이름 뒤에 "Arena ##"를 붙이는 상상을 하면서 뭔가 멋진데..? 라고 생각했으니 말입니다.

또 TF 비용 최적화 측면에서도 아레나 대회는 빼놓을 수 없는 옵션이었습니다.

**문제 초안 준비**

우선 대부분의 문제는 23년 11월 즈음에 초안 작업이 마무리되었습니다. 저도 아직 군에 복무할 때 상황병 야간 근무를 서면서, 상황이 여유로운 새벽에 작업을 거듭했던 기억이 있습니다.

초안은 출제진당 3문제 정도 준비했으므로 대략 문제의 2배수를 준비한 셈입니다. 이전 대회에서도 그러하였듯, 내부 검수 과정을 거치면서 30%정도의 문제를 제거하고, 30%의 예비 문제를 추가했습니다. (%p가 아니므로 결과적으로 문제 셋이 감소했습니다.)

## 핌파티 추진 공지, 검수 시작

24년이 되고, 전역하는 기차에서 핌파티 추진을 본격적으로 알렸습니다.  

[동시에 검수진 모집을 시작](https://www.acmicpc.net/board/view/133507)했는데, 정말 감사하게도 23년 대회 TF에서 고생해주셨던 분들도 함께 해주신데다가 생각보다 많은 분이 관심을 가져주셨습니다.   

덕분에 굉장히 조기에 검수진 모집을 마감했던 기억이 있습니다. 기본적으로 결격사유가 없는 이상 지원하신 분들과 되도록 함께하고자 해서 벌어진 소소한 해프닝이었습니다.  

## 그래픽 리소스, 솔브드 프로필 배경과 뱃지

### 졸업식 현수막으로 사골 끓이기

핌 파티 참여 상품으로 제공하는 솔브드 프로필 배경은 사실 전기 학위수여식에서 사용한 현수막입니다.

우선 TF 내에서는 리소스를 만들어 낼 인력도, 여유도 없었기 때문에 어딘가에는 제작을 의뢰해야 했습니다. 저번처럼 솔브드에 작업을 의뢰하는 것도 고려했지만 비용 최적화 측면에서 피하고 싶은 옵션이었습니다.

![_DSF2418.jpeg](/static/posts/2024-03-13-rewinding-24-1-pimm-party/DSF2418.jpeg)

이렇게 배경 리소스로 한창 고민중일 때, 마침 동아리에서 졸업식 현수막을 위해 작업하고 있었던 현수막 작업이 마무리되었습니다. 처음에 현수막 리소스를 받아보고는 이거다! 싶었습니다. 조금만 수정하면 배경으로 활용할 수 있겠거니 싶을 정도로 퀄리티가 좋았습니다.

![IMG_5462.JPG](/static/posts/2024-03-13-rewinding-24-1-pimm-party/IMG_5462.JPG)

잿가루만 남을 위기에 처한 배경 리소스는 치킨 하나와 맞바꿔서 불구덩이에서 구출해냈습니다. 희수님 대회 협조 감사합니다 ㅎㅎ..

### 양말대를 솔브드로!

어느 학교나 다 그렇듯, 학교를 주제로 한 인스타툰 작가님이 한두 분씩 계십니다. 제 입대 전인 21-22년도에는 양말대가 교내에서 유명한 인스타툰이었습니다. 꽤 활동적이었고, 굿즈도, 이벤트도 여러번 배포하고 열고 했으니 아마 당시에 가장 인기있지 않았을까 싶습니다.

<blockquote class="instagram-media" data-instgrm-captioned data-instgrm-permalink="https://www.instagram.com/p/CEvy-HKFu4H/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:16px;"> <a href="https://www.instagram.com/p/CEvy-HKFu4H/?utm_source=ig_embed&amp;utm_campaign=loading" style=" background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;" target="_blank"> <div style=" display: flex; flex-direction: row; align-items: center;"> <div style="background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;"></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 100px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;"></div></div></div><div style="padding: 19% 0;"></div> <div style="display:block; height:50px; margin:0 auto 12px; width:50px;"><svg width="50px" height="50px" viewBox="0 0 60 60" version="1.1" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g transform="translate(-511.000000, -20.000000)" fill="#000000"><g><path d="M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.652,21.575 C558.743,20.834 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.257,20.834 521.349,21.575 C519.376,22.342 517.703,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.574,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.035,40.831 511,41.851 511,50 C511,58.147 511.035,59.17 511.181,62.369 C511.326,65.562 511.834,67.743 512.574,69.651 C513.342,71.625 514.368,73.296 516.035,74.965 C517.703,76.634 519.376,77.658 521.349,78.425 C523.257,79.167 525.438,79.673 528.631,79.82 C531.831,79.965 532.853,80.001 541,80.001 C549.148,80.001 550.169,79.965 553.369,79.82 C556.562,79.673 558.743,79.167 560.652,78.425 C562.623,77.658 564.297,76.634 565.965,74.965 C567.633,73.296 568.659,71.625 569.425,69.651 C570.167,67.743 570.674,65.562 570.82,62.369 C570.966,59.17 571,58.147 571,50 C571,41.851 570.966,40.831 570.82,37.631"></path></g></g></g></svg></div><div style="padding-top: 8px;"> <div style=" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;">Instagram에서 이 게시물 보기</div></div><div style="padding: 12.5% 0;"></div> <div style="display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;"><div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);"></div> <div style="background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(3px) translateY(1px); width: 12.5px; flex-grow: 0; margin-right: 14px; margin-left: 2px;"></div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(9px) translateY(-18px);"></div></div><div style="margin-left: 8px;"> <div style=" background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 20px; width: 20px;"></div> <div style=" width: 0; height: 0; border-top: 2px solid transparent; border-left: 6px solid #f4f4f4; border-bottom: 2px solid transparent; transform: translateX(16px) translateY(-4px) rotate(30deg)"></div></div><div style="margin-left: auto;"> <div style=" width: 0px; border-top: 8px solid #F4F4F4; border-right: 8px solid transparent; transform: translateY(16px);"></div> <div style=" background-color: #F4F4F4; flex-grow: 0; height: 12px; width: 16px; transform: translateY(-4px);"></div> <div style=" width: 0; height: 0; border-top: 8px solid #F4F4F4; border-left: 8px solid transparent; transform: translateY(-4px) translateX(8px);"></div></div></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center; margin-bottom: 24px;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 224px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 144px;"></div></div></a><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/p/CEvy-HKFu4H/?utm_source=ig_embed&amp;utm_campaign=loading" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;" target="_blank">양말대(@socks_univ)님의 공유 게시물</a></p></div></blockquote> <script async src="//www.instagram.com/embed.js"></script>

무엇보다 캐릭터 자체가 용봉캠퍼스 모양에서 유래했다는 점이 마음에 쏙 들었습니다. 

그래서 사실 23년 대회에 잡았던 목표 중 하나가 양말대 캐릭터를 솔브드에 등록하는 것이었습니다. 하지만 23년도는 군 복무중인 시기였고, 외부에 협조 요청으로 연락 주고받는 것이 여러모로 부담이었던지라 제대로 이루어지지 못했습니다.

그리고 24년에 이르러 다시 양말대를 솔브드로!를 추진하게 되었습니다. 사실 양말대 활동이 어느정도 중지된 상황이기도 한데다 양말대 작가님 입장에서는 TF에 협조해주실 이유가 하나도 없었기 때문에 반쯤 포기하고 있었습니다. 양말대가 다른 곳과 협업을 하는 것을 거의 본적 없기도 했구요. 그래서 양말대 작가님께서 협업 제안을 수락해주셔서 너무 감사했습니다.

작가님 감사합니다..!

### 포스터.. 만들기

백준 홍보 게시물에는 따로 사용하지 않았지만, 교내에서 홍보에 사용하기 위해 만든 포스터와 카드뉴스도 있습니다. 사실 이쪽은 계획이 있지는 않았습니다.

포스터는 학과 신입생 OT에 대응해서 자료를 만드는 중에 만들었습니다. 뭔가 이것저것 자료를 넣다 보니, 이 참에 신입생들한테 대회 홍보하자! 라는 의견이 있었습니다.

마침 자료 양도 뻥튀기해야겠다 싶어서, 주변의 도움을 받아 이것저것 만들었습니다.

![Basic.png](/static/posts/2024-03-13-rewinding-24-1-pimm-party/Basic.png)

포스터는 23년 대회 [&lt;C. 인기투표&gt;](https://www.acmicpc.net/problem/29616) 문제 그림을 만들어준 강도희 씨한테 다시 한번 도움을 받았습니다. 처음엔 조언만 좀 받으려고 도움을 부탁했는데, 어느 순간 자기 일처럼 본격적으로 이것저것 해주는걸 보고 너무너무 고마웠습니다.

항상 고마워요 도희 누님!

<blockquote class="instagram-media" data-instgrm-captioned data-instgrm-permalink="https://www.instagram.com/p/C37DSE9LjAR/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:16px;"> <a href="https://www.instagram.com/p/C37DSE9LjAR/?utm_source=ig_embed&amp;utm_campaign=loading" style=" background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;" target="_blank"> <div style=" display: flex; flex-direction: row; align-items: center;"> <div style="background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;"></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 100px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;"></div></div></div><div style="padding: 19% 0;"></div> <div style="display:block; height:50px; margin:0 auto 12px; width:50px;"><svg width="50px" height="50px" viewBox="0 0 60 60" version="1.1" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g transform="translate(-511.000000, -20.000000)" fill="#000000"><g><path d="M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.652,21.575 C558.743,20.834 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.257,20.834 521.349,21.575 C519.376,22.342 517.703,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.574,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.035,40.831 511,41.851 511,50 C511,58.147 511.035,59.17 511.181,62.369 C511.326,65.562 511.834,67.743 512.574,69.651 C513.342,71.625 514.368,73.296 516.035,74.965 C517.703,76.634 519.376,77.658 521.349,78.425 C523.257,79.167 525.438,79.673 528.631,79.82 C531.831,79.965 532.853,80.001 541,80.001 C549.148,80.001 550.169,79.965 553.369,79.82 C556.562,79.673 558.743,79.167 560.652,78.425 C562.623,77.658 564.297,76.634 565.965,74.965 C567.633,73.296 568.659,71.625 569.425,69.651 C570.167,67.743 570.674,65.562 570.82,62.369 C570.966,59.17 571,58.147 571,50 C571,41.851 570.966,40.831 570.82,37.631"></path></g></g></g></svg></div><div style="padding-top: 8px;"> <div style=" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;">Instagram에서 이 게시물 보기</div></div><div style="padding: 12.5% 0;"></div> <div style="display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;"><div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);"></div> <div style="background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(3px) translateY(1px); width: 12.5px; flex-grow: 0; margin-right: 14px; margin-left: 2px;"></div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(9px) translateY(-18px);"></div></div><div style="margin-left: 8px;"> <div style=" background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 20px; width: 20px;"></div> <div style=" width: 0; height: 0; border-top: 2px solid transparent; border-left: 6px solid #f4f4f4; border-bottom: 2px solid transparent; transform: translateX(16px) translateY(-4px) rotate(30deg)"></div></div><div style="margin-left: auto;"> <div style=" width: 0px; border-top: 8px solid #F4F4F4; border-right: 8px solid transparent; transform: translateY(16px);"></div> <div style=" background-color: #F4F4F4; flex-grow: 0; height: 12px; width: 16px; transform: translateY(-4px);"></div> <div style=" width: 0; height: 0; border-top: 8px solid #F4F4F4; border-left: 8px solid transparent; transform: translateY(-4px) translateX(8px);"></div></div></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center; margin-bottom: 24px;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 224px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 144px;"></div></div></a><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/p/C37DSE9LjAR/?utm_source=ig_embed&amp;utm_campaign=loading" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;" target="_blank">전남대학교 게임개발동아리 PIMM(@pimm.jnu)님의 공유 게시물</a></p></div></blockquote> <script async src="//www.instagram.com/embed.js"></script>

그리고 이참에 카드뉴스도 제작했습니다. 이쪽은 사실 대회 홍보를 의도한 것은 아닙니다. 동아리 연락 창구 느낌으로 인스타그램 계정을 새로 만들었는데, 게시물이 없어 너무 휑한 느낌이었습니다. 그래서 뭐라도 넣자는 느낌으로 만들었습니다.

카드 뉴스는 핌 인스타그램 담당자인 박현솔 님과 TF의 [김근성<sup>onsbtyd</sup>](https://www.acmicpc.net/user/onsbtyd) 씨가 담당해주셨습니다. 두분 모두 고생 많았어요!

포스터와 카드뉴스 모두 흠을 잡자면 오픈 컨테스트를 Competition이라고 표현한건데.. 사실 제가 벌인 잘못이기도 하고, 문제를 알아차렸을 땐 이미 너무 늦었어서, 대회 영문 명칭 자체를 "PIMM Algorithm Party Competition"라고 생각하기로 했습니다.

## 똥통에 빠진 휴대폰, 똥통에 빠진 총괄

대회 추진은 절대 23년 대회같이 잘 흘러가지 못했습니다. [&lt;똥통에 빠진 휴대폰&gt;](https://github.com/ShapeLayer/blog.jonghyeon.me/tree/main/static/posts/2024-03-13-rewinding-24-1-pimm-party/phone-in-toilet.md)이라고, 제 출제 역량을 벗어나는 문제를 출제했던 것이 문제였습니다.

원래대로라면 검수 과정이 지연되거나 출제 역량을 벗어난다고 판단한 문제는 과감하게 자릅니다. 23년 대회때도, 이번에도 그렇게 잘려나간 문제가 꽤 있습니다. 사실 몇번 자르려고 했는데, 출제진 사이에서 난이도 곡선 생각하면 살려야 한다, 조금 시간을 두고 보자 의견이 꽤 있었던지라 제때 자르지 못했습니다.

결과적으로 대회 진행과 총괄 업무에 비중을 많이 줄 수 있었던 23년 대회와 달리, 이번 대회는 대부분의 시간을 이 &lt;똥통에 빠진 휴대폰&gt; 문제를 수정하는데 사용하게 되었습니다. 대회 관계자 사이에 끼어서 이런 저런 사항을 조정하고, 대회 전반을 확인해야하는 총괄이 문제 하나에만 잡혀있었던 셈입니다.

그리고 이 문제는 그렇게 많은 투자를 했음에도 결국 잘라낼 수밖에 없었습니다.

그래서 추진 일정을 조정하는데 꽤 차질이 있었고, 많은 부분의 운영을 검수진의 우려, 조언, 관심에 의존했습니다. 정말 죄송한 일입니다.  

![](/static/posts/2024-03-13-rewinding-24-1-pimm-party/스크린샷%202024-03-13%20오후%205.37.15.png)  
_...네_

## 주변에서 불이 나요

대회 한두달 전부터 주변에 크고 작은 이슈가 터지면서 핌 파티도 꽤 영향을 받았습니다.

이슈가 있을때마다 출제진에게 정해 논리가 정말 잘 증명되는지 체크해달라고 몇 번씩 주문했고, 검수진도 더 타이트한 조건으로 이런 저런 테스트를 돌려보거나 했습니다. 특히 &lt;힘세고 강한 아침&gt; 문제가 고생하면서 이 과정에서 정말 다양한 사이드케이스, 저격 데이터를 찾아낸 것으로 압니다.

검수 자체도 더 빡빡하게 이루어져서, 각종 논리, 컨벤션, 표현을 체크하고 또 체크하고.. 같은 부분도 수 없이 체크했습니다. 아직도 "~는 정의되지 않았습니다. 정의를 넣거나 표현을 수정해야합니다."는 자주 들어서 아직도 기억에서 잊히질 않습니다.

관계없을지 모르지만 솔브드 아레나 문의를 이 시기를 전후해서 컨택했는데, 솔브드도 이런 저런 처리가 지연되는 모양이었습니다. 결국 제반 상황이나 여건이 충족되지 않아 핌파티의 아레나 포맷 적용도 불발되었습니다.

## 라스트 댄스

23년 대회때도 잘 조정하지 못했는데, 본문 컨벤션 맞추기는 꽤 많이 소모적인 일입니다. 9개에 이르는 본문의 분위기, 용어 사용, 어체를 통일하는 작업이 절대 쉬울 리 없습니다.

![IMG_5425.jpg](/static/posts/2024-03-13-rewinding-24-1-pimm-party/IMG_5425.jpg)

컨벤션 조정은 대회 전날인 9일 토요일 심야에 진행했습니다. 대회 시작으로부터 24시간이 채 남지 않은 시간입니다. 당초 계획은 20시부터 한시간동안 검수하는 것이었지만, 시간 계획을 잘못 짜도 단단히 잘못짰습니다.

컨벤션 조정은 20시부터 2시까지 쉬지 않고 6시간 강행군이었습니다. 모두 각자의 사정에 맞춰 중간에 들어왔다 나갔다 했지만, 대부분 5~6시간 함께해주셨습니다. 다시 생각해도 TF의 모두들, 정말 대단하십니다.

## 대회 모니터링

![](/static/posts/2024-03-13-rewinding-24-1-pimm-party/스크린샷%202024-03-13%20235311.png)  

데이터 보강은 대회 직전까지 이어져서, 정말 정신없이 시간을 보냈습니다. 마지막으로 데이터 최종 체크하고, 이와중에 새로 제기되는 사이드케이스들, 별해를 막을지 말지.. 모두가 이성을 살짝 놓은 것 같기도 했습니다. 저 역시 &lt;똥통에 빠진 휴대폰&gt;에 시간을 쏟느라 &lt;전역 역전&gt;에는 힘을 많이 쏟지 못했기 때문에 마지막의 마지막까지 작업을 거듭할수밖에 없었습니다.

![Untitled](/static/posts/2024-03-13-rewinding-24-1-pimm-party/2403101455.png)

&lt;전역 역전&gt; 작업이 어느정도 마무리된 뒤에는 에디토리얼 작업에 들어가느라 여전히 대회 진행에는 깊게 신경쓰지 못했습니다. 23년 대회에서도 에디토리얼 작업때문에 대회 진행에 신경을 막 쓰진 못했던 것 같은데, 이번에도 이렇게 되어버렸습니다.

![](/static/posts/2024-03-13-rewinding-24-1-pimm-party/KakaoTalk_20240313_224552660_11_.jpg)

다행히도 &lt;전역 역전&gt;에 질문이나 오류가 없어서 대회 진행에 큰 문제는 없었습니다.  

## 에디토리얼

tw 성능 개선 작업을 포기하고, 에디토리얼을 준비하면서도 선택지가 꽤 여럿 있었습니다. 대표적으로는.. 그래도 tw를 사용해서 에디토리얼을 뽑아낼 것인가? UCPC 2020 솔루션 레이텍을 사용할 것인가? 그냥 마크다운 파일을 깃허브에 올리고 말 것인가? 입니다.

![Untitled](/static/posts/2024-03-13-rewinding-24-1-pimm-party/2403081138.png)

지금 백준에서 열리는 대부분 오픈 컨테스트들의 에디토리얼이 UCPC 2020 솔루션 스타일을 채택해서 공개되고 있으므로, 백준 대회의 표준 에디토리얼이 UCPC 2020으로 자리잡았구나 하는 생각은 있었습니다.

게다가 이번엔 비용 최적화라던가, 에디토리얼에 추가로 들일 여유도 없고 해서, 전 대회처럼 에디토리얼을 책자로 뽑아낼 생각은 하지 않았습니다. 그래서 자연스럽게 UCPC 2020 스타일로 갔던 것 같습니다. typst 이야기 나온 김에, kiwiyou님께서 typst 버전 템플릿을 제공해주셔서 이번엔 typst로 쪄냈습니다.

![Untitled](/static/posts/2024-03-13-rewinding-24-1-pimm-party/pimm-dev-github-repo.png)

여담으로 저번 대회와 달리 소스를 함께 공개하지 않은것도 저희가 직접 짜낸 소스가 아니기 때문이었습니다.

함부로 공개해도 될지 감은 안잡히고.. 이거 통짜로 올려도 되나요? 하고 물어보는 것도 어딘가 이상한 것 같고.. 무엇보다 어딘가에 연락 넣고 물어보는 걸 근래 몰아서 너무 많이 했더니 피로감에 덮여서 이런 것 하나 물어볼 여력도 없었습니다.

## 다음 대회를 열게 된다면..

✅ 는 이번 대회에서 잘 해냈다고 생각한 사항이나 앞으로 가져야 할 태도, ⚠️ 는 이번 대회에서 잘 안되었다고 생각한 사항이나 앞으로 피해야 할 태도입니다.

* ⚠️ 당연한 이야기지만, 모든 출제자가 각 출제 문제를 제대로 다룰 능력이 있는지 확인해야합니다. &lt;똥통에 빠진 휴대폰&gt;은 그게 제대로 이루어지지 않았습니다.
  * ✅ &lt;똥통에 빠진 휴대폰&gt;은 문제를 다루는 데 있어 필요한 역량이 어느정도 수준인지 제대로 가늠하지 못한 것도 있다고 생각합니다. 이런 일을 대비해 검수진을 모집하므로, 우선 검수진을 통해 역량 요구사항을 평가해보는 것도 괜찮을 것 같습니다.

* ✅ TF 총괄같이 무언가 잡일이 많은 역할을 맡게 되면 자신 역량 미만의 문제를 출제해야 합니다. 역량 수준의 문제보다도 난이도가 낮은 문제를 출제하면서 여유를 만들어야합니다.
  * ✅ 그래야만 출제 작업 외에도 TF에 산재한 이슈들을 처리할 수 있고, 예상치 못한 비상 상황에서도 주도적으로 일을 이끌어나갈 수 있습니다.

* ⚠️ 검수진이 열심히 검수하면 검수 내용이 순수하게 양적으로 많습니다. 그럼에도 불구하고 출제진은 검수진의 의견을 "프리패스"해서는 안됩니다.
  ![](/static/posts/2024-03-13-rewinding-24-1-pimm-party/스크린샷%202024-03-14%20001256.png)  
  * ⚠️ 특히 컨벤션 잡을 때, 단어 한 두개의 수정 의견은 특별한 평가 없이 수용하게 됩니다. 체력적으로나 비용적으로나 모든 의견에 대해서, 의견을 반영했을 때의 영향을 고려하는 것은 부담되는 일입니다.
  * ⚠️ 그럼에도 불구하고, 각 의견이 무엇을 의도하고 제시된 것인지, 의견을 반영했을 때 어떠한 결과를 초래하는지 등을 면밀히 판단하지 않으면 지문 전체를 갈아엎어야 하게 될지도 모릅니다.

* ✅ 무엇이든 TF에 의견이 제시된다면 최대한 12시간 내에는 의견이 평가되고 이야기가 진전되어야 합니다. 또 어떤 일이든 12시간 내에는 완료되지 않았더라도 진척 상황을 공유해야 합니다.
  * ✅ "~~라고 생각해봤는데, 이 방향은 잘 안되는 것 같습니다. 조금만 더 시간을 주세요."와 같이 최소한 답이 나오지 않더라도 누구든 본인 사고의 진척 상황은 표현해야합니다. 
  * ⚠️ 만약 의견 이어나가기가 끊긴다면, 모두들 점차 잊게 되고 한참 뒤에서야 논의가 재개되어 일정이 지연될 수 있습니다.
  * ✅ 맡은 업무의 진척 상황을 특정 시간 간격으로 공유해야만 한다면 어떻게든 업무를 진척시키는 효과가 있습니다. "타이니 데드라인" 느낌인 것 같습니다.
    * ⚠️ &lt;똥통에 빠진 휴대폰&gt; 문제는 이게 잘 안되었습니다.

* ⚠️ 항상 전체 기간의 30%를 여유 기간으로 잡고, 지속적으로 데드라인을 설정해야 합니다.
  * ✅ 데드라인을 설정하면 100% 수준은 아니더라도 일이 어느정도 진행됩니다. 또, 지금 TF가 전체 공정에서 어느 수준까지 도달했는지 추정하기 쉬워지고, 앞으로의 계획을 설계하기도 용이합니다.
  * ✅ 저번 대회에서는 보름에 한 번 꼴로 죽이 되는 밥이 되든 데드라인을 설정했었습니다. 그 덕분인지 이번 대회처럼 대회 전날에 6시간 마라톤 회의를 경험하지는 않았었습니다.

* ⚠️ 이번 대회는 솔브드 아레나 형식 적용을 추진했던 첫 번째 대회입니다. 아레나 적용 가이드라인을 숙지하지 못해서 이런 저런 조율로 추진이 지연되다가 불발되었습니다.
  * ✅ 다음에는 낯선 일을 할 때 조금 더 여유를 두고, 불명확한 부분은 최대한 빨리 관계자에게 문의하거나 협의해야할 것 같습니다.

* ✅ 양말대를 솔브드에 등록하자는 목표 하나로 무작정 양말대 계정을 두드렸습니다. 무작정 두드리는 것이 옳은지 옳지 않은 것인지는 차치하고서라도, 최대한 예의를 갖춰 컨택한 목적을 명확히 밝힌 것은 짚어둘만한 것 같습니다.
  * ✅ 무슨 일이든 안하고 후회하는 것보다 하고 후회하는 것이 더 나은 것 같습니다.

## 마무리

![Untitled](/static/posts/2024-03-13-rewinding-24-1-pimm-party/2403121854.png)

준비 기간을 오래 잡고 갔는데도, 결과물은 그에 비해 막 만족스럽지 않은 것 같습니다. 대회 자체만 놓고 보면 큰 문제 없이 난이도 커브도 그럭저럭 그려졌으니 꽤 성공적이라고 볼 수도 있습니다.

그럼에도 불구하고 시작할 때 잡았던 목표는 잘 달성해내지 못했고, 많은 것을 포기해야했던 것, 그러면서도 끝까지 위태로웠던 것은 결코 바람직하지 못했던 것 같습니다.  

당연한 말이지만, 오래 준비한다고 해서 항상 결과가 좋지만은 않다는 것을 경험하게 된 좋은 기회였던 것 같습니다.

## Special Thanks

이번 대회는 제가 할 일을 다른분께서 해주시거나 해서 모두에게 죄송하고 감사한 마음이 큽니다.  

특히 몇몇분은 정말 대회 준비에 핵심적인 역할을 해주셨습니다.

* utilforever - 저번 대회에 이어 소중한 사재를 TF에 지원해주셨습니다. 항상 감사합니다.

* measurezero, vkdldjvkdnj - 정말 열성적으로 검수해주신 검수진이십니다. 이분들 덕에 검수 전체 지문 $N$회독이라는 말을 처음 들었습니다.

* kiwiyou - 저번 대회에 이어 기술적으로 도움을 주셨습니다. 덕분에 에디토리얼 배포를 문제 없이 마무리할 수 있었습니다.

## 더 읽어보기

- [2024 상반기 전남대학교 PIMM 알고리즘 파티 후기](https://b1ackhand.tistory.com/276) - 이윤수<sup>lys9546</sup>

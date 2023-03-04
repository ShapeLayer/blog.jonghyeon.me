---
layout: post
title: Eleventy와 Stylus를 이용한 블로그 작성
date: '2023-03-04'
categories: [web, blog]
tags: [web, blog, nodejs, eleventy, stylus]
---

최근 부대 안에서 종종 책을 읽게 되면서 독서 기록을 남기는 일이 잦습니다. 무언가 독후감을 작성해보겠다기보다 책을 읽고 덮으면 얼마 지나지 않아 잊어버리게 되니 책 내용을 기록하는 행위에 가깝습니다. 독서기록을 그냥 노트에 작성해두기만 하려고 보니 군 부대 안에서 노트를 계속해서 보관하는 것이 부담스러웠습니다. 개인 물건을 보관할 자리도 많지 않은데다, 서류대, 사물함(으로 사용중인 신발장) 모두 책으로 가득해 새 물건을 늘리기보다 줄여나가야 하기도 했습니다. 이를 계기로 [별도의 블로그를 개설하여](https://books.jonghyeon.me) 독서 기록을 노트에서 인터넷으로 옮기기 시작했습니다.  

## 블로그 엔진 고르기
요즘 많은 블로그들이 Jekyll으로 운영됩니다. 무료고, 커스터마이징 편의도 높아 좋은 디자인을 구성하기도 어렵지 않습니다. 이제는 원래의 형태를 확인하기 어렵지만 입대 직전에 제가 작성한 [호남 대학간 침해대응/분석 대회 2022](https://hccc2022.github.io)와 [IWFCV 2023](https://iwfcv2023.github.io/) 사이트 역시 Jekyll을 사용하고 있습니다.  

Jekyll은 분명히 유용하고 간편해서 독서 기록 블로그에도 사용할 만 합니다. 그렇지만 무언가 아쉽습니다. 너무 많은 사람들이 Jekyll을 사용한 나머지 더 이상 매력적인 소프트웨어가 아니게 되었습니다. 새로 사이트를 만들어도 흔한 Jekyll 사이트 내지 깃허브 사이트들 중 하나 정도로 치부될 것 같았습니다.  

그래서 이번엔 Eleventy를 사용해보았습니다. Eleventy도 Jekyll과 비슷하게 동작합니다. 마크다운 파일을 HTML로 빌드하는 것이 주 기능입니다. 차이점이 있다면 조금 더 많은 종류의 템플릿 언어와 문서 형식을 사용할 수 있다는 것입니다. [실제로 Eleventy 문서를 참조하면 다양한 형식의 코드 예시가 첨부되어 있는 것을 확인할 수 있습니다.](https://www.11ty.dev/docs/layouts/)

## SCSS 대신 Stylus 사용하기
그래서 새 시도를 시작한 김에 한가지 새 시도를 더 했습니다. Jekyll에선 SCSS를 주로 사용했지만, [이번엔 Stylus를 사용했습니다.](https://github.com/ShapeLayer/bookshelf/tree/main/src/stylus)  

```stylus
.cards
  display: grid
  grid-column: 2 / span 12
  grid-template-columns: repeat(12, minmax(auto, 60px))
  grid-gap: 40px
  list-style: none
  padding: 0
  @media only screen and (max-width: 500px)
    grid-column: 2 / span 6
    grid-template-columns: repeat(8, 1fr)
    grid-gap: 20px
```

사실 Jekyll과 Eleventy의 관계처럼 Stylus도 SCSS와 비교해서 큰 틀에서 스타일 정의 매커니즘이 달라진 것은 없으므로 단순히 새로운 언어 포맷을 도입한 것에 지나지 않긴 합니다.  

## Eleventy를 사용하며
Eleventy는 Node.js를 기반으로 하므로 Ruby 기반의 Jekyll보다 웹 라이브러리가 다소 더 풍부한 감이 있습니다. Stylus 역시 npm 패키지 매니저가 없었다면 생각조차 하지 못했을 것입니다.  

Eleventy는 꽤 매력적이지만 여전히 부족합니다. Eleventy 소개 포스트를 오래전에 접한 것 같은데도 아직 미완성이라는 인상이 강합니다. 블로그 작성 도중 사용하려고 했던 기능들은 2.0 실험 버전에서나 사용 가능한 것이 많았으므로 1.* stable 본에서는 사용감이 만족스럽지는 않았습니다.  
\* _현 시점에서 2.0이 릴리즈된 모양이나, 제대로 사용하려면 여유 시간이 조금은 더 필요할 것 같습니다._  

## 마무리
[bookshelf라고 이름 붙인 독서 기록 블로그](https://books.Jonghyeon.me)는 우선 동작이 되는 수준에는 이르렀습니다. 한동안 계속 원인 모를 버그로 삽질을 하는데 집중했기 때문에 디자인이나 이것저것 상상한 수준만큼 블로그를 만들어내진 못했습니다.  

bookshelf가 어느정도 만들어지자마자 독서 속도가 뚝 떨어진 것 같지만 5주간 이어진(!) [군 FTX](https://en.wikipedia.org/wiki/Field_training_exercise)의 영향이라고 생각하고 다시 열심히 책을 읽을 수 있도록 노력해봐야겠습니다.  

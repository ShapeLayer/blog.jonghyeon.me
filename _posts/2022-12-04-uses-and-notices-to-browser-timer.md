---
layout: post
title: 웹에서 마우스 오버 시 더 많은 소수부를 보여주는 실수 구현; 브라우저의 Nested time
date: '2022-12-04'
categories: [web, browser]
tags: [web, browser, computer-science, javascript, svelte]
---

## 야호 해냈다
![](/static/posts/2022-12-04-uses-and-notices-to-browser-timer/RPReplay_Final1670122781.webm)

어제 개인 프로필 사이트를 수정하며 군 복무율에 마우스를 올리면 진행도의 표현 소수점이 늘어나는 기능을 추가했습니다.  
간단한 기능이지만, 구현하며 고민했던 것들을 정리하려고 합니다.  

## onHover 계열 이벤트들은 CSS 속성 제어만을 위해 사용하는 것이 아니다.
onHover 계열 이벤트들은 CSS 속성 제어만을 위해 사용하는 것이 아닙니다.  
당연한 말이지만 onHover는 주로 CSS 단계에서 작성했으므로 다른 방법으로 구현하는 것을 생각하지 못했습니다.  

위 사항을 추가하기 위해 제일 처음 시도한 건 아래 코드입니다.  

```css
.percentage {
  width: 30%;
  overflow: hidden;
  transition: .2s ease-in-out;
}
.percentage:hover {
  width: 100%;
  transition: .2s ease-in-out;
}
```

당연히 잘 될 리 없었습니다.  
CSS는 위 기능을 만들어내기 위해 존재하는 것이 아닙니다. 지정한 HTML 엘리멘트의 크기를 임의로 줄이더라도 텍스트는 여전히 제대로 출력해야 하므로 단순히 강제 개행이 될 뿐입니다.  

이렇게 접근한 이유는 지금의 구현 방식이 조금 거부감이 있었기 때문입니다.  
하지만 이제와서 생각해보면 이 방식은 생각한대로 작동한다 하더라도 사용하지 않아야 할 이유가 더 많았으므로 처음부터 틀린 방식인 모양입니다.  

## setInterval과 clearInterval을 번갈아가며 사용하기
```svelte
<span
  id="percentage-displayer"
  on:mouseover={onMouseOverHandler}
  on:mouseout={onMouseOutHandler}
  on:focus={onMouseOverHandler}
  on:blur={onMouseOutHandler}
>{ leftPercentage }%
</span>
<script lang="ts">
  let displayUpdater: any
  $: leftPercentage = Math.max((1 - nowLefts / totalLefts) * 100, 0).toFixed(displayPoint)
  ...
  const __invokeUpdater = (fn: Function, ms: number) => {
    clearInterval(displayUpdater)
    displayUpdater = setInterval(fn, ms)
  }
<script lang="ts">
```
지금의 사이트는 복무율에 마우스오버 시 `clearInterval`과 `setInterval`을 번갈아가며 실행합니다.  
왠지 위 두 API를 번갈아가며 실행하면 브라우저에 부하를 일으킬것만 같은 근거없는 느낌이 있었으므로, 이 방식을 피하고자 했습니다.  

당연하게도 실제로 큰 부하는 없었습니다.  

## setTimeout으로 재구현해보기
구현 목표는 달성했지만, 여전히 아쉽습니다.  
분명 더 많은 소수부를 표현하면 더 빨리 복무율을 갱신해야할 필요가 있었으므로 많은 양의 함수 호출은 불가피합니다.  

하지만 복무율을 펼치는 과정에서도 완전히 펼쳤을 때 수준만큼 함수를 호출할 필요는 없습니다.  
예를 들어 소수점 아래 2자리에서 12자리가 보이도록 복무율 소수점 표현이 전환되는 과정에 있다고 생각해봅시다.  

![](/static/posts/2022-12-04-uses-and-notices-to-browser-timer/apple_promotion.webm)  
_Source: Apple_  

12자리가 표시될 때만큼의 함수 호출이 9자리가 표시될 때 이루어질 필요가 없습니다. 마치 고주사율 디스플레이 휴대기기에서 사용하는 가변 주사율처럼 말이죠.  
따라서 setTimeout을 사용하여 재귀적으로 소수점 표현 자릿수를 수정하고 복무율을 갱신해보려고 시도했습니다.  

```svelte
...
<script lang="ts">
  const processUpdateDisplayValueInDurationSetTimeout = (toFixed, nextInterval, deltaIntervalInCalls) => {
    setTimeout(() => {
      if (toFixed == displayPoint) {
        invokeDisplayValueToSetInterval()
      } else {
        //call internal
        if (deltaIntervalInCalls > 0) isFolded = true
        else isFolded = false
        __followDisplayFixedPointUsingTimeout(toFixed)
        __setDisplayUpdateInterval(nextInterval)
        processUpdateDisplayValue()
        processUpdateDisplayValueInDurationSetTimeout(toFixed, nextInterval + deltaIntervalInCalls, deltaIntervalInCalls)
      }
    }, nextInterval)
  }
  ...
</script>
```

확실한건 기능의 복잡성에 비해 코드의 복잡성이 지나치게 커졌다는 사실입니다. 난방도 안되는 컨테이너 사지방에서 얼어버린 손가락으로 계속 작업을 진행하기에는 의욕만 꺾일 일이었으므로 다시 롤백할하기로 했습니다.  
게다가 이 방법 역시 CSS때와 마찬가지로 고려하지 못한, 사용하지 않아야 할 이유가 많았으므로 좋은 방식은 아닙니다.  

일단 자명한 사실은 이 방식을 구현하며 복무율 갱신을 담당하는 코드와 표현 소수점을 수정하는 코드를 의존적으로 작성하였으므로 구현을 마치더라도 처음의 의도를 달성하지 못했을 것입니다.  

## 브라우저 단계에서의 `setInterval`과 `setTimeout` 최적화
하지만 일련의 걱정은 기우였습니다. 이미 브라우저들은 시간 지연 호출 API들을 빠른 시간 안에 여러번 호출하는 상황에 대한 최적화 대책을 마련해두었습니다.  

[HTML 표준의 브라우저 타이머 명세](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#timers)를 확인해보면 `setInterval`과 `setTimeout`은 매개변수로 넘긴 딜레이 시간 뒤에 작동할 수도 있고 작동하지 않을 수도 있다는 것을 알 수 있습니다.  
브라우저가 당장 처리해야 할 타이머 사용 호출이 5건 이상이라면 최소한 4ms는 지연되어야 합니다.  

```html
<div>
  <button id="run">시작</button>
  <pre>이전        현재         실제 딜레이</pre>
  <div id="log"></div>
</div>
<script>
  let last = 0;
  let iterations = 10;

  function timeout() {
    // log the time of this call
    logline(new Date().getMilliseconds());

    // if we are not finished, schedule the next call
    if (iterations-- > 0) {
      setTimeout(timeout, 0);
    }
  }

  function run() {
    // clear the log
    const log = document.querySelector("#log");
    while (log.lastElementChild) {
      log.removeChild(log.lastElementChild);
    }

    // initialize iteration count and the starting timestamp
    iterations = 10;
    last = new Date().getMilliseconds();

    // start timer
    setTimeout(timeout, 0);
  }

  function pad(number) {
    return number.toString().padStart(3, "0");
  }

  function logline(now) {
    // log the last timestamp, the new timestamp, and the difference
    const newLine = document.createElement("pre");
    newLine.textContent = `${pad(last)}         ${pad(now)}          ${now - last}`;
    document.getElementById("log").appendChild(newLine);
    last = now;
  }

  document.querySelector("#run").addEventListener("click", run);
</script>
```
```
이전        현재         실제 딜레이
527         528          1
528         528          0
528         528          0
528         528          0
528         533          5
533         539          6
539         544          5
544         548          4
548         552          4
552         558          6
558         562          4
```
_Source: Mozilla_

즉 너무 빠른 시간 안에 타이머 호출을 걸었다면, 브라우저 단계에서 최적화가 이루어질 수도 있다는 의미입니다.  

이 처리는 함수 호출을 무시하는게 아니라 지연해서 실행하는 것입니다. 따라서 걱정한 것처럼 "너무 많은 호출로 브라우저에 부하가 가는 것"처럼 보일 수도 있을 것이고 걱정한 문제가 근본적으로 해결된 것이 아닙니다.  

하지만 위 명세에서 최소 4ms의 딜레이라고 명시했습니다. 하지만 구현한 코드는 아무리 빨라도 30ms의 딜레이를 가져가니 사실 걱정할 일이 없어진 것이나 다름없을지 모르겠습니다.  

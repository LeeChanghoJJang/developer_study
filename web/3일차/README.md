## Bootstrap
> CSS 프론트엔드 프레임워크(Toolkit)
> 미리 만들어진 다양한 디자인 요소들을 제공하여 웹사이트를 빠르고 쉽게 개발 가능 

### CDN
> 1. 지리적 제약 없이 빠르고 안전하게 콘텐츠를 전송할 수 있는 전송 기술
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

```
> 2. 서버와 사용자 사이의 물리적인 거리를 줄여 콘텐츠 로딩에 소요되는 시간을 최소화(웹 페이지 로드 속도를 높임)
> 3. 지리적으로 사용자와 가까운 CDN 서버에 콘텐츠를 저장해서 사용자에게 전달

#### 기본 사용법
> `mt-5` : `property`, `sides` `size` 
- property : m(`margin`), p(`padding`)
- sides : t(`top`),b(`bottom`),s(`left`),e(`right`),y(`top,bottom`),x(`left,right`),blank(4 sides)
- size : 1rem(`16px`)
```html
<p class ="mt-5">Hello, world!</p>
```

#### Reset CSS
> 1. 모든 HTML 요소 스타일을 일괄된 기준으로 재설정하는 간결하고 압축된 규칙 세트
> 2. HTML element, Table,List 등의 요소들에 일관성 있게 스타일을 적용시키는 기본 단계
> 3. 모든 브라우저는 각자의 `user agent stylesheet`를 가지고 있음(웹사이트를 보다 읽기 편하게 하기 위해) --> 브라우저에서 기본적으로 적용하는 스타일
> 4. 문제는 이 설정이 브라우저마다 상이하다는 것
> 5. 모든 브라우저에서 웹사이트를 동일하게 보이게 만드렁야 하는 개발자에겐 매우 골치 아픈 일
> 6. 모두 똑같은 스타일 상태로 만들고 스타일 개발을 시작하자

#### Nomarlize CSS
> 1. Reset CSS 방법 중 대표적인 방법
> 2. 웹 표준 기준으로 브라우저 중 하나가 불일치 한다면 차이가 있는 브라우저를 수정하는 방법(경우에 따라 IE 또는 EDGE 브라우저는 표준에 따라 수정할 수 없는 경우도 있는데, 이 경우 IE 또는 EDGE의 스타일을 나머지 브라우저에 적용시킴)

#### Bootstrap 활용
> Typography : 제목, 본문 텍스트, 목록 등
> colors : Text, Border, Background 및 다양한 요소에 사용하는 Bootstrap의 색상 키워드

#### Bootstrap Component 
> UI 관련 요소 : 버튼, 네비게이션 바, 카드, 폼, 드롭다운 등
> 1. Alerts(알림창), Badge, cards, nav, carosoul 등
> 2. 빠른 개발과 유지보수 및 커스터마이징 용이
> 3. 손쉬운 반응형 웹 디자인 구현
> carousel의 id 값과 각 버튼의 data-bs-target이 일치하는지 잘봐야함

#### Semantic Web
> 웹 데이터를 의미론 적으로 구조화된 형태로 표현하는 방식
> 즉, 이 요소가 가진 목적과 역할은 무엇일까??
```html
<p style="font-size:30px;">Heading</p>
<h1>Heading</h1> 
<!-- 페이지 내 최상위 제목이라는 의미를 담은 요소 -->
```
> `HTML Semantic Element` : 기본적인 모양과 기능 이외 HTML 요소 
> 검색엔진 및 개발자가 웹페이지 콘텐츠를 이해하기 쉽도록
> `header, nav, main, article, section, aside, footer` : `div`와 동일한 100% 역할

#### CSS 방법론
> CSS를 효율적이고 유지보수가 용이하게 작성하기 위한 일련의 가이드라인 
> `OOCSS` :Object oriented CSS 객체 지향적 접근법을 이용하여 cSS를 구성하는 방법론
  - 기본원칙(묶지 말고 분리)
    - 1. 구조와 스킨을 분리
    - 2. 컨테이너와 콘텐츠를 분리

#### 의미론적인 마크업이 필요한 이유
> 검색엔진 최적화(CEO)
> 웹 접근성(Web Accessibility) : 웹 사이트, 도구, 기술이 고령자나 장애를 가진 사용자 들이 사용할 수 있도록 설계 및 개발하는 것
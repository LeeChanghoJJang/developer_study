### Bootstrap Grid System
> 1. 웹페이지의 레이아웃을 조정하는 데 사용되는 12개의 컬럼으로 구성된 시스템
> 2. `Grid system` 목적 : 반응형 디자인을 지원해 웹 페이지를 모바일, 태블릿, 데스크탑 등 다양한 기기에서 적절하게 표시할 수 있도록 도움
> 3. `반응형 웹 디자인` : 디바이스 종류나 화면 크기에 상관없이, 어디서든 일관된 레이아웃 및 사용자 경험을 제공하느 디자인 기술 

#### Grid system 기본 요소
> CSS가 아닌 편집 디자인에서 나온 개념으로 구성요소를 잘 배치해서 시각적으로 좋은 결과물을 만들기 위함.
1. Container : column들을 담고 있는 공간
2. Column : 실제 컨텐츠를 포함하는 부분
3. Gutter : 컬럼과 컬럼 사이의 여백 영역
4. 1개의 row안에 12개의 column영역이 구성
```html
<!-- 12개 중 몇개를 줄것인가 -->
<div class="container">
  <div class="row">
    <div class="col-4"></div>
    <div class="col-4"></div>
    <div class="col-4"></div>
  </div>
</div>
```
#### Gutters
> x축은 padding, y축은 margin으로 여백 생성

#### Grid system breakpoints
> 웹페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점
> 화면 너비에 따라 6개의 분기점 제공(xs, sm, md, lg, xl, xxl)

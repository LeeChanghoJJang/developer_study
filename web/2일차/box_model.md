# BOX_MODEL

### 정의
> 모든 HTML 요소를 사각형으로 나타내는 개념 
> `내용`(content), `안쪽 여백`(padding), `테두리`(border), `외부 간격`(margin)
> 각각 top, bottom, left, right 방향이 있음 

### width, height 기준
> `content`의 너비와 높이를 지정할 수 있음
```css
*{
  box-sizing : border-box;
  /* box-sizing : content-box가 기준임 */
}
```

### 박스 타입
> Block(막는다) vs inline(안쪽 사이에 들어가있는 느낌)
```css
.index{
  display:block;
  display:inline;
}
```
---
### display 속성
#### Block
> 1. `Block`은 입력하고 나서 아래로 가지만, `inline`은 옆으로 흐름
> 2. 항상 새로운 행으로 나뉨. 기본적으로 `width` 속성을 지정하지 않으면 박스는 `inline` 방향으로 사용가능한 공간을 모두 차지함.(너비를 사용가능 공간 100%로 채움)
  - Block : `div`, `h1~ h6`, `p` 등
> 3. `block`은 `margin`을 통해 수평 정렬

#### inline
> 1. 새로운 행으로 나뉘지 않음
> 2. `width`와 `height` 속성을 사용할 수 없음
> 3. 수직방향 : padding, margins, borders가 적용되지만 다른 요소를 밀어낼 수는 없음
> 4. 수평방향 : padding, margins, borders가 적용되어 다른 요소를 밀어낼 수 있음
  - inline : `span`, `a`, `img` 등
  - 단 `img`는 width, height 조정가능
> 5. `inline`은 `text-align`을 통해 수평정렬

#### inline-block
> 기본적으로는 `inline`의 속성을 지님 + `block` 속성
> 요소가 줄바꿈되는 것을 원하지 않으면서, 너비와 높이를 적용하고 싶은 경우
> `text-align`으로 수평정렬 가능

#### None
> 화면에서 사라지게 함

### shorthand 속성 
> 1. border
  - `border-width`, `border-style`, `border-color` 한번에 설정하기 위함
  - 순서는 상관 없음
> 2. margin & padding
  - 갯수에 따라 상우하좌, 상/좌우/하, 상하/좌우, 공통

### Margin Collapsing (마진 상쇄)
> 1. 두 block 타입 요소의 `margin top`과 `bottom`이 만나 더 큰 `margin`으로 결합되는 현상 (각 요소마다 설정하지 않고, 한 요소에 대해서만 설정)

### CSS Position
> CSS Layout : 각 요소의 위치와 크기를 조정하여 웹페이지의 디자인을 결정하는 것
> CSS Position : 요소를 `Normal Flow`에서 제거하여 다른 위치로 배치하는 것

#### Position 유형
> 1. static : 포지션값을 아무것도 처리하지 않았을 때 (주나마나)
> 2. relative
> - `top 100px` : 위쪽에 100px만큼 주므로, 밑쪽으로 `100px` 이동 
> - 본인의 static 시절의 원래 위치에서 움직임
> - `static` 위치가 막 바뀌면 `relative`도 같이 움직임
> - 그러면 이동하게 되면 빈공간은? --> 과거의 영역은 그대로 똑같이 차지하고 있음
> 3. absolute
> - 집을 나가는 친구. 본인의 영역을 버렸기 때문에 나머지 얘들한테 영향을 미침
> - 움직이려면 새로운 기준점을 찾아가야함 --> 바로 static이 아닌 부모를 찾아감
> - 즉 부모가 최소 `relative`는 되야 함 
> 4. fixed
> - 집을 나가는 친구. 브라우저 상의 위치를 지정(top : 0, right: 0 우측 상단)
> - 문서에서 차지하는 공간이 없어짐
> 5. sticky
> - 특정한 임계점이 오지 않으면 `normal flow`임
> - 우리가 조건을 건 그 지점으로 갈 때 `fixed`로 바뀜
> - 다음 `sticky`가 있으면 걔한테 넘겨줌

#### z-index 
> 요소를 겹쳤을 때 순서 정하기(z.index = 숫자)

#### Flex-box
> 요소를 행과 열형태로 배치하는 1차원 레이아웃 방식 
> `Flex Container`부모와 각 `Flex item`이 있음
> `display:flex` 하면 메인 축이 아래에서 우측으로 바뀜
> `flex-direction` : row-reverse 하면 흐름순서가 바뀜
> `flex-wrap` : 기본은 nowrap이나, wrap으로 설정하면 원래 모양에 영향 안미치고 밑으로 이동시킴
> `justify-content` : `flex-start`가 기본값이며 현재 축을 기준으로 바뀜
> `align-content` : 교차축에 따라 여러 줄을 정렬 
> `align-items` : 교차축에 따라 한줄만 가운데 정렬 
> `align-self` : 부모에 상관없이 정렬
##### 공간배분
> `flex-grow` : 빈 공간에 영역할당 가능. 나머지 빈공간들을 N등분하여 나눠줌 
> `flex-basis` : 기본 크기를 지정
#### Flex-속성정리
> 배치 : flex-direction(축방향), flex-wrap(배치)
> 공간분배 : justify-content(축방향), align-content(교차축방향)
> 정렬 : aling-items,aling-self

#### 추가 용어
> content : 여러줄
> items : 한 줄
> self : 요소 한개
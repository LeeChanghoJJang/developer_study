# Web

### 정의
> `World Wide Web` : 인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 공유 공간
> `Web` : `Web site`, `Web application` 등을 통해 사용자들이 검색하고 상호 작용하는 기술

### Web site
> 인터넷에서 여러 개의 `Web page`가 모인 것으로, 사용자들에게 정보나 서비스를 제공하는 공간

### Web page
> `HTML`, `CSS` 등의 웹 기술을 이용하여 만들어진 `Web site`를 구성하는 하나의 요소
1. `HTML` : 구조물
2. `CSS` : 스타일링
3. `JavaScript` : Behavior

### HTML
> `HyperText Markup Language` : 웹페이지의 **의미**와 **구조**를 정의하는 언어 
> `HyperText` : 웹 페이지를 다른 페이지로 연결하는 링크(참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트)
  - 없었을 때에는 앞과 뒤로 밖에 이동이 안되었음
> `Markup Language` : 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어(`HTML`, `Markdown`) => 구조화한다. 마크업한다고 함
  - 가독성 용이

#### 문법
<!DOCTYPE html> : 해당 문서가 html로 문서라는 것을 나타냄. 해석하는 주체는 브라우저(`크롬`)임
<html></html> : 전체 페이지의 콘텐츠를 포함
<title></title> : 브라우저 탭 및 즐겨찾기 시 표시되는 제목 사용
<head></head> : 머리(사용자에게 보여지지 않음)
<body></body> : 몸통(페이지에 표시되는 모든 컨텐츠)

- 개발자 도구 : `Ctrl + Shift + I`

#### HTML Element(요소)
> `<p class="editor-note"> My cat is very grumpy</p>` 
> 태그를 포함하지 않은 내용은 `content`고, 포함하면 `element`다 
> `class`,`id`를 속성이라고 하며, 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함

#### HTML Text structure
> 텍스트와 구조를 전달하는 것
> 웹페이지의 의미와 구조를 정의하는 언어

### CSS
> 웹페이지의 디자인과 레이아웃(배치)을 구성하는 언어
> 속성 : 값 형태로 이뤄지며, 선택자에 {}를 한다.
> 선언을 하면, ;을 넣어준다(자바처럼)
```css
h1 {
  color: red;
  font-size: 30px;
}
```
#### inline 방법

```html
  <h1 style="color:blueviolet; background-color: yellow;">Inline Style</h1>
```

#### Internal 방법
```html
 <style>
    h2 {
    color: red;
    font-size: 30px;
  }
  </style>
```
#### External 방법
```css
  <link rel="stylesheet" href="style.css">
```

#### CSS 종류
1. 전체선택자(`*`) : `HTML`의 모든 요소를 선택. 사실 잘안씀
2. 요소선택자 : 지정한 모든 태그를 선택. 사실 잘안씀
3. 클래스선택자(`.`) : 클래스 선택
4. 아이디선택자(`#`) : 아이디 선택(클래스보다 우선하며 문서에서 유일 ==> 에러는 나지 않으며, 우리가 찾아야 함)
5. 자손결합자(" ") : 첫번째 요소의 자손 요소들 선택
  - `p span`은 <p> 안에 있는 모든 <span> 선택 (하위레벨 노상관)
  - `class`도 <p class="green orange"> 이런식으로 가능
  - `class` 옆에 쓰는 순서는 상관없음 
6. 자식결합자(">") : 첫번째 요소의 직계자식만 선택
  - `ul > li`는 <ul>안에 있는 모든 <li>를 선택(한단계 아래 자식들만)
  - 상속 구조를 활용하여 좀 더 디테일하게 적용가능

#### 명시도
> 결과적으로 요소에 적용할 CSS 선언을 결정하기 위한 알고리즘
  - 가중치를 계산하여 어떤 스타일을 적용할 것인가
> `Cascade` : 한 요소에 동일한 가중치를 가진 선택자가 적용될 때 CSS에서 마지막에 나오는 선언이 사용됨 
> !important > inline > id > class > 요소 > 전체 순으로 명시도가 높음
  - `!important` 는 안쓰는 것을 권장
```css
h2 {color: darkviolet !important;}
```
> 속성은 되도록 `class`만 사용할 것
> 괜히 다른 것들을 섞으면 계속 가중치를 생각해야 함.
> 문서에서 단 한번 유일하게 적용될 스타일 경우에만 `id 선택자` 사용을 고려 

#### CSS 상속
> 상속되는 속성 : Text 관련요소(font,color,text-align,opacity,visibility)
> 상속되지 않는 속성 : Box model 관련 요소(width,heigth,border,box-sizing), position 관련 요소(position,top/right/bottom/left,z-index)
  - MDM 문서에서 상속여부 확인 가능

#### HTML 관련 사항
> 요소(태그) 이름은 대소문자를 구분하지 않지만 "소문자" 사용 권장
> 작은 따옴표와 큰 따옴표 구분하지 않지만 "큰 따옴표" 권장
> 에러를 반환하지 않기 때문에 작성 시 주의
> CSS와 HTML 구조정보가 혼합되어 작성되기 때문에 `inline`스타일은 잘 작성하지 않아야 함
> CSS의 모든 속성은 외우는 것이 아님(검색하여 사용)
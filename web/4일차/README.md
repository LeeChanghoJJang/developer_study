### 4일차

#### 간단한 Emmet 활용방법(Visual Studio에 내장됨)
> 아래와 같이 문법 사용하면 됨 
> 구글에 emmet -> documentation을 누르면 참고가능 
> `emmet cheet sheet`에서 한장으로 간단하게 정리됨
```html
<!-- div>.container>h1{hello}+nav>ul>li*5>a{Link $} -->
<div>
  <div class="container">
    <h1>hello</h1>
    
    <nav>
      <ul>
        <li><a href="">Link 1</a></li>
        <li><a href="">Link 2</a></li>
        <li><a href="">Link 3</a></li>
        <li><a href="">Link 4</a></li>
        <li><a href="">Link 5</a></li>
      </ul>
    </nav>
  </div>
</div>

<!-- p*3>lorem*3  -->
<p><span>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolore repudiandae mollitia</span><span>Odit esse consectetur doloribus quo alias accusamus autem aut facere, quide Nesciunt velit in, non enim temporibus est officiis ipsa molestias.</span><span>Optio aliquam sunt a quidem obcaecati unde architecto necessitatibus accusantium, sed error sint fuga ut eos nemo minima enim quam. </span></p>
<p><span>Lorem ipsum, dolor sit amet consectetur adipisicing elit. </span><span>Odit quisquam asperiores, nulla suscipit autem minima voluptas consequatur dicta nemo dolores quidem facilis cupiditate laudantium? </span><span>Iste vero, odio excepturi voluptatem harum soluta, architecto natus aliquam itaque sint minima!</span></p>
<p><span>Lorem ipsum dolor sit amet consectetur adipisicing elit. Optio cum fuga doloribus vel ipsa. Ab repellat et consequatur?</span><span>Dolorem eligendi, corrupti cumque odit ducimus facilis ipsam quidem. </span><span>Officia, laudantium! Doloribus laudantium quos quas! </span></p>
```
#### 단축키 정리
> `ctrl + l` : 한 줄 선택
> `ctrl + d` : 동일한 키워드 선택
> `ctrl + alt + 화살표` : 멀티커서(같은 방향만 가능)
> `alt + 클릭` : 멀티커서(각 원하는 위치에서)
> `alt + 화살표` : 선택한 라인 끌고가기
> `alt + shift + 화살표` : 선택한 라인 복사
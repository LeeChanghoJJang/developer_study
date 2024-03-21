# 패턴 매칭에 사용되는 알고리즘

### 고지식한 패턴 검색 알고리즘(Brute Force)
  - 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식으로 동작
```python
p = 'is'
t = 'This is a book~!"
M = len(p)
N = len(t)

def BruteForce(p,t):
  i=0 # t의 인덱스
  j=0 # p의 인덱스
  while j<M and i <N:
    if t[i] != p[j]:
        i -= j
        j = -1
      i +=1
      j +=1
    if j ==M: return i-M
    else: return -1

def f(pat,txt,M,N):
  for i in range(N-M+1):
    for j in range(M):
      if txt[i+j] != pat[j]:
        break
    else:
      return 1
  # 모든 위치에서 비교가 끝난 경우
  return 0

T = int(input())
for tc in range(1,T+1):
  pat = input()
  txt = input()
  M = len(pat)
  N = len(txt)

```


### KMP 알고리즘
  - 불일치가 발생한 텍스트 스트링의 앞 부분에 어떤 문자가 있는지 미리 알고 있으므로, 불일치가 발생한 앞 부분에 대해 다시 비교하지 않고 매칭을 수행
  - 시간복잡도 O(M+N)
  - 아이디어
    - a b c d a b c d    [T]
    - a b c d a b c e f  [P]
    - ------- a b c d a b 불일치나면 알고있는 위치는 건너서 shift
  - 매칭이 실패했을 때 돌아갈 곳을 계산한다.
```python
def kmp(t,p):
  N = len(t) # 전체
  M = len(p) # 찾기 대상
  lps = [0] * (M+1)
  j = 0
  lps[0] = -1
  for i in range(1,M):
    lps[i] =j
    if p[i] == p[j]:
      j+=1
    else:
      j = 0
  lps[M] = j
  i=0
  j=0
  if j==-1 or t[i] ==p[i]:
    i+=1
    j+=1
  else:
    j=lps[j]
  if j==M:
    print(i-M,end=' ')
    j = lps[j]
```

### 보이어 무어 알고리즘 (KMP보다도 듬성듬성 비교)
  - 오른쪽에서 왼쪽으로 비교
  - 대부분의 상용 소프트웨어에서 채택하고 있는 알고리즘
  - 패턴에 오른쪽 끝에 있는 문자가 불일치하고, 이 문자가 패턴 내 존재하지 않는 경우, 이동거리는 패턴의 길이만큼이 된다. (굳?)
  
#### 문자열 매칭 알고리즘 비교
  - 찾고자 하는 문자열 패턴의 길이 m, 총 문자열 길이 n
  - 고지식한 패턴 검색 알고리즘 : 수행시간 O(mn)
  - 카프-라빈 알고리즘 : 수행시간 θ(n)
  - KMP 알고리즘 : 수행시간 θ(n)

#### 보이어 무어 알고리즘
  - 앞의 두 매칭 알고리즘들의 공통점 텍스트 문자열의 문자를 적어도 한번씩 훑는다는 것. 최선의 경우에도 Ω(n)
  - 보이어 무어 알고리즘은 텍스트 문자를 다 보지 않아도 된다.
  - 패턴의 오른쪽부터 비교한다!!
  - 최악의 경우 수행시간 θ(mn)
  - 입력에 따라 다르지만 일반적으로 θ(n)보다 시간이 덜 든다

#### 문자열 암호화
  - 단일 치환 암호(카이사르 암호화)
  - 평문   S A V E   P R I V A T E   R Y A N
  - 암호문 T B W F A Q S J W B U F A S Z B O
  - 1만큼 평행했을 때, 1을 키값이라 함
  - 수신자 이외의 사람이 암호문을 보고 다른정보 없이 메시지 맞출 수 있을까?

#### 단일 치환 암호의 복호화
  - 모든 키의 조합(key space)가 필요함
  - 단일 치환 암호의 키의 총수는 26! 1초에 10억개를 넣는다 해도 120억년 걸린다고 함

#### bit열의 암호화
  - 배타적 논리합 연산 사용
  - 평문   1 0 0 1 1 0 0 0 1 1 1 0
  - 키     1 1 0 0 0 1 1 1 0 0 1 1
  - 암호문 0 1 0 1 1 1 1 1 1 1 0 1

#### 문자열 압축
  - Run-length encoding 알고리즘
  - 같은 값이 몇번 반복되는 가를 나타냄으로써 압축
  - A B B B B B B B B A
  - A 1 B 8 A 1
  - 이 방법은 이미지 파일 포맷 중 BMP 파일 포맷의 압축방법
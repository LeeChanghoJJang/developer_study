#  Queue

### 정의

1. 선입선출 구조 (스택과 마찬가지로 삽입과 삭제의 위치가 제한된 자료구조)
  - 삽입 : rear(꼬리)에 삽입. enQueue --> push
  - 삭제 : front(머리)에서 삭제. deQueue --> pop

2. 가장 먼저 삽입된 원소는 가장 먼저 삭제된다 (스택은 후입선출)

#### 주요 연산
  - enQueue : 큐의 뒤쪽에 원소를 삽입하는 연산
  - deQueue : 큐의 앞쪽에서 원소를 삭제하고 반환하는 연산
  - createQueue() : 공백 상태의 큐를 생성하는 연산
  - isEmptry() : 큐가 공백상태인지를 확인하는 연산
  - isFull() : 큐가 포화상태인지를 확인하는 연산
  - Qpeek() : 큐의 앞쪽에서 원소를 삭제없이 반환하는 연산

#### 큐의 연산 과정
  - 공백 큐 생성 : createQueue() front = rear = -1
  - 원소 A 삽입 : enQueue(A) rear를 증가시키고 A를 저장
  - 원소 B 삽입 : enQueue(B) rear를 증가시키고 B를 저장 
  - 원소 반환/삭제 : deQueue(); front를 증가시키고 꺼내기
  - 원소 C 삽입 : enQueue(C); rear를 증가시키고 C를 저장
  - 만약 가장 마지막 꺼 꺼내면 => front == rear ==> 큐가 빔

#### 선형큐
  1. 1차원 배열을 이용한 큐
    1. 큐의 크기 = 배열의 크기
      - front = 저장된 첫 원소의 인덱스
      - rear = 저장된 마지막 원소의 인덱스
    2. 상태 표현
       - 초기 상태 : front == rear = -1
       - 공백 상태 : front == rear
       - 포화 상태 : rear == n-1
#### 선형큐 구현
  1. 삽입 : enQueue -> 마지막 원소 뒤에 새 원소 삽입위해 rear값 증가시킴
    - rear값 하나 증가시켜 새 원소 삽입자리 마련 
    - 그 인덱스에 해당하는 배열원소 `Q[rear]`에 item 저장
  ```python
  def enQueue(item):
    global rear
    if isFull():
      print('Queue_Full')
    else:
      rear +=1
      Q[rear] = item
  ```
  2. 삭제 : deQueue -> 가장 앞에 있는 원소 삭제하기 위해 front 증가 
    - front 증가시켜, 큐에 남은 첫번째 원소 이동
    - 첫원소를 리턴함으로써 삭제와 동일한 기능
  ```python
  def deQueue():
    if (isEmpty()): 
      Queue_Empty()
    else:
      front +=1
      return Q[front]
  ```
  3. 공백상태 및 포화상태 검사 : isEmpty(), isFull()
    - 공백상태 : front == rear
    - 포화상태 : rear == n-1
  ```python
  def isEmpty():
    return front == rear
  
  def isFull():
    return rear == len(Q)-1
  ```
  4. Qpeek() : 가장 앞에 있는 원소를 검색하여 반환하는 연산
    - 가장 앞에 있는 원소를 검색하여 반환하는 연산
    - 현재 front의 한자리 뒤에 있는 원소. 즉 큐의 첫번째 원소를 반환
  ```python
  if isEmpty(): print('Queue_Empty')
  else: return Q[front+1]
  ```

#### 원형큐
  1. 선형큐의 문제
    - 선형 큐를 이용하여 원소 삽입과 삭제 계속할 때, 배열의 앞부분에 활용가능한 공간이 있음에도 불구하고, rear = n-1인 상태
    - 즉, 포화상태로 인식하여 더 이상 삽입은 없음
  2. 해결방법 
    - 매 연산이 이뤄질 때마다 저장된 원소들을 배열의 앞부분으로 모두 이동
    - 원소 이동에 많은 시간 소요되어 큐의 효율성이 급격히 떨어짐
  3. 해결방법 2
    - 1차원 배열을 사용하되, 논리적으로는 배열의 처음과 긑이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용
  4. front 변수 : 공백과 포화를 구분 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 빈자리로 둠
    - 삽입위치
      - 선형큐 : rear +=1
      - 원형큐 : (rear + 1) mod n
    - 삭제 위치
      - 선형큐 : front +=1
      - 원형큐 : (front + 1) mod n
    - front가 rear의 다음자리면 꽉 찬것!

#### 원형큐 구현
  1. 공백상태 : front == rear
  2. 포화상태 : 삽입할 rear의 다음 위치 == 현재 front
    - (rear + 1) mod n == front
  3. 공백상태 및 포화 상태 검사
   ```python
  def isEmpty():
    return front == rear
  def isFull():
    return (rear+1) % len(cQ) == front
   ```
  1. 삽입 : 마지막 원소 뒤에 새 원소를 삽입하기 위해 rear값 조정
    - rear = (rear+1) mod n
  ```python
  def enQueue(item):
    global rear
    if isFull():
      print('Queue_Full')
    else:
      rear = (rear+1) % len(cQ)
      cQ[rear] = item
  ```
  2. 삭제 : 가장 앞에 있는 원소를 삭제하기 위해 front값을 조정하여 삭제할 자리 준비
    - front값을 조정하여 삭제할 자리 준비.
    - 새로운 원소를 리턴함으로써 삭제와 동일한 기능
  ```python
  def deQueue():
    global front
    if isEmpty():
      print('Queue_Empty')
    else:
      rear = (front+1) % len(cQ)
      return cQ[front]
  ```

#### 연결큐
  1. 단순 연결 리스트를 이용한 큐
    - 큐의 원소 : 단순 연결 리스트의 노드
    - 큐의 원소 순서 : 노드의 연결 순서. 링크로 연결되어 있음
    - front : 첫번째 노드를 가리키는 링크
    - rear : 마지막 노드를 가리키는 링크

  2. 상태표현
    - 초기상태 : front == rear == null
    - 공백상태 : front == rear == null
    - 공백 큐 생성 : front : null, rear : null
    - 원소 A 삽입 : enQueue(A) rear 1 증가 -> rear:null
    - 원소 B 삽입 : enQueue(B) A의 rear에 B의 주소 삽입 -> B의 rear는 null
  
#### deque (덱)
  1. 양쪽 끝에서 빠르게 추가와 삭제를 할 수 있는 리스트류 컨테이너
  2. 연산
    - append : 오른쪽에 x 추가
    - popleft() : 왼쪽의 요소를 제거하고 반환
  ```python
  from collections import deque
  q = deque()
  q.append(1) # enqueue()
  t = q.popleft() # dequeue()
  ```

#### 우선순위 큐(Priority Queue)
  1. 정의
    - 우선순위를 가진 항목들을 저장하는 큐
    - FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나가게 된다.
  
  2. 적용분야
    - 시뮬레이션 시스템
    - 네트워크 트래픽 제어
    - 운영체제의 테스크 스케쥴링
  
  3. 구현
    - 배열을 이용한 우선순위 큐
    - 리스트를 이용한 우선순위 큐
  
  4. 배열을 이용한 우선순위 큐 구현
    - 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입
    - 가장 앞에 최고 우선순위의 원소가 위치하게 됨
    - 문제점
      - 배열 이용하므로, 삽입과 삭제 연산 발생 시, 원소의 재배치 발생
      - 이에 소요되는 시간과 메모리 낭비 큼
  
#### 버퍼 
> 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
  - 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미
  - 자료구조
    - 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용됨
    - 순서대로 입력/출력/전달되어야 하므로 FIFO 방식의 자료구조인 큐 활용
  - 예시
    - 키보드 버퍼는 사용자 입력 -> enter 입력 -> 
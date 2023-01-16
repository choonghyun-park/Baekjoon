# Function
백준 단계별 문제풀이 챕터 5 : Function을 풀면서 중요한 점들을 정리해놓은 페이지입니다.

## lst.remove
list를 쓰다보면 append는 많이 쓰는데, 특정 원소를 지우는 코드는 잘 안썼던 것 같다. 특정 원소를 지우고 싶을 때는 `lst.remove()` 를 사용하면 된다.
```
lst = [1,2,3,4]
lst.remove(3)
```

## set
list를 이용해서 ~ in lst 구문을 사용하니, 백준 5.2번 문제에서 시간 초과가 나왔다. lst에서 in을 사용하는 경우 앞에서부터 해당 원소가 존재하는지 탐색하기 떄문에 시간 복잡도는 O(n)이다. 만약 순서상 뒤에 존재하는 원소를 찾는 경우 시간 복잡도가 최대가 되는 것이다.\
list의 시간 복잡도 문제를 해결하기 위해서 set을 사용하였다. set의 시간복잡도는 O(1)이다. set은 해시함수와 해시 테이블을 이용해서 만든 자료구조이기 때문에 list처럼 선형적으로 탐색하지 않는다. 이는 dict도 마찬가지이다. 다시말하면, set은 원소 순서와 상관없이 탐색 속도가 거의 일정하다.\
다만, 원소의 개수가 작을 때는 list의 탐색 속도가 조금 더 빠르다. 하지만 데이터 크기가 커지는 경우 탐색속도는 set이 압도적으로 빨라진다. (O(n)과 O(1)을 비교해 보아라.)

### set(집합) 기본함수
set의 기본함수를 정리해 보았다. 참고한 포스팅은 [여기](https://www.codingfactory.net/10043).
* set 정의
중괄호로 정의한다.
```py
s = {1,2,3,4,5}
```
* 집합의 길이
```py
s = {1,2,3,4,5}
print(len(s))
>>> 5
```
* 값이 있는지 확인
```py
s = {1,2,3}
print(1 in s)
>>> True
print(5 in s)
>>> False
```
* 하나의 원소 추가하기
```py
s = {1,2,3}
s.add(4)
```
* 여러 원소 추가하기
```py
s = {1,2,3}
s.update([4,5,6])
```
* 원소 제거
```py
s = {1,2,3}
s.remove(2)

# s.remove(5) => Error
```
만약 remove에서 Error가 나지 않는 버전을 쓰고싶으면 discard()를 쓰면 된다.
```py
s = {1,2,3}
s.discard(5) # No Error
```
* 임의의 원소를 가져온 후 삭제 : pop
```py
s = {1,2,3}
p = s.pop(1)
print(s) 
# {2,3}
```
* 원소 비우기 (공집합)
```py
s = {1,2,3}
s.clear()
```



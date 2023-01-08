# loop
백준 단계별 문제풀이에서 반복문 관련 중요사항들을 정리한 페이지입니다.

## 빠른 A+B
for문을 사용할 때 보통 python에서는 `input()` 함수를 이용한다. 하지만 for 문을 사용하여 많은 input을 받는 경우 input() 함수는 속도가 느려서 시간초과가 날 수도 있다. 따라서 `sys.stdin.readline()` 함수를 사용하여 빠르게 입출력 처리를 할 수 있다고 한다. \
언어별로 정리하면 아래와 같이 함수를 사용하여 입출력을 빠르게 처리할 수 있다.
* python
```py
import sys
inp = sys.stdin.readline()
```
위 함수는 개행문자를 포함하여 입력을 받기 때문에, 문자열을 저장하고 싶은 경우에는 `.rstrip()` 을 추가로 사용하는 것이 좋다. rstrip()을 사용하면 마지막 개행은 받지 않는다.\
예제) test str을 받는 경우
```py
import sys
inp1 = sys.stdin.readline()
inp2 = sys.stdin.readline().rstrip()

print("inp1",inp1)
print("type(inp1)",type(inp1))
print("len(inp1)",len(inp1))
print("inp1[-1]",inp1[-1])
print()
print("inp2",inp2)
print("type(inp2)",type(inp2))
print("len(inp2)",len(inp2))
print("inp2[-1]",inp2[-1])
```
결과
```
test str
test str
inp1 test str

type(inp1) <class 'str'>
len(inp1) 9
inp1[-1]


inp2 test str
type(inp2) <class 'str'>
len(inp2) 8
inp2[-1] r
```

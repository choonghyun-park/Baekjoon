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
* C++
C++을 사용하고 있고 cin/cout을 사용하고자 한다면, cin.tie(NULL)과 sync_with_stdio(false)를 둘 다 적용해 주고, endl 대신 개행문자(\n)를 쓰자. 단, 이렇게 하면 더 이상 scanf/printf/puts/getchar/putchar 등 C의 입출력 방식을 사용하면 안 된다.
* Java
Java를 사용하고 있다면, Scanner와 System.out.println 대신 BufferedReader와 BufferedWriter를 사용할 수 있다. BufferedWriter.flush는 맨 마지막에 한 번만 하면 된다.

## 별 그리기
별 그리기 문제에서 별을 출력할 때, 자릿수를 맞춰야 하는 문제가 있었다. 참고한 링크는 [여기](https://blackhippo.tistory.com/entry/Python-print%EB%AC%B8-%EC%98%A4%EB%A5%B8%EC%AA%BD%EC%99%BC%EC%AA%BD-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-%EC%9D%80%ED%96%89%EB%B2%88%ED%98%B8%ED%91%9C-%ED%91%9C%ED%98%84%ED%95%98%EA%B8%B0)
* 왼쪽 정렬
```py
a = 10
print(str(a).rjust(5))
```
* 오른쪽 정렬
```py
a = 10
print(str(a).ljust(5))
```
## input 여러개 받기
기본적으로 input을 여러개 받는 방법은 `.split()`함수를 사용하는 것이다.
```py
a,b = input().split()
```
위처럼 하면 공백을 하나씩 가지고 주는 input을 나누어서 list형식으로 받는다. 만약 int 값을 여러개 받는 경우는 각각을 int로 묶어주면 된다.
```py
a,b = input().split()
a = int(a)
b = int(b)
```
위처럼 하는 것이 기억하기 쉬운 단순한 벙법이다. 이거를 한줄로 표현하려면 `map` 함수를 사용하면 된다.
```py
a,b = map(int, input().split())
```
위에서는 input()으로 받는 예제를 살펴봤는데, readline을 사용하는 경우도 똑같다.
```py
import sys
a,b = map(int, sys.stdin.readline().split())
```
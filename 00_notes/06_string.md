# String
백준 단계별 문제풀이

## 아스키코드
ord함수를 이용해 아스키코드를 구할 수 있다. 기본적인 아스키 코드값은 아래와 같으니 참고하자.
```py
print(ord('a')) # 97
print(ord('z')) # 122
print(ord('z')-ord('a')) # 25

print(ord('A')) # 65
print(ord('Z')) # 90
```
반대로 아스키 코드를 문자로 전환할 때는 chr 함수를 사용하면 된다.
```py
print(chr(97)) #a
print(chr(122)) #z
```
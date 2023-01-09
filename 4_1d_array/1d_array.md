# 1d array
1차원 배열 문제를 풀면서 중요 사항을 정리한 페이지입니다.

## 소숫점 자릿수 맞춰서 출력하기
마지막 문제에서 소숫점 3째 자리까지 맞춰서 반올림 한 후에 출력하는 부분이 있었다. 처음에 문자열 자릿수 맞추는 함수를 사용했는데, 오답이 나왔다. 뭔가 반례가 있는 것 같다. 그래서 {:.3f} 형식을 사용해서 출력하였더니 통과했다.
```py
for i in range(len(ratio)):
    print("{:.3f}%".format(ratio[i]))
```
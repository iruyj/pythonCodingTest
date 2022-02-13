# 피보나치 수 5
# 0과 1로 시작, 0번째 피보나치수는 0, 1번째 피보나치 수는 1이다. 
# 2번째부터는 앞 두 피보나치수의 합
# n번째 피보나치수를 구하는 프로그램을 작성하시오

# 계획
# 앞에서 풀었던 팩토리얼이 생각난다.팩토리얼처럼 풀되
# 곱셈을 덧셈처럼 하면 될거같다.
# 자기자신과 리턴받은 수(전에수)를 더하기 : 그 다음 수
# 1부터 n-1까지 리턴을 받으면 될거같다.
# 함수 :매개변수 n,(인덱스)ㄴ
# if n이 1이면 1,0리턴
# pre1, pre2 = 호출(-1)
# 리턴 : pre1+pre2, pre1(지금, 이전)
# n번째 수까지 재귀
# 결과값 : 마지막 pre1

import sys
def solution(n):
    if n<=1:
        return 1,0
    pre1,pre2= solution(n-1)
    return pre1+pre2,pre1

pre1,pre2 = solution(int(sys.stdin.readline())+1)
print(pre2)

# 재귀로 시간제한 1초안에 들수 있었지만
# 팩토리얼과 비슷하게 조건을 제대로 확인하지않아서 0을 넣었을때 런타임이 발생햇다.
# 그래도 이미 겪었던 문제라 저번보다는 빠르게 문제를 찾을수 있었다.
# 0때문에 if문을 따로 넣고싶지 않아 n+1까지 재귀를 돌며 0일때는 0을 뱉게했다.
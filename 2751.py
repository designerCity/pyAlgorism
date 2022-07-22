import sys
n = int(input())
n_list = []

for i in range(n):
    num_input = int(sys.stdin.readline())
    n_list.append(num_input)

n_list.sort()
for i in n_list:
    print(i)
# input() 이 sys.stdin.readline() 보다 느린 이유 :

# input() 내장 함수는 sys.stdin.readline()과 비교해서 prompt message를 출력하고,

# 개행 문자를 삭제한 값을 리턴하기 때문에 느리다.
# 내 코드 72ms
N = int(input())

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
rvr= list(str(factorial(N)))

cnt = 0
i = len(rvr) - 1
while int(rvr[i]) == 0:
    i -= 1
    cnt += 1
print(cnt)

# 다른 사람 풀이 68ms
n=int(input());f=0
while n:f+=n//5;n//=5
print(f)
while 1:
    m = int(input())
    if m == 0:
        break
    # 소수의 개수를 출력하는 것이기 땨문에
    n = 2 * m + 1 # 2m 이하이기 때문에

    prime = [True] * (n) # index 0 ~ 2m
    # 작은 수 중에 배수가 되는 것들을 빼줘야 한다.
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i, n, i):
                prime[j] = False
    count = 0
    for i in range(m, n):
        if i > 1 and i > m and prime[i] == True:
            count += 1
    print(count)
    
    

## 시간 복잡도를 줄이는 방법

import sys
import math

limit = 123456

eratos = [1]*(2*limit+1)
eratos[0] = 0
eratos[1] = 0

for i in range(2, int(math.sqrt(len(eratos)))):
    if eratos[i]:
        for j in range(i+i, len(eratos), i):
            eratos[j] = 0
            
while True:
    n = int(sys.stdin.readline())
    
    if n==0:
        break
    else:
        print(sum(eratos[n+1:(2*n)+1]))
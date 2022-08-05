# t = int(input())
# li = list(map(int, input().split()))

# idx = 1
# mom = 1
# while idx < t:
#     stand = li[0]
#     su = stand % li[idx] ## 나누는 숫자
#     if su == 0:
#         mom = 1
#         son = stand // li[idx]
#     else: 
#         son = stand // su
#         mom = li[idx] // su
#     print('{}/{}'.format(son, mom))
#     idx += 1

## 내 코드 80 ms 
def eclid(a, b):
    left = a % b # 나머지
    if left == 0:
        return b
    else:
        return eclid(b, left)

N = int(input())
li = list(map(int, input().split()))

for i in range(1, len(li)):
    aswr = ''
    num = eclid(max(li[0], li[i]), min(li[0], li[i]))
    aswr += str(li[0]//num) +'/' + str(str(li[i]//num))
    print(aswr)

## 다른 사람 코드 72ms 
import sys
import math
n = int(sys.stdin.readline())
ar = list(map(int,sys.stdin.readline().split()))
for i in range(len(ar)):
    if i == 0:
        p = ar[i]
    else:
        g = math.gcd(p,ar[i]) # 최대 공약수 계산하는 내장함수 gcd
        print('%d/%d' % (p//g,ar[i]//g))
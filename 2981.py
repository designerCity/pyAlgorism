# # ## 시간 복잡도가 O(N**2)
# # n = int(input())

# # inspect = []
# # for _ in range(n):
# #     inspect.append(int(input()))
# # inspect.sort()
# # a = inspect[0]
# # for i in range(2, a+1): # i 는 나누는 숫자
# #     left_n = 0
# #     cnt = 0
# #     for j in range(n): # n idx
# #         if j == 0:
# #             left_n = inspect[j] % i
# #             cnt += 1
# #         elif inspect[j] % i == left_n : # 첫 번째로 나눈 나머지와 그 후의 나머지가 다르면 break
# #             cnt += 1
# #     if cnt == n:
# #         print(i, end=' ')
# ## 이것 또한 시간 복잡도가 큼
# n = int(input())
# all_li = []
# srch_li = []
# sub = 0
# for i in range(n):
#     all_li.append(int(input()))

#     if i == 0:
#         sub = all_li[0]
#     else:
#         sub = abs(all_li[i] - all_li[i-1])
#     srch_li.append(sub)
# srch_li.sort()

# for j in range(2, all_li[0]):
#     cnt = len(srch_li) - 1
#     for i in range(len(srch_li)):
#         if srch_li[i] % j == 0:
#             cnt -= 1
#     if cnt == 0:
#         print(j, end=' ')


import math
t = int(input())
s = []
answer = []
gcd = 0
# math gcd 는 최대 공약수를 구하는 method 이다. 
# # 각 정수를 받고 그 이후에 차이가 1 나는 index 끼리 뺄셈한 것들을 최대공약수를 구해준다.
for i in range(t):
    s.append(int(input()))
    if i == 1:
        gcd = abs(s[1] - s[0])  
    gcd = math.gcd(abs(s[i] - s[i - 1]), gcd)

gcd_a = int(gcd ** 0.5)
# 최대 공약수는 짝을 이루고 있기 때문에 루트까지만 탐색해도 된다. 
for i in range(2, gcd_a + 1):
    if gcd % i == 0:
        answer.append(i)
        answer.append(gcd // i)
answer.append(gcd)
answer = list(set(answer))
answer.sort()

for i in answer:
    print(i, end = ' ')
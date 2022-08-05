# # 내 코드 시간 초과
# a, b = map(int, input().split())

# def factorial(n):
#     if n == 0:
#         return 1
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result

# rvr= list(str(factorial(a) // (factorial(b) * factorial(a-b))))

# cnt = 0
# for i in range(len(rvr)-1, 0,-1):
#     if int(rvr[i]) == 0:
#         cnt += 1
#     else:
#         print(cnt)
#         break

n, m = map(int, input().split())

def two_cnt(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two

def five_cnt(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five
# 조합 n! / ((n -m)! * m! )
t_f_cnt = min(two_cnt(n) - two_cnt(n - m) - two_cnt(m), five_cnt(n) - five_cnt(n - m) - five_cnt(m))
print(t_f_cnt)
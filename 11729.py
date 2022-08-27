# n = int(input()) # 첫번째 장대에 쌓인 원판의 개수 
# n1 = list(range(1, n+1))
# circle_1 = list(reversed(n1)) # 1번 원판
# circle_2 = [] # 2번 원판
# circle_3 = [] # 2번 원판
# # 원판을 1->3으로 옮기려고 함
# # 쌓아 놓은 원판은 항상 위의 것이 아래 것보다 작아야 한다. 

# def hamoi(m):
#     # x = circle_1[-1]

#     if n == m:
#         circle_3.append(circle_1[-1])
#         circle_1.remove(circle_1[-1])
#         circle_2.append(circle_1[-1])
#         circle_1.remove(circle_1[-1])
#     # y = circle_2[-1]
#     # z = circle_3[-1]
#     # if (x > z) and (y > z):

#     # if 
#     # cnt = 0 # 옮긴 횟수     

# # def hamoi():
# #     circle_1.remove(1)
# hamoi(n)

# print(circle_1)
# print(circle_2)
# print(circle_3)








import sys
input = sys.stdin.readline
n = int(input())

def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return
    else:
        hanoi(n-1, start, 6 -start -end)
        print(start, end)
        hanoi(n-1, 6 -start -end, end)

print(2 ** n - 1)
hanoi(n, 1, 3)
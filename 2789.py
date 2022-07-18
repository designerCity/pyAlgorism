# bruceforce 알고리즘 모든 경우의 수 탐색하는 알고리즘
# #  IDE 에서는 맞았지만, baekJoon 에서 억까한다...
# # # 생각했지만, 문제는 n 을 넘으면 안된다.
n, m = map(int, input().split())
# 굳이 이것을 반복문으로 받을 필요가 전혀 없다.
arr = list(map(int, input().split()))

forker = []
for i in range(n):
    for j in range(i+1, n):
        for z in range(j+1, n):
            if arr[i] + arr[j] + arr[z] <= m:
                forker.append(arr[i] + arr[j] + arr[z])

min_forker = []
# forker 리스트에서 m 과 가까운 리스트를 빼주는 작업
for a in forker:
    min_forker.append(abs(m - a)) # abs() method 를 통해서 절댓값을 씌운다

min_num = min(min_forker)
list_num = min_forker.index(min_num)
num = int(forker[list_num])
print(num)

# # 다른 사람의 코드를 참조한 코드
# n, m = map(int, input().split())
# # 굳이 이것을 반복문으로 받을 필요가 전혀 없다.
# arr = list(map(int, input().split()))
# result = 0
# for i in range(n):
#     for j in range(i+1, n):
#         for z in range(j+1, n):
#             if arr[i] + arr[j] +arr[z] > m:
#                 continue
#             else:
#                 result = max(result, arr[i] + arr[j] +arr[z])
# print(result)
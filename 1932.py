n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))




# # 이거도 그리디인거 같음@@!@@!@!@!
# value_all = []
# # idx = 0
 
# for i in range(1, n): # 한 줄 row
#     b = []
#     for j in range(i):  # j : row 에서 하나 둘씩
#         a = li[i-1][j] # 
#         for idx in range(2): # j 하나당 양 옆으로 가게끔
#             if idx == 0:
#                 c = a + li[i][j+ idx]
#             # elif idx == 1:
#             #     d = a + li[i][j+ idx]
#             print(a, c)
#             b.append(c)
#     value_all.append(b)
#     # if li[i][idx] >  li[i][idx + 1]:
#     #     a += li[i][idx] 
#     # else:
#     #     a += li[i][idx+1]
#     #     idx = idx + 1

# print(value_all)    
# # # 첫 [] 는 row
# # for j in range(n):
# #     for i in range(n):
# #         max(li[n-i-1][i], li[n-i-1][i])

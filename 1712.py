# # 손익분기점

# interest_num = list(map(int, input().split()))
# break_even_point = 1
# if interest_num[1] >= interest_num[2]:
#     break_even_point = -1

# while interest_num[1] < interest_num[2]:
#     interest = interest_num[2] - interest_num[1]
#     if interest_num[0] > break_even_point * interest:
#         break_even_point += 1
#     else:
#         break_even_point += 1
#         break
    

# print(break_even_point)

a,b,c = map(int,input().split())

if b >= c:  # 가변비용이 노트북 가격보다 같거나 크면
    print(-1)
else:
    print(a//(c-b)+1)
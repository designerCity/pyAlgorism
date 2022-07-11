noon, night, height = map(int, input().split())
days = (height - noon) / (noon - night) + 1
print(int(days) if days == int(days) else int(days)+1)

# # 부등식의 계산은 시간이 비교적 오래 걸린다. 
# noon, night, height = map(int, input().split())

# days = 0 # 올라가는 데 걸리는 일수
# now_height = 0

# while 1:
#     days += 1
#     if days * noon - night *(days - 1) >= height:
#         break

# print(days)



# tree = list(map(int, input().split()))

# noon = tree[0]
# night = tree[1]
# height = tree[2]

# days = 1 # 몇일
# while noon < height:
#     days += 1
#     height -= noon
#     height += night
    
# print(days)

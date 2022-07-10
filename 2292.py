# 벌집
num = int(input())
cnt = 1
num_beehouse = 1 # 벌집의 개수
while num > num_beehouse:
    num_beehouse += 6 * cnt
    cnt +=1

print(cnt)

# cnt = 1
# if num == 1:
#     cnt = 1
# elif num <= 7:
#     cnt = 2
# elif num <= 19:
#     cnt = 3
# elif num <= 37:
#     cnt = 4
# elif num <= 61:
#     cnt = 5
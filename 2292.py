# 벌집
num = int(input())
cnt = 1
num_beehouse = 1 # 벌집의 개수
while num > num_beehouse:
    num_beehouse += 6 * cnt
    cnt +=1

print(cnt)
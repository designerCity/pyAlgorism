repeat_num = int(input())

for _ in range(repeat_num):
    cnt, word = input().split()
    for x in word:
        print(x*int(cnt), end='')
    print() # 줄넘김
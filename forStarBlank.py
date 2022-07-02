star = int(input())

for i in range(1, (star+1)):
    
    star_num = i * '*'
    blank_num = " " * (star - i)
    print(blank_num + star_num)

    
# 더 간단한 풀이
star=int(input())
for i in range(1,(star+1)):
    print(" "*(star-i) + "*"*i)

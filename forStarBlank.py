star = int(input())

for i in range(1, (star+1)):
    
    star_num = i * '*'
    blank_num = " " * (star - i)
    print(blank_num + star_num)

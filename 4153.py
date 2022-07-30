while True:
        r_tri = list(map(int, input().split()))
        max_num = max(r_tri)
        if sum(r_tri) == 0:
                break
        r_tri.remove(max_num)
        if r_tri[0] ** 2 + r_tri[1] ** 2 == max_num ** 2:
                print('right')
        else:
                print('wrong')

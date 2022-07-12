t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())

    num = n // h + 1 # w 의 길이가 얼마나 되는지를 볼 수 있다. 
    floor = n % h
    if n % h == 0:
        num = n // h
        floor = h
    print(f'{floor*100 + num}')



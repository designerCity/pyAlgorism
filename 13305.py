n = int(input())

distance = list(map(int, input().split()))
oil_value = list(map(int, input().split()))
all_value = distance[0] * oil_value[0]

i = 0
minimum = oil_value[0]

while n != 2:
    i += 1
    if oil_value[i] >= minimum: # 다음 것이 큰 경우
        all_value += minimum * distance[i]
    else:
        minimum = oil_value[i]
        all_value += minimum * distance[i]
    n-=1

print(all_value)

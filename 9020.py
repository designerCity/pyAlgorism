# # 정답은 맞았지만, 시간 초과 .....

# n = int(input()) # test 개수

# for _ in range(n):

#     a = int(input())
#     list_gold = []

#     # print(list_gold)

#     for i in range(2, a+1):
#         error = 0
#         for j in range(2, i):
#             if i % j == 0: # 나누어떨어짐
#                 error += 1
#         if error == 0:
#             list_gold.append(i)

#     psb_gold = [] # 골드바흐 추측이 성립할 수 있는 소수의 쌍을 담을 리스트
#     min_gold = [] # 가장 작은 값을 담을 리스트

#     for z in range(len(list_gold)):
#         for v in range(z, len(list_gold)):
#             if a == list_gold[z] + list_gold[v] :
#                 psb_gold.append([list_gold[z], list_gold[v]])
#                 min_gold.append(list_gold[v] - list_gold[z])
#     min_index = min_gold.index(min(min_gold))

#     print(psb_gold[min_index])




def Goldbug():
    check = [False, False] + [True] * 10000
    # check list 에 소수만 남도록 (소수는 True)
    for i in range(2, 101):
        if check[i] == True:
            for j in range(i+i, 10001, i):
                check[j] = False

    gold_num = int(input())
    for _ in range(gold_num):
        n = int(input())
        
        half_up = n // 2 # 절반
        half_dwn = half_up

        for _ in range(10000):
            if check[half_dwn] and check[half_up]:
                print(half_dwn, half_up)
                break
            half_up += 1
            half_dwn -= 1
Goldbug()

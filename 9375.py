t = int(input()) # test number

for _ in range(t):
    test_num = int(input())
    dic_closet = {}
    for i in range(test_num):
        wear = list((input().split()))
        # 동일하면 같은 리스트에 아니면 다른 객체에 둬야한다. 
        if wear[1] in dic_closet:
            dic_closet[wear[1]].append(wear[0])
        else:
            dic_closet[wear[1]] = [wear[0]]

    cnt = 1

    for k in dic_closet:
        cnt *= (len(dic_closet[k])+1)
    print(cnt-1)

# # python list 화에 대해서
# dic = {'test': [0, 1, 2, 3]}

# print(dic.values()) # dict_values([[0, 1, 2, 3]])
# print(dic.items()) # dict_items([('test', [0, 1, 2, 3])])
# print(dic) # {'test': [0, 1, 2, 3]}

# # dic - value 가 list 일 때 list append
# dic['test'].append(5)
# print(dic) # {'test': [0, 1, 2, 3, 5]}
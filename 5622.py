alph_num = input().upper()
count = 0

for al in alph_num:
    if ((al == 'A') or (al == 'B') or (al == 'C')):
        count += 3
    elif ((al == 'D') or (al == 'E') or (al == 'F')):
        count += 4
    elif ((al == 'G') or (al == 'H') or (al == 'I')):
        count += 5
    elif ((al == 'J') or (al == 'K') or (al == 'L')):
        count += 6
    elif ((al == 'M') or (al == 'N') or (al == 'O')):
        count += 7
    elif ((al == 'P') or (al == 'Q') or (al == 'R') or (al == 'S')):
        count += 8
    elif ((al == 'T') or (al == 'U') or (al == 'V')):
        count += 9
    elif ((al == 'W') or (al == 'X') or (al == 'Y') or (al == 'Z')):
        count += 10
print(count)


# alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# word = input()

# time = 0
# for unit in alpabet_list :  
#     for i in unit:  # alpabet 리스트에서 각 요소를 꺼내서 한글자씩 분리
#         for x in word :  # 입력받은 문자를 하나씩 분리
#             if i == x :  # 두 알파벳이 같으면
#                 time += alpabet_list.index(unit) +3  # time = time + index +3
# print(time)
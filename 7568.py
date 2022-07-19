n = int(input())
mass_list = []

for _ in range(n):
    mass_list.append(list(map(int, input().split())))

mass_ranking = [1] * 5
# 덩치가 작은 경우 + 1 을 해주자
for i in range(n):
    for j in range(n):
        # # 몸무게 비교 and 키 비교

        if (mass_list[i][0] < mass_list[j][0]) and (mass_list[i][1] < mass_list[j][1]):
            mass_ranking[i] = mass_ranking[i] + 1
# 정수 요소를 가지고 있는 리스트를 정수 띄어쓰기형으로
print(mass_ranking)
for i in range(len(mass_ranking)):
    print(mass_ranking[i], end=" ")

    
# # n = int(input())
# # mass_list = []

# # for _ in range(n):
# #     mass_list.append(list(map(int, input().split())))

# # mass_ranking = []
# # # 덩치가 작은 경우 + 1 을 해주자
# # for i in range(n):
# #     grade = 1
# #     for j in range(i+1, n):
# #         # 몸무게 비교 and 키 비교
# #         if (mass_list[i][0] < mass_list[j][0]) and (mass_list[i][1] < mass_list[j][1]):        
# #             grade = grade + 1
# #     print(grade,end=' ')



# # ############# 정답
# num_student = int(input())
# student_list = []

# for _ in range(num_student):
#     wt, ht = map(int, input().split())
#     student_list.append((wt, ht))

# for i in student_list:
#     rank = 1
#     for j in student_list:
#         if i[0] < j[0] and i[1] < j[1]:
#                 rank += 1
#     print(rank, end = " ")
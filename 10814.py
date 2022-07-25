# 안정 정렬(stable sort)

n = int(input()) # 온라인 저지 회원 수
member_list = []
for _ in range(n):
    member_list.append(input().split())

member_list.sort(key= lambda x: int(x[0]))

for i in range(n):
    print(member_list[i][0], member_list[i][1])
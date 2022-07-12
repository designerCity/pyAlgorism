sugar_kg = int(input())

# 5 또는 3만 사용할 때
sugar_list = []

kg_5 = sugar_kg // 5

for i in range(kg_5+1):
    left_sugar = sugar_kg - (i * 5)
    kg_3 = left_sugar // 3

    if (sugar_kg == int(kg_3 * 3 + i * 5)):
        sugar_list.append(i + kg_3)
if sugar_list == []:
    sugar_list.append(-1)
print(min(sugar_list))
# min_sugar = min(sugar_list)
# print(min_sugar)
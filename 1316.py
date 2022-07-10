rp_num = int(input())
# grp_word_list = []
result = rp_num
# 문자열을 리스트화 그룹 단어는 연속하는지를 봐야한다. 
for i in range(rp_num):
    # word = grp_word_list.append(input())
    word = input()
    for j in range(0, len(word) - 1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            result -= 1
            break
print(result)


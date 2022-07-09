words = input().upper() # 모든 입력 문자를 대문자화
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list =[]
# count mehtod 를 사용하면 비교적 쉽게 해결 가능
for i in unique_words: 
    cnt = words.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) >= 2:
    print('?')
else:
    print(unique_words[cnt_list.index(max(cnt_list))])
# 연속된 일부분의 부분 문자열

all_str = str(input())
set1 = set()
for i in range(len(all_str)):
    set1.add(all_str[i])
    set1.add(all_str[i:])
    for j in range(len(all_str) - i+1):
        set1.add(all_str[i:len(all_str)-j-1])
set1.remove('')

print(len(set1))

# 쪼금 더 빠른 방법(다른 사람 code)
word = input()
s = set()
l = len(word)

for i in range(1, l + 1):
    for j in range(l - i + 1):
        s.add(word[j:j+i])
print(len(s))
# # 왜 str out of range 가 안나오는지 모르겠다.
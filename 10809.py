# 알파벳 찾기
word = input()
abc = 'abcdefghijklmnopqrstuvwxyz'

for i in abc:
    # in mehthod 를 사용하면 비교적 간단하게 풀 수 있다. 
    if i in word:
        print(word.index(i), end=' ')
    else:
        print( -1, end=' ')



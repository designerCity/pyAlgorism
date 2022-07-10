word1, word2 = input().split()
word1 = int(word1[::-1]) # [::-1] : 역순
word2 = int(word2[::-1])


print(max(word1, word2))
# 분수 출력 알고리즘

num = int(input()) # n 번째 분수

line = 0
end = 0

top = 0
bottom = 0 
# 이전까지의 합을 구하는 반복문
while num > end:
    line += 1
    end += line


diff = end - num # 반복문의 마지막 부분 때문에 num- end 가 아닌 end - num 이 되어야 함.


# line 이 짝수, 분모가 크게 시작
if line % 2 == 0: 
    top = line - diff # num 보다 작은 곳까지가 아닌 num 이 포함된 라인까지 이므로 
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff

print("%d/%d"%(top,bottom))
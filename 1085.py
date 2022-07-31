# 직사각형에서 탈출

x, y, w, h = map(int, input().split())
all = []
# y 는 h

if y > h:
    all.append(y-h)
else:
    all.append(min(h-y, y))
if x > w:
    all.append(x-w)
else:
    all.append(min(w-x, x))
print(min(all))
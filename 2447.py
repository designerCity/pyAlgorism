
# 기준은 9개로 생각해야한다.

# 3분의 1 까지는 채우고 
# 그 이후의 3분의 1 까지는 비우고
# 나머지 3분의 1은 지우고

def star_jg(m):
    if m == 1:
        return ['*']
    
    Stars = star_jg(m//3)
    L = []
    
    # Star 는 줄을 의미한다.
    for star in Stars:
        L.append(star*3)
    for star in Stars:
        L.append(star + ' ' * (m//3) + star)
    for star in Stars:
        L.append(star*3)

    return L

n = int(input())

print('\n'.join(star_jg(n)))

# def draw_stars(n):
#   if n==1:
#     return ['*']

#   Stars=draw_stars(n//3)
#   L=[]

#   for star in Stars:
#     L.append(star*3)
#   for star in Stars:
#     L.append(star+' '*(n//3)+star)
#   for star in Stars:
#     L.append(star*3)

#   return L

# N=int(input())
# print('\n'.join(draw_stars(N)))

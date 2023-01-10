n = int(input())
all_li = list(map(int, input().split()))

m = int(input())
srch_li = list(map(int, input().split()))
all_li = sorted(all_li)

all_li.sort()

# 이 binary_srch 는 해당하는 index 를 리턴한다
def binary_search(target, data):
    # data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return True # 함수를 끝내버린다.
        if data[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return False

for i in range(m):
    idx = binary_search(srch_li[i], all_li)
    if idx:
        print(1)
    else:
        print(0)

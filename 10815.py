card_num = int(input())  # card 의 개수 

have_card = list(map(int, input().split()))
srch_num = int(input())
srch_card = list(map(int, input().split()))

have_card.sort()
# 시간복잡도를 줄이기 위한 방안으로 이진탐색법 사용 (숫자에 대한 이진탐색법)
def binary_srch(arr, tgt, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == tgt:
            return mid
        elif arr[mid] < tgt:
            start = mid + 1
        else:
            end = mid - 1
    return None
for i in range(srch_num):
    if binary_srch(have_card, srch_card[i], 0, card_num -1) != None:
        print(1, end=' ')
    else:
        print(0, end=' ')
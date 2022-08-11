#영어로 문제는 이해가 처음에 잘 안되었었음. 문제 자체는 쉬움
# 
# A = [0, 1, 0, 1, 1]이라고 했을 때, 0이 출력되면 그 뒤로 나오는 1의 개수(3) + 2번째 0이 출력된 뒤로 나오는 1의 개수(2)인 5를 출력하면 됩니다.
#그리고 출력할 값이 1000000000보다 크면 -1을 출력합니다.



def solution(A):
    ones,ans = 0,0
    if 1 in A : ones = A.count(1)
    else: return 0
    for a in A:
        if a: ones-=1
        else:ans+=ones
        if ans>1000000000: return -1
    return -1  if ans>1000000000 else ans
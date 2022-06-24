import sys #패션왕  #조합(combination)
reader = sys.stdin.readline

t = int(reader().rstrip())
for _ in range(t):
    n = int( reader().rstrip() )
    dic = {}
    for _ in range(n):
        c, g = reader().split()
        if g in dic : dic[g] += 1
        else : dic[g] = 1
    ans = 1
    for i in dic.keys()  :
        ans *= (dic[i] + 1)       # 아이디어 
    ans -= 1                      # 아이디어 
    print(ans)        
    



#조합(combination) - 순서x itertools.combinations(리스트 ,개수)
#순열(permutation) - 순서o itertools.permutations(리스트 ,개수)
# 둘다 오브젝트를 반환하기때문에 list로 형변환 필요
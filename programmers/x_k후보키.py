def solution(relation):
    ans = 0
    ans_list = []
    for i in range(1, 1<<len(relation[0])): # 후보키 combination
        # 후보키가 될수있는지 확인 과정
        se = set() 
        for y in range(len(relation)): 
            tmp = ''
            for x in range(len(relation[0])):
                if i &(1<<x) : tmp += str( relation[y][x] )
            se.add(tmp)
        if len(se) == len(relation): # 후보키가 될 수 있을때 - 최소성 만족 검사 
            notDupl = True
            for num in ans_list :
                if (num & i) == num: notDupl = False; break # 최소성을 만족하지 못하는 경우
            if notDupl : ans_list.append(i)

    return len(ans_list)
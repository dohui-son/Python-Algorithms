def solution(array, commands):
    ans = []
    for c in commands:
        tmp = array[c[0]-1:c[1]]
        tmp = sorted(tmp)
        ans.append(tmp[c[2]-1])
    return ans

    ###
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
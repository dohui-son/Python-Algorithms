from collections import defaultdict, deque
from itertools import permutations


def cal_res(a,b,what):
    if what == '-': return a-b
    elif what == '+': return  a+b
    else: return a*b

def cal_one(arr, op):
    ret = deque([arr[0]])
    for i in range(1,len(arr), 2):
        if arr[i] != op: ret.extend([arr[i],arr[i+1]])
        else: ret[-1] = cal_res(ret[-1], arr[i+1], op)
    return ret


def cal(arr, op):
    for oper in op : arr = cal_one(arr,oper)
    return abs(arr[0])


def solution(exp):
    ans = 0
    arr = []
    st = ''
    for s in exp:
        if s=='+' or s=='*' or s=='-': 
            arr.append(int(st)) 
            st = ''
            arr.append(s)
        else: st+=s
    arr.append(int(st))

    for l in permutations(['+','-','*'], 3):
        ans = max(ans, cal(arr.copy(), list(l)) )
    return ans




# 숏코딩
def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)
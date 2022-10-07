from collections import deque
def solution(s):
    stk = deque()
    for ss in s:
        try:
            if ss == ")" and stk[-1] == "(": stk.pop()
            elif ss == ")" and stk[-1] != "(": return False 
            elif ss == "}" and stk[-1] == "{": stk.pop()
            elif ss == "}" and stk[-1] != "{": return False 
            elif ss == "]" and stk[-1] == "[": stk.pop()
            elif ss == "]" and stk[-1] != "[": return False 
            else: stk.append(ss)
        except: return False
    return False if stk else True
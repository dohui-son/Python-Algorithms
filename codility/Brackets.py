from collections import deque
def solution(S):
    n = len(S)
    if n == 0 : return 1
    st = deque()
    
    for s in S:
        if s == "{" or s == "[" or s == "(": st.append(s)
        elif  s == "}" or s == "]" or s == ")":
            if len(st) == 0: return 0
            if s == "}": 
                if st[-1] !="{": return 0
                else: st.pop()
            elif  s == "]":  
                if st[-1] !="[": return 0
                else: st.pop()
            elif s == ")": 
                if st[-1] !="(": return 0
                else: st.pop()
        else: continue
    if len(st): return 0
    else: return 1
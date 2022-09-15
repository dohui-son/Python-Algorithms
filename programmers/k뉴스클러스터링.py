from collections import Counter,deque,defaultdict

def solution(s1, s2):
    s1 = s1.lower(); s2 = s2.lower()
    orda, ordz = ord('a'), ord('z')
    ans = 0
    n,m = len(s1),len(s2)
    dic1 = defaultdict(int)
    dic2 = defaultdict(int)
    se = set()

    longer = n if n>m else m
    f1 , f2 = True,True
    for i in range(longer):
        if i<n-1: 
            o1,o2 = ord(s1[i]), ord(s1[i+1])
            if orda <= o1 and o1<=ordz and orda <= o2 and o2<=ordz:
                se.add( s1[i]+s1[i+1] )
                dic1[s1[i]+s1[i+1]] += 1; f1 =False
        if i<m-1: 
            o1,o2 = ord(s2[i]), ord(s2[i+1])
            if orda <= o1 and o1<=ordz and orda <= o2 and o2<=ordz: 
                se.add( s2[i]+s2[i+1] )
                dic2[s2[i]+s2[i+1]] += 1; f2 = False
    if f1 and f2: return 65536

    maxi,mini = 0,0
    for s in se:
        maxi += max(dic1[s], dic2[s])
        mini += min(dic1[s],dic2[s])

    return int(mini/maxi*65536-mini/maxi*65536%1)
def solution(people, limit):
    ans = 0
    people.sort()
    s,e = 0, len(people)-1
    while s<=e:
        if people[s]+people[e] <= limit : ans+=1; s+=1;e-=1
        else : ans+=1; e-=1
    return ans
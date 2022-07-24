from itertools import permutations
def makePrime(n):
    prime=[0,0]+[1]*~-n 
    for i in range(int(n**.5)+1):
        if prime[i]:prime[i*i::i]=[0]*(n//i-i+1)
    return prime

def solution(numbers):
    ans = 0; nlen = len(numbers)
    nums = [i for i in numbers]
    p = makePrime(10000000)
    nums = [n for n in numbers]                   
    per = []                                      
    for i in range(1, len(numbers)+1):            
        per += list(permutations(nums, i))        
    new_nums = [int(("").join(p)) for p in per]  
    for i in new_nums: 
        if p[i]: ans+=1  ;p[i] = 0
    return ans
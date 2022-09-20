n = int(input().rstrip())
# p = [0,0]+[1]*~-n
# for i in range(int(n**.5)+1):
#     if p[i] : p[i*i::i] = [0]*(n//i-i+1)
# p = [2] + [ i for i in range(3,n+1,2) if p[i]]
# print(p)


p = [0,0]+[1]*~-n
for i in range(int(n**.5)+1):
    if p[i] : p[i*i::i] = [0]*(n//i-i+1)
p = [2] + [i for i in range(3,n+1,2) if p[i]]


def isPrime(k):
    if k == 2 or k == 3: return True  
    if k % 3 == 0 or k % 2 == 0 or k < 2: return False 
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0 : return False
    return True
n = int(input().rstrip())
p = [0,0]+[1]*~-n
for i in range(int(n**.5)+1):
    if p[i]: p[i*i::i] = [0]*(n//i-i+1)
p = [2]+[i for i in range(3,n+1,2) if p[i]]
print(p)
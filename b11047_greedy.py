p,*q=list(open(0))
k=int(p[2:])
c=0
for i in map(int,q[::-1]):c+=k//i;k%=i
print(c)
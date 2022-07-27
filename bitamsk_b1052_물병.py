n,k=map(int,input().split())
nn=n
while bin(nn).count('1')>k:
    nn+=nn&-nn
print(nn-n)
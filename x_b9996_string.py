#https://www.acmicpc.net/source/14670293
n=int(input()) #한국이 그리울 땐 서버에 접속하지  #못풀었던문제
a,b = input().split('*')
for x in range(n):
	c=input()
	d,e=c[:len(a)],c[len(c)-len(b):]
	if((a==d and b==e) and (len(c) >= len(a)+len(b))):
		print("DA")
	else:
		print("NE")
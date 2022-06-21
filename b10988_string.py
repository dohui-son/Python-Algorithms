import sys #팰린드롬인지 확인하기
reader = sys.stdin.readline
str = reader().rstrip()
if str == str[::-1] : print(1)   #문자열 거꾸로 str[::-1]
else : print(0)
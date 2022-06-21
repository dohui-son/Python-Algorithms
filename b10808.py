import sys #알파벳 개수 - 아스키코드
reader = sys.stdin.readline
str = reader().rstrip()
arr = [0]*26
for i in str:
    arr[ord(i)-ord('a')] += 1
for i in arr:
    print(i, end=' ')




# ord('a') 문자를 넣으면 그 문자에 해당하는 아스키코드를 숫자로 반환
# chr(65) // A // 괄호( ) 안에 숫자를 넣으면 그 숫자의 아스키코드에 대응하는 문자를 반환
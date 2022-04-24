#자료형
#data type - 숫자, 문자열, bool
#자료구조 - 변수, 리스트, 튜플, 딕셔너리, 집합

#data type 1) 숫자형
# Int 정수형 1, -1
# Float 실수 1.23, -34.54 (소수점 아래 17자리까지 저장가능)
# 컴퓨터식 지수 표현 4.24e10 (4.24 곱하기 10의 10승), 4.24e-10(4.24곱하기 10의 -10승 소수점 표현)
# 8진수 0o37
# 16진수 0x7A




a = 1
print(type(a))

a = 1.123456789123456789
print(a)
print(type(a))

a = 4.24e10
print (a)
print(type(a))

a = 4.24e-10 #소수점 표현
print(a)
print(type(a))

#사칙연산
a = 3
b = 4
print(a/b) #나누기 결과값
print(a//b) #나누기 몫
print(a%b) #나누기 나머지값
print(a**b) #제곱


#data type 2) 문자열
a = 'dohee'
a = "dohee's \n"
print(type(a))
a = """dohee
with enter without escape code"""
print(a)
#(1)에스케이프코드
print('\t 탭')
print('\\ 백슬래시 출력')
print('\' 작은따옴표 사용')
print('\" 큰따옴표 사용')
print('\000 널문자')

print('\r 캐리지 리턴(줄바꿈 문자, 현재 커서를 가장 앞으로 이동)')
print('\f 폼피드 (줄바꿈 문자, 현재 커서를 다음줄로 이동)')
print('\b 백스페이스')

a = 'a'
b = 'b'
print(a+b)
print(a*100)

#(2)인덱싱
#(3)슬라이싱 문자열변수명[이상 : 미만 : 간격]
a = '0123456789'
print(a[0:3])
print(a[:3])
print(a[0:-1])
print(a[:-1])
print(a[1:-1])
print(a[-1:-1])
print(a[-1:3])
print(a[-9:-3])
print(a[:-2])
print(a[:])
print(a[::2])
print(a[::-1])
print(a[:6:-1])
print(a[:6:-2])

#(4)문자열 포맷팅 - 매핑되어서 들어감
# %s 문자열(문자, 정수, 부동소수,8진수 등등 대신 쓸수 잇음)
# %c character
# %d Integer
# %f 부동소수 float
# %o 8진수
# %x 16진수
## %% literal (문자 %자체)

a = "I eat %d apples. " % 3
print(a)
num = 5
day = "3일"
a = "I ate %d apples %s ago. " %(num,day)
print(a)
a = "I ate %s appples %s ago." %(num,day)
print(a)

a = "12345 {} ads".format("안녕")
print(a)

a = "12345{name} 1234 {name}".format(name="이름")
print(a)

a = "1234 {name} 123 {}".format("빈칸", name="이름")
print(a)

a = "aaa {age} aaaaa {name}".format(age=3, name="이름")
print(a)

#파이썬 3.6버전 이상
name = "int"
a = f"나의 이름은 {name}입니다"
print(a)

#정렬과 공백
a = "%10s" %"hi"
print(a)
a = "%-10sjane"%'hi' # 마이너스는 왼쪽정렬
print(a)

# 소수점 자르기
print("%0.4f" % 0.123456789) #4번째자리수까지 반올림하여 매핑
print("%0.4f" %0.123123123) #4번째자리수까지 반올림하여 매핑

# count 문자열 개수 세기
a = "bbbbbbbbbbbbbbbbaaaaaaaa"
print( a.count('b') )
# find 해당문자열이 최초로 발견되는 인덱스
print( a.find('a') ) 
print( a.find('d') ) # 없으면 -1을 리턴 // 동일 경우 a.index('d')는 에러가 난다

a = ",".join('aaaaaabccccd')   
print(a)
#join 리스트에서 자주씀
a = ",".join(["a","b","c"])
print(a)
a = "\t".join(["a","b","c"])
print(a)

#lower upper 소문자로 대문자로
a = "hi"
print(a.upper())
a = a.upper()
print(a.lower())

#strip 양쪽 공백 지우기
a = "      d   "
print(a.strip())
a = "    a    d     d    d "
print(a)

#replace
a = "hi hi hi"
print( a.replace("h","t"))
print( a.replace(" ","") )
print( a.replace("hi ","to") )
print( a.replace("hi ","  to") )

# split
# (띄어쓰기)기준으로 잘라서 리스트형으로 만듬
a = "abc def ggg"
print( a.split() ) 
a = "a:b:c:d"
print( a.split(':') )
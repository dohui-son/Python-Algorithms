num = 10
day="three"
a = "I ate %d apples for %s" %(num,day)
print(a)
a = "I ate %s apples for %s" %(num,num)
print(a)

a = "I ate {} apples for %s".format("안녕")
print(a)

a = "I ate {name} apples for %s".format(name="사과")
print(a)

a = "{you} ate {name} apples for %s".format(you=18,name="사과") %(day)
print(a)

# 파이썬 버전 3.6 이상
name ="이름"
a =f"my name is {name}. "
print(a)

a= "%f" % 3.1223444555 #3.122344 까지만 출력됨
print(a)
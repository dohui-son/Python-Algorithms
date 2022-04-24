# DataStructure : 변수, 리스트, 튜플, 딕셔너리, 집합(set)
# (1) 리스트
#리스트나 튜플은 거의 유사하지만 리스트는 값과 크기 변동이 가능하다.
a = [0,1,"hi", 3, ["안녕",4]]
print(a)
print(a[4])
print(a[4][1])
print(a[-1])
#리스트 슬라이싱
a = [1,2,3,4,5,6,7]
print( a[0:2] )  #변수명[이상:미만:간격]
print( a[:2] )
print(a[:-1])
print(a[::2])
#리스트 더하기
b = ["a","a","a","a"]
print(a+b)
print(b*10)

#리스트 교체
b[0] = 0
print(b)
#리스트 이렇게 하면 에러남 b[0:2] = 1
b[0:2] = [0,1]
print( b )

#리스트 삭제
b[:2] = []
print( b )
#리스트 삭제
del b[0]
print(b)

#append 리스트 맨뒤에 요소 추가
b.append("추가추가")
print(b)

#sort - 자료타입 혼합안됨 / 오름차순 / 알파벳 or 가나다순
b = [9,8,7,6,5,4,3]
b.sort()
print(b)
b = ['d','e','a']
b.sort()
print(b)

#뒤집기
b.reverse()
print(b)
b = [9,8,7,2,55,5,4,3]
b.reverse()
print(b)

#index 해당 인덱스 반환
print(b.index(55)) #없으면 에러남

#insert 특정인덱스에 삽입
a = [1,5,3]
a.insert(0,4) # 0번째 인덱스에 4를 추가해라
print(a.index(4))
#remaove
a.insert(0,4)
a.insert(-1,4)
a.remove(4) # 해당 값을 삭제해라 - 해당 값이 여러개일 경우 인덱스 낮은 값을 지움
print(a)

#pop 
a.pop()
print(a)

#count
print( a.count(1) ) #해당 값의 개수
print( a.count(-1) ) #해당 값이 리스트에 없을때 0출력

# extend 리스트 확장
a = [1,2,3]
a.extend([4,5])
print(a)
b.extend(a)
print(b)

#join 리스트에서 자주씀
a = ",".join(["a","b","c"])
print(a)
a = "\t".join(["a","b","c"])
print(a)

# split
# (띄어쓰기)기준으로 잘라서 리스트형으로 만듬
a = "abc def ggg"
print( a.split() ) 
a = "a:b:c:d"
print( a.split(':') )

# DataStructure : 변수, 리스트, 튜플, 딕셔너리, 집합(set)
# (2) 튜플 
# 리스트와 달리 처음 설정한 길이와 값의 수정이 불가능하다
# 삭제 / 삽입 / 추가 (값변동) 불가능
t1 = (1,2,'a','b')

# del t1[0] 불가능
# t1[0] = 0 불가능

# 인덱싱, 슬라이싱 가능 --> 해당 튜플의 값 자체는 변동이 없음
print( t1[0:2] )
print(t1)
t2 = (1,2,3,'t','t')
print(t1+t2) #t1 t2 자체가 바뀌지는 않음
print(t1*3)

t3 = (1,2)
t3 = t3*3 #값을 변화시킨 것이 아니라 새로 정의함!!!!
print(t3)

# DataStructure : 변수, 리스트, 튜플, 딕셔너리, 집합(set)
# (3) 딕셔너리 
# == hash, map , object, JSON(API에 자주 활용됨)
#key를 통해 value를 얻는다(키로 값을 찾을 수 있음) ***key는 유일무이
dic = {1:'a', 1:'b'}
print(dic)
 
dic = {'name': 'Eric', 'age':15, 'list':[1,2,3,4,5]}
print( dic["list"])

# 새로운 키 및 값 추가
dic['name'] = 'dodo' #덮어쓰기 가능
print(dic['name'])
print(dic)
dic[1] = "안녕"
print(dic)

#del 삭제
del dic['name']
print(dic) 

# keys key들만 따로 뽑기
print(dic.keys())
a = dic.keys()
print(a)
print(type(a))

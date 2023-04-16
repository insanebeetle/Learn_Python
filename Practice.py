print(5)
print("풍선")
print("ㅋ"*10)
print(not True) #!가 아니라 not으로 역법 

animal = "강아지"
name = "킹"
age = 4
is_adult = age>3

print(animal + "의 이름은 "+name+"입니다. 이 아이는 "+ str(age) +"살입니다"+ str(is_adult))
"""
파이선의 print출력은 기본이 str값. 정수, 
불리언이 들어가면 str(변수)로 형변환 해줘야함
이게 주석문임.. 작은따옴표도 ㅇㅋ... 존나 근본없는 언어...
전체주석은 컨드롤+/ 
"""

#퀴즈
station = "사당"
print(station + "행 열차")
station = "신도릭"
print(station + "행 열차")
station = "인천공항"
print(station + "행 열차")

print(2**3) #8
print(20//3) #나누기

print(1 !=3 )

print(3>0 and 3<5) 
print((3>0)  & (3<5)) 

print(3>0 or 3<5) 
#print(3>0 짝대기 3<5) 

print(abs(-4)) #절대값
print(pow(4,2)) #제곱승
print(max(5,12)) #범위내 최대값
print(min(5,12)) #범위내 최솟값
print(round(3.245)) #반올림

from math import * #math 관련 함수 임포트하기
print(floor(4.99))
print(ceil(4.99))
print(sqrt(4.99))

from random import *

print(random()) #0.0~1.0 미만 임의의 값
print(random()*10)
print(int(random()*10)) #정수값 랜덤
print(int(random()*10)+1) #1~10사이의 정수값

# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)

print(randrange(1,46)) #1~46미만의 임의의값
print(randint(1,45)) #1~45 이라의 랜덤값

day = randint(4,28)
print("오프라인 스터티 : " + str(day) +"일" )
day = randint(4,28)
print("온라인 스터티 : " + str(day) +"일" )
day = randint(4,28)
print("온라인 스터티 : " + str(day) +"일" )
day = randint(4,28)
print("온라인 스터티 : " + str(day) +"일" )
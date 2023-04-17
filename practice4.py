# weather = input("오늘 날시는 어때요? ")
# if weather == "비":
#     print("우산")
# elif weather == "먼지":
#     print("마스크")
# else:
#     print("날씨 좋음")

# temp = int(input("기온은 ? "))
# if 30<= temp:
#     print("너무 더움")
# elif 10 <= temp & temp<30:
#     print("날씨 좋음")      
# elif 0 <=temp <10:
#     print("다소 추움")
# else:
#     print("졸라 추움")

#for waiting in [0,1,2,3,4]: #배열 수만큼 들어가서 나옴
for waiting in range(1, 6):    
    print("대기번호 : {0}".format(waiting))    

starb = ["유재호", "김인경", "손연경"]
for cust in starb:
    print("{0}.커피준비 됨".format(cust))     

cus = "유재호"
index = 5
while index >=1:
    print("{0}, 커피준비 됨. {1}번 남음".format(cus, index))
    index -= 1
    if index == 0:
        print("커피 매진")

# while True:
#         print("{0}, 커피준비 됨. {1}번 남음".format(cus, index))
#무한 반복루프 문 주의

# cus2 = "김인경"
# person = "Unknown"
# while person != cus2:
#     print("{0}, 커피 ㅇㅋ".format(cus2))
#     person = input("이름은? ")

absent = [2,5]
no_book = [7]
for student in range(1,11):
    if student in absent: #교집합일경우
        continue #이번 실행을 넘기고 실행 -스킵
    if student in no_book:
        print("오늘 수업 끝. {0}는 교무실".format(student))
        break #뒤 반복 무시하고 반복문 탈출
    print("{0}가 책을 읽는중".format(student))

student = [1,2,3,4,5]
print(student)
student = [i+100 for i in student] 
#i라는 변수에 100을 더해라, 이 i는 stu2의 값이다
print(student)   

#학생이름을 길이로 변환
student = ["김인경", "우재호", "손연경"]
student = [len(i) for i in student]
print(student)

#대문자변환
student = ["thor", "cap", "iron"]
student = [i.upper() for i in student]
print(student)


from random import *
#quiz
customer = 0
for i in range(1,51):
    time = randrange(5,51)
    if 5<= time <15:
        print("O {0}번째손님- 시간: {1}".format(i, time))
        customer +=1
    else:
        print("X {0}번째손님- 시간: {1}".format(i, time))

print("총 승객 : {0}".format(customer))
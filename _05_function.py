def open_account():
    print("새 계좌 오픈")

open_account()

def deposit(balance, money):
    print("입금 완료 잔액 = {0}".format(balance+money))
    return balance + money

balance = deposit(20000, 5000)
print(balance)

def withdraw(balance, money):
    if balance<money:
        print("잔액이 부족합니다")
        return balance
    else:
        print("출금 완료, 출금후 잔액 : {0}".format(balance-money))   
        return balance - money 
    
balance = withdraw(20000, 5000)
print(balance)    
balance = withdraw(2000, 5000)
print(balance)    

def withdraw_n(balance, money):
    com = 100 #수수료
    return com, balance - money - com
#두개의 값 리턴
com, balance = withdraw_n(balance,500)
print("수수료 {0}, 잔액은 {1}".format(com, balance))


def profile(name, age=17, lang="한국어"):
    print("이름 : {0} 나이:{1} 언어:{2}".format(name,age,lang))

profile("유재호",20,"일본어")    

#동일 값에 대한 디폴드값설정 ex같은 학생 나이
profile("손연경")
profile("김인경",20)
profile(name = "김연경", age = 20)
profile(name ="김지훈", lang ="프랑스어")
#위처럼 키워드 잡아다가 넣을수도 있음

# def profile(name, age, lang1, lang2, lang3):
#     print("이름 : {0} 나이:{1} ".format(name,age), end=" ") 
#     #end사용시 줄바꿈 없이 뒤에 이어서 출력
#     print(lang1, lang2, lang3)


def profile(name, age, *lang):
    print("이름 : {0} 나이:{1} ".format(name,age), end=" ") 
    for lang in lang:
        print(lang, end =" ")
    print()
#위처럼 다른 갯수의 매개변수를 표현 가능 for문 활용!
profile("유재호",20,"일본어","c","한국어","java")
profile("안준명", 25, "한국어", "영어")    


gun = 10

def checkpoint(sol):
    global gun #전역 공간에 있는 변수 사용
    gun = gun -sol
    print("함수 내 남은총: {0}".format(gun))

def checkpoint_ret(gun, sol):
    gun = gun - sol
    print("함수 내 남은 총 : {0}".format(gun))
    return gun
#파라메타를 받는 식으로 사용할 경우 반드시 리턴값으로 
#밖의 변수 값을 변경해서 운영 해야함


print("전체총 : {0}".format(gun))
checkpoint(4)
print("남은 총 : {0}".format(gun))

print("전체총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

from math import *
def std_weight(height, gender):
    if gender == "여자":
        print(round((height/100)*(height/100)*21, 2))
    else:
        print(round((height/100)*(height/100)*22, 2))

std_weight(175,"남자")
std_weight(155, "여자")
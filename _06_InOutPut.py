import sys

print("응애", "헤응", "호엥" ,sep = ", " ,end = "?")
#sep은 프린트 중간물에 문자열을 추가
#end는 출력 맨 마지막에 문자열 추가 + 줄바꿈 없애기


print("응애", "헤응", "호엥" ,file=sys.stdout) #표준출력
print("응애", "헤응", "호엥" ,file=sys.stderr) #표준에러

score = {"수학":0, "영어":50, "코딩": 100}
for sub, score in score.items(): #items로 키밸류 get
    #print (sub, score)
    print (sub.ljust(4), str(score).rjust(4), sep=" : ")
    #ljust(8) 8칸 확보후 왼쪽 정렬


for num in range(1,21):
    print("대기번호 : " + str(num).zfill(2))
    #zfill(3) 3의 크기 확보하고 비면 0으로 채우기


#answer = input("아무 값 입력 ㄱ : ") 
#인풋은 문자열로 입력받음

#빈자리는 빈공간으로 두고(: ), 오른쪽 정렬(>),10자리 공간 확보(10)
print("{0: >10}".format(500))

#양수일땐 +로 표시, 음수일땐-
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

#왼쪽 정렬, 빈간 _로 채우기
print("{0:_<10}".format(300))

#세자리마다 콤마찍기
print("{0:,}".format(10000000000))
print("{0:+,}".format(10000000000))

#응용 -순서 익히기!
print("{0:^<+30,}".format(100000000000000))

#소수점 출력
print("{0:f}".format(5/3))
print("{0:0.2f}".format(5/3)) #소수점 3째자리 반올림


# score_file = open("score.txt", "w", encoding="utf8")
# #(파일명, 쓰기(w -덮어쓰기),엔코디-언어)
# print("수학 : 0", file=score_file)
# print("영어 : 100", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# #a는 덧붙이기 append
# score_file.write("\n과학 : 0")
# score_file.write("\n코딩 : 100")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read()) #콘솔창 출력
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") #한줄 읽고 커서는 다음줄 이동
print(score_file.readline(),end="")
print(score_file.readline(),end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True: #무한 루프로 호출
    line = score_file.readline()
    if not line:
        break
    print(line,end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readline() #list형태 저장
for line in lines:
    print(line, end="")
score_file.close()

import pickle
# profile_file = open("profile.pickle", "wb")
# #바이너리 타입
# profile = {"이름":"유재호", "나이": 30, "취미":["게임, 운동"]}
# pickle.dump(profile, profile_file) #profile 정보를 file에 저장
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) #file정보를 변수에 넣기
print(profile)
profile_file.close()

#with 일일이 파일열닫 ㄴ
with open("profile.pickle", "br") as profile_file:
    print(pickle.load(profile_file))

#whit로 파일 저장
# with open("study.txt", "w", encoding = "utf8") as study_file:
#     study_file.write("파이썬 공부중 ㅅㅂ")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

for i in range(1,11):
    with open("{0}주차 보고서.txt".format(i), "w", encoding = "utf8") as rep_file:
        rep_file.write("{0}주차 보고서".format(i))
        rep_file.write("\n부서 : ")
        rep_file.write("\n이름 : ")
        rep_file.write("\n업무 요약 : ")

for i in range(1,11):
    with open("{0}주차 보고서.txt".format(i), "r", encoding = "utf8") as rep_file:
        print(rep_file.read())
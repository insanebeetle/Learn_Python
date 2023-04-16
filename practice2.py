jumin = "910417-1192214"

print(jumin[7])
print(jumin[0:2]) #년도 0~2직전까지
print(jumin[2:4])
print(jumin[7:]) #7번째 부터 끝까지

st = "Python is Amaizing"

print(st.lower())
print(st.upper())
print(st[0:2].lower())
print(st[0:2].isupper())
print(len(st))
print(st.replace("Python", "Java"))

index = st.index("n")
print(index)
index = st.index("n",index+1) #n을찾고나서 다음 자리의 n 찾기
print(st.find("Java")) 
#인덱스랑 같지만 해당없을 경우 -1 반환
#print(st.index("Java")) 
#그에 반해 인덱스는 해당값이 없을 경우 에러로 종료

print(st.count("n")) #해당 파라메타 몇개 있음?

print("나는 %d살입니다" % 20) #자바랑 비슷한 문법 %d는 정수
print("나는 %s살입니다" % "파이썬") #자바랑 비슷한 문법 %s는 문자열
print("나는 %c살입니다" % "A") #자바랑 비슷한 문법 %c는 문자 하나
#그런데 결국 문자열 값을 사용하기 때문에 연산이 없다면 그냥 %s를 쓰는게 편함
print("나는 %s살 %s띠입니다" % ("A", "헤응"))
print("나는 {} 색과 {} 색을 좋아합니다".format("파란","빨간"))
#위처럼 표현도 가능 {}의 경우 숫자를 부여해 순서를 조절 가능
print("나는 {1} 색과 {0} 색을 좋아합니다".format("파란","빨간")) #like this
print("나는 {age} 색과 {color} 색을 좋아합니다".format(age = "파란", color ="빨간"))
#리액트 프롭스마냥 사용도 가능 실제 변수널기

#탈출문자
# \n :줄바꿈  \", \': 따옴표 
#문장내에서  \를 사용할 경우  \\ 두번 쓰기
print("C:\\Users\\YU\\Desktop\\Pythonworkspace")

# \r : 앞으로 땡겨와서 덮어쓰기
print("red pepper\rHot")

# \b :백스페이스,지우기
print("redd\bapple")

# \t : 탭
print("redd\tapple")

nv = "http://naver.com"
print(nv[7:])
nv = nv[7:nv.find(".")]
print(nv)
print(nv[0:3] + str(len(nv)) + str(nv.count("e")) + "!")
print("-----------------------------")
nv = "http://naver.com"
nv = nv[7:nv.find(".")]
sr = nv[0:3]
leng = len(nv)
ecount = nv.count("e")
dkt = "!"
print(f"{sr}{leng}{ecount}{dkt}")
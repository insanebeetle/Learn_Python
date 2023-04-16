subway = [10, 20, 30]
print(subway.index(10))
subway.append(40) #배열 추가
print(subway)

subway = ["유재호", "김인경", "손연경"]
subway.insert(0, "정형돈") #배열 사이에 끼워넣기 (끼울순서, 끼워넣을 값)
print(subway)

print(subway.pop()) #맨 뒤의 요소 삭제
print(subway)

#같은 값 카운팅

subway.append("유재호")
print(subway.count("유재호"))

#정렬 동일 요소에 한해서만 가능 문자숫자열 섞인건 안됨
num = [5,4,2,3,1]
num.sort()
print(num)

#뒤집기
num.reverse()
print(num)

#전체 삭제
num.clear()
print(num)

#리스트 확장
num = [5,4,2,3,1]
num.extend(subway)
print(num)

print("-----------------------------")
#dict

cab = {3:"유재호", 100:"손연경"}
print(cab[3])
print(cab[100])
print(cab.get(3))
print(cab.get(100))
#print(cabinet[5])
#위의 코드로 호출할 경우 키값이 존재하지 않으면 에러종료
print(cab.get(5)) #none 출력
print(cab.get(5, "비어있음")) #뒤쪽 문자열이 none대신 출력

print(3 in cab) #불리언 문 있나 없나


cab = {"a-3":"유재호", "b-10" : "손연경"}
print(cab["a-3"])
cab["c-5"] = "김수정" #추가하기
cab["b-10"] = "김인경" #갈아 끼우기
print(cab)

del cab["b-10"] #항목 삭제
print(cab)

print(cab.keys()) #키값만 출력
print(cab.values()) #밸류값만 출력
print(cab.items()) #키, 밸류값 모두 출력

cab.clear() #모두 삭제
print(cab)



print("-----------------------------")
#튜플- 변경되지 않는 값(상수?) 값이 빠름
#주의!!!! 리스트[]랑 만드는 법 다름()
menu = ("돈까스", "치즈까스") #선언과 동시에 형태고정
print(menu[0])
print(menu[1])

#menu.add 사용 불가

name, age, hobby = ("유재호", 20, "야스")
print(name, age, hobby)
#위처럼 한번에 여러 항목을 생성할 수 있음 



print("-----------------------------")
#집합 (set) - 중복안됨, 순서 없음
ms = {1,2,3,4,4}
print(ms) #중복이 안되므로 자동으로 4 컷함

#교집합 만들기
java = {"유재호", "김인경", "손연경"}
python = set(["유재호", "유민하"])
print(java & python)
print(java.intersection(python))

#합집합
#print(java 짝대기  python)
print(java.union(python)) #순서 없으므로 랜덤으로 순서정해짐

#차집합
print(java - python)
print(java.difference(python))

#추가 / 제거
python.add("하야마")
print(python)
python.remove("유민하")
print(python)

print(python, type(python))
python = list(python)
print(python, type(python))
python = tuple(python)
print(python, type(python))
python = set(python)
print(python, type(python))


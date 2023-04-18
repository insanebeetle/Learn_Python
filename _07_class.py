# name = "marin"
# hp = 40
# damage = 5

# print("{}유닛이 생성 됨".format(name))
# print("체력 {0}, 공격력{1}".format(hp, damage))

# tank_name= "tank"
# tank_hp = 150
# tank_damage =35

# print("{}유닛이 생성 됨".format(tank_name))
# print("체력 {0}, 공격력{1}".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0}:{1} 방향으로 공격. 공격력 {2}".format(name,location,damage))

# attack(tank_name,"1시",tank_damage)

class Unit:
    def __init__(self,name,hp,speed):
        # __init__은 생성자 
        # 생성자 패러메터에서 self 넣어야됨!(this스스로 만들지 못해서.. ㄹㅇㅄ언어)
        self.name= name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("지상유닛 이동")
        print("{0}:{1}방향 이동. 속도:{2}".format(self.name, location, self.speed))
        
        # self.damage = damage
        # print("{0}유닛이 생성".format(self.name))
        # print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

# marine1 = Unit("마린",40,5)
# marine2 = Unit("마린",40,5)        
# tank = Unit("탱크",40,5)
# wraith =Unit("레이스",80,5)
# print("유닛이름 : {0} 공격력: {1}".format(wraith.name,wraith.damage) )

# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True
# #외부에서 변수를 추가 할당 가능 - 레이스2 있으나 1는 없음

# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹".format(wraith2.name))

class Attackunit(Unit): #상속
    def __init__(self,name,hp,speed,damage): 
        Unit.__init__(self,name,hp,speed) #생성자 상속
        self.damage = damage

    def attack(self, location):
        print("{0} : {1}방향으로 공격. 공격력:{2}".format(self.name,location,self.damage))

    def damaged(self, damage):
        print("{0}:{1}데미지를 입었습니다".format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴됨".format(self.name))

# firebat1 =Attackunit("firebat",50,16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)             

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self,name,location):
        print("{0}:{1}시 날아감. 속도{2}".format(name, location, self.flying_speed))    

# 공중 공격
class FlyableAttackUnit(Attackunit, Flyable):
    def __init__(self,name,hp,damage, flying_speed):
        Attackunit.__init__(self,name,hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
            print("공중유닛 이동")
            self.fly(self.name, location)
        
# valkyrie = FlyableAttackUnit("발키리",200,6,5)
# valkyrie.fly(valkyrie.name, 5)        

#메소드 오버라이딩
vulture = Attackunit("벌쳐", 80, 10, 20)

battle = FlyableAttackUnit("배틀",500,25,3)

vulture.move("11시") 
battle.move(9)
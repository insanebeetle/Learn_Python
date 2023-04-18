from random import *

class Unit:
    def __init__(self,name,hp,speed):
        self.name= name
        self.hp = hp
        self.speed = speed
        print("{0}유닛이 생성됨".format(name))
    def move(self, location):
        print("지상유닛 이동")
        print("{0}:{1}방향 이동. 속도:{2}".format(self.name, location, self.speed))
    def damaged(self, damage):
        print("{0}:{1}데미지를 입었습니다".format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴됨".format(self.name))    


class Attackunit(Unit):
    def __init__(self,name,hp,speed,damage): 
        Unit.__init__(self,name,hp,speed) 
        self.damage = damage

    def attack(self, location):
        print("{0} : {1}방향으로 공격. 공격력:{2}".format(self.name,location,self.damage))

class Marine(Attackunit):
    def __init__(self):
        Attackunit.__init__(self, "마린", 40, 1, 5)
    def steampack(self):
        print("공격속도 업")
        if self.hp >10:
            self.hp -= 10
            print("{0} 스팀팩사용 ".format(self.name))
        else:
            print("{0}체력이 부족".format(self.name))    

class Tank(Attackunit):
    sieze_developed = False
    def __init__(self):
      Attackunit.__init__(self, "탱크", 150, 1, 35)
      self.seize_mode =False

    def set_sieze(self):
        if Tank.sieze_developed == False:
            return
        if self.seize_mode == False:
            print("{0}:시즈모드 전환".format(self.name))
            self.damage *= 2
            self.seize_mode =True
        else:
            print("{0}시즈모드 해제".format(self.name))
            self.damage /= 2
            self.seize_mode = False    
            

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

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == False:
            print("{0}: 클로킹 모드".format(self.name))
            self.clocked = True
        else:
            print("{0}:클로킹 모드 해제".format(self.name))
            self.clocked = False      
        
def game_start():
    print("새로운 게임 시작")

def game_over():
    print("gg")   

game_start()
m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_unit = []
attack_unit.append(m1)
attack_unit.append(m2)
attack_unit.append(m3)
attack_unit.append(t1)
attack_unit.append(t2)
attack_unit.append(w1)

for unit in attack_unit:
    unit.move("1시")

Tank.sieze_developed =True
print("탱크 시즈모드 개발 완료")

for unit in attack_unit:
    if isinstance(unit, Marine):
        unit.steampack()
    elif isinstance(unit, Tank):
        unit.set_sieze()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_unit:
    unit.attack("1시")        

for unit in attack_unit:
    unit.damaged(randint(5,41)) #공격 랜덤맞기

game_over()    
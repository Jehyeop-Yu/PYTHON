# 메소드 오버라이딩

# 일반 유닛
class Unit: # 부모클레스(상속을 해줌)
    def __init__(self, name, hp, speed): # init 사용시 self 빼고 뒤의 정의된 개수 중요
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit): # 자식 클래스(상속을 받음)
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}이 파괴 되었습니다.".format(self.name))
            
# 날 수 있는 기능을 가진 클래스
class Flyable: 
    def __init__(self, flying_speed):
       self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed = 0
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("[공중 유닛]")
        self.fly(self.name, location)

# 벌쳐 : 지상유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루져 : 공주 유닛, 체력 좋고, 공격력 좋다
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# 활용전
vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")

# 활용후
vulture.move("11시")
battlecruiser.move("9시")

# #pass (아무것도 안하고 그냥 넘어간다.)
# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass 

# # 서플라이 디폿 :  건물, 1개 건물 = 8 유닛.
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# # pass 예시
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()

#super

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # 윗줄 동작과 같은 역할이나 표기가 다르다.
        self.location = location
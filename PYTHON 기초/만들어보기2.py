class Person:
    def __init__(self, name):
        self.name = name
    def say_hello(self, to_name):
        print("안녕" + to_name + "나는" +self.name)


wonie = Person("워니")
michael = Person("마이클")
jenny = Person("제니")

wonie.say_hello("철수")
michael.say_hello("영희")
jenny.say_hello("미지")

from random import*
off = randint(4,28)
on = randint(4,28), randint(4,28),  randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 "+ str(off) +"일로 선정되었습니다.")
print("온라인 스터디 모임 날짜는 매월 "+ str(on) +"일로 선정되었습니다.")
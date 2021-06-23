## cls 터미널 정리

# # 패키지 : 모듈들을 모아놓은 집합 
# # ex) 여행사 패키지 
# import travel.thailand # import 에는 class 네임을 사용 할 수 없다. 
# trip_to = travel.thailand.ThailandPackage() # travel안에 thailand안에 ThailandPackage (. = 안의 모듈 가져오기)
# trip_to.detail()

# from travel.thailand import ThailandPackage # from 뒤의 import의 경우는 class 네임을 사용 할 수 있다.
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# # [오류]  __init__ 파일에 명시해줘야한다.
from travel import *
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# 패키지 위치 찾기
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))
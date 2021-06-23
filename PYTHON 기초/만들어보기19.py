# # 모듈 : 코드를 부품 및 부분만 수정가능

# # 방법1
# # 불러오기
# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 떄

# # 방법2
# # 별명으로 이름 줄이기 (as 다음 별명 만들기)
# import theater_module as mv 
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# # 방법3
# # 'theater_module' 필요없이 안의 모듈 사용하기
# from theater_module import* 
# # from random import* 과 같은 방식 
# price(3)
# price_morning(4)
# price_soldier(5)

# # 방법4
# # 필요한 모듈만 가져오기(없는 모듈 사용시 오류 ex) price_soldier는 없으므로 사용 불가 )
# from theater_module import price, price_morning
# price(5)
# price_morning(6)

# # 방법5
# # theater_module의 price_soldier를 가져다 쓰지만 price로 바꿔서 사용
# from theater_module import price_soldier as price
# price(5) # 기존의 price값이 아닌 별명을 지정해준 price_soldier의 값
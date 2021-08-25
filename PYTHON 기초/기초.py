# 명령 프롬프트 실행 
python 
pwd (print working directory) : 내 위치 경로 표시
ls (list segments) : 폴더 안에 폴더와 파일 목록 보여주기
cd (change directory) : 폴더 이동 사용법 : cd '이동할 폴더 이름'
cd .. : 상위 폴더로 이동
cp (copy) : 파일 복사  사용법 : cp '복사할 파일 이름' '붙여넣을 파일 이름'
rm (remove) : 파일 삭제 사용법 : 
파일 이름 입력 EASY : 파일이름 처음 두글자만 쓰고 TAP 누르기 그럼 자동 완성 ex) 파일이름: apple -> 입력: ap -> tap -> apple(자동완성)

random.choice(list) : 리스트 안에서 랜덤으로 하나만 골라 출력

url모듈 사용법
def get_web(url):
    "URL을 넣으면 페이지 내용을 올려주는 함수"
    import urllib.request
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('urf-8')
    return decoded

url = input('웹 페이지 주소?')
content = get_web(url)
print(content)

모듈 불러오기
import '파일이름' # 같은 폴더 안에 있어야 동작한다. 

검색하기 (공식문서)
google : < python3 "검색 이름" generation site: python.org >

------------------------------------------------
리스트 []
딕셔너리 {}
튜플 ()

리스트 추가
list.append(a) # a를 리스트에 추가

리스트 빼기 
list = [1, 2, 3, 4, 5]
del list[0]
list.remove(1)

딕셔너리 
ages = {'Tod':35, 'Jane':23, ...} # {key : value}

결합 
리스트 : list1 + list2 or list1.update(lise2)
딕셔너리 : dit1.update(dit2)
------------------------------------------------
튜플 : 값을 한번 넣으면 변경 및 삭제 할 수가 없다.

a,b = 1,2 이것도 튜플 (이것도 튜플 )
c = (3,4)

unpacking (튜플)
d,e = c
-> d = 3
-> c = 4 

packing (튜플)
f = d,e 
-> f = (3,4)


두 튜플 값 바꾸기
x = 5
y = 10

1) temp라는 변수에 임의로 저장
temp = x 
x = y
y = temp 
2) 두개 자리 바꾸기
x,y = y,x

def tuple_func():
    return 1,2
q,w = tuple_func()
-> q = 1
-> w = 2

튜플을 이용한 함수의 리턴값
 1) 리스트 (아래 동작 모두 다 같은 동작이다.)
    list = [1,2,3,4,5]
    for i,v in enumerate(list):
        print('{}번재 값: {}'.format(i,v))

    list = [1,2,3,4,5]
    for a in enumerate(list):
        print('{}번재 값: {}'.format(a[0], a[1]))

    list = [1,2,3,4,5]
    for a in enumerate(list):
        print('{}번재 값: {}'.format(*a)) -> *a 값을 나눠준다.

 2) 딕셔너리 (아래 동작 모두 다 같은 동작이다.)
    ages = {'Tod':35, 'Jane':23, 'Paul': 32}
    for kdy,val in ages.items():
        pritn('{}의 나이는: {}'.format(key, val))

    ages = {'Tod':35, 'Jane':23, 'Paul': 32}
    for a in ages.items():
        pritn('{}의 나이는: {}'.format(a[0], a[1]))

    ages = {'Tod':35, 'Jane':23, 'Paul': 32}
    for a in ages.items():
        pritn('{}의 나이는: {}'.format(*a))
------------------------------------------------
예외 처리 (try , except) -> (몇개 이외엔 if, else 로 처리가능)
try:
    에러가 발생할 가능성이 있는 코드
except 에러종류:
    에러가 발생 했을 경우 처리할 코드

1) ValueError
    text = '100%'
    try:
        number = int(text)
    except ValueError:
        print('{}는 숫자가 아니네요.'.format(text))

2) IndexError
    def safe_pop_print(list, index):
        try:
            print(list.pop(index))
        except IndexError:
            print('{} index의 값을 가져올 수 없습니다.'.format(index))
    safe_pop_print([1, 2, 3], 5)

2-1) 위와 같은 동작 
    def safe_pop_print(list, index):
        if(index < len(list)):
            print(list.pop(index))
        else:
            print('{} index의 값을 가져올 수 없습니다.'.format(index))
    safe_pop_print([1, 2, 3], 5)

3) try,except 구문 이어만 하는 코드
    try:
        import my_module
    except ImportError:
        print("모듈이 없습니다.")

4) 예외 이름을 모르는 경우 처리 방법
    try:
        # 에러가 발생할 가능성이 있는 코드
    except Exception as ex: # 에러 종류
        print('에러가 발생 했습니다', ex) # ex는 발생한 에러의 이름을 받아오는 변수

5) 예외 발생 
    def rsp(mine,yours):
        allowed = ['가위', '바위', '보']
        if mine not in allowed:
            raise ValueError
        if yours not in ValueError

    try:
        rsp('가위', '바')
    except ValueError:
        print('잘못된 값을 넣은것 같습니다.')

5-1) 모든 코드를 종료하고 싶을때 사용하기도함 
('try,except' 구문에 넣어주면 에러창이 깔끔하게 나온다, 너무 많이 사용하면 코드를 읽기 어렵게 만들기도 한다.)
    school = {'1반':[172, 185, 198, 177], '2반':[165, 154, 190, 168]}
    try:
        for class_number, students in school.items():
            for student in students:
                if student > 190:
                    print(class_number,'반에 190을 넘는 학생이 있습니다.')
                    raise StopIteration
    except StopIteration:
        print('정상종료')
------------------------------------------------
bool 사용법 
1) 1 or 2 일 경우 1 이 true 일경우 1 만 실행 false 일경우 2 를 실행 
    value = input('입력해 주세요>') or '아무것도 못받았어요'
    print('입력받은값>', value) 
------------------------------------------------
1) list 추가 기능
    list.index( value ) : 값을 이용하여 위치를 찾는 기능
    list.extend( [value1, value2] ) : 리스트 뒤에 값을 추가
    list.insert( index, value ) : 원하는 위치에 값을 추가 (index 위치에 값을 추가 )
    list.sort( ) : 값을 순서대로 정렬
    list.reverse( ) : 값을 역순으로 정렬

2) split
    str = "오늘은 날씨가 맑음"
    list = str.split('') : ' '(공백)을(를) 기준으로  문자열에서 리스트로 나눈다 (ex ['오늘은','날씨가','맑음'])
    " ".join( list ) : : " "을 기준으로 리스트에서 문자열으로

3) Slice : 리스트나 문자열에서 값을 여러개 가져오는 기능
    text = "hello world"
    text = text[ 1:5 ]
    list = [ 0, 1, 2, 3, 4, 5 ]
    list = list[ 1:3 ]

    3-1) 시작과 끝부분을 얻어 오는 방법
        list[ 2: ] : 2번째부터 끝까지 반환
        list[ : 2 ] : 처음부터 2번째 까지 반환
        list[ : ] : 처음부터 끝까지 전부 반환

    3-2) step
        slice한 값의 범위에서 step 값을 주어 그 값만큼 건너뛰어 가져오는 기능
        list[ 시작값 : 끝값 : step ] -> step : 건너 뛰는 값 지정

    3-3) slice 활용 (리스트 수정)
    삭제
        del list[ :5 ] : 처음부터 5번째까지 삭제
    수정
        list[ 1:3 ] = [ 77, 88 ]
        list[ 1:3 ] = [ 77, 88 ,99 ] : 더 많은 개수로 변환
        list[ 1:4 ] = [ 8 ] : 더 적은 개수로 변환
------------------------------------------------
자료형
    type( a ) # type( 변수명 ) : 자료형
    isinstance( 42, int ) # isinstance( 값, 자료형 ) : 자료형 검사
    isinstance( a, b ) # a의 값이 b형태인지 검사
------------------------------------------------
class 

1) 같은 class인지 확인 
    list1 = list(range(10))
    list2 = [1, 2, 3]

    if isinstance( 
    list1
    , list) and isinstance( 
    list2
    , list):
        print("list1과 list2는 둘 다 list클래스 입니다.")

2) class 선언
    class Human( ):
    '''사람'''

    인스턴스 생성
    person1 = Human( )
    person2 = Human( )

3) 메소드(Method)
    class Human( ):
        '''인간'''
        def create( name, weight ): # 다음 강의에서 자세히 설명
            person = Human()
            person.name = name
            person.weight = weight
            return person

        def eat( self ):
            self.weight += 0.1
            print("{}가 먹어서 {}kg이 되었습니다".format(self.name, self.weight))

        def walk( self ):
            self.weight -= 0.1
            print("{}가 걸어서 {}kg이 되었습니다".format(self.name, self.weight))

    person = Human.create("철수", 60.5)
    person.eat()

4) 특수한 메소드 
    class Human( ):
        '''인간'''
        def __init__( self, name, weight ): #-> __init__ : 인스턴스를 만들 때 실행되는 함수
            '''초기화 함수'''
            self.name = name
            self.weight = weight

        def __str__( self ): #-> __str__ : 인스턴스 자체를 출력 할 때의 형식을 지정해주는 함수
            '''문자열화 함수'''
            return "{} ( 몸무게 {}kg )".format( self.name, self.weight )

    person = Human( "사람", 60.5 ) # 초기화 함수 사용
    print( person ) # 문자열화 함수 사용

5) 상속
    - 상속하는 클래스를 부모 클래스
    - 상속받는 클래스를 자식 클래스
    - 자식 클래스가 부모 클래스의 내용을 가져다 쓸 수 있는 것
    class Animal( ):
        def walk( self ):
            print( "걷는다" )

        def eat( self ):
            print( "먹는다" )

    class Human( Animal ):
        def wave( self ):
            print( "손을 흔든다" )

    class Dog( Animal ):
        def wag( self ):
            print( "꼬리를 흔든다" )

6) 오버라이드
    - 같은 이름을 가진 메소드를 덮어 쓴다는 의미
    class Animal( ):
        def greet( self ):
            print( "인사한다" )

    class Human( Animal ):
        def greet( self ):
            print( "손을 흔든다" )

    class Dog( Animal ):
        def greet( self ):
            print( "꼬리를 흔든다" )

7) super()
    - 자식클래스에서 부모클래스의 내용을 사용하고 싶은 경우
    - super().부모클래스내용
    class Animal( ):
        def __init__( self, name ):
            self.name = name

    class Human( Animal ):
        def __init__( self, name, hand ):
            super().__init__( name ) # 부모클래스의 __init__ 메소드 호출
            self.hand = hand

    person = Human( "사람", "오른손" )

8) 직접 예외 만들기
    파일1 
    class BadUserName(Exception):
        '''이름 불량 동작'''
    class PasswordNotMatched(Exception):
        '''이름 불량 동작'''

    파일2  -> 파일1에서 만든 예외 동작을 불러온다
    try:
        sign_up( )
    except BadUserName:
        print( "이름으로 사용할 수 없는 입력" )
    except PasswordNotMatched:
        print( "입력한 패스워드 불일치")
------------------------------------------------
Comprehension
    List
        예1 = [ i*i for i in range(1,11) ] # [ 계산식 for문 ]
        예2 = [ i*i for i in range(1,11) if i % 2 == 0 ] # [ 계산식 for문 조건문 ]
        예3 = [ ( x, y ) for x in range(15) for y in range(15) ] # [ 계산식 for문 for문 ]

    Dictionary
        scores = [85, 92, 78, 90, 100]
        students_dict = { "{}번".format(number):name for number, name in enumerate(students) } # [ 형식 for문 ]
        score_dict = {student:score for student, score in zip(students, scores)}
------------------------------------------------
datetime 
    import datetime
    christmas_2016 = datetime.datetime(2016, 12, 25)
    print(christmas_2016)

1)hundred_after가 지금으로부터 100일 후, 9시 정각을 값으로 가지는 datetime클래스의 인스턴스가 되도록 만들어 보세요. (단, 정각의 기준은 초 단위까지만 맞으면 됩니다.)
    import datetime
    hundred_after = datetime.datetime.now().replace(hour = 9, minute = 0, second = 0) + datetime.timedelta(days = 100)
    print("{}/{}/{}  {}:{}:{}".format(hundred_after.year,hundred_after.month, hundred_after.day, hundred_after.hour, hundred_after.minute, hundred_after.second))
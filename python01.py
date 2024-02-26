
#tpye 함수 -> 정수,실수,문자열 인지 알려주는 함수
'''
print((type('3.14')))
'''

#변수 주소값 출력 ( id )
'''
아이스크림 = 1000
print('주소값 :', id(아이스크림))
'''

#리스트 수정가능
'''
a = [1,2,3]
#a.remove(2)
#a.append(2)
#print(a[0],a[1],a[2])#인덱싱
print(a[0:2])#슬라이싱 0부터 2-1번까지 [:]
'''

#튜플 수정불가능
'''
b = (1,2,3)
print('튜플',b)
'''

#딕셔너리
'''
c = {'사과':2000, '배':3000}
print(c)
'''

#반복문 for, while
'''
카트 =['과자','음료수','과일']
for i in 카트:
    print(i)

num=0
while num<5:
    print(num)
    num+=1
'''

#함수
'''
def sum(a,b,c):
    sum = a+b+c
    return sum
sum = sum(100,200,300)
print(sum)

num = 10
def foo():
    #함수 내부의 num이랑 바깥의 num이랑은 전혀 다르다
    #global 변수이름 을 선언해 주면 전역변수를 함수 내에서 사용 가능 global num
    num=20
    print(num)

foo()
print(num)
'''

#LEGB 규칙 (변수 참소 순서)
#Local 지역 변수(함수 내부)
#Enclosing 내부함수에서 자신의 외부 함수의 범위
#Global 함수 바깥쪽 의미
#Built-in open, range같은 파이썬 내장 함수를 의미

'''
a=10
def test():
    global a #이런 스타일의 참조는 되도록 하지않는게 좋음
    a=20

test()
print(a)
'''

#모듈 = 라이브러리 생성 및 사용
#mymod.(변수or함수)

'''
import mymod
print(mymod.hap(20, mymod.var))
'''

'''
모듈 호출 방식 4가지
1. improt mymod -> mymod.hap(3,4) 이런 식으로 사용 [서로 다른 모듈안에 동일한 이름을 가진 함수가 존재할 때 구분하기 편함 --권장--]
2. form mymod import hap -> mymod 모듈 내의 hap 함수만 사용
3. from mymod import* -> mymod 모듈 내의 모든 변수,함수 이름을 사용
4. import mymod as mm -> mymod가 길다 mm.hap(3,4)로 사용 가능
'''

#모듈과 패키기
'''
모듈 -> .py파일
패키지 -> multimedia패키지, 디렉토리에 여러 파이썬 모듈이 있는 구조 ex) __init__/py , video.py , audio.py이렇게 구성
모듈과 패키지를 크게 막 구분하지 않음
'''

#multimedia 패키지 생성 및 사용

#1번 방법으로 호출
'''
import multimedia.audio
import multimedia.video

multimedia.audio.play_audio()
multimedia.video.play_video()
'''

#2번 방법으로 호출
'''
from multimedia.audio import play_audio
from multimedia.video import play_video

play_audio()
play_video()
'''

#3번 방법으로 호출
'''
from multimedia.video import *
from multimedia.audio import *

play_audio()
play_video()
'''

#4번 방법으로 호출
'''
import multimedia.audio as ma
import multimedia.video as mv

ma.play_audio()
mv.play_video()
'''

#클래스는 왜 사용할까?

#클래스 생성 및 객체 생성
'''
class 붕어빵틀:
    pass

내빵 = 붕어빵틀()
너빵 = 붕어빵틀()

내빵.앙꼬 ='딸기맛'  #내빵 -> {"앙꼬(key)":"딸기맛(value)"} 딕셔너리 형식으로 저장
너빵.앙꼬 ='초코맛'  #너빵 -> {"앙꼬(key)":"초코맛(value)"} 딕셔너리 형식으로 저장

print(내빵.앙꼬)
print(너빵.앙꼬)
'''

#클래스와 메서드
'''
class 붕어빵틀:
    def 앙꼬넣기(어떤빵,앙꼬맛):
        어떤빵.앙꼬 = 앙꼬맛

내빵 = 붕어빵틀()
너빵 = 붕어빵틀()
붕어빵틀.앙꼬넣기(내빵,'딸기맛')
붕어빵틀.앙꼬넣기(너빵,'초코맛')
print(내빵.앙꼬)
print(너빵.앙꼬)
'''

#class 에서의 self
'''
class 계좌:
    def 개설(self,넣을이름,넣을금액):
        self.이름 = 넣을이름
        self.잔고 = 넣을금액

계좌1 = 계좌()
계좌2 = 계좌()

계좌.개설(계좌1,'김섭섭',10000)
계좌.개설(계좌2,'김십섭',20000)
print(계좌1.잔고)
print(계좌2.이름)
'''

#메서드 호출 방식
'''
class 계좌:
    def 개설(self,넣을이름,넣을금액):
        self.이름 = 넣을이름
        self.잔고 = 넣을금액

계좌1 = 계좌()
계좌2 = 계좌()
계좌3 = 계좌()
계좌4 = 계좌()

#           a=[1,2,3]
#방식 1 ex) list.append(a,4)
계좌.개설(계좌1,'김섭섭',10000)
계좌.개설(계좌2,'김십섭',20000)

#방식 2 ex) a.append(4)
계좌3.개설('이호섭',30000)
계좌4.개설('이호호섭',60000)

print(계좌1.이름, 계좌1.잔고)
print(계좌2.이름, 계좌2.잔고)
print(계좌3.이름, 계좌3.잔고)
print(계좌4.이름, 계좌4.잔고)
'''

#클래스 생성자 __init__
'''
클래스로부터 객체가 생성될 때 파이썬 인터프리터에 의해 자동으로 호출되는 특별한 메서드
-프로그래머가 호출 x 인터프리터에 의해 호출됨
-메모리에 생성된 객체 공간에 데이터를 넣거나 초기화
-__init__이라는 특별한 이름을 가짐
-첫 인자 self
'''

'''
class 붕어빵틀:
    def __init__ (self,앙꼬맛):
        self.앙꼬 = 앙꼬맛


내빵 = 붕어빵틀('초코맛')
너빵 = 붕어빵틀('딸기맛')

print(내빵.앙꼬)
print(너빵.앙꼬)
'''

'''
class 계좌:
    def __init__ (self,이름,금액):
        self.이름 = 이름
        self.금액 = 금액

국민은행 = 계좌('일호섭',100000)
농협은행 = 계좌('이호섭',200000)

print(국민은행.이름,국민은행.금액)
print(농협은행.이름,농협은행.금액)
'''
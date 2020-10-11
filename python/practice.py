
'''
# 변수
animal = "강아지"
name = "해피"
age = 4
is_adult = age>=3

print("우리집" + animal + "은" + str(age) + "살" + name)
print("우리집", animal, "은" ,age ,"살", name)
name = "쿠키"
print("우리집", animal, "은" ,age, "살", name)

print("==========")
print(name,"는 어른일까요?", str(is_adult))

station = "사당"
print(station + "행 열차가 들어오고 있습니다")
station = "신도림"
print(station,"행 열차가 들어오고 있습니다")
station = "인천"
print(station,"행 열차가 들어오고 있습니다")

print(abs(-5)) #절대값
print(pow(4,2)) #4^2 (4의 2승) = 16
print(max(5,10)) #최대값
print(min(5,10)) #최소값
print(round(3.1)) #반올림
print(round(3.9)) #반올림

from math import *
print(floor(4.99)) #내림
print(ceil(3.14)) #올림
print(sqrt(16)) #제곱근
'''

'''
from random import *

print(random()) # 0.0 ~ 1.0미만의 값
print(random() * 10) # 0.0 ~ 10.0미만의 값
print(int(random() * 10)) # 0 ~ 10미만의 값
print(int(random() * 10)+1) # 1 ~ 10이하의 값

print(int(random() * 45 + 1)) # 1 ~ 45이하 (로또값)
print(randrange(1, 46)) #1 ~ 46미만의 값
print(randint(1,45))#양끝을 포함, 1이상 45이하

#연산자 퀴즈
from random import *
date = randint(4,28)
print('오프라인 스터디 모임 날짜는 매월 ' + str(date) + '일로 선정되었습니다.')

#문자열
sentence = '나는 부자다'
print(sentence)
sentence2 = '나는 거지다'
print(sentence2)
sentence3 = """
파이썬공부
매니션
"""
print(sentence3)
'''
'''
#슬라이싱
jumin = "900122-1234567"
print("성별 : "+ jumin[7]) #7번째 문자
print("연 : " + jumin[0:2]) #0부터 2 직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])#처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:])#7번쨰부터 끝까지
print("뒤 7자리(뒤에서부터) : " + jumin[-7:])  # 뒤에서 7번쨰 ~ 맨뒤까지
'''
'''
#문자열처리함수
python = "Python is Amazing"
print(python.lower()) #모두 소문자
print(python.upper()) #모두 대문자
print(python[0].isupper()) #첫번째(0번째)글자가 대문자인지, 참거짓
print(len(python)) # 글자수
print(python.replace("Python","Java")) #Python 글자를 Java로 바꿔서 출력

index = python.index("n") 
print(index) #n이 몇번째 있는지 출력(첫번째 문자만)
index = python.index("n",index+1)
print(index) # 2번째 n의 위치
print(python.find("python")) #문장에서 글자찾기(대소문자 구별)

print(python.find("Java")) #문장에 Java라는 문자 찾기
print(python.index("Java")) #문장에 Java라는 문자 찾기

# find = 다음 문장 있으면 그대로 실행
# index = 다음 문장 있어도 실행 안하고 종료

print(python.count("n")) #python문장에서 n의 갯수
'''

'''
#문자열포맷

#방법1
print("나는 %d살입니다." %20) # d=정수
print("나는 %s을 좋아해요." %"파이썬") # s = 문자열(스트링)
print("Apple은 %c로 시작해요." %"A") #c = 문자(1글자)
print("나는 %s색과 %s색을 좋아해요" %("파란","빨간")) #2개이상

#방법2
print("나는 {}살 입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요" .format("파란","빨간"))

#방법3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간"))

#방법4 (파이썬버전 3.6이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")
'''

'''
#탈출문자
print("백문이 불여일견 \n백견이 물여일타") #\n : 출력시 줄바꿈
print("저는 \"매니\"입니다") # \ : \뒤에 ""를 쓰면 그대로 출력
print("C:Users\\file") #\\ : 문장 내에서 \
print("red Apple\rPine") # \r : 커서를 맨 앞으로 이동 (뒤에 글자만큼 앞글자 삭제)
print("Redd\bApple") # \b : 백스페이스(1글자 삭제) 띄어쓰기도 인식
print("Red\tApple") # \t : Tab키와 동일한 기등(넓게 띄어쓰기)
'''

#퀴즈3
'''
Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오
예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자중 처음 세자리(nav) + 글자 갯수(5) + 글자 내 'e'갯수(1) + "!"로 구성(!)
= 생성된 비밀번호 : nav51!
'''

'''
#site = "http://naver.com"
site = "http://goole.com"
cut = site[7:-4]
pw = cut[:3] + str(len(cut)) + str(site.count("e")) + "!"
print(pw)
# ※문자, 정수부분 str로 감싸기

#풀이
my_str = site.replace("http://","") #규칙1
my_str = my_str[:my_str.index(".")] #규칙2
print(my_str)
pw = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(pw)
'''

'''
#리스트 [] : 순서를 가지는 객체의 집합 
test = ["테스트1","테스트2","테스트3"]
print(test)

#리스트 목록에 맨 뒤에 추가 append
test.append("테스트04")
print(test)

#목록 중간에 넣기
test.insert(2,"테스트2.5")
print(test)

#맨 뒤 목록 삭제
print(test.pop()) #삭제된 항목
print(test) #삭제된 후
 
#같은 이름의 항목 갯수 확인
test.append("테스트2")
print(test)
print(test.count("테스트2"))

#정렬
num_list = [5,2,4,3,1]
num_list.sort() #오름차순으로 정렬
print(num_list)

num_list.reverse() #리버스. 반대로 정렬
print(num_list)

num_list.clear() # 내부 항목 전체삭제
print(num_list)

#다양한 자료형 함께 사용 가능 (문자열, 숫자, 불린)

num_list = [5,4,3,2,1]
mix_list = ["테스트",22.2,True]
print(mix_list)

#리스트 확장
num_list.extend(mix_list)
print(num_list)
'''

'''
#사전
cabinet = {3:"화사", 1:"헨리"}
print(cabinet[3])
print(cabinet[1])
print(cabinet.get(3))
print(cabinet.get(5)) #없는 값 = None
#print(cabinet[5]) #오류나면 종료
print(cabinet.get(5,"사용 가능")) #없는 값의 기본값 설정
print(3 in cabinet) #참,거짓(숫자 in 변수)


#새 손님
cabinet = {"a-3":"화사", "b-1":"헨리"}
print(cabinet["a-3"])
print(cabinet["b-1"])

#새 손님
print(cabinet)
cabinet["a-3"] = "한혜진"
cabinet["c-20"] = "박나래"
print(cabinet)

#간 손님(삭제)
del cabinet["a-3"]
print(cabinet)

#key만 출력
print(cabinet.keys())

#value만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

#영업종료
cabinet.clear()
print(cabinet)
'''
'''
#튜플 (내용변경,추가 불가 - 리스트보다 빠름)
menu = ("돈까스", "치즈까스")
print(menu[0])
'''
'''
#집함(set) 중복안됨, 순서 없음
my_set = {1,3,3,3,2} #{1,2,3} 출력
print(my_set)
coffee = {"아메리카노","카페라떼","바닐라라떼"}
tea = set(["허브티","레몬티"])

#교집합
print(coffee & tea)
print(coffee.intersection(tea))

#합집합
print(coffee | tea)
print(coffee.union(tea))

#차집합
print(coffee - tea)
print(coffee.difference(tea))

#추가
tea.add("루이보스")
print(tea)

#제거
coffee.remove("아메리카노")
print(coffee)
'''

'''
#자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu,type(menu)) #class 'set(현재 자료 형태){}

menu = list(menu)
print(menu,type(menu)) #class 'list(현재 자료 형태)[]

menu = tuple(menu)
print(menu,type(menu)) #class 'tuple(현재 자료 형태)()

menu = set(menu)
print(menu,type(menu)) #class 'set(현재 자료 형태)
'''

'''
Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.

조건1 : 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
조건2 : 무작위 추첨, 중복불가
조건3 : rendom 모듈과 shuffle 과 sample을 활용

출력예제
-- 당첨자 발표 --
치킨당첨자 : 1
커피당첨자 : [2,3,4]
-- 축하합니다 --
'''
#활용 예제
# from random import *
# lst = [1,2,3,4,5]
# shuffle(lst) #리스트 안의 항목 순서를 무작위로 바꿈
# print(lst)
# print(sample(lst,1)) # 변주중 n개를 무작위로 뽑음


from random import * 
users = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(users)
print(users)
# print("-- 당첨자 발표 --" + "치킨당첨자 : " + str(sample(users,1)) +"커피당첨자 : " + str(member,3) +"-- 축하합니다 --")

#풀이
user = range(1,21) 
user = list(user)
shuffle(user)
winner = sample(user,4)
print("--당첨자 발표--")
print("치킨 당첨자 : {0}".format(winner[0]))
print("커피 당첨자 : {0}".format(winner[1:]))
print("--축하합니다--")

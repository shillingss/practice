from ast import Num
from operator import index
from symbol import parameters
from time import time


print(1+1)# 실수형 문자형 같은 경우는 엔트리 같은 경우에서 배워서 잘 암 
# 실수형 같은 경우는 1+1 할때 2가 나오지만 문자형은 11이 나옴



#변수 공부

print("이 집은 황가온의 집이다")
print("그래서 황가온의 집을 들어오지 말것")

# 이집 이름이 바뀌면 글 전체를 바꿔줘야함 실수가 나올수 있음 = 변수로 쉽게 바꾸기

name = "황가온"

year = "16"

print("이 집은 "+str(year)+"살 " + name + "의 집이다")
print("그래서 "+name+"의 집을 들어오지 말것")

#,형으로 글쓰기 실수형 문자형을 신경안써도 된다

print("이 집은" , year,"살 ", name,"의 집이다")
print("그래서 ",name,"의 집을 들어오지 말것")

#이렇게 변수 지정해서 편하게 할수 있다! 문자 변환은 str
#그리고 나중에 내가 정보같은걸 크롤링 해서 엑샐처럼 표를 만들어 보고싶다

  #문제 xx행 열차가... 들어오고 있습니다 

지하철역 = "사당"

print("이번역은",지하철역, "입니다" )


지하철역 = "신도림"

print("이번역은",지하철역, "입니다" )

지하철역 = "인청공항"

print("이번역은",지하철역, "입니다" )

print(1+1) #더하기
print(1-1) #뺴기
print(1*1) #더하기
print(1/1) #나누기

print(2**3) #2의 세재곱
print(5%3) #나머지
print(5//3) #나누기값

print(10>3) #참 
print(4>=7) #거짓 (같거나 크다 반대도 마찬가지)

print(10==10) #앞뒤값이 같으면 참
print (10 != 5) #참 앞,뒤값이 다를때 참

print(not(1!=1)) # !=에서 거짓이 나오는데 not 때문에 참

print( (3>2) and (10 > 7)) #둘다 맞으면 참 &=and
print((3>0) or (102<27)) #둘중 하나만 맞아도 참

a = 1

a +=2


print(a) 

#절대값 (abs(-5)) 5 절대값   (pow(2, 2)) 제곱 max 최대값 min 최솟값 round 반올림


from random import *


print(random) #0~1 랜덤
print(random, 10)

print(randint(1 , 45)) #1~45이하 숫자 랜덤

print("오프라인 스터디 모임 날짜는 매월", randint(4,28), "일 입니다") #시작할때 from~import 해주고 랜덤인트를 변수에 넣어서 사용할수도 있


dkdmdk = '나는 응애' 

print(dkdmdk)

주민등록 = "xx0919-323456"

print(" 생일은 :" + 주민등록[0:6] + "년도 주민등록 번호는" + 주민등록[7:]) # [-7:] 맨 뒤부터 7번째 까지

print(len(주민등록)) #문자열 길이를 알수있게 됨

print(4+4+5+4+4+3+4+4+4+4+3+4+4+5) #과학 시험 점수

korean = "Best python"

print(korean.lower())#대소문자 변환
print(korean.upper())
print(korean[0].isupper())#[]번쨰 글자 대문자인지 확인
print(len(korean))#글자수
print(korean.replace("Best", "very best")) #해당 글자를 정한거로 바꾸기 오류나면 "" , 대소문자 확인 

print (korean.index("B"))# 위치값을 알려줌

# 특정 값의 b에 위치를 알려줌 /프린트에 못씀/// 변수명.index("목표")
#index랑 비슷한거 find 사용법은 같음 근데 오류가 덜남 해당 목표가 없으면 -1로 반환



print("나는 %d살입니다" % 16) # %d 정수형 (1,2, 3,5,7, 소수점x 숫자만)
print("나는 %s을 좋아해요." %"파이썬")  # %s 문자열 "" 해주는거 잊지 말기
print("내 성은 %c 이에요."% "황" ) #%c 한글자만 가능


랜덤 = 0
횟수 = 0 
시험문항수 = 25

while 횟수 < 시험문항수:
      if 횟수 == 0:
         print("당신의 시험 정답")
      랜덤 = randint(1, 5)
      횟수 += 1
      print("{0} 번 문제 정답 {1}".format(횟수, 랜덤))
      if 횟수 == 시험문항수:
        print("100점 가즈아")


# {}{}.pormet(x,y)
# f{}{}.pormet(x,y) 변수 사용 가능

print("줄바꿈\n하기") #/n 줄바꿈

#텍스트 안에 "" 넣기

print("큰 \"따음표\" 쓰기") #문장내에서 ""쓰기 /"

#문장 내에서 \
#\\ 두번쓰기

#\r \b \t (커서 위치 0, 백스페이스, 탭)

사이트 = "http://naver.com"

사이트 = 사이트.replace("http://","")
사이트 = 사이트[:사이트.index(".")]
비밀번호 = 사이트[0:3] + str(len(사이트)) + str(사이트.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format("https://" + 사이트 + ".com" , 비밀번호))

#리스트 = [, , ,]
valol_entry = ["레이나", "제트", "레이즈"]
print(valol_entry)

#리스트 안에 제트 위치 찾기
print(valol_entry.index("제트"))

#맨 뒤에 추가하기
valol_entry.append("요루")
print(valol_entry)

#리스트 2번째에 넣기 나머지는 뒤로 밀림
valol_entry.insert(2,"네온")
print(valol_entry)

#리스트 속 요루 수가 몇 개 인지 확인
print(valol_entry.count("요루"))
print(valol_entry)

#정렬
num_list = [3, 2, 5, 4, 1]
num_list.sort()
print(num_list)

#순서 뒤집기
num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

#리스트는 다양한 자료형을 함께 사용할수 있음
mix_list = ["황가온", 20 , True]
print(mix_list)

#리스트 합치기
num_list = [1, 2, 3, 4, 6]
print(num_list)

num_list.extend(mix_list)
print(mix_list)

cabinet = {1: "레이즈", 3:"제트", 100: "요루"}
print(cabinet[1])
print(cabinet[100])

#[]과 get()의 차이

#print(cabinet[5]) 5번이라는 키값이 없어서 오류
#print(cabinet.get(5)) 5번이라는 키값이 없어도 오류 없이 none 반환

print(cabinet.get(5))
print(cabinet.get(5, "사용가능")) #none 대신 사용가능 반환

print(3 in cabinet)#true
print(5 in cabinet)#false

#추가

cabinet[3] = "네온"#키 값이 없으면 추가 있으면 네온으로 변경
print(cabinet)


#삭제

del cabinet[3]
print(cabinet)

# 키만 출력
print(cabinet.keys())

#값(valuses)만 출력
print(cabinet.values())

#키 값 한깨 충력

print(cabinet.items())

#다 지우기
cabinet.clear

#재미용 시험 정답 찍기 리스트ver

random = 0 #랜덤
repeat = 0 #횟수
total_problem = 25 #문제 수
perfect_score = 100 #만점
answer = [] #정답
stu_answer = [] #학생 답
ox = []
score = 0 #점수

print("만점 100점")
print("문항 수 {0}".format(total_problem))

while repeat < total_problem:  #시험 정답 생성하기
      answer.append(randint(1,5))
      repeat += 1

print("시험 정답 생성 완료")

repeat = 0 #변수 초기화

while repeat < total_problem: # 학생 정답 생성하기
      stu_answer.append(randint(1,5))
      repeat += 1

print("당신의 정답 생성 완료")

repeat = 0

while repeat < total_problem: # 정답 맞추기
      if answer[repeat] == stu_answer[repeat]:
         score += perfect_score/total_problem
         ox.append("O")
         repeat += 1
      else:
          ox.append("X")
          repeat += 1
          

print("정답")
print(perfect_score,"/",score)

print(answer)
print(stu_answer)
print(ox)


menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#추가, 변경 불가능

name, age , hobby = ("가온", "16", "코딩")
print(name, age , hobby)

#세트 중복, 순서 x
set = {1,2,3,4,4,4,4,}

java = {"a", "b", "c"}
python = {"a","d","s"}

#교집합
print(java & python)

#합집합
print(java | python)

#차집합 (자바는 가능하지만 파이썬은 모름)
print(java - python)

#추가
python.add("뀨")
print(python)

#삭제
python.remove("뀨")

#자료구조 변경
print(type(python))#타입확인
python= list(python) #타입 변경 set list tuple

comment = range(1, 21)
comment = list(comment)
shuffle(comment)
print(comment)

print("1등은 {0} 입니다\n2,3,4등은{1}입니다 축하드립니다!".format(comment[0], comment[1:4]))

absent = [2,5]
stu = 11

for stu in range(1,stu):
      if stu in absent:
            continue
      print(stu)


repeat_num = 0
total_time = 0


while repeat_num < 50:
      repeat_num += 1 
      random_time = randint(5, 51)
      print("{0}번 손님 (요구시간 {1}분)".format(repeat_num, random_time))
      if random_time < 15:
        total_time += random_time
        print(total_time)
      

print("총 소요 시간은", total_time , "입니다")

def hi():
      print("님 ㅎㅇ")

hi()


def plus(num1=0, num2=1):
      print("더하기 값은{}입니다".format(num1 + num2))
      num3 = num1 + num2
      return num3


def minus (num1, num2):
      print("빼기 값은 {}입니다".format(num1 - num2))


plus()

def plus_many (num1, num2, *any):
     result = num1 +num2 
     for num3 in any:
          result += num3
     print("더하기 결과는 {0} 입니다".format(result)) 


plus_many(1,2,41,212,11)

def sum (num):
     repeat =0
     str1 = "*"
     str2 = "/"
     str3 = "+"
     str4 = "-"
     if (type(num)) != str:
          num = str(num)
     print(1)          
     while repeat < len(num):
            if num[repeat:repeat+1] == str3 or num[repeat:repeat+1] == str1 or num[repeat:repeat+1] == str2 or num[repeat:repeat+1] == str4:
              print("{0}찾음".format(repeat))
            repeat += 1        

     return 1
          
     
import time
          
          #1


ts = input("")





sum(ts)


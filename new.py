from random import *

any = "고양이"
way = 4
wer = "공놀이"

print(any + "는 "+ wer + "을 좋아해")



station = "사당"
print(station + "행 열차가 들러옴")

station = "신도림"
print(station + "행 열차가 들러옴")

station = "인천"
print(station + "행 열차가 들러옴")

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

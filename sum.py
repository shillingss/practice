from ast import Num
from operator import index
from symbol import parameters
from time import time
from random import *


def mtpy_div (spilt):
     if "*" or "/" in spilt:
          repeat = 0
          demi = 1
          while repeat < len(spilt):
               if str(spilt[repeat]) == "*" or "/":
                    if str(spilt[repeat]) == "*":

                       demi = float(spilt[repeat-1])*float(spilt[repeat+1])#계산
                       del spilt[repeat]
                       spilt.insert(repeat, demi)#저장 후 리스트 관리
                       del spilt[repeat-1]
                       del spilt[repeat]
                       mtpy_div(spilt)

                    elif str(spilt[repeat]) == "/":

                       demi = float(spilt[repeat-1])/float(spilt[repeat+1])
                       del spilt[repeat]
                       spilt.insert(repeat, demi)
                       del spilt[repeat-1]
                       del spilt[repeat]
                       mtpy_div(spilt)
               repeat +=1


def pl_mi(spilt):
     if "+" or "-" in spilt:
          repeat = 0
          demi = 1
          while repeat < len(spilt):
               if str(spilt[repeat]) == "+" or "-":
                    if str(spilt[repeat]) == "+":

                       demi = float(spilt[repeat-1])+float(spilt[repeat+1])
                       del spilt[repeat]
                       spilt.insert(repeat, demi)
                       del spilt[repeat-1]
                       del spilt[repeat]
                       mtpy_div(spilt)

                    elif str(spilt[repeat]) == "-":

                       demi = float(spilt[repeat-1])-float(spilt[repeat+1])
                       del spilt[repeat]
                       spilt.insert(repeat, demi)
                       del spilt[repeat-1]
                       del spilt[repeat]
                       mtpy_div(spilt)
               repeat +=1

def sum (num):
     repeat =0
     str1 = "*"
     str2 = "/"
     str3 = "+"
     str4 = "-"
     start, end = 0 ,0
     split = []
     symbol = "*/+-"
     if (type(num)) != str:
          num = str(num)    
     num = num.replace(" ", "")    
     while repeat < len(num):
            if symbol.count(num[repeat:repeat+1]) == 1:
              end = repeat
              split.append(num[start:end])
              split.append(num[end:end+1])
              start = end+1
            repeat += 1    
            
     if repeat < len(num)+1:
          split.append(num[start:len(num)]) #마지막 글자 추가
     print(split)

     repeat = 0

     mtpy_div(split)#*/ 먼저 하고 +-계산
     pl_mi(split)

     print(split)





ts = input("")

sum(ts)

#음수 넣으면 오류남 5*-2 이런거 소괄호 넣으면서 고칠 예정
from ast import Num
from operator import index
from symbol import parameters
from time import time
from random import *





def sum (num):
     repeat =0
     str1 = "*"
     str2 = "/"
     str3 = "+"
     str4 = "-"
     start, end = 0 ,0
     split = []
     if (type(num)) != str:
          num = str(num)        
     while repeat < len(num):
            if num[repeat:repeat+1] == str3 or num[repeat:repeat+1] == str1 or num[repeat:repeat+1] == str2 or num[repeat:repeat+1] == str4:
              print("{0}찾음".format(repeat))#오류 찾기용
              end = repeat
              split.append(num[start:end])
              split.append(num[end:end+1])
              start = end+1
            repeat += 1    
            print("값",start)

     if repeat < len(num)+1:
          split.append(num[start:len(num)])
     print(split)
    

sum(input(""))

#미완

#input 1+1-1 output ['1', '+', '1', '-', '1']

#input 20-1+1 output ['20', '-', '1', '+', '1']

#input 211-93*21-1& D:/Python38-32/python.exe output ['211', '-', '93', '*', '21', '-', '1& D:', '/', 'Python38', '-', '32', '/', 'python.exe c:', '/', 'Users', '/', '3D', '-', '01', '/', 'Desktop', '/', 'PytonWarkspace', '/', 'sum.py']
#(my mistake but very good)

#input 211-24-12+24/1 output ['211', '-', '24', '-', '12', '+', '24', '/', '1']
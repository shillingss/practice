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
     if (type(num)) != str:
          num = str(num)
     print(1)          
     while repeat < len(num):
            if num[repeat:repeat+1] == str3 or num[repeat:repeat+1] == str1 or num[repeat:repeat+1] == str2 or num[repeat:repeat+1] == str4:
              print("{0}찾음".format(repeat))
            repeat += 1        

     return 1



#미완
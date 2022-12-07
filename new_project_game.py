from random import *
import time

item_code = ["체력포션", "마나포션", "크리티컬 포션"]
Request_Quantity = []
score = 0


#주문
#처음에 랜덤한 2개를 item code에서 정하고 요청에 넣음 그리고 랜덤한 시간마다 iteam code 값을 랜덤하게 요청에 넣음 요청 수량도 볼수 있게 코딩p
Request_Quantity.append(randint(1, len(item_code)))
Request_Quantity.append(randint(1, len(item_code)))

while score >= 40:
      time.sleep(randint(1,5)) #반복문 말고 외부에서 랜덤 조정할수 있도록 (튜토리얼 등 통제를 위해서)
      Request_Quantity.append(randint(1, len(item_code)))

print(Request_Quantity)


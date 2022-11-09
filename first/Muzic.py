import os
from playsound import playsound


list1 = os.listdir('D:/МУЗ_02.10')
print(list1)
print(len(list1))

for k in list1:
    os.remove(f'G:/NGH/{k}')

#for i in list1[1:]:
  #  playsound(f'D:/МУЗ_02.10/{i}')
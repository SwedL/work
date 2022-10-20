import os
from playsound import playsound


list1 = os.listdir('D:/МУЗ_02.10')

for i in list1[1:]:
    playsound(f'D:/МУЗ_02.10/{i}')
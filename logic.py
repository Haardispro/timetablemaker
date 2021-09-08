import os
import random
import time 

os.system("figlet timetable maker")
ran = []
inst = input("Enter the name of your institution: ")
periods = int(input("Enter the number of periods: "))
for i in range(periods):
    print("Enter period ", i+1)
    x = input(":")
    ran.append(x)
days = int(input("Enter the number of working days: "))
print("Making the timetable" )
dot = "."
for i in range(4):
    time.sleep(0.5)
    print(dot)
    dot = dot + "."

print("Timetable for {} ->".format(inst))
for i in range(periods):
    #print(ran[i])
    print(random.choice(ran))
#Periods
"""
periods = ["maths", "physics", "chemistry", "biology", "hindi", "english", "computer", "sports"]
#print(periods[1])

for i in range(8):
    #print(periods[i])
    x = random.choice(periods)
    print(x)
"""
"""
per = 45*8
time = 14.5 - 8.0
print(per/time)
"""
#time 
#8:00 to 14:30
#each period 45 min

#weekdays
#days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
#on Saturday only 4 periods




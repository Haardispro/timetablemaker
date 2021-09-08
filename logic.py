import os
import random
import time 

#os.system("figlet timetable maker")
print("""
     _   _                _        _     _                        _             
    | |_(_)_ __ ___   ___| |_ __ _| |__ | | ___   _ __ ___   __ _| | _____ _ __ TM
    | __| | '_ ` _ \ / _ \ __/ _` | '_ \| |/ _ \ | '_ ` _ \ / _` | |/ / _ \ '__|
    | |_| | | | | | |  __/ || (_| | |_) | |  __/ | | | | | | (_| |   <  __/ |   
     \__|_|_| |_| |_|\___|\__\__,_|_.__/|_|\___| |_| |_| |_|\__,_|_|\_\___|_|
""")
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
print(ran)


x = random.randint(0, periods-1)
y = random.randint(0, periods-1)

while x != y:
    for i in range(periods):
        ran.insert(x, ran.pop(y))
        print(ran)
    break
#MyList.insert(index_to_insert,MyList.pop(index_to_remove))
"""
for i in range(periods):
    print(ran[i])
    #print(random.choice(ran))
"""
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




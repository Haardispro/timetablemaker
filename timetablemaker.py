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
Info = input("Enter the name of your institution: ")
periods = int(input("Enter the number of subjects in total: "))
for i in range(periods):
    print(f"Enter subject no.{i+1}")
    x = input(":")
    ran.append(x)

# Oneday = random.shuffle(ran)
days = int(input("Enter the number of working days: "))

print("Making the timetable ")
dot = "."
for i in range(3):
    time.sleep(0.5)
    print(dot)
    time.sleep(0.5)
    dot = dot + "."

print(f"Timetable for {Info} ->")
for j in range(days):
    j=j+1
    daysList= ["Monday    ","Tuesday   ","Wednesday ","Thursday  ","Friday    ","Saturday  ","Sunday    "]
    random.shuffle(ran)
    print(f"{daysList[j-1]} : {ran}")
    
    




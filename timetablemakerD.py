# this is a freakin trial
# Author - ur mama
# Credits - dEV sHAH , hardiik

# lemme try this @Haardispro
from random import sample
import time


Username = input("Enter your good name : ")
print(f"\nWelcome to timetablemaker™ {Username}")

UserInfo = input("Optional infomation/Institute name  : ")
print(f"\n Thank you ! \n Information : {UserInfo}")

# We will be having 5 days (M,T,W,T,F) and 8 classes in each day = 40 slots for lectures

print("\n We have 8 classes per day and 5 days in a week by default ie. 40 slots for your subjects")

noOfsubjects = int(input("How many subjects do you have(max-10,min-2) : "))
subjects=[]
# # I tried for loop but it doesnt let me have my operations with the subjects outside the loop , I may have to make a list of all inputs from that in a list
# Subject1 = input("Enter the name of first subject :")
# Subject2 = input("Enter the name of second subject :")
# Subject3 = input("Enter the name of  third subject :")
# Subject4 = input("Enter the name of first subject :")
# Subject5 = input("Enter the name of first subject :")

for i in range(noOfsubjects):
    nameOfsubject = input(f"Enter the name of {i+1}st/nd/rd/th : ")
    subjects.append(nameOfsubject)

print(subjects)

print("\n\n\n Timetable is processing ... ")

time.sleep(1)

print(" Timetable successfully made ... (Made in 0.9 seconds) \n\n")
#(sample(subjects,8-len(subjects)))
def listToString(s): 
    
    str1 = "" 
    
    for ele in s: 
        str1 += ele  
subjectFillerlst = sample(subjects,8-len(subjects))
# print(listToString(subjectFillerlst)) 

if(len(subjects)<8):
    subjects.append(subjectFillerlst)
print(subjects)
# print("\n\n\n ***Monday***\n")
# print(sample(subjects,8))

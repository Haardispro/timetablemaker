import random 

#main list in which everything is stored
subjects_list = []
x = """
 _   _                _        _     _                      _             
| |_(_)_ __ ___   ___| |_ __ _| |__ | | ___ _ __ ___   __ _| | _____ _ __ 
| __| | '_ ` _ \ / _ \ __/ _` | '_ \| |/ _ \ '_ ` _ \ / _` | |/ / _ \ '__|
| |_| | | | | | |  __/ || (_| | |_) | |  __/ | | | | | (_| |   <  __/ |   
 \__|_|_| |_| |_|\___|\__\__,_|_.__/|_|\___|_| |_| |_|\__,_|_|\_\___|_|   
"""
print(x)
#Basic Inputs
institution = input("What is the name of your institution?:")
subjects = int(input("Number of Subjects:"))

#Enter subjects
for i in range(subjects):
    sub = input("Enter subject:")
    subjects_list.append(sub)

#Number of Periods in one day
days_periods = int(input("Number of periods in 1 day:"))

#Number of working days
days = int(input("Number of working days:"))

#The final timetable
print("Timetable for {}".format(institution))
#The main loop
for i in range(days):
    random.shuffle(subjects_list)
    if days_periods < subjects:
        tt = subjects_list[0:days_periods]
        separator = "   |   "
        print(separator.join(tt))
    elif days_periods == subjects:
        separator = "   |   "
        print(separator.join(subjects_list))
    elif days_periods > subjects:
        #add an extra subject from the given list
        #doing logic until condition in met
        while len(subjects_list) != days_periods:
            x = random.randrange(0, subjects)
            y = subjects_list[x]
            subjects_list.append(y)
        separator = "   |   "
        print(separator.join(subjects_list))

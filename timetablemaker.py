import random 

#main list
subjects_list = []

institution = input("What is the name of your institution?:")
subjects = int(input("Number of Subjects:"))

for i in range(subjects):
    sub = input("Enter subject:")
    subjects_list.append(sub)


days_periods = int(input("Number of periods in 1 day:"))

days = int(input("Number of working days:"))


print("Timetable for {}".format(institution))
for i in range(days):
    random.shuffle(subjects_list)
    if days_periods < subjects:
        tt = subjects_list[0:days_periods]
        separator = " , "
        print(separator.join(tt))
    elif days_periods == subjects:
        separator = " , "
        print(separator.join(subjects_list))
    elif days_periods > subjects:
        #add an extra subject from the given list
        #doing logic until conditioin in met

        while len(subjects_list) != days_periods:
            x = random.randrange(0, subjects)
            y = subjects_list[x]
            subjects_list.append(y)
        separator = " , "
        print(separator.join(subjects_list))

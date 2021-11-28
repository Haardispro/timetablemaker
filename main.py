from tkinter import *

w = Tk()
w.title("Timetable maker")
w.geometry("800x600")

#Main list
subjects_list = []

def timetable():
    dyget = int(days.get())
    dpget = int(days_periods.get())
    inget = int(institution.get())
    
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

def ask():
    x = int(days_periods.get())
    for i in range(x):
        subject = Entry(w, width=20)
        subject.grid(row = i+4, column=0)
    #return

institution = Entry(w, width=20)
days_periods = Entry(w, width=20)
days = Entry(w, width=20)



#Positions
institution.grid(row=1, column=0)
days_periods.grid(row=2, column=0)
days.grid(row=3, column=0)

w.mainloop()

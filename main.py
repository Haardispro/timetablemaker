from tkinter import *

w = Tk()
w.title("Timetable maker")
w.geometry("800x600")

def timetable():
    return


institution = Entry(w, width=10)
institution.grid(row=1, column=0)
periods = Entry(w, width=10)
periods.grid(row=2, column=0)

w.mainloop()

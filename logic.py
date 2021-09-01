#here is the logic 
# I don't know how to do it.
import random

maths = "maths"
science = "science"
ss = "ss"
english = "english"
hindi = "hindi"
computer = "computer"
sports = "sports"

tt = [maths, science, ss, english, hindi, computer, sports]
for i in range(9):
    s = random.choice(tt)
    print(s)

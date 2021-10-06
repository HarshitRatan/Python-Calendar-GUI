#Code By Harshit Ratan Shukla
from tkinter import *
import tkinter as tk
import calendar

#GUI
root = tk.Tk()
root.geometry('275x500')
root.title('Calender')
root.resizable(False, False)

#Define Show Calender Function

def show():
    cal.delete(1.0, 'end')
    mon = int(month.get()) #Getting Months From User
    yr = int(year.get()) #Getting Year From User
    Cal_data = calendar.month(yr, mon)

    cal.insert('end', Cal_data)


#Define Clear Button Function
def clear():
    cal.delete(1.0, 'end')

#Define Exit Button Function
def exit():
    root.destroy()


#Display Months Name and Its Code
mon_dis_label = Label(root, text="Codes For Months::", font=('verdana', '10', 'bold'))
mon_dis_label.place(x=1, y=1)

jan = Label(root, text="Jan - 01", font=('verdana', '10', 'bold'))
jan.place(x=1, y=20)

feb = Label(root, text="Feb - 02", font=('verdana', '10', 'bold'))
feb.place(x=1, y=40)

mar = Label(root, text="Mar - 03", font=('verdana', '10', 'bold'))
mar.place(x=1, y=60)

Ap = Label(root, text="April - 04", font=('verdana', '10', 'bold'))
Ap.place(x=1, y=80)

May = Label(root, text="May - 05", font=('verdana', '10', 'bold'))
May.place(x=1, y=100)

june = Label(root, text="June - 06", font=('verdana', '10', 'bold'))
june.place(x=1, y=120)



july = Label(root, text="July - 07", font=('verdana', '10', 'bold'))
july.place(x=1, y=140)

Aug = Label(root, text="Aug - 08", font=('verdana', '10', 'bold'))
Aug.place(x=1, y=160)

sept = Label(root, text="Sept - 09", font=('verdana', '10', 'bold'))
sept.place(x=1, y=180)

octo = Label(root, text="Oct - 10", font=('verdana', '10', 'bold'))
octo.place(x=1, y=200)

nov = Label(root, text="Nov - 11", font=('verdana', '10', 'bold'))
nov.place(x=1, y=220)

dec = Label(root, text="Dec - 12", font=('verdana', '10', 'bold'))
dec.place(x=1, y=240)



#Months Label And Input Field
mon_label = Label(root, text="Month", font=('verdana', '10', 'bold'))
mon_label.place(x=1, y=280)

month = Spinbox(root, from_=1, to=12, width="5")
month.place(x=60, y=280)

#Year Label And Input Field
yr_label = Label(root, text="Year", font=('verdana', '10', 'bold'))
yr_label.place(x=150, y=280)

year = Spinbox(root, from_=1990, to=3000, width="8")
year.place(x=190, y=280)

#Output Screen
cal = Text(root, width=33, height=8, relief=RIDGE, borderwidth=2)
cal.bind("<Key>", lambda e : "break")
cal.place(x=1, y=300)


#Buttons
show = Button(root, text="Show", font=('verdana', 10, 'bold'), relief=RIDGE, borderwidth=2, command=show)
show.place(x=200, y=450)

clear = Button(root, text="Clear", font=('verdana', 10, 'bold'), relief=RIDGE, borderwidth=2, command=clear)
clear.place(x=100, y=450)

exit = Button(root, text="Exit", font=('verdana', 10, 'bold'), relief=RIDGE, borderwidth=2, command=exit)
exit.place(x=1, y=450)


root.mainloop()

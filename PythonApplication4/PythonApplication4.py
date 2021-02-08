from tkinter import *
import time
from tkinter.messagebox import *

root=Tk()
root.geometry('500x700')
M=Menu(root)
root.config(menu=M)

click = 0
mult = 1


def Plus(cps,K):
    global click
    global mult
    if click < cps:
        showinfo('Upgrader','Message: Not enough clicks! It Costs 100')
    elif click >= cps:
        mult = mult+K
        click = click - cps
        showinfo("Upgrader",f"Message: +{K} Clicks Purchased!")

def Doubler():
    global click
    global mult
    if click < 1000000:
        print("Not enough clicks! It Costs 1 Mil")
        blankLine()
    elif click >= 1000000:
        mult = mult * 2
        click = click - 1000000
        showinfo("Upgrader","Message: Double Clicks Purchased!")
        blankLine()

def count():
    global click
    global mult
    click += mult 
    entry.delete(0, 'end')
    entry.insert(0,click)
    if click >50 and click <53:
        showinfo('Achievements','Message: Achievement Unlocked: Junior Clicker! BONUS 100 Clicks')
        click += 100

    elif click > 1000 and click<1020:
        showinfo('Achievements','Message: Achievement Unlocked: Little Clicker! BONUS 200 Clicks')
        click += 200

    elif click > 5000 and click <5100:
        showinfo('Achievements','Message: Achievement Unlocked: Big Clicker! BONUS 1000 Clicks')
        click += 1000

    elif click == 9000:
        showinfo('Achievements','Message: Achievement Unlocked: ITS OVER 9000! BONUS 4000 Clicks')
        click+= 4000

    elif click == 25000:
        showinfo('Achievements','Message: Achievement Unlocked: Huge Clicker! BONUS x2 Clicks')
        mult = mult * 2

    elif click == 25000:
        showinfo('Achievements','Message: Achievement Unlocked: Mega Clicker! BONUS x3 Clicks')
        mult = mult * 3

    elif click == 500000:
        showinfo('Achievements','Message: Achievement Unlocked: God Clicker! BONUS +100000 Clicks')
        click += 100000


root.title("Clicker! v0.1")

m1=Menu(M,tearoff=0)
M.add_cascade(label='Click Upgrader', menu=m1)
m1.add_command(label='+1 points per click',command=lambda:Plus(10,1))
m1.add_command(label='+5 points per click',command=lambda:Plus(100,5))
m1.add_command(label='+10 points per click',command=lambda:Plus(1000,10))
m1.add_command(label='+20 points per click',command=lambda:Plus(5000,20))
m1.add_command(label='+50 points per click',command=lambda:Plus(10000,50))
m1.add_command(label='+100 points per click',command=lambda:Plus(1,1))
m1.add_command(label='+200 points per click',command=lambda:Plus(1,1))
m1.add_command(label='+500 points per click',command=lambda:Plus(1,1))
m1.add_command(label='+1000 points per click',command=lambda:Plus(1,1))
m1.add_command(label='Double points per click',command=lambda:Doubler())
button = Button(text="CLICK",command=lambda:count())
label = Label(text="SCORE",font = 'arial 20',bg = 'red')
entry = Entry(root)
label.pack(side = TOP , pady = 5)
entry.pack(side = TOP , pady = 5)
button.pack(side=TOP , pady = 5)
root.mainloop()

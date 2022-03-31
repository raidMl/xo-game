from tkinter import *
from tkinter import ttk
from  tkinter import messagebox
root=Tk()
style=ttk.Style()
style.configure('TButton',foreground='yellow',background='red',font=('comic sans ms',18,'bold'))


root.title("X O  game :player 1")
ActivePlayer=1

p1=[]   #what player 1 selected
p2=[]   #what player 2 selected


bu1=ttk.Button(root,text=" ")
bu1.grid(column=0,row=0,sticky="nsew",ipadx=40,ipady=40)
bu1.config(command=lambda : butclick(1))

bu2=ttk.Button(root,text=" ")
bu2.grid(column=1,row=0,sticky="nsew",ipadx=40,ipady=40)
bu2.config(command=lambda : butclick(2))

bu3=ttk.Button(root,text=" ")
bu3.grid(column=2,row=0,sticky="nsew",ipadx=40,ipady=40)
bu3.config(command=lambda : butclick(3))

bu4=ttk.Button(root,text=" ")
bu4.grid(column=0,row=1,sticky="nsew",ipadx=40,ipady=40)
bu4.config(command=lambda : butclick(4))

bu5=ttk.Button(root,text=" ")
bu5.grid(column=1,row=1,sticky="nsew",ipadx=40,ipady=40)
bu5.config(command=lambda : butclick(5))

bu6=ttk.Button(root,text=" ")
bu6.grid(column=2,row=1,sticky="nsew",ipadx=40,ipady=40)
bu6.config(command=lambda : butclick(6))

bu7=ttk.Button(root,text=" ")
bu7.grid(column=0,row=2,sticky="nsew",ipadx=40,ipady=40)
bu7.config(command=lambda : butclick(7))

bu8=ttk.Button(root,text=" ")
bu8.grid(column=1,row=2,sticky="nsew",ipadx=40,ipady=40)
bu8.config(command=lambda : butclick(8))

bu9=ttk.Button(root,text=" ")
bu9.grid(column=2,row=2,sticky="nsew",ipadx=40,ipady=40)
bu9.config(command=lambda : butclick(9))

style.configure('TButton',foreground='yellow')


def butclick(id):
    global ActivePlayer
    global p1
    global p2
    if(ActivePlayer==1):
        SetLayout(id,"X")
        p1.append(id)
        root.title("X O game:player 2")
        ActivePlayer=2
        print("P1:{}".format(p1))
        ChekWinner()
    elif (ActivePlayer == 2):
        SetLayout(id,"O")
        p2.append(id)
        root.title("X O game:player 1")
        ActivePlayer = 1
        print("P2:{}".format(p2 ))
        ChekWinner()
def SetLayout(id,text):
  if(id==1):
      bu1.config(text=text)
      bu1.state(["disabled"])

  elif (id == 2):
      bu2.config(text=text)
      bu2.state(["disabled"])
  elif (id == 3):
      bu3.config(text=text)
      bu3.state(["disabled"])
  elif (id == 4):
      bu4.config(text=text)
      bu4.state(["disabled"])
  elif (id == 5):
      bu5.config(text=text)
      bu5.state(["disabled"])
  elif (id == 6):
      bu6.config(text=text)
      bu6.state(["disabled"])
  elif (id == 7):
      bu7.config(text=text)
      bu7.state(["disabled"])
  elif (id == 8):
      bu8.config(text=text)
      bu8.state(["disabled"])
  elif (id == 9):
      bu9.config(text=text)
      bu9.state(["disabled"])
def ChekWinner():
    winer=-1
    if((1 in p1)and(2 in p1) and(3 in p1)):
     winer=1
    if((1 in p1)and(2 in p2) and(3 in p2)):
     winer=2
    if ((4 in p1) and (5 in p1) and (6 in p1)):
        winer = 1
    if ((4 in p2) and (5 in p2) and (6 in p2)):
        winer = 2
    if ((7 in p1) and (8 in p1) and (9 in p1)):
        winer = 1
    if ((7 in p2) and (8 in p2) and (9 in p2)):
        winer = 2
    if ((1 in p1) and (4 in p1) and (7 in p1)):
        winer = 1
    if ((1 in p2) and (4 in p2) and (7 in p2)):
        winer = 2
    if ((2 in p1) and (5 in p1) and (8 in p1)):
        winer = 1
    if ((2 in p2) and (5 in p2) and (8 in p2)):
        winer = 2
    if ((3 in p1) and (6 in p1) and (9 in p1)):
        winer = 1
    if ((3 in p2) and (6 in p2) and (9 in p2)):
        winer = 2
    if ((1 in p1) and (5 in p1) and (9 in p1)):
        winer = 1
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        winer = 2

    if ((3 in p1) and (5 in p1) and (7 in p1)):
        winer = 1
    if ((3 in p2) and (5 in p2) and (7 in p2)):
        winer = 2

    if( winer==1):
        messagebox.showinfo(title="congratulation", message="player 1 is the winer")
    elif (winer==2):
        messagebox.showinfo(title="congratulation", message="player 2 is the winer")
root.mainloop()
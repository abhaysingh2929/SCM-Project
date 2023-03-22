from tkinter import Tk,ttk,Button
from tkinter import messagebox
from random import randint

ActivePlayer = 1
p1 = []
p2 = []
mov = 0

def SetLayout(id,player_symbol):
    if id==1:
        b1.config(text= player_symbol)
        b1.state(['disabled'])
    elif id==2:
        b2.config(text= player_symbol)
        b2.state(['disabled'])
    elif id==3:
        b3.config(text= player_symbol)
        b3.state(['disabled'])
    elif id==4:
        b4.config(text= player_symbol)
        b4.state(['disabled'])
    elif id==5:
        b5.config(text= player_symbol)
        b5.state(['disabled'])
    elif id==6:
        b6.config(text= player_symbol)
        b6.state(['disabled'])
    elif id==7:
        b7.config(text= player_symbol)
        b7.state(['disabled'])
    elif id==8:
        b8.config(text= player_symbol)
        b8.state(['disabled'])
    elif id==9:
        b9.config(text= player_symbol)
        b9.state(['disabled'])

def CheckWinner():
    global mov 
    winner = -1

    if(1 in p1) and (2 in p1) and (3 in p1):
        winner = 1
    if(1 in p2) and (2 in p2) and (3 in p2):
        winner = 2

    if(4 in p1) and (5 in p1) and (6 in p1):
        winner = 1
    if(4 in p2) and (5 in p2) and (6 in p2):
        winner = 2

    if(7 in p1) and (8 in p1) and (9 in p1):
        winner = 1
    if(7 in p2) and (8 in p2) and (9 in p2):
        winner = 2

    if(1 in p1) and (4 in p1) and (7 in p1):
        winner = 1
    if(1 in p2) and (4 in p2) and (7 in p2):
        winner = 2

    if(2 in p1) and (5 in p1) and (8 in p1):
        winner = 1
    if(2 in p2) and (5 in p2) and (8 in p2):
        winner = 2

    if(3 in p1) and (6 in p1) and ( 9 in p1):
        winner = 1
    if(3 in p2) and (6 in p2) and (9 in p2):
        winner = 2

    if(1 in p1) and (5 in p1) and ( 9 in p1):
        winner = 1
    if(1 in p2) and (5 in p2) and (9 in p2):
        winner = 2

    if(3 in p1) and (5 in p1) and ( 7 in p1):
        winner = 1
    if(3 in p2) and (5 in p2) and (7 in p2):
        winner = 2

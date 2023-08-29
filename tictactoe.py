from tkinter import *
import tkinter.messagebox as mb

tk=Tk()
tk.title('tic tac toe')
p1=StringVar()
p2=StringVar()
p1_turn=True
flag=0


def btn_click(bu):
    global p1_turn,flag
    if bu['text']=='' and p1_turn:
        bu['text']='X'
        p1_turn=False
        check_winner()
        flag+=1
    elif bu['text']=='' and not p1_turn:
        bu['text'] = 'O'
        p1_turn = True
        check_winner()
        flag += 1
    else:
        mb.showinfo('tic tac toe','Grid already filled')


def check_winner():
    if (btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or
        btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X' or
        btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X' or
        btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X' or
        btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X' or
        btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X' or
        btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X' or
        btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X'):
        mb.showinfo('tic tac toe',p1.get()+" Wins!")
        disable_button()
    elif (btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
          btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O' or
          btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O' or
          btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O' or
          btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O' or
          btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O' or
          btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O' or
          btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O'):
        mb.showinfo('tic tac toe', p2.get() + " Wins!")
        disable_button()
    elif flag==8:
        mb.showinfo('tic tac toe', 'It is a Tie')
        disable_button()

def disable_button():
    btn1.configure(state=DISABLED)
    btn2.configure(state=DISABLED)
    btn3.configure(state=DISABLED)
    btn4.configure(state=DISABLED)
    btn5.configure(state=DISABLED)
    btn6.configure(state=DISABLED)
    btn7.configure(state=DISABLED)
    btn8.configure(state=DISABLED)
    btn9.configure(state=DISABLED)

def restart_button():
    global flag,p1_turn
    flag=0
    p1_turn=True
    player1.delete(0,END)
    player2.delete(0, END)
    btn1['text'] = btn2['text'] = btn3['text'] = btn4['text'] = btn5['text'] = btn6['text'] = btn7['text'] = btn8['text'] = btn9['text'] = ''
    btn1.configure(state=NORMAL)
    btn2.configure(state=NORMAL)
    btn3.configure(state=NORMAL)
    btn4.configure(state=NORMAL)
    btn5.configure(state=NORMAL)
    btn6.configure(state=NORMAL)
    btn7.configure(state=NORMAL)
    btn8.configure(state=NORMAL)
    btn9.configure(state=NORMAL)


l1=Label(tk,text='Player1:(X)',font='Times 12 bold',fg='black')
l1.grid(row=0,column=0)
player1=Entry(tk,textvariable=p1,bd=5)
player1.grid(row=0,column=1)

l2=Label(tk,text='Player2:(O)',font='Times 12 bold',fg='black')
l2.grid(row=1,column=0)
player2=Entry(tk,textvariable=p2,bd=5)
player2.grid(row=1,column=1)

restart=Button(tk,text='Restart',font='Times 15 bold',bg='brown',fg='white')
restart.grid(row=1,column=2)
restart.config(command=lambda:restart_button())

btn1 = Button(tk,text='',font='Times 20 bold',bg='black',fg='white',height=4,width=8,command=lambda:btn_click(btn1))
btn1.grid(row=2,column=0)

btn2 = Button(tk, text='', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btn_click(btn2))
btn2.grid(row=2, column=1)

btn3 = Button(tk, text='', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btn_click(btn3))
btn3.grid(row=2, column=2)

btn4 = Button(tk, text='', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btn_click(btn4))
btn4.grid(row=3, column=0)

btn5 = Button(tk, text='', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btn_click(btn5))
btn5.grid(row=3, column=1)

btn6 = Button(tk, text='', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btn_click(btn6))
btn6.grid(row=3, column=2)

btn7 = Button(tk, text='', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btn_click(btn7))
btn7.grid(row=4, column=0)

btn8 = Button(tk, text='', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btn_click(btn8))
btn8.grid(row=4, column=1)

btn9 = Button(tk, text='', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btn_click(btn9))
btn9.grid(row=4, column=2)

tk.mainloop()

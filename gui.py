import tkinter as tk
from tkinter.constants import END
import random

root=tk.Tk()
output = tk.Text(root, height = 50, 
              width = 25, 
              bg = "light cyan")

def comp():
    complist=['rock','paper','scissors']
    n=random.randint(0,2)
    return complist[n]

        
def score(a,b):
    a=str(a)
    b=str(b)
    output.insert(END,'\nSCORE :')
    output.insert(END,'\nUser = '+a+' Comp = '+b)

def checkwin(a,b,c):
    c=int(c)
    if a==c:
        output.insert(END,'\nCONGARATULATIONS YOU HAVE WON')
        return 0
    if b==c:
        output.insert(END,'\nGAME OVER')
        return 0
        



root.title("ROCK-PAPER-SCISSORS")

# setting the windows size
root.geometry("600x400")

# declaring string variable

score_int=tk.StringVar()
inp_var=tk.StringVar()

i=0
i=int(i)
j=0
j=int(j)



def scorefun():
    global scorevar
    scorevar=score_int.get()
    output.insert(END,"The maximum score is : " + scorevar)
    score_int.set("")
    

def submit():
    global inp,i,j
    
    inp=inp_var.get()
    #inp_var.set("")
    inp=inp.lower()
    if inp=='rock'or inp=='paper' or inp=='scissors':
        may=1
    else:
        output.insert(END,"\nWrong Input")
    if may==1 :
        output.insert(END,"\nUser chose : " + inp)
        l=inp
        k=comp()
        output.insert(END,"\nComp chose "+ k)
            
        if(l == 'rock' and k == 'scissors'):
            i += 1
            score(i, j)
        elif(l == 'paper' and k == 'rock'):
            i += 1
            score(i, j)
        elif(l == 'scissors' and k == 'paper'):
            i += 1
            score(i, j)
        elif(k == 'scissors' and l == 'paper'):
            j += 1
            score(i, j)
        elif(k == 'paper' and l == 'rock'):
            j += 1
            score(i, j)
        elif(k == 'rock' and l == 'scissors'):
            j += 1
            score(i, j)
        else:
            output.insert(END,"\nDraw")
            score(i, j)
        flag = checkwin(i, j,scorevar)
        
	





	

score_label = tk.Label(root, text = 'Enter the Maximum Score', font=('calibre',10, 'bold'))


score_entry = tk.Entry(root,textvariable = score_int, font=('calibre',10,'normal'))


inp_label = tk.Label(root, text = 'Rock-Paper-Scissors?', font = ('calibre',10,'bold'))


inp_entry=tk.Entry(root, textvariable = inp_var, font = ('calibre',10,'normal'))


sub_btn1=tk.Button(root,text = 'Submit', command = submit)
sub_btn2=tk.Button(root,text = 'Submit', command = scorefun)


score_label.grid(row=0,column=0)
score_entry.grid(row=0,column=1)
inp_label.grid(row=1,column=0)
inp_entry.grid(row=1,column=1)
sub_btn2.grid(row=0,column=3)
sub_btn1.grid(row=1,column=3)
output.grid(row=2,column=1)


root.mainloop()

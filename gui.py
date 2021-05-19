import tkinter as tk
from tkinter.constants import END

root=tk.Tk()
root.title("ROCK-PAPER-SCISSORS")

# setting the windows size
root.geometry("600x400")

# declaring string variable

score_var=tk.StringVar()
inp_var=tk.StringVar()



def sub():
    global score
    score=score_var.get()
    Output.insert(END,"The maximum score is : " + score)
    score_var.set("")
    

def submit():
    global inp
    inp=inp_var.get()
    Output.insert(END,"\nUser chose : " + inp)
    inp_var.set("")
	


Output = tk.Text(root, height = 25, 
              width = 25, 
              bg = "light cyan")


	

score_label = tk.Label(root, text = 'Enter the Maximum Score', font=('calibre',10, 'bold'))


score_entry = tk.Entry(root,textvariable = score_var, font=('calibre',10,'normal'))


inp_label = tk.Label(root, text = 'Rock-Paper-Scissors?', font = ('calibre',10,'bold'))


inp_entry=tk.Entry(root, textvariable = inp_var, font = ('calibre',10,'normal'))


sub_btn1=tk.Button(root,text = 'Submit', command = submit)
sub_btn2=tk.Button(root,text = 'Submit', command = sub)


score_label.grid(row=0,column=0)
score_entry.grid(row=0,column=1)
inp_label.grid(row=1,column=0)
inp_entry.grid(row=1,column=1)
sub_btn2.grid(row=0,column=3)
sub_btn1.grid(row=1,column=3)
Output.grid(row=2,column=1)


root.mainloop()

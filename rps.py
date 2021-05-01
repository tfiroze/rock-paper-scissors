import random
def comp():
    complist=['rock','paper','scissors']
    n=random.randint(0,2)
    return complist[n]

def userinput():
    x=input("Enter your choice [rock,paper,scissors] \n")
    x=x.lower()
    if x=='rock'or x=='paper' or x=='scissors':
        return x
    else:
        return("Wrong Input")
        userinput()
        
def score(a,b):
    
     print('User = ',a,'Comp = ',b)

def checkwin(a,b,c):
    if a==c:
        print('CONGARATULATIONS YOU HAVE WON \n')
        return 0
    if b==c:
        print('GAME OVER \n')
        return 0
        
i=0
i=int(i)
j=0
j=int(j)
flag=1
n=input("Enter the winning score")
n=int(n)

while flag!=0:
    l=userinput()
    k=comp()
    print("User chose ",l)
    if(l!='Wrong Input'):
        print("Comp chose ",k)
        if(l=='rock'and k=='scissors'):
            i+=1        
            score(i,j)
        elif(l=='paper'and k=='rock'):
            i+=1        
            score(i,j)
        elif(l=='scissors'and k=='paper'):
            i+=1        
            score(i,j)
        elif(k=='scissors'and l=='paper'):
            j+=1        
            score(i,j)
        elif(k=='paper'and l=='rock'):
            j+=1        
            score(i,j)
        elif(k=='rock'and l=='scissors'):
            j+=1                    
            score(i,j)
        else:
            print("Draw")
            score(i,j)
    flag=checkwin(i,j,n)      

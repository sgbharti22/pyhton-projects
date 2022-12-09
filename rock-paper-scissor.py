from tkinter import *
from PIL import Image,ImageTk
from  random import *

root=Tk()
root.title("ROCK-PAPER-SCISSOR")
root.config(background="#ABEBC6")

#user 1=computer    user2=player
r_img=ImageTk.PhotoImage(Image.open("r.png"))
p_img=ImageTk.PhotoImage(Image.open("p.png"))
s_img=ImageTk.PhotoImage(Image.open("s.png"))

comp=Label(root, image=s_img, bg="#ABEBC6")
user=Label(root, image=s_img, bg="#ABEBC6")
comp.grid(row=1,column=0)
user.grid(row=1,column=4)

#for comp
l=["rock","paper","scissor"]

msg=Label(root,font=50,bg="#ABEBC6")
msg.grid(row=3,column=2)
u1l=Label(root,text=0,font=100,bg="#ABEBC6",fg="red")
u2l=Label(root,text=0,font=100,bg="#ABEBC6",fg="red")
u1l.grid(row=1,column=1)
u2l.grid(row=1,column=3)


u1ind=Label(root,font=50,text="COMPUTER",bg="#ABEBC6").grid(row=0,column=1)
u2ind=Label(root,font=50,text="PLAYER",bg="#ABEBC6").grid(row=0,column=3)

def updateMessage(x):
    msg['text']=x

def updateCompScore():
    score=int(u1l["text"])
    score=score+1
    u1l["text"]=str(score)

def updateUserScore():
    score = int(u2l["text"])
    score=score+1
    u2l["text"]=str(score)




def checkwin(comp,user):
    if comp==user:
        updateMessage("Its a tie!!!")
    elif user=="rock":
        if comp=="paper":
            updateMessage("you loose!!")
            updateCompScore()
        else:
            updateMessage("you win!!")
            updateUserScore()
    elif user=="paper":
        if comp=="scissor":
            updateMessage("you loose!!")
            updateCompScore()
        else:
            updateMessage("you win!!")
            updateUserScore()
    elif user=="scissor":
        if comp=="rock":
            updateMessage("you loose!!")
            updateCompScore()
        else:
            updateMessage("you win!!")
            updateUserScore()
    else:
        pass


def updateChoice(x):
    #for comp
    y=choice(l)
    if y=='rock':
        comp.configure(image=r_img)
    elif y =='paper':
        comp.configure(image=p_img)
    else:
        comp.configure(image=s_img)

    # for user
    if x =='rock':
        user.configure(image=r_img)
    elif x =='paper':
        user.configure(image=p_img)
    else:
        user.configure(image=s_img)
    checkwin(y,x)

rock=Button(root,width=20,height=2,text="ROCK",bg="blue",fg="white",command = lambda: updateChoice("rock")).grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",bg="red",fg="white",command = lambda: updateChoice("paper")).grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text="SCISSOR",bg="purple",fg="white",command = lambda: updateChoice("scissor")).grid(row=2,column=3)

root.mainloop()
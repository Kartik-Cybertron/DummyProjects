from tkinter import *

root = Tk()
root.geometry("400x600+0+0")
root.title("Restaurant Management System")

text_Input = StringVar()
opt = ""

def btnClick(num):
    global opt
    opt = opt + str(num)
    text_Input.set(opt)

def cleardisplay():
    global opt
    opt=""
    text_Input.set("")

def btnEqual():
    global opt
    sumup = str(eval(opt))
    text_Input.set(sumup)
    opt = ""
    

    # Tops
tops = Frame(root,width = 500,bg="powder blue",relief=SUNKEN)
tops.pack(side=TOP)
    
f2 = Frame(root,width=200,height=700,relief=SUNKEN) #bg="powder blue",
f2.pack(side=LEFT)

# title
lblInfo=Label(tops,font=('arial',50,'bold'),text="Calculator",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

txtDisplay = Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=10,insertwidth=4,bg="powder blue" ,justify='left')
txtDisplay.grid(row=0,columnspan=5)

# display numeric buttons
btn1=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),text=1,bg="powder blue" ,
                             command=lambda : btnClick(1)).grid(row=2,column=0)
btn2=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),text=2,bg="powder blue" ,
                             command=lambda : btnClick(2)).grid(row=2,column=1)
btn3=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),text=3,bg="powder blue" ,
                             command=lambda : btnClick(3)).grid(row=2,column=2)

btn4=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),text=4,bg="powder blue" ,
                             command=lambda : btnClick(4)).grid(row=3,column=0)
btn5=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),text=5,bg="powder blue" ,
                             command=lambda : btnClick(5)).grid(row=3,column=1)
btn6=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),text=6,bg="powder blue" ,
                             command=lambda : btnClick(6)).grid(row=3,column=2)

btn7=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),text=7,bg="powder blue" ,
                             command=lambda : btnClick(7)).grid(row=4,column=0)
btn8=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),text=8,bg="powder blue" ,
                             command=lambda : btnClick(8)).grid(row=4,column=1)
btn9=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),text=9,bg="powder blue" ,
                             command=lambda : btnClick(9)).grid(row=4,column=2)

btn0=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),text=0,bg="powder blue" ,
                             command=lambda : btnClick(0)).grid(row=5,column=1)

# special characters buttons
addbtn=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="powder blue" ,
                             command=lambda : btnClick("+")).grid(row=2,column=3)

subbtn=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),text="-",bg="powder blue" ,
                             command=lambda : btnClick("-")).grid(row=3,column=3)

mulbtn=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="powder blue" ,
                             command=lambda : btnClick("*")).grid(row=4,column=3)

divbtn=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),text="/",bg="powder blue" ,
                             command=lambda : btnClick("/")).grid(row=5,column=3)

eqbtn=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="powder blue" ,
                             command=btnEqual).grid(row=5,column=2)

clbtn=Button(f2,padx=15,pady=15,bd=8,fg="black",font=('arial',20,'bold'),text="C",bg="powder blue" ,
                             command=cleardisplay).grid(row=5,column=0)

root.mainloop()
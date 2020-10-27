from tkinter import *
import random
import time

root = Tk()
root.geometry("1300x600+0+0")
root.title("Restaurant Management System")

text_Input = StringVar()
opt = ""

rand=StringVar()
fries=StringVar()
burger=StringVar()
chicken_burger=StringVar()
cheese_burger=StringVar()
filet=StringVar()
service=StringVar()
drinks=StringVar()
tax=StringVar()
cost=StringVar()
subtot=StringVar()
tot=StringVar()

# Tops
tops = Frame(root,width = 1300,height=50,bg="powder blue",relief=SUNKEN)
tops.pack(side=TOP)

# frames
f1 = Frame(root,width=800,height=700,relief=SUNKEN) #bg="powder blue",
f1.pack(side=LEFT)

f2 = Frame(root,width=300,height=700,relief=SUNKEN) #bg="powder blue",
f2.pack(side=RIGHT)

# time
localTime=time.asctime(time.localtime(time.time()))


# title
lblInfo=Label(tops,font=('arial',50,'bold'),text="Restaurant Management System",fg="Steel Blue",
                            bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(tops,font=('arial',10,'bold'),text=localTime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)


# calculator
def btnClick(num):
    global opt
    opt = opt + str(num)
    text_Input.set(opt)

def cleardisplay():
    global opt
    opt.set("")
    text_Input.set("")

def btnEqual():
    global opt
    sumup = str(eval(opt))
    text_Input.set(sumup)
    opt = ""
    
def Ref():
    x=random.randint(12908,500876)
    randRef=str(x)
    rand.set(randRef)

    CoF= float(fries.get())
    CoBr=float(burger.get())
    CoChiB=float(chicken_burger.get())
    CoChsB=float(cheese_burger.get())
    CoFi=float(filet.get())
    CoD=float(drinks.get())

    CostofFries = CoF * 70
    CostofBurger= CoBr * 99
    CostofChiBurger= CoChiB * 175
    CostofChsBurger= CoChsB * 155
    CostofFilet= CoFi * 200
    CostofDrink= CoD * 50

    costofMeal="Rs.",str('%.2f' % (CostofFries+CostofBurger+CostofChiBurger+CostofFilet+
                                CostofChsBurger+CostofDrink))

    payTax=((CostofFries+CostofBurger+CostofChiBurger+CostofFilet+CostofChsBurger+CostofDrink) * 0.2)

    totcost=(CostofFries+CostofBurger+CostofChiBurger+CostofFilet+CostofChsBurger+CostofDrink)

    serTax=((CostofFries+CostofBurger+CostofChiBurger+CostofFilet+CostofChsBurger+CostofDrink) /99)

    serv="Rs.",str('%.2f' % serTax)

    ovr_allCost="Rs.",str('%.2f' % (payTax+totcost+serTax))
    paidTax="Rs.",str('%.2f' % payTax)

    service.set(serv)
    cost.set(costofMeal)
    tax.set(paidTax)
    subtot.set(costofMeal)
    tot.set(ovr_allCost)

def qexit():
    root.destroy()

def reset():
    rand.set("")
    fries.set("")
    burger.set("")
    chicken_burger.set("")
    cheese_burger.set("")
    filet.set("")
    service.set("")
    drinks.set("")
    tax.set("")
    cost.set("")
    subtot.set("")
    tot.set("")



txtDisplay = Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,
                             bg="powder blue" ,justify='right')
txtDisplay.grid(columnspan=4)

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

# Labels and textboxes


lblref=Label(f1,font=('arial',16,'bold'),text="Reference",bd=16,anchor='w')
lblref.grid(row=0,column=0)
txtref=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth = 4,
                        bg="#ffffff", justify='right')
txtref.grid(row=0,column=1)


lblfries=Label(f1,font=('arial',16,'bold'),text="Fries",bd=16,anchor='w')
lblfries.grid(row=1,column=0)
txtfries=Entry(f1,font=('arial',16,'bold'),textvariable=fries,bd=10,insertwidth = 4,
                        bg="#ffffff", justify='right')
txtfries.grid(row=1,column=1)

lblburger=Label(f1,font=('arial',16,'bold'),text="Burger",bd=16,anchor='w')
lblburger.grid(row=2,column=0)
txtburger=Entry(f1,font=('arial',16,'bold'),textvariable=burger,bd=10,insertwidth = 4,
                        bg="#ffffff", justify='right')
txtburger.grid(row=2,column=1)

lbl_chiburger=Label(f1,font=('arial',16,'bold'),text="Chicken Burger",bd=16,anchor='w')
lbl_chiburger.grid(row=3,column=0)
txt_chiburger=Entry(f1,font=('arial',16,'bold'),textvariable=chicken_burger,bd=10,insertwidth = 4,
                        bg="#ffffff", justify='right')
txt_chiburger.grid(row=3,column=1)

lbl_chsburger=Label(f1,font=('arial',16,'bold'),text="Cheese Burger",bd=16,anchor='w')
lbl_chsburger.grid(row=4,column=0)
txtchsburger=Entry(f1,font=('arial',16,'bold'),textvariable=cheese_burger,bd=10,insertwidth = 4,
                        bg="#ffffff", justify='right')
txtchsburger.grid(row=4,column=1)

lblfilet=Label(f1,font=('arial',16,'bold'),text="Filet",bd=16,anchor='w')
lblfilet.grid(row=5,column=0)
txtfilet=Entry(f1,font=('arial',16,'bold'),textvariable=filet,bd=10,insertwidth = 4,
                        bg="#ffffff", justify='right')
txtfilet.grid(row=5,column=1)

lbldrinks=Label(f1,font=('arial',16,'bold'),text="Drinks",bd=16,anchor='w')
lbldrinks.grid(row=0,column=2)
txtdrinks=Entry(f1,font=('arial',16,'bold'),textvariable=drinks,bd=10,insertwidth = 4,
                        bg="#ffffff", justify='right')
txtdrinks.grid(row=0,column=3)

lbltax=Label(f1,font=('arial',16,'bold'),text="Tax",bd=16,anchor='w')
lbltax.grid(row=1,column=2)
txttax=Entry(f1,font=('arial',16,'bold'),textvariable=tax,bd=10,insertwidth = 4,
                        bg="#ffffff", justify='right')
txttax.grid(row=1,column=3)

lblcost=Label(f1,font=('arial',16,'bold'),text="Cost",bd=16,anchor='w')
lblcost.grid(row=2,column=2)
txtcost=Entry(f1,font=('arial',16,'bold'),textvariable=cost,bd=10,insertwidth = 4,
                        bg="#ffffff", justify='right')
txtcost.grid(row=2,column=3)

lblserv=Label(f1,font=('arial',16,'bold'),text="Service Charge",bd=16,anchor='w')
lblserv.grid(row=3,column=2)
txtserv=Entry(f1,font=('arial',16,'bold'),textvariable=service,bd=10,insertwidth = 4,
                        bg="#ffffff", justify='right')
txtserv.grid(row=3,column=3)

lblsubtot=Label(f1,font=('arial',16,'bold'),text="Sub-Total",bd=16,anchor='w')
lblsubtot.grid(row=4,column=2)
txtsubtot=Entry(f1,font=('arial',16,'bold'),textvariable=subtot,bd=10,insertwidth = 4,
                        bg="#ffffff", justify='right')
txtsubtot.grid(row=4,column=3)

lbltot=Label(f1,font=('arial',16,'bold'),text="Total",bd=16,anchor='w')
lbltot.grid(row=5,column=2)
txttot=Entry(f1,font=('arial',16,'bold'),textvariable=tot,bd=10,insertwidth = 4,
                        bg="#ffffff", justify='right')
txttot.grid(row=5,column=3)

btntot=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,
                    text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)

btnexit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,
                    text="Exit",bg="powder blue",command=qexit).grid(row=7,column=2)

btnreset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,
                    text="Reset",bg="powder blue",command=reset).grid(row=7,column=3)


root.mainloop()
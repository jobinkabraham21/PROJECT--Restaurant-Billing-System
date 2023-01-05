from tkinter import*
import random
import time

wd = Tk()
wd.geometry("1300x720")

wd.title("Restaurant Billing System")
Tops = Frame(wd,width = 1000,height=50)
Tops.pack(side=TOP)

frame1 = Frame(wd,width = 900,height=700,relief=SUNKEN)
frame1.pack(side=LEFT)

frame2 = Frame(wd ,width = 400,height=500,bg="BLACK",relief=SUNKEN)
frame2.pack(side=TOP)
localtime=time.asctime(time.localtime(time.time()))
labelinformation = Label(Tops, font=('aria',30,'bold'),text="Restaurant Billing System",fg="TOMATO",bd=10,anchor='w')
labelinformation.grid(row=0,column=0)
labelinformation = Label(Tops, font=('aria',20,),text=localtime,fg="BLUE",anchor=W)
labelinformation.grid(row=1,column=0)

text_Input=StringVar()
operator =""

textdisplay = Entry(frame2,font=('ariel' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="KHAKI",justify='right')
textdisplay.grid(columnspan=4)

def  buttonclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""

def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cof=float(Coffee.get())
    bf= float(Breakfast.get())
    hb=float(Hamburger.get())
    pz=float(Pizza.get())
    cb=float(Biriyani.get())
    codr=float(Drinks.get())

    costofcoffee = cof*15
    costofbreakfast= bf*50
    costofhamburger = hb*30
    costofpizza = pz*40
    costofbiriyani = cb*140
    costofdrinks = codr*30

    costofmeal = "Rs.",str('%.2f'% (costofcoffee + costofbreakfast + costofhamburger + costofpizza + costofbiriyani + costofdrinks))
    PayTax=((costofcoffee +  costofbreakfast + costofhamburger + costofpizza +  costofbiriyani + costofdrinks)*0.33)
    Totalcost=(costofcoffee +  costofbreakfast + costofhamburger + costofpizza  + costofbiriyani + costofdrinks)
    Ser_Charge=((costofcoffee +  costofbreakfast + costofhamburger + costofpizza + costofbiriyani + costofdrinks)/99)
    Service="Rs.",str('%.2f'% Ser_Charge)
    OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="Rs.",str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Total.set(OverAllCost)


def qexit():
    wd.destroy()

def reset():
    rand.set("")
    Coffee.set("")
    Breakfast.set("")
    Hamburger.set("")
    Pizza.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Biriyani.set("")


button7=Button(frame2,padx=14,pady=14,bd=4, fg="RED", font=('ariel', 20 ,'bold'),text="7",bg="black", command=lambda: buttonclick(7) )
button7.grid(row=2,column=0)

button8=Button(frame2,padx=14,pady=14,bd=4, fg="RED", font=('ariel', 20 ,'bold'),text="8",bg="black", command=lambda: buttonclick(8) )
button8.grid(row=2,column=1)

button9=Button(frame2,padx=14,pady=14,bd=4, fg="RED", font=('ariel', 20 ,'bold'),text="9",bg="black", command=lambda: buttonclick(9) )
button9.grid(row=2,column=2)

Addition=Button(frame2,padx=14,pady=14,bd=4, fg="BLACK", font=('ariel', 20 ,'bold'),text="+",bg="RED", command=lambda: buttonclick("+") )
Addition.grid(row=2,column=3)

button4=Button(frame2,padx=14,pady=14,bd=4, fg="RED", font=('ariel', 20 ,'bold'),text="4",bg="black", command=lambda: buttonclick(4) )
button4.grid(row=3,column=0)

button5=Button(frame2,padx=14,pady=14,bd=4, fg="RED", font=('ariel', 20 ,'bold'),text="5",bg="black", command=lambda: buttonclick(5) )
button5.grid(row=3,column=1)

button6=Button(frame2,padx=14,pady=14,bd=4, fg="RED", font=('ariel', 20 ,'bold'),text="6",bg="black", command=lambda: buttonclick(6) )
button6.grid(row=3,column=2)

substraction=Button(frame2,padx=14,pady=14,bd=4, fg="BLACK", font=('ariel', 20 ,'bold'),text="-",bg="RED", command=lambda: buttonclick("-") )
substraction.grid(row=3,column=3)

button1=Button(frame2,padx=14,pady=14,bd=4, fg="RED", font=('ariel', 20 ,'bold'),text="1",bg="black", command=lambda: buttonclick(1) )
button1.grid(row=4,column=0)

button2=Button(frame2,padx=14,pady=14,bd=4, fg="RED", font=('ariel', 20 ,'bold'),text="2",bg="black", command=lambda: buttonclick(2) )
button2.grid(row=4,column=1)

button3=Button(frame2,padx=14,pady=14,bd=4, fg="RED", font=('ariel', 20 ,'bold'),text="3",bg="black", command=lambda: buttonclick(3) )
button3.grid(row=4,column=2)

multiply=Button(frame2,padx=14,pady=14,bd=4, fg="BLACK", font=('ariel', 20 ,'bold'),text="*",bg="RED", command=lambda: buttonclick("*") )
multiply.grid(row=4,column=3)

button0=Button(frame2,padx=14,pady=14,bd=4, fg="RED", font=('ariel', 20 ,'bold'),text="0",bg="black", command=lambda: buttonclick(0) )
button0.grid(row=5,column=0)

buttonc=Button(frame2,padx=14,pady=14,bd=4, fg="RED", font=('ariel', 20 ,'bold'),text="C",bg="black", command=clrdisplay)
buttonc.grid(row=5,column=1)

buttonequal=Button(frame2,padx=14,pady=14,bd=4,width = 16, fg="BLACK", font=('ariel', 20 ,'bold'),text="=",bg="RED",command=eqals)
buttonequal.grid(columnspan=4)

Decimal=Button(frame2,padx=14,pady=14,bd=4,fg="RED", font=('ariel', 20 ,'bold'),text=".",bg="black", command=lambda: buttonclick(".") )
Decimal.grid(row=5,column=2)

Division=Button(frame2,padx=14,pady=14,bd=4, fg="BLACK", font=('ariel', 20 ,'bold'),text="/",bg="RED", command=lambda: buttonclick("/") )
Division.grid(row=5,column=3)

status = Label(frame2,font=('aria', 15, 'bold'),fg="RED",width = 16, text="JOBIN K ABRAHAM",bg="BLACK",bd=2,relief=FLAT)
status.grid(row=7,columnspan=7)

rand = StringVar()
Coffee = StringVar()
Breakfast = StringVar()
Hamburger = StringVar()
Pizza = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Biriyani = StringVar()


labelref = Label(frame1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="black",bd=10,)
labelref.grid(row=0,column=0)
textref = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="SILVER" ,justify='right')
textref.grid(row=0,column=1)

labelCoffee = Label(frame1, font=('aria' , 16, 'bold'), text="Coffee", fg="black", bd=10,)
labelCoffee.grid(row=1, column=0)
textcoffee = Entry(frame1, font=('ariel' , 16, 'bold'), textvariable=Coffee, bd=6, insertwidth=4, bg="SILVER", justify='right')
textcoffee.grid(row=1, column=1)

labelBreakfast = Label(frame1, font=('aria' , 16, 'bold'), text="Breakfast", fg="black", bd=10,)
labelBreakfast.grid(row=2, column=0)
textBreakfast = Entry(frame1, font=('ariel' , 16, 'bold'), textvariable=Breakfast, bd=6, insertwidth=4, bg="SILVER", justify='right')
textBreakfast.grid(row=2, column=1)


labelHamburger = Label(frame1, font=( 'aria' ,16, 'bold' ),text="Hamburger",fg="black",bd=10)
labelHamburger.grid(row=3,column=0)
textHamburger = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=Hamburger , bd=6,insertwidth=4,bg="SILVER" ,justify='right')
textHamburger.grid(row=3,column=1)

labelPizza = Label(frame1, font=( 'aria' ,16, 'bold' ),text="Pizza",fg="black",bd=10)
labelPizza.grid(row=4,column=0)
textPizza = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=Pizza , bd=6,insertwidth=4,bg="SILVER" ,justify='right')
textPizza.grid(row=4,column=1)

labelBiriyani = Label(frame1, font=( 'aria' ,16, 'bold' ),text="Chicken Biriyani",fg="black",bd=10)
labelBiriyani.grid(row=5,column=0)
textBiriyani = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=Biriyani , bd=6,insertwidth=4,bg="SILVER" ,justify='right')
textBiriyani.grid(row=5,column=1)

labelDrinks = Label(frame1, font=( 'aria' ,16, 'bold' ),text="Cold Drinks",fg="black",bd=10)
labelDrinks.grid(row=6,column=0)
textDrinks = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="SILVER" ,justify='right')
textDrinks.grid(row=6,column=1)

labelcost = Label(frame1, font=( 'aria' ,16, 'bold' ),text="Cost",fg="black",bd=10)
labelcost.grid(row=2,column=2)
textcost = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="SILVER" ,justify='right')
textcost.grid(row=2,column=3)

labelService_Charge = Label(frame1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="black",bd=10)
labelService_Charge.grid(row=3,column=2)
textService_Charge = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="SILVER" ,justify='right')
textService_Charge.grid(row=3,column=3)

labelTax = Label(frame1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="black",bd=10)
labelTax.grid(row=4,column=2)
textTax = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="SILVER" ,justify='right')
textTax.grid(row=4,column=3)


labelTotal = Label(frame1, font=( 'aria' ,16, 'bold' ),text="Total",fg="RED",bd=10)
labelTotal.grid(row=5,column=2)
textTotal = Entry(frame1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg= "KHAKI" ,justify='right')
textTotal.grid(row=5,column=3)



buttonTotal=Button(frame1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="GREEN",command=Ref)
buttonTotal.grid(row=8, column=1)

buttonreset=Button(frame1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="BLUE",command=reset)
buttonreset.grid(row=8, column=2)

buttonexit=Button(frame1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="RED",command=qexit)
buttonexit.grid(row=8, column=3)

def price():
    ws = Tk()
    ws.geometry("300x250")
    ws.title("Item Price List")
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="ITEM", fg="black")
    labelinformation.grid(row=0, column=0)

    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="PRICE", fg="black")
    labelinformation.grid(row=0, column=3)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="Coffee", fg="blue")
    labelinformation.grid(row=1, column=0)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="15", fg="red")
    labelinformation.grid(row=1, column=3)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="Breakfast", fg="blue")
    labelinformation.grid(row=2, column=0)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="50", fg="red")
    labelinformation.grid(row=2, column=3)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="Hamburger", fg="blue")
    labelinformation.grid(row=3, column=0)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="30", fg="red")
    labelinformation.grid(row=3, column=3)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="Pizza", fg="blue")
    labelinformation.grid(row=4, column=0)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="40", fg="red")
    labelinformation.grid(row=4, column=3)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="Chicken Biriyani", fg="blue")
    labelinformation.grid(row=5, column=0)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="140", fg="red")
    labelinformation.grid(row=5, column=3)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="Cold Drinks", fg="blue")
    labelinformation.grid(row=6, column=0)
    labelinformation = Label(ws, font=('aria', 15, 'bold'), text="30", fg="red")
    labelinformation.grid(row=6, column=3)

buttonprice=Button(frame1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="YELLOW",command=price)
buttonprice.grid(row=8, column=0)

wd.mainloop()

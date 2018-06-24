%config IPCompleter.greedy=True
from tkinter import*
import random
import time;
import datetime
import psycopg2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A6
from tkinter import messagebox
from decimal import Decimal

root = Tk()
root.geometry("1350x750+0+0")
root.title("Café Management Systems")
root.configure(background='#EEE8CD')

Tops = Frame(root, width = 1350,height = 100, bd=10, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 900,height = 650, bd=8, relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root, width = 440,height = 650, bd=8, relief="raise")
f2.pack(side=RIGHT)

ft2 = Frame(f2, width = 440,height = 650, bd=12, relief="raise")
ft2.pack(side=TOP)
fb2 = Frame(f2, width = 440,height = 50, bd=16, relief="raise")
fb2.pack(side=BOTTOM)

f1a = Frame(f1, width = 900,height = 330, bd=10, relief="raise")
f1a.pack(side=TOP)
f2a = Frame(f1, width = 900,height = 320, bd=10, relief="raise")
f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width = 400, height = 330, bd=8, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width = 400, height = 330, bd=8, relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width = 450,height = 330, bd=14, relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width = 450,height = 330, bd=14, relief="raise")
f2ab.pack(side=RIGHT)

Tops.configure(background='#8B7355')
f1.configure(background='black')
f2.configure(background='black')

#=======================CostofItem====================================
def CostofItem():
    Item1 = float(E_Latte.get())
    Item2 = float(E_Espresso.get())
    Item3 = float(E_Iced_Latte.get())
    Item4 = float(E_Vale_Coffee.get())
    Item5 = float(E_Cappuccino.get())
    Item6 = float(E_African_Coffee.get())
    Item7 = float(E_American_Coffee.get())
    Item8 = float(E_Iced_Cappuccino.get())

    Item9 = float(E_Coffee_Cake.get())
    Item10 = float(E_Red_Velvet_Cake.get())
    Item11 = float(E_Black_Forest_Cake.get())
    Item12 = float(E_Boston_Cream_Cake.get())
    Item13 = float(E_Lagos_Chocolate_Cake.get())
    Item14 = float(E_Kilburn_Chocolate_Cake.get())
    Item15 = float(E_Carlton_Chocolate_Cake.get())
    Item16 = float(E_Queen_Park_Chocolate_Cake.get())
    
#Calculate
    PriceofDrinks = (Item1 * 1.99) + (Item2 * 1.75) + (Item3 * 2.05) \
                            + (Item4 * 1.89) + (Item5 * 1.99) + (Item6 * 2.99) + (Item7 * 2.39) + (Item8 * 1.29)

    PriceofCakes = (Item9 * 1.35) + (Item10 * 2.29) + (Item11 * 1.99) \
                    + (Item12 * 1.49) + (Item13 * 1.8) + (Item14 * 1.67) + (Item15 * 1.6) + (Item16 * 1.99)
    
    It1 = Item1 * 1.99
    It2 = Item2 * 1.75    
    It3 = Item3 * 2.05
    It4 = Item4 * 1.89
    It5 = Item5 * 1.99
    It6 = Item6 * 2.99
    It7 = Item7 * 2.39
    It8 = Item8 * 1.29
    It9 = Item9 * 1.35
    It10 = Item10 * 2.29
    It11 = Item11 * 1.99
    It12 = Item12 * 1.49    
    It13 = Item13 * 1.8
    It14 = Item14 * 1.67    
    It15 = Item15 * 1.6
    It16 = Item16 * 1.99   
    
    Itm1.set(It1)
    Itm2.set(It2)
    Itm3.set(It3)
    Itm4.set(It4)
    Itm5.set(It5)
    Itm6.set(It6)
    Itm7.set(It7)
    Itm8.set(It8)
    Itm9.set(It9)
    Itm10.set(It10)
    Itm11.set(It11)
    Itm12.set(It12)
    Itm13.set(It13)
    Itm14.set(It14)
    Itm14.set(It14)
    Itm15.set(It15)
    Itm16.set(It16)
    
    DrinksPrice = "$", str('%.2f' %(PriceofDrinks))
    CakesPrice = "$", str('%.2f' %(PriceofCakes))
    CostofCakes.set(CakesPrice)
    CostofDrinks.set(DrinksPrice)
    SC = "$", str('%.2f' %(0.59))

    SubTotalofITEMS = "$", str('%.2f' %(PriceofDrinks + PriceofCakes + 0.59))

    Tax = "$", str('%.2f' %((PriceofDrinks + PriceofCakes + 0.59) * 0.15))

    TT = "$", str('%.2f' %((PriceofDrinks + PriceofCakes + 0.59) * 0.15))
    TT1 = (PriceofDrinks + PriceofCakes + 0.59) * 0.15
    TC = "$", str('%.2f' %(PriceofDrinks + PriceofCakes + 0.59 + TT1))  
    
    PaidTax.set(Tax)
    ServiceCharge.set(SC)
    SubTotal.set(SubTotalofITEMS)
    TotalCost.set(TC)    

    DrinksPrice1 = PriceofDrinks
    CakesPrice1 = PriceofCakes
    SC1 = 1.59
    SubTotalofITEMS1 = PriceofDrinks + PriceofCakes + 0.59
    Tax1 = ((PriceofDrinks + PriceofCakes + 0.59) * 0.15)
    TC1 = PriceofDrinks + PriceofCakes + 0.59 + TT1
    
    CostofCakes1.set(CakesPrice1)
    CostofDrinks1.set(DrinksPrice1)
    ServiceCharge1.set(SC1)
    PaidTax1.set(Tax1)
    SubTotal1.set(SubTotalofITEMS1)
    TotalCost1.set(TC1) 
    
    
def qExit():
    qExit = messagebox.askyesno("Quit System", "Do you want to quit?")
    if qExit > 0:
        root.destroy() 
        return        
    
def Reset(): 
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofCakes.set("")
    ServiceCharge.set("")    
    txtReceipt.delete("1.0",END)

    E_Latte.set("0")
    E_Espresso.set("0")
    E_Iced_Latte.set("0")
    E_Vale_Coffee.set("0")
    E_Cappuccino.set("0")
    E_African_Coffee.set("0")
    E_American_Coffee.set("0")
    E_Iced_Cappuccino.set("0")

    E_Coffee_Cake.set("0")
    E_Red_Velvet_Cake.set("0")
    E_Black_Forest_Cake.set("0")
    E_Boston_Cream_Cake.set("0")
    E_Lagos_Chocolate_Cake.set("0")
    E_Kilburn_Chocolate_Cake.set("0")
    E_Carlton_Chocolate_Cake.set("0")
    E_Queen_Park_Chocolate_Cake.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtLatte.configure(state=DISABLED)
    txtEspresso.configure(state=DISABLED)
    txtIced_Latte.configure(state=DISABLED)
    txtVale_Coffee.configure(state=DISABLED)
    txtCappuccino.configure(state=DISABLED)
    txtAfrican_Coffee.configure(state=DISABLED)
    txtAmerican_Coffee.configure(state=DISABLED)
    txtIced_Cappuccino.configure(state=DISABLED)
    txtCoffee_Cake.configure(state=DISABLED)
    txtRed_Velvet_Cake.configure(state=DISABLED)
    txtBlack_Forest_Cake.configure(state=DISABLED)
    txtBoston_Cream_Cake.configure(state=DISABLED)
    txtLagos_Chocolate_Cake.configure(state=DISABLED)
    txtKilburn_Chocolate_Cake.configure(state=DISABLED)
    txtCarlton_Chocolate_Cake.configure(state=DISABLED)
    txtQueen_Park_Chocolate_Cake.configure(state=DISABLED)

def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL"+ randomRef)
    
    
    txtReceipt.insert(END, 'Receipt Ref:\t\t\t'+ Receipt_Ref.get() +'\t\t'+ DateofOrder.get()+"\n")
    txtReceipt.insert(END,'Items\t\t\t\t'+ "Cost of Items \n\n")
    txtReceipt.insert(END,'Latte: \t\t\t\t\t'+ E_Latte.get()+ "\n")
    txtReceipt.insert(END,'Espresso: \t\t\t\t\t'+ E_Espresso.get()+ "\n")
    txtReceipt.insert(END,'Iced Latte: \t\t\t\t\t'+ E_Iced_Latte.get()+ "\n")
    txtReceipt.insert(END,'Vale Coffee: \t\t\t\t\t'+ E_Vale_Coffee.get()+ "\n")
    txtReceipt.insert(END,'Cappuccino: \t\t\t\t\t' + E_Cappuccino.get()+ "\n")
    txtReceipt.insert(END,'African Coffee: \t\t\t\t\t' + E_African_Coffee.get()+ "\n")
    txtReceipt.insert(END,'American Coffee: \t\t\t\t\t' + E_American_Coffee.get()+ "\n")
    txtReceipt.insert(END,'Iced Cappuccino: \t\t\t\t\t' + E_Iced_Cappuccino.get()+ "\n")
    txtReceipt.insert(END,'Coffee Cake: \t\t\t\t\t' + E_Coffee_Cake.get()+ "\n")
    txtReceipt.insert(END,'Red Velvet Cake: \t\t\t\t\t' + E_Red_Velvet_Cake.get()+ "\n")
    txtReceipt.insert(END,'Black Forest Cake: \t\t\t\t\t' + E_Black_Forest_Cake.get()+ "\n")
    txtReceipt.insert(END,'Boston Cream Cake: \t\t\t\t\t' + E_Boston_Cream_Cake.get()+ "\n")
    txtReceipt.insert(END,'Lagos Chocolate Cake: \t\t\t\t\t' + E_Lagos_Chocolate_Cake.get()+ "\n")
    txtReceipt.insert(END,'Kilburn Chocolate Cake: \t\t\t\t\t' + E_Kilburn_Chocolate_Cake.get()+ "\n")
    txtReceipt.insert(END,'Carlton Hill Chocolate Cake: \t\t\t\t\t' + E_Carlton_Chocolate_Cake.get()+ "\n")
    txtReceipt.insert(END,'Queens Park Chocolate Cake: \t\t\t\t\t' + E_Queen_Park_Chocolate_Cake.get()+ "\n")   
    txtReceipt.insert(END,'Cost of Drinks: \t\t' + CostofDrinks.get()+ '\tService Charge:\t\t' + ServiceCharge.get()+"\n")  
    txtReceipt.insert(END,'Cost of Cakes: \t\t' + CostofCakes.get()+ '\tTax Paid:\t\t' + PaidTax.get() +"\n")
    txtReceipt.insert(END,'Sub Total:\t\t'+ SubTotal.get()+'\tTotal Cost:\t\t' + TotalCost.get() + "\n")    
    
#==========================================save to pdf=========================================================== 
    ldate = DateofOrder.get()[:2] + DateofOrder.get()[3:5] + DateofOrder.get()[6:10]
    filename1 = Receipt_Ref.get() + '_' + ldate + '.pdf' 
    c = canvas.Canvas(filename1, pagesize=A6)
    c.setFont('Helvetica', 8)
    c.drawString(45,400,"Halal Café")
    c.drawString(20,390,"...It's more than just good food!")
    c.drawString(15,380,"Receipt Ref:")
    c.drawString(65,380,Receipt_Ref.get())
    c.drawString(135,380,DateofOrder.get())
    c.drawString(15,370,"----------------------------------------------------------------")
    c.drawString(15,360,"Latte:")
    c.drawString(135,360,E_Latte.get())
    c.drawString(150,360,Itm1.get())    
    c.drawString(15,350,"Espresso:")
    c.drawString(135,350,E_Espresso.get())
    c.drawString(150,350,Itm2.get())
    c.drawString(15,340,"Iced Latte:")
    c.drawString(135,340,E_Iced_Latte.get())
    c.drawString(150,340,Itm3.get())
    c.drawString(15,330,"Vale Coffee:")
    c.drawString(135,330,E_Vale_Coffee.get())
    c.drawString(150,330,Itm4.get())
    c.drawString(15,320,"Cappuccino:")
    c.drawString(135,320,E_Cappuccino.get())
    c.drawString(150,320,Itm5.get())
    c.drawString(15,310,"African Coffee:")
    c.drawString(135,310,E_African_Coffee.get())
    c.drawString(150,310,Itm6.get())
    c.drawString(15,300,"American Coffee:")
    c.drawString(135,300,E_American_Coffee.get())
    c.drawString(150,300,Itm7.get())
    c.drawString(15,290,"Iced Cappuccino:")
    c.drawString(135,290,E_Iced_Cappuccino.get())
    c.drawString(150,290,Itm8.get())
    c.drawString(15,280,"Coffee Cake:")
    c.drawString(135,280,E_Coffee_Cake.get())
    c.drawString(150,280,Itm9.get())
    c.drawString(15,270,"Red Velvet Cake:")
    c.drawString(135,270,E_Red_Velvet_Cake.get())
    c.drawString(150,270,Itm10.get())
    c.drawString(15,260,"Black Forest Cake:")
    c.drawString(135,260,E_Black_Forest_Cake.get())
    c.drawString(150,260,Itm11.get())
    c.drawString(15,250,"Boston Cream Cake:")
    c.drawString(135,250,E_Boston_Cream_Cake.get())
    c.drawString(150,250,Itm12.get())
    c.drawString(15,240,"Lagos Chocolate Cake:")
    c.drawString(135,240,E_Lagos_Chocolate_Cake.get())
    c.drawString(150,240,Itm13.get())
    c.drawString(15,230,"Kilburn Chocolate Cake:")
    c.drawString(135,230,E_Kilburn_Chocolate_Cake.get())
    c.drawString(150,230,Itm14.get())
    c.drawString(15,220,"Carlton Hill Chocolate Cake:")
    c.drawString(135,220,E_Carlton_Chocolate_Cake.get())
    c.drawString(150,220,Itm15.get())
    c.drawString(15,210,"Queen's Park Chocolate Cake:")
    c.drawString(135,210,E_Queen_Park_Chocolate_Cake.get())
    c.drawString(150,210,Itm16.get())
    c.drawString(15,200,"----------------------------------------------------------------")
    c.drawString(15,190,"Cost of Drinks:")
    c.drawString(75,190,CostofDrinks.get())
    c.drawString(15,180,"Cost of Cakes:")
    c.drawString(75,180,CostofCakes.get())
    c.drawString(15,170,"Sub Total:")
    c.drawString(75,170,SubTotal.get())
    c.drawString(145,190,"Service Charge:")
    c.drawString(208,190,ServiceCharge.get())
    c.drawString(145,180,"Tax Paid:")
    c.drawString(208,180,PaidTax.get())
    c.drawString(145,170,"Total Cost:")
    c.drawString(208,170,TotalCost.get())
    c.showPage()
    c.save()
    
#==========================================PostgreSQL - save to database===========================================================    
    vbl1 = datetime.date.today()
    conn = psycopg2.connect(database = "cafe", user = "admin", password = "admin", host = "127.0.0.1", port = "5432")
    print ("Opened database successfully")

    cur = conn.cursor()
    cur.execute("""INSERT INTO sales.receipt ("ID", "DATE", "LATTE", "ESPRESSO", "ICED_LATTE", "VALE_COFFEE", "CAPPUCCINO",
             "AFRICAN_COFFEE", "AMERICAN_COFFEE", "ICED_CAPPUCCINO", "COFFEE", "RED_VELVET", "BLACK_FOREST", 
             "BOSTON_CREAM", "LAGOS_CHOCOLATE", "KILBURN_CHOCOLATE", "CARLTON_CHOCOLATE", "QUEEN_PARK_CHOCOLATE", 
             "COST_DRINKS", "COST_CAKES", "SERVICE_CHARGE", "PAID_TAX", "SUBTOTAL", "TOTAL_COST") VALUES (%s, %s, 
             %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", 
             (Receipt_Ref.get(), vbl1, E_Latte.get(), E_Espresso.get(), E_Iced_Latte.get(), 
              E_Vale_Coffee.get(), E_Cappuccino.get(), E_African_Coffee.get(), E_American_Coffee.get(), 
              E_Iced_Cappuccino.get(), E_Coffee_Cake.get(), E_Red_Velvet_Cake.get(), E_Black_Forest_Cake.get(),
              E_Boston_Cream_Cake.get(), E_Lagos_Chocolate_Cake.get(), E_Kilburn_Chocolate_Cake.get(), 
              E_Carlton_Chocolate_Cake.get(), E_Queen_Park_Chocolate_Cake.get(), CostofDrinks1.get(), 
              CostofCakes1.get(), ServiceCharge1.get(), PaidTax1.get(), SubTotal1.get(), TotalCost1.get()))

    conn.commit()
    conn.close()     
    
#===============================================Heading=============================================================
lblInfo = Label(Tops, font=('arial',35, 'bold'),text = "Halal Café", bd=12, anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops, font=('arial',12, 'bold'),text = "...It's more than just good food!", bd=12, anchor='w')
lblInfo.grid(row=1,column=6)

#==============================================Calculator==================================================

def chkbutton_value():
    if (var1.get() == 1):
        txtLatte.configure(state=NORMAL)
    elif var1.get()==0:
        txtLatte.configure(state=DISABLED) 
        E_Latte.set("0")
    if (var2.get() == 1):
        txtEspresso.configure(state=NORMAL)
    elif var2.get() == 0:    
        txtEspresso.configure(state=DISABLED)
        E_Espresso.set("0")
    if (var3.get() == 1):
        txtIced_Latte.configure(state=NORMAL)
    elif var3.get() == 0:    
        txtIced_Latte.configure(state=DISABLED)
        E_Iced_Latte.set("0")        
    if (var4.get() == 1):
        txtVale_Coffee.configure(state=NORMAL)
    elif var4.get() == 0:
        txtVale_Coffee.configure(state=DISABLED)
        E_Vale_Coffee.set("0")
    if (var5.get() == 1):
        txtCappuccino.configure(state=NORMAL)
    elif var5.get() == 0:
        txtCappuccino.configure(state=DISABLED)
        E_Cappuccino.set("0") 
    if (var6.get() == 1):
        txtAfrican_Coffee.configure(state=NORMAL)
    elif var6.get() == 0:
        txtAfrican_Coffee.configure(state=DISABLED)
        E_African_Coffee.set("0")   
    if (var7.get() == 1):
        txtAmerican_Coffee.configure(state=NORMAL)
    elif var7.get() == 0:
        txtAmerican_Coffee.configure(state=DISABLED)
        E_American_Coffee.set("0") 
    if (var8.get() == 1):
        txtIced_Cappuccino.configure(state=NORMAL)
    elif var8.get() == 0:
        txtIced_Cappuccino.configure(state=DISABLED)
        E_Iced_Cappuccino.set("0") 
    if (var9.get() == 1):
        txtCoffee_Cake.configure(state=NORMAL)
    elif var9.get() == 0:
        txtCoffee_Cake.configure(state=DISABLED)
        E_Coffee_Cake.set("0") 
    if (var10.get() == 1):
        txtRed_Velvet_Cake.configure(state=NORMAL)
    elif var10.get() == 0:
        txtRed_Velvet_Cake.configure(state=DISABLED)
        E_Red_Velvet_Cake.set("0") 
    if (var11.get() == 1):
        txtBlack_Forest_Cake.configure(state=NORMAL)
    elif var11.get() == 0:
        txtBlack_Forest_Cake.configure(state=DISABLED)
        E_Black_Forest_Cake.set("0") 
    if (var12.get() == 1):
        txtBoston_Cream_Cake.configure(state=NORMAL)
    elif var12.get() == 0:
        txtBoston_Cream_Cake.configure(state=DISABLED)
        E_Boston_Cream_Cake.set("0") 
    if (var13.get() == 1):
        txtLagos_Chocolate_Cake.configure(state=NORMAL)
    elif var13.get() == 0:
        txtLagos_Chocolate_Cake.configure(state=DISABLED)
        E_Lagos_Chocolate_Cake.set("0") 
    if (var14.get() == 1):
        txtKilburn_Chocolate_Cake.configure(state=NORMAL)
    elif var14.get() == 0:
        txtKilburn_Chocolate_Cake.configure(state=DISABLED)
        E_Kilburn_Chocolate_Cake.set("0") 
    if (var15.get() == 1):
        txtCarlton_Chocolate_Cake.configure(state=NORMAL)
    elif var15.get() == 0:
        txtCarlton_Chocolate_Cake.configure(state=DISABLED)
        E_Carlton_Chocolate_Cake.set("0") 
    if (var16.get() == 1):
        txtQueen_Park_Chocolate_Cake.configure(state=NORMAL)
    elif var16.get() == 0:
        txtQueen_Park_Chocolate_Cake.configure(state=DISABLED)
        E_Queen_Park_Chocolate_Cake.set("0")       
        
#-----------------------------------------Variables-------------------------------------------------------
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

# PostgreSQL
PaidTax1 = StringVar()
SubTotal1 = StringVar()
TotalCost1 = StringVar()
CostofCakes1 = StringVar()
CostofDrinks1 = StringVar()
ServiceCharge1 = StringVar()

# Pdf
Itm1 = StringVar()
Itm2 = StringVar()
Itm3 = StringVar()
Itm4 = StringVar()
Itm5 = StringVar()
Itm6 = StringVar()
Itm7 = StringVar()
Itm8 = StringVar()
Itm9 = StringVar()
Itm10 = StringVar()
Itm11 = StringVar()
Itm12 = StringVar()
Itm13 = StringVar()
Itm14 = StringVar()
Itm15 = StringVar()
Itm16 = StringVar()


E_Latte = StringVar()
E_Espresso = StringVar()
E_Iced_Latte = StringVar()
E_Vale_Coffee = StringVar()
E_Cappuccino = StringVar()
E_African_Coffee = StringVar()
E_American_Coffee = StringVar()
E_Iced_Cappuccino = StringVar()

E_Coffee_Cake = StringVar()
E_Red_Velvet_Cake = StringVar()
E_Black_Forest_Cake = StringVar()
E_Boston_Cream_Cake = StringVar()
E_Lagos_Chocolate_Cake = StringVar()
E_Kilburn_Chocolate_Cake = StringVar()
E_Carlton_Chocolate_Cake = StringVar()
E_Queen_Park_Chocolate_Cake = StringVar()

E_Latte.set("0")
E_Espresso.set("0")
E_Iced_Latte.set("0")
E_Vale_Coffee.set("0")
E_Cappuccino.set("0")
E_African_Coffee.set("0")
E_American_Coffee.set("0")
E_Iced_Cappuccino.set("0")

E_Coffee_Cake.set("0")
E_Red_Velvet_Cake.set("0")
E_Black_Forest_Cake.set("0")
E_Boston_Cream_Cake.set("0")
E_Lagos_Chocolate_Cake.set("0")
E_Kilburn_Chocolate_Cake.set("0")
E_Carlton_Chocolate_Cake.set("0")
E_Queen_Park_Chocolate_Cake.set("0")                      

DateofOrder.set(time.strftime("%d/%m/%Y"))
#================================================Drinks========================================================================
Latte = Checkbutton(f1aa, text="Latte \t", variable=var1, onvalue = 1, offvalue = 0, font=('arial',12, 'bold'),command=chkbutton_value).grid(row=0, sticky=W)

Espresso = Checkbutton(f1aa, text="Espresso \t\t", variable=var2, onvalue = 1, offvalue = 0, font=('arial',12, 'bold'),command=chkbutton_value).grid(row=1, sticky=W)

Iced_Latte = Checkbutton(f1aa, text="Iced Latte \t\t", variable=var3, onvalue = 1, offvalue = 0, font=('arial',12, 'bold'),command=chkbutton_value).grid(row=2, sticky=W)

Vale_Coffee = Checkbutton(f1aa, text="Vale Coffee \t\t", variable=var4, onvalue = 1, offvalue = 0, font=('arial',12, 'bold'),command=chkbutton_value).grid(row=3, sticky=W)

Cappuccino = Checkbutton(f1aa, text="Cappuccino \t\t", variable=var5, onvalue = 1, offvalue = 0, font=('arial',12, 'bold'),command=chkbutton_value).grid(row=4, sticky=W)

African_Coffee = Checkbutton(f1aa, text="African Coffee \t\t", variable=var6, onvalue = 1, offvalue = 0, font=('arial',12, 'bold'),command=chkbutton_value).grid(row=5, sticky=W)

American_Coffee = Checkbutton(f1aa, text="American Coffee \t\t", variable=var7, onvalue = 1, offvalue = 0, font=('arial',12, 'bold'),command=chkbutton_value).grid(row=6, sticky=W)

Iced_Cappuccino = Checkbutton(f1aa, text="Iced Cappuccino \t\t", variable=var8, onvalue = 1, offvalue = 0, font=('arial',12, 'bold'),command=chkbutton_value).grid(row=7, sticky=W)

#===============================================Cakes=======================================================================
Coffee_Cake = Checkbutton(f1ab, text="Coffee Cake \t\t", variable=var9, onvalue = 1, offvalue = 0, font=('arial',12, 'bold'),command=chkbutton_value).grid(row=0, sticky=W)

Red_Velvet_Cake = Checkbutton(f1ab, text="Red Velvet Cake \t\t", variable=var10, onvalue = 1, offvalue = 0, font=('arial',12, 'bold'),command=chkbutton_value).grid(row=1, sticky=W)

Black_Forest_Cake = Checkbutton(f1ab, text="Black Forest Cake \t\t", variable=var11, onvalue = 1, offvalue = 0, font=('arial',12, 'bold'),command=chkbutton_value).grid(row=2, sticky=W)

Boston_Cream_Cake = Checkbutton(f1ab, text="Boston Cream Cake \t\t", variable=var12, onvalue = 1, offvalue = 0, font=('arial',12, 'bold'),command=chkbutton_value).grid(row=3, sticky=W)

Lagos_Chocolate_Cake = Checkbutton(f1ab, text="Lagos Chocolate Cake \t\t", variable=var13, onvalue = 1, offvalue = 0, font=('arial',12, 'bold'),command=chkbutton_value).grid(row=4, sticky=W)

Kilburn_Chocolate_Cake = Checkbutton(f1ab, text="Kilburn Chocolate Cake \t\t", variable=var14, onvalue = 1, offvalue = 0, font=('arial',12, 'bold'),command=chkbutton_value).grid(row=5, sticky=W)

Carlton_Hill_Cake = Checkbutton(f1ab, text="Carlton Hill Chocolate Cake \t\t", variable=var15, onvalue = 1, offvalue = 0, font=('arial',12, 'bold'),command=chkbutton_value).grid(row=6, sticky=W)                      

Queen_Park_Cake = Checkbutton(f1ab, text="Queen's Park Chocolate Cake \t\t", variable=var16, onvalue = 1, offvalue = 0, font=('arial',12, 'bold'),command=chkbutton_value).grid(row=7, sticky=W)                                            

#================================Enter Widget for Cake=========================================================
txtCoffee_Cake = Entry(f1ab,font=('arial', 11,'bold'), textvariable=E_Coffee_Cake, bg="pale green", bd=12, width=6, justify='left',state=DISABLED)
txtCoffee_Cake.grid(row=0,column=1)
txtRed_Velvet_Cake = Entry(f1ab,font=('arial', 11,'bold'), textvariable=E_Red_Velvet_Cake, bg="pale green", bd=12, width=6, justify='left',state=DISABLED)
txtRed_Velvet_Cake.grid(row=1,column=1)
txtBlack_Forest_Cake = Entry(f1ab,font=('arial', 11,'bold'), textvariable=E_Black_Forest_Cake, bg="pale green", bd=12, width=6, justify='left',state=DISABLED)
txtBlack_Forest_Cake.grid(row=2,column=1)
txtBoston_Cream_Cake = Entry(f1ab,font=('arial', 11,'bold'), textvariable=E_Boston_Cream_Cake, bg="pale green", bd=12, width=6, justify='left',state=DISABLED)
txtBoston_Cream_Cake.grid(row=3,column=1)
txtLagos_Chocolate_Cake = Entry(f1ab,font=('arial', 11,'bold'), textvariable=E_Lagos_Chocolate_Cake, bg="pale green", bd=12, width=6, justify='left',state=DISABLED)
txtLagos_Chocolate_Cake.grid(row=4,column=1)
txtKilburn_Chocolate_Cake = Entry(f1ab,font=('arial', 11,'bold'), textvariable=E_Kilburn_Chocolate_Cake, bg="pale green", bd=12, width=6, justify='left',state=DISABLED)
txtKilburn_Chocolate_Cake.grid(row=5,column=1)
txtCarlton_Chocolate_Cake = Entry(f1ab,font=('arial', 11,'bold'), textvariable=E_Carlton_Chocolate_Cake, bg="pale green", bd=12, width=6, justify='left',state=DISABLED)
txtCarlton_Chocolate_Cake.grid(row=6,column=1)
txtQueen_Park_Chocolate_Cake = Entry(f1ab,font=('arial', 11,'bold'), textvariable=E_Queen_Park_Chocolate_Cake, bg="pale green", bd=12, width=6, justify='left',state=DISABLED)
txtQueen_Park_Chocolate_Cake.grid(row=7,column=1)
#=================================Enter Widget for Drinks========================================================
txtLatte = Entry(f1aa,font=('arial', 11,'bold'), textvariable=E_Latte, bg="pale green", bd=12, width=6, justify='left',state=DISABLED)
txtLatte.grid(row=0,column=1)
txtEspresso = Entry(f1aa,font=('arial', 11,'bold'), textvariable=E_Espresso, bg="pale green", bd=12, width=6, justify='left',state=DISABLED)
txtEspresso.grid(row=1,column=1)
txtIced_Latte = Entry(f1aa,font=('arial', 11,'bold'), textvariable=E_Iced_Latte, bg="pale green", bd=12, width=6, justify='left',state=DISABLED)
txtIced_Latte.grid(row=2,column=1)
txtVale_Coffee = Entry(f1aa,font=('arial', 11,'bold'), textvariable=E_Vale_Coffee, bg="pale green", bd=12, width=6, justify='left',state=DISABLED)
txtVale_Coffee.grid(row=3,column=1)
txtCappuccino = Entry(f1aa,font=('arial', 11,'bold'), textvariable=E_Cappuccino, bg="pale green", bd=12, width=6, justify='left',state=DISABLED)
txtCappuccino.grid(row=4,column=1)
txtAfrican_Coffee = Entry(f1aa,font=('arial', 11,'bold'), textvariable=E_African_Coffee, bg="pale green", bd=12, width=6, justify='left',state=DISABLED)
txtAfrican_Coffee.grid(row=5,column=1)
txtAmerican_Coffee = Entry(f1aa,font=('arial', 11,'bold'), textvariable=E_American_Coffee, bg="pale green", bd=12, width=6, justify='left',state=DISABLED)
txtAmerican_Coffee.grid(row=6,column=1)
txtIced_Cappuccino = Entry(f1aa,font=('arial', 11,'bold'), textvariable=E_Iced_Cappuccino, bg="pale green", bd=12, width=6, justify='left',state=DISABLED)
txtIced_Cappuccino.grid(row=7,column=1)

#=========================================Cost Items Information========================================
lblCostofDrinks = Label(f2aa,font=('arial', 13,'bold'), text="Cost of Drinks       ", bd=5, anchor='w')
lblCostofDrinks.grid(row=1,column=0, sticky=W)
txtCostofDrinks = Entry(f2aa,font=('arial', 13,'bold'), textvariable=CostofDrinks, bd=5, insertwidth=2, justify='left')
txtCostofDrinks.grid(row=1,column=1)

lblCostofCakes = Label(f2aa,font=('arial', 13,'bold'), text="Cost of Cakes       ", bd=5, anchor='w')
lblCostofCakes.grid(row=2,column=0, sticky=W)
txtCostofCakes = Entry(f2aa,font=('arial', 13,'bold'), textvariable=CostofCakes, bd=5, insertwidth=2, justify='left')
txtCostofCakes.grid(row=2,column=1)

lblSubTotal = Label(f2aa,font=('arial', 13,'bold'), text="Sub Total       ", bd=4, anchor='w')
lblSubTotal.grid(row=3,column=0, sticky=W)
txtSubTotal = Entry(f2aa,font=('arial', 13,'bold'), textvariable=SubTotal, bd=4, insertwidth=2, justify='left')
txtSubTotal.grid(row=3,column=1)

#=====================================Payment Information================================================
lblServiceCharge = Label(f2ab,font=('arial', 13,'bold'), text="Service Charge      ", bd=5, anchor='w')
lblServiceCharge.grid(row=1,column=0, sticky=W)
txtServiceCharge = Entry(f2ab,font=('arial', 13,'bold'), textvariable=ServiceCharge, bd=5, insertwidth=2, justify='left')
txtServiceCharge.grid(row=1,column=1)

lblPaidTax = Label(f2ab,font=('arial', 13,'bold'), text="Paid Tax      ", bd=5, anchor='w')
lblPaidTax.grid(row=2,column=0, sticky=W)
txtPaidTax = Entry(f2ab,font=('arial', 13,'bold'), textvariable=PaidTax, bd=5, insertwidth=2, justify='left')
txtPaidTax.grid(row=2,column=1)

lblTotalCost = Label(f2ab,font=('arial', 13,'bold'), text="Total Cost      ", bd=4, anchor='w')
lblTotalCost.grid(row=3,column=0, sticky=W)
txtTotalCost = Entry(f2ab,font=('arial', 13,'bold'), textvariable=TotalCost, bd=4, insertwidth=2, justify='left')
txtTotalCost.grid(row=3,column=1)

#===========================================Receipt==========================================
lblReceipt = Label(ft2,font=('arial', 12,'bold'), text="Receipt:", bd=4, anchor='w')
lblReceipt.grid(row=0,column=0, sticky=W)
txtReceipt = Text(ft2, width = 59, height = 22,bg="white",bd=14,font=('arial', 11, 'bold'))
txtReceipt.grid(row=1, column=0)

#======================================Button==============================================
btnTotal=Button(fb2,padx=16,pady=1,bd=8, fg="black", font=('arial',12,'bold'), width=5,
            text="Total", bg="green", command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(fb2,padx=16,pady=1,bd=8, fg="black", font=('arial',12,'bold'), width=5,
            text="Receipt", bg="yellow", command=Receipt).grid(row=0,column=1)
btnReset=Button(fb2,padx=16,pady=1,bd=8, fg="black", font=('arial',12,'bold'), width=5,
            text="Reset", bg="lavender", command=Reset).grid(row=0,column=2)
btnExit=Button(fb2,padx=16,pady=1,bd=8, fg="black", font=('arial',12,'bold'), width=5,
            text="Exit", bg = "red", command=qExit).grid(row=0,column=3)

root.mainloop()

                      

                      

                      




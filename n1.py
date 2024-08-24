from tkinter import *
top=Tk()
top.geometry("1400x800")
top.title("Neha")
top.config(bg="black")
welcome=Label(top,text="WELCOME",font=("TimesNewRoman",20,"bold"),bg="pink",fg="purple")
welcome.place(x=600,y=45)
def login():
    det=Frame(top,bg="navyblue",height=700,width=400)
    det.pack(fill=X)
    label1=Label(det,text="Login Page",font=("TimesNewRoman",24,"bold"),bg="navyblue",fg="white")
    label1.place(x=600,y=100)
    label2=Label(det,text="UserName",font=("TimesNewRoman",20,"bold"),bg="navyblue",fg="white")
    label2.place(x=720,y=200)
    box=Entry(top,text="",font=("TimesNewRoman",20,"bold"),fg="black")
    box.place(x=870,y=200,height=30,width=200)
    box=Entry(top,text="",font=("TimesNewRoman",20,"bold"),fg="black")
    box.place(x=870,y=250,height=30,width=200)
    label4=Label(det,text="Password",font=("TimesNewRoman",20,"bold"),bg="navyblue",fg="white")
    label4.place(x=720,y=250)
    label5=Label(det,text="Don't Have An account?",font=("TimesNewRoman",20,"bold"),bg="navyblue",fg="white")
    label5.place(x=660,y=450)
    button=Button(top,text="Login",font=("TimesNewRoman",20,"bold"),bg="red",fg="white",activebackground="yellow",activeforeground="brown")
    button.place(x=800,y=350,height=50,width=200)
    button=Button(top,text="Sign In",font=("TimesNewRoman",20,"bold"),bg="purple",fg="white",activebackground="yellow",activeforeground="brown",command=detail)
    button.place(x=990,y=450,height=40,width=200)
    button=Button(top,text="back",font=("TimesNewRoman",20,"bold"),bg="purple",fg="white",activebackground="red",activeforeground="white")
    button.place(x=100,y=50,height=40,width=100)
def detail():
    var=Frame(top,bg="grey",height=500,width=300)
    var.pack(fill=X)
    label6=Label(var,text="Details",font=("TimesNewRoman",24,"bold"),bg="grey",fg="black")
    label6.place(x=600,y=550)

    

    
label3=Label(top,text="Welcome our page",font=("CenturyGothics",32,"bold"),bg="black",fg="white")
label3.place(x=600,y=45)

button=Button(top,text="Get Started",font=("TimesNewRoman",20,"bold"),bg="white",fg="black",activebackground="yellow",activeforeground="brown",command=login)
button.place(x=500,y=450,height=60,width=500)


              
        

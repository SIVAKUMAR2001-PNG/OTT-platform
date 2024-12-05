from tkinter import*
from tkinter import messagebox
import pymysql
import webbrowser
from PIL import Image, ImageTk
import tkinter as tk


project=Tk()

project.title("Design")
project.geometry("1200x1200")
project.config(bg="black")    #9c8321 #e1b382
project.resizable(False,False)


####database
connection=pymysql.connect(
    host="localhost",
    user="root",
    password="kabi5016",
    database="kabi"
    )
 
my_database=connection.cursor()


def save():

    a=e1.get()
    b=e2.get()
    c=e3.get()
    d=e4.get()
    e=e5.get()
    print(a,b,c,d,e)

    if(a=="" or b=="" or c=="" or d=="" or e==""):
        messagebox.showerror("error","Enter All Details")
    elif(d!=e):
        messagebox.showerror("error","Check Password")
    
    else:
        query="INSERT INTO name(name,age,email,pword,rpword)VALUES(%s,%s,%s,%s,%s)"
        values=(a,b,c,d,e,)
        my_database.execute(query,values)
        connection.commit()
        my_database.close()
        messagebox.showinfo("Info","Successfully Saved..!")
        page1.destroy()
def cexp():
    webbrowser.open_new("https://youtu.be/cYXH12YFHTE")
def mck():
    webbrowser.open_new("https://youtu.be/oqcXT3tkZD0")
def stk():
    webbrowser.open_new("https://youtu.be/htwtV6qsSVo")
def kgf():
    webbrowser.open_new("https://youtu.be/gKizDojsdvs")
def mst():
    webbrowser.open_new("https://youtu.be/Kycaxw_f4RI")
def destroybw():
    pageb.destroy()
def bollywood():
    global pageb
    
    pageb=Frame(page2,bg="black",height=1200,width=1200)
    pageb.pack(fill=X)

    l1=Label(pageb,text="Hotstar",font=("Copperplate Gothic Bold", 25,),bg="black",fg="#0288d1")
    l1.place(x=550,y=25)
          ##image1
    img=Image.open('bimg1.jpg')   
    img1=ImageTk.PhotoImage(img)
    but1=Button(pageb,image=img1,bg="black",bd=0,command=cexp)
    but1.image=img1
    but1.place(x=40,y=150)
    
    lt1=Label(pageb,text="Chennai Express Full Movie HD\nShan Rukhkhan|Deepika Padukone\nNikitin Dheer",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt1.place(x=50,y=350)

          ##image2
    img=Image.open('bimg5.jpg')   
    img5=ImageTk.PhotoImage(img)
    but5=Button(pageb,image=img5,bg="black",bd=0,command=mck)
    but5.image=img5
    but5.place(x=450,y=150)
    
    lt5=Label(pageb,text="Macharla Chunaav Kshetra (M.C.K)\nNew Released Full Hindi Dubbed Movie\n Nithilin Krithi Sheety",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt5.place(x=460,y=350)

         ##image3        

    img=Image.open('bimg3.jpg')   
    img3=ImageTk.PhotoImage(img)
    but3=Button(pageb,image=img3,bg="black",bd=0,command=stk)
    but3.image=img3
    but3.place(x=850,y=150)
    
    lt2=Label(pageb,text="Maestro New Released\nHindi Dubbed Movie 2024\n Nithin, Thamannaah",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt2.place(x=900,y=350)
          ##image4
    img=Image.open('bimg4.jpg')   
    img4=ImageTk.PhotoImage(img)
    but4=Button(pageb,image=img4,bg="black",bd=0,command=kgf)
    but4.image=img4
    but4.place(x=250,y=450)

    lt4=Label(pageb,text="KGF(4K Quality) Full Movie\n Yash Blockbuster Movie| Srinidhi Sheety",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt4.place(x=250,y=700)
          ## image5       
    
    img=Image.open('bimg2.jpg')   
    img2=ImageTk.PhotoImage(img)
    but2=Button(pageb,image=img2,bg="black",bd=0,command=stk)
    but2.image=img2
    but2.place(x=650,y=480)

    
    lt2=Label(pageb,text="Sanam Teri Kasam \nSuperhit Hindi Romantic Movie\n Harshvardhan Rane| Mawra hocane ",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt2.place(x=675,y=700)

    btnd=Button(pageb,text="X",bg="red",fg="white",command=destroybw,font=(3,),width=3)
    btnd.place(x=1160,y=5)


                          ##page kollywood                           

    
def jilla():
    webbrowser.open_new("https://youtu.be/-ti9YtBnFjA")
def slk():
    webbrowser.open_new("https://youtu.be/Tz7cQ0XRN4U")
def tha():
    webbrowser.open_new("https://youtu.be/opZebYVOGms")
def mgn():
    webbrowser.open_new("https://youtu.be/j21KVOafypg")
def destroykw():
    pagek.destroy()
    
def kollywood():
    global pagek,page2
    pagek=Frame(page2,bg="black",height=1200,width=1200)
    pagek.pack(fill=X)

    l1=Label(pagek,text="Hotstar",font=("Copperplate Gothic Bold", 25,),bg="black",fg="#0288d1")
    l1.place(x=550,y=25)

          ##image2
    img=Image.open('kimg2.jpg')   
    img2=ImageTk.PhotoImage(img)
    but2=Button(pagek,image=img2,bg="black",command=jilla,bd=0)
    but2.image=img2
    but2.place(x=150,y=125)
    
    lt2=Label(pagek,text="Thalapathy Vijay in Jilla\nTamil Movie HD print\n Kajal Agarval,Mohanlal",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt2.place(x=200,y=350)

         ##image3        

    img=Image.open('kimg3.jpg')   
    img3=ImageTk.PhotoImage(img)
    but3=Button(pagek,image=img3,bg="black",command=slk,bd=0)
    but3.image=img3
    but3.place(x=800,y=125)
    
    lt2=Label(pagek,text="Sillunu Oru Kadhal\nTamil Full Movie |2006\nSuriya | Jothika",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt2.place(x=875,y=350)
          ##image4
    img=Image.open("kimg4.jpg")   
    img4=ImageTk.PhotoImage(img)
    but4=Button(pagek,image=img4,bg="black",command=tha,bd=0)
    but4.image=img4
    but4.place(x=150,y=450)

    lt4=Label(pagek,text="Thalaivaa Tamil movie\n Vijay|Amala Paul|Santhanam ",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt4.place(x=200,y=700)
          ## image5       
    
    img=Image.open('kimg5.jpg')   
    img5=ImageTk.PhotoImage(img)
    but5=Button(pagek,image=img5,bg="black",command=mgn,bd=0)
    but5.image=img5
    but5.place(x=800,y=450)

    
    lt5=Label(pagek,text="Maragadha Naanayam Tamil Full Movie\n Mime Gopi| Daniel Annie",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt5.place(x=800,y=700)
    
    btnd=Button(pagek,text="X",bg="red",fg="white",command=destroykw,font=(3,),width=3)
    btnd.place(x=1160,y=5)

                               ##Tollywood

def aru():
    webbrowser.open_new("https://youtu.be/0bEZ1NhcCOc")
def mir():
    webbrowser.open_new("https://youtu.be/b8dvhBPrGtw ")
def mhd():
    webbrowser.open_new("https://youtu.be/G7haVu5g-Qw")
def manm():
    webbrowser.open_new("https://youtu.be/mf7sk4IydGo")
    
def destroytw():
    paget.destroy()
def tollywood():
    global paget

    paget=Frame(page2,bg="black",height=1200,width=1200)
    paget.pack(fill=X)

    l1=Label(paget,text="Hotstar",font=("Copperplate Gothic Bold", 25,),bg="black",fg="#0288d1")
    l1.place(x=550,y=25)

          ##image2
    img=Image.open('img1.jpg')   
    img2=ImageTk.PhotoImage(img)
    but2=Button(paget,image=img2,bg="black",command=aru,bd=0)
    but2.image=img2
    but2.place(x=150,y=125)
    
    lt2=Label(paget,text="Arundhati (2009) - \nLatest Telugu Full Length HD Movie \n| Anushka | Sonu Sood | Shinde",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt2.place(x=170,y=350)

         ##image3        

    img=Image.open('img3.jpg')   
    img3=ImageTk.PhotoImage(img)
    but3=Button(paget,image=img3,bg="black",command=mhd,bd=0)
    but3.image=img3
    but3.place(x=800,y=125)
    
    lt2=Label(paget,text="Magadheera Telugu Full Movie \n Ram Charan, Kajal Agarwal, \nSri Hari || Geetha Arts",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt2.place(x=850,y=350)
          ##image4
    img=Image.open("img2.jpg")   
    img4=ImageTk.PhotoImage(img)
    but4=Button(paget,image=img4,bg="black",command=mir,bd=0)
    but4.image=img4
    but4.place(x=150,y=450)

    lt4=Label(paget,text="Mirchi Telugu Full Movie \n Prabhas, Anushka Shetty,\n Richa Gangopadhyay@SriBalajiMovies",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt4.place(x=160,y=650)
          ## image5       
    
    img=Image.open('img4.jpg')   
    img5=ImageTk.PhotoImage(img)
    but5=Button(paget,image=img5,bg="black",command=manm,bd=0)
    but5.image=img5
    but5.place(x=800,y=450)

    
    lt5=Label(paget,text="Manmadhudu Telugu Full Movie\nNagarjuna, Sonali Bendre, Anshu",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt5.place(x=850,y=650)
    
    btnd=Button(paget,text="X",bg="red",fg="white",command=destroytw,font=(3,),width=3)
    btnd.place(x=1160,y=5)


                                 ##Molly wood
def destroymw():
    pagem.destroy()

def mollywood():
    global pagem
    pagem=Frame(page2,bg="black",height=1200,width=1200)
    pagem.pack(fill=X)

    l1=Label(pagem,text="Hotstar",font=("Copperplate Gothic Bold", 25,),bg="black",fg="#0288d1")
    l1.place(x=550,y=25)

          ##image2
    img=Image.open('img1.jpg')   
    img2=ImageTk.PhotoImage(img)
    but2=Button(pagem,image=img2,bg="#09136E",command=aru,bd=0)
    but2.image=img2
    but2.place(x=150,y=125)
    
    lt2=Label(pagem,text="Arundhati (2009) - \nLatest Telugu Full Length HD Movie \n| Anushka | Sonu Sood | Shinde",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt2.place(x=170,y=350)

         ##image3        

    img=Image.open('img3.jpg')   
    img3=ImageTk.PhotoImage(img)
    but3=Button(pagem,image=img3,bg="black",command=mhd,bd=0)
    but3.image=img3
    but3.place(x=800,y=125)
    
    lt2=Label(pagem,text="Magadheera Telugu Full Movie \n Ram Charan, Kajal Agarwal, \nSri Hari || Geetha Arts",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt2.place(x=850,y=350)
          ##image4
    img=Image.open("img2.jpg")   
    img4=ImageTk.PhotoImage(img)
    but4=Button(pagem,image=img4,bg="black",command=mir,bd=0)
    but4.image=img4
    but4.place(x=150,y=450)

    lt4=Label(pagem,text="Mirchi Telugu Full Movie \n Prabhas, Anushka Shetty,\n Richa Gangopadhyay@SriBalajiMovies",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt4.place(x=160,y=650)
          ## image5       
    
    img=Image.open('img4.jpg')   
    img5=ImageTk.PhotoImage(img)
    but5=Button(pagem,image=img5,bg="#09136E",command=manm,bd=0)
    but5.image=img5
    but5.place(x=800,y=450)

    
    lt5=Label(pagem,text="Manmadhudu Telugu Full Movie\nNagarjuna, Sonali Bendre, Anshu",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt5.place(x=850,y=650)
    
    btnd=Button(pagem,text="X",bg="red",fg="white",command=destroymw,font=(3,),width=3)
    btnd.place(x=1160,y=5)


                            ## hollywood

def one():
    webbrowser.open_new("https://youtu.be/Ok5Q0-pQ59Q")
def two():
    webbrowser.open_new("https://youtu.be/lxjSWWgFMzA")
def three():
    webbrowser.open_new("https://youtu.be/1kSwy8ece6g")
def four():
    webbrowser.open_new("https://youtu.be/1gxQKNrHU5I")                           
def destroyhw():
    pageh.destroy()
def hollywood():
    global pageh
    pageh=Frame(page2,bg="black",height=1200,width=1200)
    pageh.pack(fill=X)

    l1=Label(pageh,text="Hotstar",font=("Copperplate Gothic Bold", 25,),bg="black",fg="#0288d1")
    l1.place(x=550,y=25)

          ##image2
    img=Image.open('h4.jpg')   
    img2=ImageTk.PhotoImage(img)
    but2=Button(pageh,image=img2,bg="black",command=one,bd=0)
    but2.image=img2
    but2.place(x=150,y=125)
    
    lt2=Label(pageh,text="Men in Black: International (2024) \nFull Movie in Hindi Dubbed \n Latest Hollywood Action Movie",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt2.place(x=170,y=300)

         ##image3        

    img=Image.open('h3.jpg')   
    img3=ImageTk.PhotoImage(img)
    but3=Button(pageh,image=img3,bg="black",command=two,bd=0)
    but3.image=img3
    but3.place(x=800,y=125)
    
    lt2=Label(pageh,text="Ragasiya Theevu Tamil Dubbed Movie \n Latest Hollywood Dubbed Movie \n Tyron Leitso, Katie Car",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt2.place(x=800,y=350)
          ##image4
    img=Image.open("h2.jpg")   
    img4=ImageTk.PhotoImage(img)
    but4=Button(pageh,image=img4,bg="black",command=three,bd=0)
    but4.image=img4
    but4.place(x=150,y=450)

    lt4=Label(pageh,text="2022 TSUNAMI - Tamil Dubbed \nHollywood Movies | Full Movie HD \n Hollywood Action Movies In Tamil",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt4.place(x=160,y=650)
          ## image5       
    
    img=Image.open('h1.jpg')   
    img5=ImageTk.PhotoImage(img)
    but5=Button(pageh,image=img5,bg="black",command=four,bd=0)
    but5.image=img5
    but5.place(x=800,y=450)

    
    lt5=Label(pageh,text=" APE X - Hollywood Dubbed Tamil Movie \n Tom Arnold, Anna Telfer \n Tamil Sci-Fi Action Movie",font=("Time new roman", 12,"bold",),bg="black",fg="#0288d1")
    lt5.place(x=800,y=650)
    
    btnd=Button(pageh,text="X",bg="red",fg="white",command=destroyhw,font=(3,),width=3)
    btnd.place(x=1160,y=5)

    


    

def destroy():
    page2.destroy()

def login():
    global imgbut,but1,but2,lab1,e1,b1,b2,b3,b4,b5,page2

    query=en1.get()
    values=en3.get()
    sql=("SELECT * from name where name=%s and pword=%s")
    my_database.execute(sql,(query,values))
    result=my_database.fetchall()
##    print(result)
    if(result):
        
        page2=Frame(project,bg="black",height=1200,width=1200)
        page2.pack(fill=X)

        l1=Label(page2,text="Hotstar",font=("Copperplate Gothic Bold", 25,),bg="black",fg="#0288d1")
        l1.place(x=550,y=25)

        b1=Button(page2,text="Bollywood",font=("Lucida Calligraphy", 25, "bold"),bg="black",fg="#0288d1")
        b1.place(x=75,y=110)
                     ##image 

        img=Image.open('bimg1.jpg')   
        img1=ImageTk.PhotoImage(img)
        but1=Button(page2,image=img1,bg="#0288d1",bd=0,command=bollywood)
        but1.image=img1
        but1.place(x=40,y=230)


        b2=Button(page2,text="Kollywood",font=("Lucida Calligraphy", 25, "bold"),bg="black",fg="#0288d1")
        b2.place(x=490,y=110)
                     ##image 
        
        img=Image.open('kimg1.jpg')   
        img2=ImageTk.PhotoImage(img)
        but2=Button(page2,image=img2,bg="black",bd=0,command=kollywood)
        but2.image=img2
        but2.place(x=460,y=230)

        b3=Button(page2,text="Tollywood",font=("Lucida Calligraphy", 25, "bold"),bg="black",fg="#0288d1")
        b3.place(x=880,y=110)
                     ##image
        img=Image.open('timg1.jpg')   
        img5=ImageTk.PhotoImage(img)
        but5=Button(page2,image=img5,bg="black",bd=0,command=tollywood)
        but5.image=img5
        but5.place(x=850,y=230)
        

        b4=Button(page2,text="Mollywood",font=("Lucida Calligraphy", 25, "bold"),bg="black",fg="#0288d1")
        b4.place(x=250,y=450)
                     ##image 
        
        img=Image.open('mimg1.jpg')   
        img4=ImageTk.PhotoImage(img)
        but4=Button(page2,image=img4,bg="black",command=mollywood,bd=0)
        but4.image=img4
        but4.place(x=225,y=560)

        b5=Button(page2,text="Hollywood",font=("Lucida Calligraphy", 25, "bold"),bg="black",fg="#0288d1")
        b5.place(x=820,y=450)
                    ##image
        img=Image.open('himg1.jpg')   
        img3=ImageTk.PhotoImage(img)
        but3=Button(page2,image=img3,bg="black",command=hollywood,bd=0)
        but3.image=img3
        but3.place(x=750,y=560)

        btnd=Button(page2,text="X",bg="red",fg="white",command=destroy,font=(3,),width=3)
        btnd.place(x=1160,y=5)


def destroyc():
    page1.destroy()
def reset():
    e1.delete(0,tk.END)
    e2.delete(0,tk.END)
    e3.delete(0,tk.END)
    e4.delete(0,tk.END)
    e5.delete(0,tk.END)


##create account
def createaccount():
    global e1,e2,e3,e4,e5,page1
    
    page1=Frame(project,bg="black",height=1200,width=1200)
    page1.pack(fill=X)
    
    lab0=Label(page1,text="Creat Account",font=("Lucida Calligraphy", 25, "bold"),bg="black",fg="#0288d1")
    lab0.place(x=450,y=70)
    
    lab1=Label(page1,text="Name",font=("Times new roman", 20, "bold"),bg="black",fg="#0288d1")
    lab1.place(x=400,y=150)

    lab2=Label(page1,text="Age",font=("Times new roman", 20, "bold"),bg="black",fg="#0288d1")
    lab2.place(x=400,y=220)

    lab3=Label(page1,text="E-mail",font=("Times new roman", 20, "bold"),bg="black",fg="#0288d1")
    lab3.place(x=400,y=290)

    lab5=Label(page1,text="Password",font=("Times new roman", 20, "bold"),bg="black",fg="#0288d1")
    lab5.place(x=400,y=360)

    lab6=Label(page1,text="Confrim",font=("Times new roman", 20, "bold"),bg="black",fg="#0288d1")
    lab6.place(x=400,y=430)

    e1=Entry(page1,bg="white",font=("Times new roman",))
    e1.place(x=600,y=150)
    e2=Entry(page1,bg="white",font=("Times new roman",))
    e2.place(x=600,y=220)
    e3=Entry(page1,bg="white",font=("Times new roman",))
    e3.place(x=600,y=290)
    e4=Entry(page1,bg="white",font=("Times new roman",))
    e4.place(x=600,y=360)
    e5=Entry(page1,bg="white",font=("Times new roman",))
    e5.place(x=600,y=430)
    
    btn1=Button(page1,text="SAVE",bg="black",fg="#0288d1",font=("Times new roman",15,),command=save)
    btn1.place(x=450,y=550)


    btn2=Button(page1,text="Reset",bg="black",fg="#0288d1",font=("Times new roman",15,),command=reset)
    btn2.place(x=650,y=550)
    btnd=Button(page1,text="X",bg="red",fg="white",command=destroyc,font=(3,),width=3)
    btnd.place(x=1160,y=5)



##first page

lab1=Label(project,text="Disney+\nHotstar",font=("Lucida Calligraphy", 30, "bold"),bg="black",fg="#0288d1",height=2,width=10)
lab1.place(x=480,y=100)
lab2=Label(project,text="Login",font=("Times new roman", 20, "bold"),bg="black",fg="#0288d1")
lab2.place(x=600,y=230)
lab3=Label(project,text="Name",font=("Times new roman", 20, "bold"),bg="black",fg="#0288d1")
lab3.place(x=450,y=300)

lab4=Label(project,text="Password",font=("Times new roman", 20, "bold"),bg="black",fg="#0288d1")
lab4.place(x=450,y=350)
en1=Entry(project,bg="white",font=("Times new roman",))
en1.place(x=600,y=300)
en3=Entry(project,bg="white",font=("Times new roman",))
en3.place(x=600,y=350)

b1=Button(project,text="Login",bg="black",fg="#0288d1",font=("Times new roman", 20, "bold"),command=login)
b1.place(x=450,y=450)
b1=Button(project,text="Create Account",bg="black",fg="#0288d1",font=("Times new roman", 20, "bold"),command=createaccount)
b1.place(x=700,y=450)


    
project.mainloop()




         

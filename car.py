from sqlite3.dbapi2 import Cursor
from  tkinter import *
from tkinter import scrolledtext
import tkinter
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
import sqlite3
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
import shutil
import os
try:
    con=sqlite3.connect(database="carpool.sqlite")
    cursor=con.cursor()
    table1="create table users(username text primary key, password text, mobile text, email text)"
    table2="create table cars(username text,src text, dest text, regno text primary key, model text, seats text,fule text)"
    cursor.execute(table1)
    cursor.execute(table2)
    con.commit()
    con.close
    print("table created")
except Exception as e:
    print(e)

win=Tk()
win.state("zoomed")
win.configure(bg="powder blue")
lbl_title=Label(win,text="Car Pooling",font=('',50,'bold','underline'),bg='powder blue')
lbl_title.pack()

img=Image.open("images/1st.jpeg").resize((400,100))
imgtk=ImageTk.PhotoImage(img,master=win)
lbl_img=Label(win,image=imgtk)
lbl_img.place(relx=0 ,rely=0)

img1=Image.open("images/2nd.jpeg").resize((400,100))
imgtk1=ImageTk.PhotoImage(img1,master=win)
lbl_img1=Label(win,image=imgtk1)
lbl_img1.place(relx=.72 ,rely=0)

img2=Image.open("images/login.png").resize((120,40))
imgtk2=ImageTk.PhotoImage(img2)

img3=Image.open("images/reset.png").resize((120,40))
imgtk3=ImageTk.PhotoImage(img3)

img4=Image.open("images/register.png").resize((150,40))
imgtk4=ImageTk.PhotoImage(img4)

img5=Image.open("images/back.png").resize((80,40))
imgtk5=ImageTk.PhotoImage(img5)

img6=Image.open("images/logout.png").resize((80,40))
imgtk6=ImageTk.PhotoImage(img6)

img7=Image.open("images/search1.png").resize((150,50))
imgtk7=ImageTk.PhotoImage(img7)

img8=Image.open("images/submit.png").resize((120,40))
imgtk8=ImageTk.PhotoImage(img8)

img9=Image.open("images/update.png").resize((120,40))
imgtk9=ImageTk.PhotoImage(img9)

img10=Image.open("images/profile.jpg").resize((150,150))
imgtk10=ImageTk.PhotoImage(img10)


def home_frame():
    frm=Frame(win,highlightbackground='brown',highlightthickness=3)
    frm.place(x=400 , y=200,relwidth=.5, relheight=.45)
    def reset(event):
        e_user.delete(0,"end")
        p_user.delete(0,"end")
        e_user.focus()
    def newuser(event):
        frm.destroy()
        newuser_frame()
    def login(event):
        global loginuser_row
        u=e_user.get()
        p=p_user.get()
        try:
            con=sqlite3.connect(database="carpool.sqlite")
            cursor=con.cursor()
            cursor.execute("select * from users where username=? and password=?",(u,p))
            loginuser_row=cursor.fetchone()
            con.close
            if(loginuser_row==None):
                messagebox.showerror('Login','Invalid UserName Password')
            else:
                frm.destroy()
                login_frame()
        except Exception as e:
            messagebox.showerror('Registraction',str(e))
        
    lbl_user=Label(frm,text="User_Name",font=('',20,'bold'))
    lbl_pass=Label(frm,text="Password",font=('',20,'bold'))
    e_user=Entry(frm,font=('',20,'bold'),bd=5)
    e_user.focus()
    p_user=Entry(frm,font=('',20,'bold'),bd=5,show="*")
    lbl_user.place(x=100,y=30)
    e_user.place(x=300,y=30)
    lbl_pass.place(x=100,y=100)
    p_user.place(x=300,y=100)

    but_login=Label(frm,image=imgtk2)
    but_login.place(x=220,y=170)
    but_login.bind("<Button>",login)

    but_reset=Label(frm,image=imgtk3)
    but_reset.place(x=400,y=170)
    but_reset.bind("<Button>",reset)
    
    but_new=Label(frm,image=imgtk4)
    but_new.place(x=280,y=240)
    but_new.bind("<Button>",newuser)

def newuser_frame():
    frm=Frame(win,highlightbackground='brown',highlightthickness=3)
    frm.place(x=400 , y=150,relwidth=.5, relheight=.55)
    
    def reset(event):
        e_user.delete(0,"end")
        e_pass.delete(0,"end")
        e_mob.delete(0,"end")
        e_email.delete(0,"end")
        e_user.focus()


    def reg_todb(event):
        u=e_user.get()
        p=e_pass.get()
        m=e_mob.get()
        e=e_email.get()

        if (len(u)==0 ):
            messagebox.showwarning('Validation','Empty Field Not allow')
        elif(len(p)==0):
            messagebox.showwarning('Validation','Empty Field Not allow')
        elif(len(m)<10):
            messagebox.showwarning('Validation','Enter Valid Mobile Number')
        elif("@" not in e or "." not in e):
            messagebox.showwarning('Validation','Enter Valid Email')
        else:
            try:
                con=sqlite3.connect(database="carpool.sqlite")
                cursor=con.cursor()
                cursor.execute("insert into users values(?,?,?,?)",(u,p,m,e))
                con.commit()
                con.close
                messagebox.showinfo('Registraction',"Registraction Done!!")
                frm.destroy()
                home_frame()
            except Exception as e:
                messagebox.showerror("Registraction","\nUserName Already Exits")

    lbl_user=Label(frm,text="User_Name",font=('',20,'bold'))
    lbl_pass=Label(frm,text="Password",font=('',20,'bold'))
    lbl_mob=Label(frm,text="Mobile",font=('',20,'bold'))
    lbl_email=Label(frm,text="Email",font=('',20,'bold'))
    
    
    e_user=Entry(frm,font=('',20,'bold'),bd=5)
    e_user.focus()
    e_pass=Entry(frm,font=('',20,),bd=5,show="*")
    e_mob=Entry(frm,font=('',20,),bd=5)
    e_email=Entry(frm,font=('',20,),bd=5)
    
    
    lbl_user.place(x=100,y=20)
    e_user.place(x=300,y=20)
    lbl_pass.place(x=100,y=90)
    e_pass.place(x=300,y=90)
    lbl_mob.place(x=100,y=160)
    e_mob.place(x=300,y=160)
    lbl_email.place(x=100,y=230)
    e_email.place(x=300,y=230)

    but_new=Label(frm,image=imgtk4)
    but_new.place(x=200,y=300)
    but_new.bind("<Button>",reg_todb)

    but_reset=Label(frm,image=imgtk3)
    but_reset.place(x=400,y=300)
    but_reset.bind("<Button>",reset)

def login_frame():
    frm=Frame(win,highlightbackground='brown',highlightthickness=3)
    frm.place(x=300 , y=150,relwidth=.65, relheight=.5)
    
    def logout(event):
        frm.destroy()
        home_frame()
    def search():
        frm.destroy()
        searchpool_frame()
    def create():
        frm.destroy()
        createpool_frame()
    def update():
        frm.destroy()
        updateprofile_frame()
    def picture():
        img_path=filedialog.askopenfilename()
        shutil.copy(img_path,f"images/{loginuser_row[0]}.png")
        img_pro=Image.open(f"images/{loginuser_row[0]}.png").resize((150,150))
        img_profile=ImageTk.PhotoImage(img_pro)
        lbl_pro['image']=img_profile
        lbl_pro.image=img_profile


    lbl_wel=Label(frm,text=f"Welcome,{loginuser_row[0]}",font=('',15,'bold'),fg='green')
    lbl_wel.place(x=0,y=0)

    lbl_pro=Label(frm,image=imgtk10)
    lbl_pro.place(x=0,y=40)
    if(os.path.exists(f"images/{loginuser_row[0]}.png")):
        img_pro=Image.open(f"images/{loginuser_row[0]}.png").resize((150,150))
        img_profile=ImageTk.PhotoImage(img_pro)
        lbl_pro['image']=img_profile
        lbl_pro.image=img_profile
        lbl_pro=Label(frm,image=img_profile)
        lbl_pro.place(x=0,y=40)



    but_logout=Label(frm,image=imgtk6)
    but_logout.place(relx=.9,rely=0)
    but_logout.bind("<Button>",logout)

    but_search=Button(frm,text='Search Pool',font=('',15,'bold'),bd=5,width=20,command=search)
    but_search.place(relx=.35,rely=.1)
    but_create=Button(frm,text='Create Pool',font=('',15,'bold'),bd=5,width=20,command=create)
    but_create.place(relx=.35,rely=.3)
    but_profile=Button(frm,text='Update Profile',font=('',15,'bold'),bd=5,width=20,command=update)
    but_profile.place(relx=.35,rely=.5)

    but_profilepic=Button(frm,text='Upload Profile',font=('',15,'bold'),bd=5,width=20,command=picture)
    but_profilepic.place(relx=.35,rely=.7)
def searchpool_frame():
    frm=Frame(win,highlightbackground='brown',highlightthickness=3)
    frm.place(x=300 , y=150,relwidth=.65, relheight=.5)
    
    def logout(event):
        frm.destroy()
        home_frame()
    def back(event):
        frm.destroy()
        login_frame()
    def searchpool_db(event):
        src=e_src.get().upper()
        dest=e_des.get().upper()
        try:
            con=sqlite3.connect(database="carpool.sqlite")
            cursor=con.cursor()
            cursor.execute("select * from cars where src=? and dest=?",(src,dest))
            pools=cursor.fetchall()
            con.close
            if(len(pools)==0):
                messagebox.showerror("Pool","Pool Does't Exit")
                frm.destroy()
                searchpool_frame()
            else:
                con=sqlite3.connect(database="carpool.sqlite")
                cursor=con.cursor()
                st=ScrolledText(frm,width=108,height=10,font=('Arial',11,'bold','underline'))
                st.place(x=0,y=140)
                st.insert("end","Username\t\tCar Model\t\tCar NO\t\tSeat\tFule\t   Mobile\t\tEmail")
                for pool in pools:
                    cursor.execute("select mobile,email from users where username=?",(pool[0],))
                    m,e=cursor.fetchone()
                    st.insert("end",f"\n\n{pool[0]}\t\t{pool[4]}\t\t{pool[3]}\t\t{pool[5]}\t{pool[6]}\t   {m}\t\t{e}","clr")
                st.tag_config("clr",font=('',10),foreground='blue')
                st.configure(state='disable')
        except Exception as e:
            messagebox.showerror('Pool',str(e))

    lbl_wel=Label(frm,text=f"Welcome,{loginuser_row[0]}",font=('',15,'bold'),fg='green')
    lbl_wel.place(x=0,y=0)

    but_back=Label(frm,image=imgtk5)
    but_back.place(relx=.8,rely=0)
    but_back.bind("<Button>",back)

    but_logout=Label(frm,image=imgtk6)
    but_logout.place(relx=.9,rely=0)
    but_logout.bind("<Button>",logout)

    lbl_src=Label(frm,text="Source",font=('',15,'bold'),fg='blue')
    lbl_src.place(relx=.1,rely=.1)
    e_src=Entry(frm,font=('',15),bd=4,width=15)
    e_src.focus()
    e_src.place(relx=.2,rely=.1)
    
    lbl_des=Label(frm,text="Destination",font=('',15,'bold'),fg='blue')
    lbl_des.place(relx=.43,rely=.1)
    e_des=Entry(frm,font=('',15),bd=4,width=15)
    e_des.place(relx=.57,rely=.1)

    lbl_srch=Label(frm,image=imgtk7)
    lbl_srch.place(relx=.38,rely=.25)
    lbl_srch.bind("<Button>",searchpool_db)

def createpool_frame():
    frm=Frame(win,highlightbackground='brown',highlightthickness=3)
    frm.place(x=300 , y=150,relwidth=.65, relheight=.5)
    def reset(event):
        e_src.delete(0,"end")
        e_src.focus()
        e_des.delete(0,"end")
        e_model.delete(0,"end")
        e_num.delete(0,"end")
        cb_ful.delete(0,"end")
        cb_seat.delete(0,"end")
    def logout(event):
        frm.destroy()
        home_frame()
    def back(event):
        frm.destroy()
        login_frame()
    def createpool_db(event):
        src=e_src.get()
        des=e_des.get()
        model=e_model.get()
        seat=cb_seat.get()
        regno=e_num.get().replace(' ','')
        fuletype=cb_ful.get()
        try:
            con=sqlite3.connect(database="carpool.sqlite")
            cursor=con.cursor()
            cursor.execute("insert into cars values(?,?,?,?,?,?,?)",(loginuser_row[0],src.upper(),des.upper(),regno.upper(),model.upper(),seat,fuletype))
            con.commit()
            con.close
            messagebox.showinfo('create Pool '," Pool Created !!")
            frm.destroy()
            login_frame()
        except Exception as e:
            messagebox.showerror("Created pool","\nCar Already Exits")



    lbl_wel=Label(frm,text=f"Welcome,{loginuser_row[0]}",font=('',15,'bold'),fg='green')
    lbl_wel.place(x=0,y=0)

    but_back=Label(frm,image=imgtk5)
    but_back.place(relx=.8,rely=0)
    but_back.bind("<Button>",back)

    but_logout=Label(frm,image=imgtk6)
    but_logout.place(relx=.9,rely=0)
    but_logout.bind("<Button>",logout)

    lbl_src=Label(frm,text="Source",font=('',15,'bold'),fg='blue')
    lbl_src.place(relx=.1,rely=.15)
    e_src=Entry(frm,font=('',15),bd=4,width=15)
    e_src.focus()
    e_src.place(relx=.25,rely=.15)
    
    lbl_des=Label(frm,text="Destination",font=('',15,'bold'),fg='blue')
    lbl_des.place(relx=.48,rely=.15)
    e_des=Entry(frm,font=('',15),bd=4,width=15)
    e_des.place(relx=.62,rely=.15)
    
    lbl_model=Label(frm,text="Car Model",font=('',15,'bold'),fg='blue')
    lbl_model.place(relx=.1,rely=.3)
    e_model=Entry(frm,font=('',15),bd=4,width=15)
    e_model.place(relx=.25,rely=.3)

    lbl_seat=Label(frm,text="Seats",font=('',15,'bold'),fg='blue')
    lbl_seat.place(relx=.49,rely=.3)
    cb_seat=Combobox(frm,values=["----Select----",2,3,4,5,6,7],font=('',15,'bold'),width=14)
    cb_seat.current(0)
    cb_seat.place(relx=.62,rely=.3)

    lbl_num=Label(frm,text="Car Number",font=('',15,'bold'),fg='blue')
    lbl_num.place(relx=.1,rely=.45)
    e_num=Entry(frm,font=('',15),bd=4,width=15)
    e_num.place(relx=.25,rely=.45)
    
    lbl_ful=Label(frm,text="Fule Type",font=('',15,'bold'),fg='blue')
    lbl_ful.place(relx=.49,rely=.45)
    cb_ful=Combobox(frm,values=["----Select----",'Diesel','Petrol','Petrol+CNG','Petrol+LPG','Electric'],font=('',15,'bold'),width=14)
    cb_ful.current(0)
    cb_ful.place(relx=.62,rely=.45)

    lbl_submit=Label(frm,image=imgtk8)
    lbl_submit.place(relx=.35,rely=.7)
    lbl_submit.bind("<Button>",createpool_db)

    but_reset=Label(frm,image=imgtk3)
    but_reset.place(relx=.55,rely=.7)
    but_reset.bind("<Button>",reset)

def updateprofile_frame():
    frm=Frame(win,highlightbackground='brown',highlightthickness=3)
    frm.place(x=300 , y=150,relwidth=.65, relheight=.55)

    lbl_wel=Label(frm,text=f"Welcome,{loginuser_row[0]}",font=('',15,'bold'),fg='green')
    lbl_wel.place(x=0,y=0)
    def reset(event):
        e_user.delete(0,"end")
        e_pass.delete(0,"end")
        e_pass.focus()
        e_mob.delete(0,"end")
        e_email.delete(0,"end")
    def logout(event):
        frm.destroy()
        home_frame()
    def back(event):
        frm.destroy()
        login_frame()
    def updatprofile_db(event):
        u=e_user.get()
        p=e_pass.get()
        m=e_mob.get()
        e=e_email.get()

        con=sqlite3.connect(database="carpool.sqlite")
        cursor=con.cursor()
        cursor.execute("update users set password=?,mobile=?,email=? where username=?",(p,m,e,u))
        con.commit()
        con.close
        messagebox.showinfo('',"updated")
        frm.destroy()
        login_frame()


    but_back=Label(frm,image=imgtk5)
    but_back.place(relx=.8,rely=0)
    but_back.bind("<Button>",back)

    but_logout=Label(frm,image=imgtk6)
    but_logout.place(relx=.9,rely=0)
    but_logout.bind("<Button>",logout)

    lbl_user=Label(frm,text="User_Name",font=('',15,'bold'))
    lbl_pass=Label(frm,text="Password",font=('',15,'bold'))
    lbl_mob=Label(frm,text="Mobile",font=('',15,'bold'))
    lbl_email=Label(frm,text="Email",font=('',15,'bold'))
    
    
    e_user=Entry(frm,font=('',15,'bold'),bd=3)
    e_user.focus()
    e_pass=Entry(frm,font=('',15,'bold'),bd=3)
    e_mob=Entry(frm,font=('',15,'bold'),bd=3)
    e_email=Entry(frm,font=('',15,'bold'),bd=3)

    
    lbl_user.place(x=220,y=30)
    e_user.place(x=350,y=30)

    lbl_pass.place(x=220,y=100)
    e_pass.place(x=350,y=100)

    lbl_mob.place(x=220,y=170)
    e_mob.place(x=350,y=170)

    lbl_email.place(x=220,y=240)
    e_email.place(x=350,y=240)

    but_new=Label(frm,image=imgtk9)
    but_new.place(x=300,y=300)
    but_new.bind("<Button>",updatprofile_db)

    but_reset=Label(frm,image=imgtk3)
    but_reset.place(x=450,y=300)
    but_reset.bind("<Button>",reset)

    con=sqlite3.connect(database="carpool.sqlite")
    cursor=con.cursor()
    cursor.execute("select password,mobile,email from users where username=?",(loginuser_row[0],))
    row=cursor.fetchone()
    e_user.delete(0,"end")
    e_user.insert(0,loginuser_row[0])
    e_user.configure(state="disabled")
    e_pass.delete(0,"end")
    e_pass.insert(0,row[0])
    e_mob.delete(0,"end")
    e_mob.insert(0,row[1])
    e_email.delete(0,"end")
    e_email.insert(0,row[2])
    con.commit()
    con.close
home_frame()
win.mainloop()


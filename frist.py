def addstudent():
    def Submitadd():
         id = idval.get() 
         name = nameval.get()
         mobile = mobileval.get() 
         email = emailval.get() 
         address = addressval.get()
         gender = genderval.get() 
         dob = dobval.get()
         addedtime = time.strftime('%H:%M:%S')
         addeddate = time.strftime('%d/%m/%Y')
         try:
             strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
             mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
             con.commit()
             res = messagebox.askyesnocancel('Notifications','Id {} Name {} Added sucessfully.. and  want to clean the form' . format(id,name),parent=addroot)
             if (res ==True):
                 idval.set('')
                 nameval.set('')
                 mobileval.set('')
                 emailval.set('')
                 addressval.set('')
                 genderval.set('')
                 dobval.set('')
         except:
             messagebox.showerror('Notifications' , 'Id Already Exist try another Id',parent=addroot)
         strr = 'select * from studentdata1'
         mycursor.execute(strr)
         datas = mycursor.fetchall()
         studenttable.delete(*studenttable.get_children())
         for i in datas:
             vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
             studenttable.insert('',END,values=vv)
             
             
    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+230+200')
    addroot.title('Student Management System')
    addroot.config(bg ='blue')
    #searchroot.iconbitmap('mana.ico')
    addroot.resizable(False,False)
################################################################  Add student Label
    
    idlabel = Label(addroot,text='Enter Id : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    idlabel.place(x=10,y=10)
    
        
    
    namelabel = Label(addroot,text='Enter Name : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    namelabel.place(x=10,y=70)
    
        
    mobilelabel = Label(addroot,text='Enter Mobile : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    mobilelabel.place(x=10,y=130)
    
        
    emaillabel = Label(addroot,text='Enter Email : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    emaillabel.place(x=10,y=190)
    
        
    addresslabel = Label(addroot,text='Enter Address : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    addresslabel.place(x=10,y=250)
    
        
    genderlabel = Label(addroot,text='Enter Gender : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    genderlabel.place(x=10,y=310)
    
        
    doblabel = Label(addroot,text='Enter D.O.B : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    doblabel.place(x=10,y=370)
    
#################################################################### Add Student Entrybox 

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    
    identry = Entry(addroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = idval)
    identry.place(x=250 , y=10)
    
    
    nameentry = Entry(addroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = nameval)
    nameentry.place(x=250 , y=70)
    
    
    mobileentry = Entry(addroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = mobileval)
    mobileentry.place(x=250 , y=130)
    
    
    emailentry = Entry(addroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = emailval)
    emailentry.place(x=250 , y=190)
    
    addressentry = Entry(addroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = addressval)
    addressentry.place(x=250 , y=250)
    
    
    genderentry = Entry(addroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = genderval)
    genderentry.place(x=250 , y=310)
    
    
    dobentry = Entry(addroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = dobval)
    dobentry.place(x=250 , y=370)
################################################################# submit button on student Label
    

    submitbtn = Button(addroot ,text = 'Submit' , font = ('roman' , 15 , 'bold'),width =20 ,bd = 5 ,activebackground='blue', 
                       activeforeground='white',bg = 'red', command=Submitadd)
    submitbtn.place(x=150 , y=425 )
    
    addroot.mainloop()
    
def searchstudent():
    def search():
        id = idval.get() 
        name = nameval.get()
        mobile = mobileval.get() 
        email = emailval.get() 
        address = addressval.get()
        gender = genderval.get() 
        dob = dobval.get()
        addeddate = time.strftime('%d/%m/%Y')
        if (id != ''):
            strr = 'select * from studentdata1 where id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall() 
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        if (name != ''):
            strr = 'select * from studentdata1 where name=%s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall() 
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv) 
        if (mobile != ''):
            strr = 'select * from studentdata1 where mobile=%s'
            mycursor.execute(strr,(mobile))
            datas = mycursor.fetchall() 
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)  
        if (email != ''):
            strr = 'select * from studentdata1 where email=%s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall() 
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        if (address != ''):
            strr = 'select * from studentdata1 where address=%s'
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall() 
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        if (gender != ''):
            strr = 'select * from studentdata1 where gender=%s'
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall() 
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        if (dob != ''):
            strr = 'select * from studentdata1 where dob=%s'
            mycursor.execute(strr,(dob))
            datas = mycursor.fetchall() 
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv) 
               
                
    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x530+230+150')
    searchroot.title('Student Management System')
    searchroot.config(bg ='firebrick1')
    #searchroot.iconbitmap('mana.ico')
    searchroot.resizable(False,False)
################################################################  Add student Label
    
    idlabel = Label(searchroot,text='Enter Id : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    idlabel.place(x=10,y=10)
    
        
    
    namelabel = Label(searchroot,text='Enter Name : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    namelabel.place(x=10,y=70)
    
        
    mobilelabel = Label(searchroot,text='Enter Mobile : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    mobilelabel.place(x=10,y=130)
    
        
    emaillabel = Label(searchroot,text='Enter Email : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    emaillabel.place(x=10,y=190)
    
        
    addresslabel = Label(searchroot,text='Enter Address : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    addresslabel.place(x=10,y=250)
    
        
    genderlabel = Label(searchroot,text='Enter Gender : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    genderlabel.place(x=10,y=310)
    
        
    
    
    doblabel = Label(searchroot,text='Enter D.O.B : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    doblabel.place(x=10,y=370)
    
    
    
    datelabel = Label(searchroot,text='Enter Date : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    datelabel.place(x=10,y=430)
   
####################################################################### Add Student Entrybox 

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    
    identry = Entry(searchroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = idval)
    identry.place(x=250 , y=10)
    
    
    nameentry = Entry(searchroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = nameval)
    nameentry.place(x=250 , y=70)
    
    
    mobileentry = Entry(searchroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = mobileval)
    mobileentry.place(x=250 , y=130)
    
    
    emailentry = Entry(searchroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = emailval)
    emailentry.place(x=250 , y=190)
    
    
    addressentry = Entry(searchroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = addressval)
    addressentry.place(x=250 , y=250)
    
    
    genderentry = Entry(searchroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = genderval)
    genderentry.place(x=250 , y=310)
    
    
    dobentry = Entry(searchroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = dobval)
    dobentry.place(x=250 , y=370)
    

    dateentry = Entry(searchroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = dateval)
    dateentry.place(x=250 , y=430)
    
########################################################## Add submit button     
    
    submitbtn = Button(searchroot ,text = 'Submit' , font = ('roman' , 15 , 'bold'),width =20 ,bd = 5 ,activebackground='blue', 
                       activeforeground='white',bg = 'red', command=search)
    submitbtn.place(x=150 , y=480 )
    
    searchroot.mainloop()

def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content ['values'][0]
    strr = 'delete from studentdata1 where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notification', 'Id {} delete   sucessfully...'.format(pp))
    strr = 'select * from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        studenttable.insert('',END,values=vv)
    

def updatestudent():
    def update():
        id = idval.get() 
        name = nameval.get()
        mobile = mobileval.get() 
        email = emailval.get() 
        address = addressval.get()
        gender = genderval.get() 
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()
        
        strr = 'update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notification', 'Id {} modified sucessfully...'.format(id),parent=updateroot)
        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)
        
    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x580+230+100')
    updateroot.title('Student Management System')
    updateroot.config(bg ='firebrick1')
    #updateroot.iconbitmap('mana.ico')
    updateroot.resizable(False,False)
#######################################################  Add student Label
    
    idlabel = Label(updateroot,text='Enter Id : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    idlabel.place(x=10,y=10)
    
        
    
    namelabel = Label(updateroot,text='Enter Name : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    namelabel.place(x=10,y=70)
    
        
    mobilelabel = Label(updateroot,text='Enter Mobile : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    mobilelabel.place(x=10,y=130)
    
        
    emaillabel = Label(updateroot,text='Enter Email : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    emaillabel.place(x=10,y=190)
    
        
    addresslabel = Label(updateroot,text='Enter Address : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    addresslabel.place(x=10,y=250)
    
        
    genderlabel = Label(updateroot,text='Enter Gender : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    genderlabel.place(x=10,y=310)
    
        
    
    
    doblabel = Label(updateroot,text='Enter D.O.B : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    doblabel.place(x=10,y=370)
    
    
    
    datelabel = Label(updateroot,text='Enter Date : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    datelabel.place(x=10,y=430)
    
    
    timelabel = Label(updateroot,text='Enter Time : ', bg = 'gold2', font = ('time' , 20 , 'bold'),relief=GROOVE,bd=3, width=12 , anchor = 'w')
    timelabel.place(x=10,y=490)
   
###################################################### Add Student Entrybox 

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()
    
    identry = Entry(updateroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = idval)
    identry.place(x=250 , y=10)
    
    
    nameentry = Entry(updateroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = nameval)
    nameentry.place(x=250 , y=70)
    
    
    mobileentry = Entry(updateroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = mobileval)
    mobileentry.place(x=250 , y=130)
    
    
    emailentry = Entry(updateroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = emailval)
    emailentry.place(x=250 , y=190)
    
    
    addressentry = Entry(updateroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = addressval)
    addressentry.place(x=250 , y=250)
    
    
    genderentry = Entry(updateroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = genderval)
    genderentry.place(x=250 , y=310)
    
    
    dobentry = Entry(updateroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = dobval)
    dobentry.place(x=250 , y=370)
    

    dateentry = Entry(updateroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = dateval)
    dateentry.place(x=250 , y=430)
    
    
    timeentry = Entry(updateroot, font = ('roman' ,15 , 'bold'), bd =5 , textvariable = timeval)
    timeentry.place(x=250 , y=490)

####################################################### add submit button    
    submitbtn = Button(updateroot ,text = 'Submit' , font = ('roman' , 15 , 'bold'),width =20 ,bd = 5 ,activebackground='blue', 
                       activeforeground='white',bg = 'red', command=update)
    submitbtn.place(x=150 , y=535 )
    
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if (len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])
     
    updateroot.mainloop()

def showstudent():
    strr = 'select * from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        studenttable.insert('',END,values=vv)
def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime = [],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),
        gender.append(pp[5]),dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd = ['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']
    df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd) 
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notification', 'Student data is saved{}'.format(paths))

          

def exitstudent():
    res = messagebox.askyesnocancel('Notification' , 'Do you want to exit?')
    if (res == True):
        root.destroy()

######################################################CONNECTION OF DATAVBASE
def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host= host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notification','Data is incorrect please try again' ,parent=dbroot)
            return
        try:
            strr = 'create database studentmanagementsystem1'
            mycursor.execute(strr)
            strr =  'use studentmanagementsystem1'
            mycursor.execute(strr)
            strr  = 'create table studentdata1(id int,name varchar(100),mobile varchar(12), email varchar(30),address varchar(100),gender varchar(12),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr =  'alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr =  'alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','database created and now you are connected to the database......', parent=dbroot)
        except:
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are connected to the database......',parent=dbroot)
        dbroot.destroy()    
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+700+200')
    #dbroot.iconbitmap('mana.ico')    dbroot.resizable(False,False)
    dbroot.config(bg='blue')
    
    #################################################  CONNECTEDdb LABELS
    hostlabel = Label(dbroot,text="Enter Host :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    hostlabel.place(x=10,y=10)
    
    Userlabel = Label(dbroot,text="Enter User :",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    Userlabel.place(x=10,y=70)
    
    Passwordlabel = Label(dbroot,text="Enter Password:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    Passwordlabel.place(x=10,y=130)
    
    ####################################################### connectdb Entry
    
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()
    
    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5, textvariable=hostval)
    hostentry.place(x=250,y=10)
    
    
    userentry = Entry(dbroot,font=('roman',15,'bold'),bd=5, textvariable=userval)
    userentry.place(x=250,y=70)
    
    passwordentry = Entry(dbroot,font=('roman',15,'bold'),bd=5, textvariable=passwordval)
    passwordentry.place(x=250,y=130)
    
    
    ############################################################# Connectdb button
    
    submitbutton = Button (dbroot , text = "Submit" , font=('roman' , 15 ,'bold'),bg='red',bd=5,width=20, 
                           activebackground = 'blue',activeforeground='white', command = submitdb)
    submitbutton.place(x=150 , y=190)
    
    dbroot.mainloop()
    
####################
def tick ():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :' +date_string+"\n" + "Time : "+time_string)
    clock.after(200,tick)
################################################################################ INTRO SLIDER
import random
colors = ['red']
def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)     
    SliderLabel.after(2,IntroLabelColorTick)
def IntroLabelTick():
    global count , text
    if (count>=len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count += 1
        
    SliderLabel.after(200,IntroLabelTick)    



from tkinter import*
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time
root =Tk()
root.title('student Management System')
root.config(bg='gold2')
root.geometry('1100x650+130+40')
#root.iconbitmap('mana.ico')
root.resizable(False,False)


###########################################################################################  frame

########################################################################## dataentry frame
DataEntryFrame = Frame(root,bg="gold2",relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=560)
frontlavel = Label(DataEntryFrame,text='--------Welcome--------',width=30,font=('arial' ,25, 'bold'),bg='gold2')
frontlavel.pack(side=TOP,expand=True)

addbtn = Button(DataEntryFrame, text= 'Add Student', width=15 , font=('arial' , 15 , 'bold' ),bd = 6,bg = 'skyblue3', activebackground= 'blue' , relief=RIDGE,
                activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame, text= 'Search Student', width=15 , font=('arial' ,15  , 'bold' ),bd = 6,bg = 'skyblue3', activebackground= 'blue' , relief=RIDGE,
                activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame, text= 'Delete Student', width=15 , font=('arial' , 15 , 'bold' ),bd = 6,bg = 'skyblue3', activebackground= 'blue' , relief=RIDGE,
                activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame, text= 'Update Student', width=15 , font=('arial' , 15 , 'bold' ),bd = 6,bg = 'skyblue3', activebackground= 'blue' , relief=RIDGE,
                activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showbtn = Button(DataEntryFrame, text= 'Show All', width=15 , font=('arial' , 15 , 'bold' ),bd = 6,bg = 'skyblue3', activebackground= 'blue' , relief=RIDGE,
                activeforeground='white',command=showstudent)
showbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame, text= 'Export data', width=15 , font=('arial' , 15 , 'bold' ),bd = 6,bg = 'skyblue3', activebackground= 'blue' , relief=RIDGE,
                activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame, text= 'Exit', width=15 , font=('arial' , 15 , 'bold' ),bd = 6,bg = 'skyblue3', activebackground= 'blue' , relief=RIDGE,
                activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)
################################################################################################ show data frame 

ShowDataFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=540,height=560)

###########--------------------------------  Showdata frame
style = ttk.Style()
style.configure('Treeview.Heading' , font=('chiller', 15 ,'bold'),foreground='red')
style.configure('Treeview',font=('times',15,'bold'),background='cyan',foreground='black')
scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
studenttable = Treeview(ShowDataFrame, columns=('Id','Name','Mobile No', 'Email','Address','Gender','D.O.B','Added Date','Added Time')
                        ,yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command = studenttable.xview)
scroll_y.config(command = studenttable.yview)
studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No',text='Mobile No')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added date')
studenttable.heading('Added Time',text='Added time')
studenttable['show']='headings'
studenttable.column('Id',width=100)    
studenttable.column('Name',width=200)
studenttable.column('Mobile No',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)
studenttable.pack(fill=BOTH,expand=1)
############################################################################################  slider

ss  =  'Welcome to Student Management System'
count  =  0
text = ' '
#################################################################################################
SliderLabel = Label(root,text=ss,font=('killer',19,'bold'),relief=RIDGE,borderwidth=5,width=35,bg='cyan')
SliderLabel.place(x=260,y=0)
IntroLabelTick()
IntroLabelColorTick()

#######################################################################################clock

clock =  Label(root,font=('times' ,11, 'bold' ),relief=RIDGE,borderwidth=2,bg='lawn green')
clock.place(x=0,y=0)

tick()

################################################################################### CONNECT DATABASE BUTTON
connectbutton = Button(root,text='CONNECT TO DB' , width=20,font=('times',13,'bold'),relief=RIDGE,borderwidth=5,bg='green2'
                       ,activebackground = 'blue',activeforeground='white' , command=Connectdb)
connectbutton.place(x=880 , y=0)
root.mainloop()
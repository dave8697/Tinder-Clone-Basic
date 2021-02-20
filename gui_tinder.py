from tkinter import *
from tinderbackend import *
from tkinter import messagebox

class TinderGUI:
    def __init__(self):
        self.root=Tk()
        self.root.title("Tinder")
        self.root.maxsize(600,600)
        self.tinderBackend=Tinder()


        self.lblWelcome=Label(self.root,width=25,height=2,bg='Red', font=('Arial',15,'bold'))
        self.lblWelcome.grid(row=0,column=0)
        self.lblWelcome.configure(text="Welcome")

        btnLogin=Button(self.root,width=10, height=2, bg='White', text="Login",
                        command=lambda: self.loginWindow()).grid(row=1,column=0)
        btnRegister = Button(self.root, width=10, height=2, bg='White', text="Register",
                             command=lambda: self.registerWindow()).grid(row=2, column=0)
        btnExit = Button(self.root, width=10, height=2, bg='White', text="Exit",
                         command=lambda: self.root.destroy()).grid(row=3, column=0)



        self.root.mainloop()


    def loginWindow(self):
        if(self.tinderBackend.currentUserId)!=0:
            self.showUserMenu()
        else:

            child=Toplevel(self.root)
            child.title("Login Screen")
            child.maxsize(500,500)

            lblLogin=Label(child,text="Email:",width=10,height=2,
                           font=('Arial',15)).grid(row=0,column=0)
            entEmail=Entry(child,width=33,font=('Arial',14))
            entEmail.grid(row=0,column=1)

            lblPass = Label(child, text="Password:", width=10, height=2,
                             font=('Arial', 15)).grid(row=1, column=0)
            entPass = Entry(child, width=33, font=('Arial', 14),show='*')
            entPass.grid(row=1, column=1)

            btnLogin=Button(child, text="Login",width=10, height=1,bg='Green',
                            font=('Arial',15), command=lambda: self.validate(child,entEmail.get(),entPass.get()))
            btnLogin.grid(row=2,column=1)

    def validate(self, child, email, password):
        result=self.tinderBackend.userLogin(email,password)

        if result:
            messagebox.showinfo('Success','Successfully Logged In!')
            self.showUserMenu()
            child.destroy()
        else:
            messagebox.showinfo('Wrong Input', 'Invalid Login!')


    def registerWindow(self):
        child = Toplevel(self.root)
        child.title("Registration Wiindow")
        child.maxsize(500, 500)

        lblName = Label(child, text="Name:", width=10, height=2,
                         font=('Arial', 15)).grid(row=0, column=0)
        entName = Entry(child, width=33, font=('Arial', 14))
        entName.grid(row=0, column=1)

        lblGender = Label(child, text="Gender:", width=10, height=2,
                          font=('Arial', 15)).grid(row=1, column=0)
        entGender = Entry(child, width=33, font=('Arial', 14))
        entGender.grid(row=1, column=1)

        lblCity = Label(child, text="City:", width=10, height=2,
                        font=('Arial', 15)).grid(row=2, column=0)
        entCity = Entry(child, width=33, font=('Arial', 14))
        entCity.grid(row=2, column=1)

        lblEmail = Label(child, text="Email:", width=10, height=2,
                        font=('Arial', 15)).grid(row=3, column=0)
        entEmail = Entry(child, width=33, font=('Arial', 14))
        entEmail.grid(row=3, column=1)

        lblPasw = Label(child, text="Password:", width=10, height=2,
                        font=('Arial', 15)).grid(row=4, column=0)
        entPass = Entry(child, width=33, font=('Arial', 14),show='*')
        entPass.grid(row=4, column=1)

        btnRegister = Button(child, text="Register", width=10, height=1, bg='Red',
                          font=('Arial', 15),
                             command=lambda: self.addUser(child,entName.get(),entGender.get(),entCity.get(),entEmail.get(),entPass.get()))
        btnRegister.grid(row=5, column=1)


    def addUser(self,child,name,gender,city,email,password):
        result = self.tinderBackend.userRegister(name, gender, city, email, password)
        if result:
            messagebox.showinfo('Success', 'Registration Successful')
        else:
            messagebox.showinfo('Unsuccessful','Email Already Exists')
        child.destroy()

    def showUserMenu(self):
        child = Toplevel(self.root)
        child.title("User Menu")
        child.maxsize(500, 500)

        uname=self.tinderBackend.fetchUserName()

        lblName = Label(child, text="Welcome %s"%((uname[0][0])), width=30, height=1,
                        font=('Arial', 15)).grid(row=0, column=0)
        btn1 = Button(child, text="View All Users", width=30, height=1, bg='Red',
                             font=('Arial', 15), command=lambda: self.showUsers())
        btn1.grid(row=1, column=0,pady=10)

        btn2 = Button(child, text="View Sent Proposals", width=30, height=1, bg='Red',
                      font=('Arial', 15), command=lambda: self.viewSent())
        btn2.grid(row=2, column=0,pady=10)

        btn3 = Button(child, text="View Received Proposals", width=30, height=1, bg='Red',
                      font=('Arial', 15),command=lambda: self.viewReceived())
        btn3.grid(row=3, column=0,pady=10)

        btn4 = Button(child, text="View Matches", width=30, height=1, bg='Red',
                      font=('Arial', 15),command=lambda: self.viewMatches())
        btn4.grid(row=4, column=0,pady=10)

        btn5 = Button(child, text="Log out", width=30, height=1, bg='Red',
                      font=('Arial', 15),command=lambda: self.logout(child))
        btn5.grid(row=5, column=0,pady=10)


    def showUsers(self):
        child = Toplevel(self.root)
        child.title("User List")
        child.maxsize(800, 800)
        child['bg']='Pink'
        userList=self.tinderBackend.viewAllUsers()
        i=1
        lWelcome=Label(child,text='User List',width=40,height=3,
                       font=('courier',15,'bold'),bg='Yellow').grid(row=0,column=0,columnspan=4)
        k=0
        for user in userList:
            if user[0]!=self.tinderBackend.currentUserId:

                lID=Label(child,text=user[0],width=10,height=2,font=('Arial',15)).grid(row=i,column=0)
                lName = Label(child, text=user[1], width=15, height=2, font=('Arial', 15)).grid(row=i, column=1)
                lGender = Label(child, text=user[2], width=15, height=2, font=('Arial', 15)).grid(row=i, column=2)
                lCity = Label(child, text=user[3], width=15, height=2, font=('Arial', 15)).grid(row=i, column=3)
                q=self.check(user[0])
                if q:
                    btnPropose = Button(child, text='Propose', width=10, height=2,
                                        font=('Arial', 14), bg='Yellow',
                                    command=lambda k=i: self.sendProposal(userList[k-1][0]))
                    btnPropose.grid(row=i, column=6)
                    i = i + 1
                else:
                    i=i+1

    def sendProposal(self,userid):
        k=self.tinderBackend.propose(userid)
        if k:
            messagebox.showinfo('Success', 'Yaay! Proposal Sent! Fingers Crossed!!')
        else:
            messagebox.showinfo('Unsuccesful', 'Kitni Baar Bhejega Bhai!!')

    def check(self,userid):
        k=self.tinderBackend.check(userid)
        return k

    def viewSent(self):
        child = Toplevel(self.root)
        child.title("Sent Proposals")
        child.maxsize(800, 800)
        child['bg'] = 'Pink'
        uList = self.tinderBackend.viewSentProposals()
        i = 1
        lWelcome = Label(child, text='Sent Proposals', width=40, height=3,
                         font=('courier', 15, 'bold'), bg='Yellow').grid(row=0, column=0, columnspan=4)
        for user in uList:
            lID = Label(child, text=user[3], width=10, height=2, font=('Arial', 15)).grid(row=i, column=0)
            lName = Label(child, text=user[4], width=15, height=2, font=('Arial', 15)).grid(row=i, column=1)
            lGender = Label(child, text=user[5], width=15, height=2, font=('Arial', 15)).grid(row=i, column=2)
            lCity = Label(child, text=user[6], width=15, height=2, font=('Arial', 15)).grid(row=i, column=3)
            i=i+1


    def viewReceived(self):
        child = Toplevel(self.root)
        child.title("Received Proposals")
        child.maxsize(800, 800)
        child['bg'] = 'Pink'
        uList = self.tinderBackend.viewReceivedProposals()
        i = 1
        lWelcome = Label(child, text='Received Proposals', width=40, height=3,
                         font=('courier', 15, 'bold'), bg='Yellow').grid(row=0, column=0, columnspan=4)
        k=0
        for user in uList:
            lID = Label(child, text=user[3], width=10, height=2, font=('Arial', 15)).grid(row=i, column=0)
            lName = Label(child, text=user[4], width=15, height=2, font=('Arial', 15)).grid(row=i, column=1)
            lGender = Label(child, text=user[5], width=15, height=2, font=('Arial', 15)).grid(row=i, column=2)
            lCity = Label(child, text=user[6], width=15, height=2, font=('Arial', 15)).grid(row=i, column=3)
            i = i + 1
            btnPropose = Button(child, text='Propose Back', width=10, height=2,
                                font=('Arial', 14), bg='Yellow',
                                command=lambda: self.sendProposal(uList[k-1][0]))
            btnPropose.grid(row=i, column=2)

    def viewMatches(self):
        child = Toplevel(self.root)
        child.title("Received Proposals")
        child.maxsize(800, 800)
        child['bg'] = 'Pink'
        uList = self.tinderBackend.viewMatches()
        i = 1
        lWelcome = Label(child, text='Matches', width=40, height=3,
                         font=('courier', 15, 'bold'), bg='Yellow').grid(row=0, column=0, columnspan=4)
        for user in uList:
            lID = Label(child, text=user[3], width=10, height=2, font=('Arial', 15)).grid(row=i, column=0)
            lName = Label(child, text=user[4], width=15, height=2, font=('Arial', 15)).grid(row=i, column=1)
            lGender = Label(child, text=user[5], width=15, height=2, font=('Arial', 15)).grid(row=i, column=2)
            lCity = Label(child, text=user[6], width=15, height=2, font=('Arial', 15)).grid(row=i, column=3)
            i = i + 1

    def logout(self,child):
        messagebox.showinfo('Thanks','Thanks For Coming By!!')
        self.tinderBackend.logout()
        child.destroy()
obj=TinderGUI()
import mysql.connector


class Tinder:
    def __init__(self):
        self.conn = mysql.connector.connect(
            user="root", password="", host="localhost", database="tinderclone")
        self.mycursor = self.conn.cursor()
        self.currentUserId = 0
        self.showMainMenu()

    def showMainMenu(self):
        print("\nWELCOME TO TINDERGARDEN!!\n")
        print("\nEnter 1 to Login\nEnter 2 to Register\nEnter 3 to Exit")
        ch = int(input())
        if (ch == 1):
            self.userLogin()
        elif (ch == 2):
            self.userRegister()
        elif (ch == 3):
            print("Thanks for coming by!!")
        else:
            print("Theek se enter kar!")
            self.showMainMenu()

    def userLogin(self):
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        self.mycursor.execute("""select * from `users` where `email` like '%s' and `password` like '%s'
        """ % (email, password))
        userList = self.mycursor.fetchall()
        i = 0
        for k in userList:
            i = i+1
        if i == 1:
            self.currentUserId = userList[0][0]
            self.showUserMenu()
        else:
            print("Invalid Login")
            self.showMainMenu()

    def showUserMenu(self):
        self.mycursor.execute("""
        select `name` from `users` where `userid` like '%s' 
        """ % (self.currentUserId))

        row = self.mycursor.fetchall()
        print("Hii ", row[0][0], "\n")
        print("""
        Enter 1 to View All Users
        Enter 2 to View Sent Proposals
        Enter 3 to View Received Proposals
        Enter 4 to View Matches
        Enter 5 to Logout
        """)
        ch = int(input())
        if ch == 1:
            self.viewAllUsers()
        elif ch == 2:
            self.viewSentProposals()
        elif ch == 3:
            self.viewReceivedProposals()
        elif ch == 4:
            self.viewMatches()
        elif ch == 5:
            print("Logged Out Succesfully")
            self.showMainMenu()
        else:
            print("Invalid Input mat daal!!")

    def userRegister(self):
        name = input("Enter your name: ")
        gender = input("Enter your gender: ")
        city = input("Enter your city: ")
        email = input("Enter your email: ")

        self.mycursor.execute("""
        select * from `users` where `email` like '%s'
        """ % (email))
        userList = self.mycursor.fetchall()
        i = 0
        for k in userList:
            i = i+1
        if i > 0:
            print("Email already exists!")
            self.showMainMenu()
        password = input("Enter your password: ")

        self.mycursor.execute("""insert into `users` (`name`, `gender`, `city`, `email`, `password`)
        values('%s','%s','%s','%s','%s')
        """ % (name, gender, city, email, password))

        self.conn.commit()

    def viewAllUsers(self):
        self.mycursor.execute("""
        select * from `users`
        """)
        userList = self.mycursor.fetchall()
        for row in userList:
            print(row[0], "\t", row[1], "\t", row[2], "\t", row[3], "\n")

        print("\n Enter the User ID of your crush, enter 69 to return\n")
        ch = int(input())
        if ch == 69:
            self.showUserMenu()
        else:
            self.propose(ch)

    def propose(self, julietid):

        self.mycursor.execute("""
        select * from `proposals` where `julietid` like '%s' and `romeoid` like '%s'
        """ % (julietid, self.currentUserId))
        row = self.mycursor.fetchall()
        i = 0
        for k in row:
            i = i+1
        if i > 0:
            print("Kitne baar propose karega bhai?? Chal Bhaag")
            self.showUserMenu()
        else:
            self.mycursor.execute("""
            insert into `proposals`(`romeoid`,`julietid`)
            values('%s', '%s')
            """ % (self.currentUserId, julietid))

            self.conn.commit()
            print("Yay!! Proposal Sent! Fingers Crossed!")
            self.showUserMenu()

    def viewSentProposals(self):
        self.mycursor.execute("""
        select * from `proposals` p join `users` u 
        on p.`julietid` = u.`userid` where 
        `romeoid` like '%s'
        """ % (self.currentUserId))

        rows = self.mycursor.fetchall()
        for row in rows:
            print(row[4], "\t", row[5], "\t", row[6], "\t", row[7], "\n")

    def viewReceivedProposals(self):
        self.mycursor.execute("""
        select * from `proposals` p join `users` u 
        on p.`romeoid`= u.`userid` where `julietid` like '%s'
        """ % (self.currentUserId))

        rows = self.mycursor.fetchall()
        for row in rows:
            print(row[3], "\t", row[4], "\t", row[5],
                  "\t", row[6], "\t", row[7], "\n")

        print("\n Enter the User ID to Match , enter 69 to return\n")
        ch = int(input())
        if ch == 69:
            self.showUserMenu()
        else:
            self.propose(ch)

    def viewMatches(self):
        self.mycursor.execute("""
        select * from `proposals` p join `users` u
        on p.`julietid`=u.`userid` where `romeoid`like '%s' 
         and `julietid` in 
        (select `romeoid` from `proposals` where `julietid` like '%s')
        """ % (self.currentUserId, self.currentUserId))

        rows = self.mycursor.fetchall()
        for r in rows:
            print(r[4])


obj = Tinder()

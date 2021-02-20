import mysql.connector


class Tinder:
    def __init__(self):
        self.conn = mysql.connector.connect(
            user="root", password="", host="localhost", database="tinderclone")
        self.mycursor = self.conn.cursor()
        self.currentUserId = 0

    def userLogin(self, email, password):
        self.mycursor.execute("""select * from `users` where `email` like '%s' and `password` like '%s'
        """ % (email, password))
        userList = self.mycursor.fetchall()
        i = 0
        for k in userList:
            i = i+1
        if i == 1:
            self.currentUserId = userList[0][0]
            return True
        else:
            return False

    def userRegister(self, name, gender, city, email, password):
        self.mycursor.execute("""
        select * from `users` where `email` like '%s'
        """ % (email))
        userList = self.mycursor.fetchall()
        i = 0
        for k in userList:
            i = i+1
        if i > 0:
            return False
        else:
            self.mycursor.execute("""insert into `users` (`name`, `gender`, `city`, `email`, `password`)
                                    values('%s','%s','%s','%s','%s')
                                    """ % (name, gender, city, email, password))
            self.conn.commit()
            return True

    def fetchUserName(self):
        self.mycursor.execute("""
                select `name` from `users` where `userid` like '%s' 
                """ % (self.currentUserId))

        name = self.mycursor.fetchall()
        return name

    def viewAllUsers(self):
        self.mycursor.execute("""
        select * from `users`
        """)
        userList = self.mycursor.fetchall()
        return userList

    def propose(self, julietid):

        self.mycursor.execute("""
        select * from `proposals` where `julietid` like '%s' and `romeoid` like '%s'
        """ % (julietid, self.currentUserId))
        row = self.mycursor.fetchall()
        i = 0
        for k in row:
            i = i+1
        if i > 0:
            return False
        else:
            self.mycursor.execute("""
            insert into `proposals`(`romeoid`,`julietid`)
            values('%s', '%s')
            """ % (self.currentUserId, julietid))

            self.conn.commit()
            return True

    def check(self, julietid):
        self.mycursor.execute("""
                select * from `proposals` where `julietid` like '%s' and `romeoid` like '%s'
                """ % (julietid, self.currentUserId))
        row = self.mycursor.fetchall()
        i = 0
        for k in row:
            i = i + 1
        if i > 0:
            return False
        else:
            return True

    def viewSentProposals(self):
        self.mycursor.execute("""
        select * from `proposals` p join `users` u 
        on p.`julietid` = u.`userid` where 
        `romeoid` like '%s'
        """ % (self.currentUserId))

        rows = self.mycursor.fetchall()
        return rows

    def viewReceivedProposals(self):
        self.mycursor.execute("""
        select * from `proposals` p join `users` u 
        on p.`romeoid`= u.`userid` where `julietid` like '%s'
        """ % (self.currentUserId))

        rows = self.mycursor.fetchall()
        return rows

    def viewMatches(self):
        self.mycursor.execute("""
           select * from `proposals` p join `users` u
           on p.`julietid`=u.`userid` where `romeoid`like '%s' 
            and `julietid` in 
           (select `romeoid` from `proposals` where `julietid` like '%s')
           """ % (self.currentUserId, self.currentUserId))

        rows = self.mycursor.fetchall()
        return rows

    def logout(self):
        self.currentUserId = 0

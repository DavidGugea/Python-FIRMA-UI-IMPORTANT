import tkinter, tkinter.messagebox, sqlite3, pickle, sys, random, glob 

root = tkinter.Tk()

class Project:
    def __init__(self, master):
        self.master = master 
                
        self.master.title("Firma")
        self.master.geometry("350x250")

        #Create Login Form 
        
        tkinter.Label(self.master, text="Firma Login", font=('Consolas', 20)).place(x=80, y=10)
        
        tkinter.Label(self.master, text="Username").place(x=30, y=80)
        self.USERNAME_ENTRY = tkinter.Entry(self.master, width=30)
        self.USERNAME_ENTRY.place(x=100, y=80)
        tkinter.Label(self.master, text="Password").place(x=30, y=110)
        self.PASSWORD_ENTRY = tkinter.Entry(self.master, width=30)
        self.PASSWORD_ENTRY.place(x=100, y=110)
        tkinter.Label(self.master, text="UEC Code").place(x=30, y=140)
        self.UEC_ENTRY = tkinter.Entry(self.master, width=30)
        self.UEC_ENTRY.place(x=100, y=140)
        
        self.submitButton = tkinter.Button(self.master, text="Confirm", command=self.CONFIRM_DATA)
        self.END_MASTER = tkinter.Button(self.master, text="End", command=self.END_MASTER_WINDOW)
        
        self.submitButton.place(x=298, y=225)
        self.END_MASTER.place(x=0, y=225)

        #Create Login Form 
    def CONFIRM_DATA(self):
        self.connection = sqlite3.connect('userData.db')
        self.connection_cursor = self.connection.cursor()

        self.connection_cursor.execute("SELECT * FROM userTable")
        
        ###########################
        self.USER_DATA_TABLE = []
        self.USER_LIST = []
        ###########################

        for DB_ELEMENT in self.connection_cursor:
            self.USER_DATA_TABLE.append(DB_ELEMENT)

        self.USERNAME = self.USERNAME_ENTRY.get()
        self.PASSWORD = self.PASSWORD_ENTRY.get()
        self.UEC = self.UEC_ENTRY.get()
        
        if not self.USERNAME or not self.PASSWORD or not self.UEC:
            tkinter.messagebox.showwarning("Warning", "Please insert the username, the password and the UEC")
            sys.exit(0)

        self.user_find_BOOLEAN = False 
        
        for DB_TUPLE in self.USER_DATA_TABLE:
            if DB_TUPLE[-1] == self.USERNAME and DB_TUPLE[-2] == self.PASSWORD:
                self.user_find_BOOLEAN = True 
                self.USER_LIST = DB_TUPLE
                break 
            else:
                self.user_find_BOOLEAN = False 

        if bool(self.user_find_BOOLEAN) == False:
            tkinter.messagebox.showerror("Error", "Error ! The username and the password that you introduced aren't correct. Try again !")
            sys.exit(0)

        # Read the UEC code from the binary file 
        dfile = open("fBinary_UEC_SCRIPT.bin", "rb")
        self.BinaryList = []
        while True:
            try:
                self.BinaryList.append(pickle.load(dfile))
            except:
                break
        # self.BinaryList[0] is -- > Admin
        # self.BinaryList[1] is -- > Worker 

        #print(self.BinaryList)
        
        if self.UEC != self.BinaryList[0] and self.UEC != self.BinaryList[1]:
            tkinter.messagebox.showerror("Error", "Sorry, but your UEC code is not valid. Try again !")
            sys.exit(0)
        
        if self.UEC == self.BinaryList[0] and self.USER_LIST[-3] == "User":
            tkinter.messagebox.showerror("Error", "Sorry, but your UEC code is not valid with your account !")
            sys.exit(0)
        elif self.UEC == self.BinaryList[1] and self.USER_LIST[-3] == "Admin":
            tkinter.messagebox.showerror("Error", "Sorry, but your UEC code is not valid with your account !")
            sys.exit(0)
        else:
            if self.UEC == self.BinaryList[0]:
                self.RAISE_ADMINISTRATOR_UI()
            elif self.UEC == self.BinaryList[1]:
                self.RAISE_WORKER_UI()
    def RAISE_ADMINISTRATOR_UI(self):
        self.ADMINISTRATOR_MASTER = tkinter.Toplevel(self.master)
        self.ADMINISTRATOR_MASTER.title("Administrator UI")
        self.ADMINISTRATOR_MASTER.geometry("1400x700")

        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Administrator Menu", font=("Times", 20)).place(x=600, y=0)

        #### INSERT USER MENU ####
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Insert User Here", font=("Bahnschrift", 13)).place(x=0, y=55)
            
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="First Name", font=("Courier", 10)).place(x=0, y=90)
        self.INSERT_FirstName_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.INSERT_FirstName_entry.place(x=100, y=90)
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Second Name", font=("Courier", 10)).place(x=230, y=90)
        self.INSERT_SecondName_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.INSERT_SecondName_entry.place(x=330, y=90)

        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Age", font=("Courier", 10)).place(x=0, y=120)
        self.INSERT_Age_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.INSERT_Age_entry.place(x=100, y=120)
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Street Name", font=("Courier", 10)).place(x=230, y=120)
        self.INSERT_StreetName_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.INSERT_StreetName_entry.place(x=330, y=120)

        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Post Code", font=("Courier", 10)).place(x=0, y=150)
        self.INSERT_PostCode_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.INSERT_PostCode_entry.place(x=100, y=150)
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="City", font=("Courier", 10)).place(x=230, y=150)
        self.INSERT_City_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.INSERT_City_entry.place(x=330, y=150)

        tkinter.Label(self.ADMINISTRATOR_MASTER, text="House Number", font=("Courier", 10)).place(x=0,y=180)
        self.INSERT_HouseNumber_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.INSERT_HouseNumber_entry.place(x=100, y=180)
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Salary", font=("Courier", 10)).place(x=230, y=180)
        self.INSERT_Salary_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.INSERT_Salary_entry.place(x=330, y=180)

        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Hours Worked", font=("Courier", 10)).place(x=0, y=210)
        self.INSERT_HoursWorked_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.INSERT_HoursWorked_entry.place(x=100, y=210)
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="User Type", font=("Courier", 10)).place(x=230, y=210)
        self.INSERT_UserType_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.INSERT_UserType_entry.place(x=330, y=210)

        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Password", font=("Courier", 10)).place(x=0, y=240)
        self.INSERT_Password_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.INSERT_Password_entry.place(x=100, y=240)
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Username", font=("Courier", 10)).place(x=230, y=240)
        self.INSERT_Username_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.INSERT_Username_entry.place(x=330, y=240)
        
        self.INSERT_BUTTON = tkinter.Button(self.ADMINISTRATOR_MASTER, text="Insert User in DB")
        self.INSERT_BUTTON.configure(command=self.INSERT_METHOD)
        self.INSERT_BUTTON.place(x=160, y=270)
        #### INSERT USER MENU #### 

        #### UPDATE USER MENU ####
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Update User Here(First and Second name are indicators)", font=("Bahnschrift", 13)).place(x=950, y=25)
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="If you don't want to update something write NONE", font=("Bahnschrift", 13)).place(x=950, y= 55)

        tkinter.Label(self.ADMINISTRATOR_MASTER, text="First Name", font=("Courier", 10)).place(x=900, y=90)
        self.UPDATE_FirstName_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.UPDATE_FirstName_entry.place(x=1000, y=90)
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Second Name", font=("Courier", 10)).place(x=1130, y=90)
        self.UPDATE_SecondName_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.UPDATE_SecondName_entry.place(x=1230, y=90)
        
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Age", font=("Courier", 10)).place(x=900, y=120)
        self.UPDATE_Age_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.UPDATE_Age_entry.place(x=1000, y=120)
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Street Name", font=("Courier", 10)).place(x=1130, y=120)
        self.UPDATE_StreetName_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.UPDATE_StreetName_entry.place(x=1230, y=120)

        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Post Code", font=("Courier", 10)).place(x=900, y=150)
        self.UPDATE_PostCode_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.UPDATE_PostCode_entry.place(x=1000, y=150)
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="City", font=("Courier", 10)).place(x=1130, y=150)
        self.UPDATE_City_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.UPDATE_City_entry.place(x=1230, y=150)

        tkinter.Label(self.ADMINISTRATOR_MASTER, text="House Number", font=("Courier", 10)).place(x=900, y=180)
        self.UPDATE_HouseNumber_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.UPDATE_HouseNumber_entry.place(x=1000, y=180)
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Salary", font=("Courier", 10)).place(x=1130, y=180)
        self.UPDATE_Salary_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.UPDATE_Salary_entry.place(x=1230, y=180)

        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Hours Worked", font=("Courier", 10)).place(x=900, y=210)
        self.UPDATE_HoursWorked_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.UPDATE_HoursWorked_entry.place(x=1000, y=210)
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="User Type", font=("Courier", 10)).place(x=1130, y=210)
        self.UPDATE_UserType_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.UPDATE_UserType_entry.place(x=1230, y=210)

        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Password", font=("Courier", 10)).place(x=900, y=240)
        self.UPDATE_Password_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.UPDATE_Password_entry.place(x=1000, y=240)
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Username", font=("Courier", 10)).place(x=1130, y=240)
        self.UPDATE_Username_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.UPDATE_Username_entry.place(x=1230, y=240)

        self.UPDATE_BUTTON = tkinter.Button(self.ADMINISTRATOR_MASTER, text="Update")
        self.UPDATE_BUTTON.configure(command=self.UPDATE_METHOD)
        self.UPDATE_BUTTON.place(x=1115, y=270)
        #### UPDATE USER MENU ####

        #### DELETE USER MENU ####
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Delete User Here", font=("Bahnschrift", 13)).place(x=0, y=300)

        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Username", font=("Courier", 10)).place(x=0, y=335)
        self.DELETE_USERNAME_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.DELETE_USERNAME_entry.place(x=100, y=335)
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Password", font=("Courier", 10)).place(x=230, y=335)
        self.DELETE_PASSWORD_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.DELETE_PASSWORD_entry.place(x=330, y=335)
        
        self.DELETE_BUTTON = tkinter.Button(self.ADMINISTRATOR_MASTER, text="Delete User")
        self.DELETE_BUTTON.configure(command=self.DELETE_METHOD)
        self.DELETE_BUTTON.place(x=160, y=365)
        #### DELETE USER MENU ####
        
        #### SHOW INFO USER MENU ####
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Show User Here", font=("Bahnschrift", 13)).place(x=950, y=300)
        
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="Username", font=("Courier", 10)).place(x=900, y=330) 
        self.SHOWINFO_Username_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.SHOWINFO_Username_entry.place(x=1000, y=330)
        tkinter.Label(self.ADMINISTRATOR_MASTER, text="First name", font=("Courier", 10)).place(x=1130, y=330)
        self.SHOWINFO_FirstName_entry = tkinter.Entry(self.ADMINISTRATOR_MASTER, width=20)
        self.SHOWINFO_FirstName_entry.place(x=1230, y=330)

        self.SHOWINFO_BUTTON = tkinter.Button(self.ADMINISTRATOR_MASTER, text="Show info")
        self.SHOWINFO_BUTTON.configure(command=self.SHOWINFO_METHOD)
        self.SHOWINFO_BUTTON.place(x=1300, y=360)
        #### SHOW INFO USER MENU ####

    def SHOWINFO_METHOD(self):
        if not self.SHOWINFO_Username_entry.get() or not self.SHOWINFO_FirstName_entry.get():
            tkinter.messagebox.showerror("Error !", "Sorry, but you have to fill in all the input boxes !")
        else:
            self.connection_cursor.execute("SELECT * FROM userTable")
            userFind = False 
            self.TRACK_SHOWINFO_LIST = []
            for TRACK_DB in self.connection_cursor:
                if TRACK_DB[0] == self.SHOWINFO_FirstName_entry.get() and TRACK_DB[-1] == self.SHOWINFO_Username_entry.get():
                    userFind = True 
                    self.TRACK_SHOWINFO_LIST = TRACK_DB
                    break 
                else:
                    userFind = False 
                    continue 

            if bool(userFind) == False:
                tkinter.messagebox.showwarning("Warning", "Sorry, but the user that you are looking for, doesn't exist !")
                sys.exit(0)
            
            self.SHOWINFO_LEVEL = tkinter.Toplevel(self.ADMINISTRATOR_MASTER)
            self.SHOWINFO_LEVEL.title("User Info !")
            tkinter.Label(self.SHOWINFO_LEVEL, text="First name: {0}".format(self.TRACK_SHOWINFO_LIST[0])).pack()
            tkinter.Label(self.SHOWINFO_LEVEL, text="Second name: {0}".format(self.TRACK_SHOWINFO_LIST[1])).pack()
            tkinter.Label(self.SHOWINFO_LEVEL, text="Age: {0}".format(self.TRACK_SHOWINFO_LIST[2])).pack()
            tkinter.Label(self.SHOWINFO_LEVEL, text="Street name: {0}".format(self.TRACK_SHOWINFO_LIST[3])).pack()
            tkinter.Label(self.SHOWINFO_LEVEL, text="Post code: {0}".format(self.TRACK_SHOWINFO_LIST[4])).pack()
            tkinter.Label(self.SHOWINFO_LEVEL, text="City: {0}".format(self.TRACK_SHOWINFO_LIST[5])).pack()
            tkinter.Label(self.SHOWINFO_LEVEL, text="House number: {0}".format(self.TRACK_SHOWINFO_LIST[6])).pack()
            tkinter.Label(self.SHOWINFO_LEVEL, text="Salary: {0}".format(self.TRACK_SHOWINFO_LIST[7])).pack()
            tkinter.Label(self.SHOWINFO_LEVEL, text="Hours worked: {0}".format(self.TRACK_SHOWINFO_LIST[8])).pack()
            tkinter.Label(self.SHOWINFO_LEVEL, text="User type: {0}".format(self.TRACK_SHOWINFO_LIST[9])).pack()

    def DELETE_METHOD(self):
        if not self.DELETE_USERNAME_entry.get() or not self.DELETE_PASSWORD_entry.get():
            tkinter.messagebox.showerror("Error !", "Sorry, but you must fill in all the input boxes !")
        else:
            self.connection_cursor.execute("SELECT * FROM userTable")
            userFind = False 
            for DB_TRACK_UDB in self.connection_cursor:
                if DB_TRACK_UDB[-1] == self.DELETE_USERNAME_entry.get() and DB_TRACK_UDB[-2] == self.DELETE_PASSWORD_entry.get():
                    userFind = True 
                    break
                else:
                    userFind = False 
                    continue 

            if bool(userFind) == False:
                tkinter.messagebox.showwarning("WARNING", "Sorry, but the user that you are looking for, couldn't be found in the database. Try again !")
                sys.exit(0)
            
            self.connection_cursor.execute("DELETE FROM userTable WHERE Username='{0}' AND Password='{1}'".format(
                self.DELETE_USERNAME_entry.get(), self.DELETE_PASSWORD_entry.get()))
            self.connection.commit()
            tkinter.messagebox.showinfo("Info", "The user has been succesfully deleted from the database !")
    def UPDATE_METHOD(self):
        if not self.UPDATE_FirstName_entry.get() or not self.UPDATE_SecondName_entry.get() or not self.UPDATE_Age_entry.get() or not self.UPDATE_StreetName_entry.get() or not self.UPDATE_PostCode_entry.get() or not self.UPDATE_City_entry.get() or not self.UPDATE_HouseNumber_entry.get() or not self.UPDATE_Salary_entry.get() or not self.UPDATE_HoursWorked_entry.get() or not self.UPDATE_UserType_entry.get() or not self.UPDATE_Password_entry.get() or not self.UPDATE_Username_entry.get():
            tkinter.messagebox.showwarning("Warning !", "Sorry, but you have to fill in all the input boxes !")
        else:
            self.connection_cursor.execute("SELECT * FROM userTable")
            track_userFind = False 
            for DB_TRACK_TUPLE in self.connection_cursor:
                if DB_TRACK_TUPLE[0] == self.UPDATE_FirstName_entry.get() and DB_TRACK_TUPLE[1] == self.UPDATE_SecondName_entry.get():
                    track_userFind = True 
                    break 
                else:
                    track_userFind = False 
                    continue 

            if bool(track_userFind) == False:
                tkinter.messagebox.showerror("Error", "Sorry, but the user that you are trying to find, couldn't be found in the database !")
                sys.exit(0) 

            trackBool = True 
            try:
                trackVar = eval(self.UPDATE_Age_entry.get()) 
            except:
                trackBool = False 
            try:
                trackVar = eval(self.UPDATE_PostCode_entry.get())
            except:
                trackBool = False 
            try:
                trackVar = eval(self.UPDATE_HouseNumber_entry.get())
            except:
                trackBool = False 
            try:
                trackVar = eval(self.UPDATE_Salary_entry.get())
            except:
                trackBool = False 
            try:
                trackVar = eval(self.UPDATE_HoursWorked_entry.get())
            except:
                trackBool = False 
            
            if bool(trackBool) == False:
                tkinter.messagebox.showwarning("Warning !", "Sorry, but you have to fill in correctly the input boxes !")
            else:
                if self.UPDATE_Age_entry.get() != "NONE":
                    self.us_reform("Age", int(self.UPDATE_Age_entry.get()))
                if self.UPDATE_StreetName_entry.get() != "NONE":
                    self.us_reform("StreetName", str(self.UPDATE_StreetName_entry.get()))
                if self.UPDATE_PostCode_entry.get() != "NONE":
                    self.us_reform("PostCode", int(self.UPDATE_PostCode_entry.get()))
                if self.UPDATE_City_entry.get() != "NONE":
                    self.us_reform("City", str(self.UPDATE_City_entry.get()))
                if self.UPDATE_HouseNumber_entry.get() != "NONE":
                    self.us_reform("HouseNumber", int(self.UPDATE_HouseNumber_entry.get()))
                if self.UPDATE_Salary_entry.get() != "NONE":
                    self.us_reform("Salary", int(self.UPDATE_Salary_entry.get()))
                if self.UPDATE_UserType_entry.get() != "NONE":
                    self.us_reform("UserType", str(self.UPDATE_UserType_entry.get()))
                if self.UPDATE_Password_entry.get() != "NONE":
                    self.us_reform("Password", str(self.UPDATE_Password_entry.get()))
                if self.UPDATE_Username_entry.get() != "NONE":
                    self.us_reform("Username", str(self.UPDATE_Username_entry.get()))
                self.connection.commit()
                tkinter.messagebox.showinfo("Info", "The user data has been succesfully updated !")
    def us_reform(self, var, replace_Var):
        if type(replace_Var) == int or type(replace_Var) == float:
            self.connection_cursor.execute("UPDATE userTable SET {0}={1} WHERE FirstName='{2}' AND SecondName='{3}'".format(
                var, replace_Var, self.UPDATE_FirstName_entry.get(), self.UPDATE_SecondName_entry.get()))
        else:
            self.connection_cursor.execute("UPDATE userTable SET {0}='{1}' WHERE FirstName='{2}' AND SecondName='{3}'".format(
                var, replace_Var, self.UPDATE_FirstName_entry.get(), self.UPDATE_SecondName_entry.get()))
    def INSERT_METHOD(self):
        if not self.INSERT_FirstName_entry.get() or not self.INSERT_SecondName_entry.get() or not self.INSERT_Age_entry.get() or not self.INSERT_StreetName_entry.get() or not self.INSERT_PostCode_entry.get() or not self.INSERT_City_entry.get() or not self.INSERT_HouseNumber_entry.get() or not self.INSERT_Salary_entry.get() or not self.INSERT_HoursWorked_entry.get() or not self.INSERT_UserType_entry.get() or not self.INSERT_Password_entry.get() or not self.INSERT_Username_entry.get():
            tkinter.messagebox.showerror("Error", "Sorry, but you have to fill in all the input boxes !")
        else:
            Q = tkinter.messagebox.askyesno("Confirm", "Hi ! Are you sure that you want to add this user in the database ?")
            if Q:
                ### CHECK ###
                trackError = False  #Boolean Var 
                
                try:
                    trackVar = eval(self.INSERT_Age_entry.get())
                except:
                    trackError = True 
                try:
                    trackVar = eval(self.INSERT_PostCode_entry.get()) 
                except:
                    trackError = True 
                try:
                    trackVar = eval(self.INSERT_HouseNumber_entry.get())
                except:
                    trackError = True 
                try:
                    trackVar = eval(self.INSERT_Salary_entry.get())
                except:
                    trackError = True 
                try:
                    trackVar = eval(self.INSERT_HoursWorked_entry.get())
                except:
                    trackError = True 
                
                if bool(trackError) == True:
                    tkinter.messagebox.showerror("Error", "Sorry, but you have to put the correct input in the boxes.")
                elif bool(trackError) == False:
                    self.connection_cursor.execute("INSERT INTO userTable VALUES('{0}', '{1}', {2}, '{3}', {4}, '{5}', {6}, {7}, {8}, '{9}', '{10}', '{11}')".format(self.INSERT_FirstName_entry.get(), self.INSERT_SecondName_entry.get(), self.INSERT_Age_entry.get(), self.INSERT_StreetName_entry.get(), self.INSERT_PostCode_entry.get(), self.INSERT_City_entry.get(), self.INSERT_HouseNumber_entry.get(), self.INSERT_Salary_entry.get(), self.INSERT_HoursWorked_entry.get(), self.INSERT_UserType_entry.get(), self.INSERT_Password_entry.get(), self.INSERT_Username_entry.get()))
                    self.connection.commit()
                    tkinter.messagebox.showinfo("Info", "The user has been added in the database !")
            else:   
                tkinter.messagebox.showinfo("Info", "The user hasn't been added in the database !")
    def RAISE_WORKER_UI(self):
        self.WORKER_MASTER = tkinter.Toplevel(self.master)
        #tkinter.Label(self.WORKER_MASTER, text="ASD").pack()
        self.WORKER_MASTER.title("Worker UI")
        tkinter.Label(self.WORKER_MASTER, text="First Name: {0}".format(self.USER_LIST[0])).pack()
        tkinter.Label(self.WORKER_MASTER, text="Second Name: {0}".format(self.USER_LIST[1])).pack()
        tkinter.Label(self.WORKER_MASTER, text="Age: {0}".format(self.USER_LIST[2])).pack()
        tkinter.Label(self.WORKER_MASTER, text="Street name: {0}".format(self.USER_LIST[3])).pack()
        tkinter.Label(self.WORKER_MASTER, text="Post code: {0}".format(self.USER_LIST[4])).pack()
        tkinter.Label(self.WORKER_MASTER, text="City: {0}".format(self.USER_LIST[5])).pack()
        tkinter.Label(self.WORKER_MASTER, text="House number: {0}".format(self.USER_LIST[6])).pack()
        tkinter.Label(self.WORKER_MASTER, text="Salary: {0}".format(self.USER_LIST[7])).pack()
        tkinter.Label(self.WORKER_MASTER, text="Hours worked: {0}".format(self.USER_LIST[8])).pack()
        tkinter.Label(self.WORKER_MASTER, text="User type: {0}".format(self.USER_LIST[9])).pack()
        tkinter.Label(self.WORKER_MASTER, text="Password: {0}".format(self.USER_LIST[10])).pack()
        tkinter.Label(self.WORKER_MASTER, text="Username: {0}".format(self.USER_LIST[11])).pack()
    def END_MASTER_WINDOW(self):
        self.master.destroy()
project = Project(root)
root.mainloop()

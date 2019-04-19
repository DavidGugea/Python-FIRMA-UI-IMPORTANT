import random, sqlite3

connection = sqlite3.connect("userData.db")
connection_cursor = connection.cursor()

connection_cursor.execute("CREATE TABLE IF NOT EXISTS userTable(FirstName TEXT, SecondName TEXT, Age INTEGER, StreetName TEXT, PostCode INTEGER, City TEXT, HouseNumber INTEGER, Salary INTEGER, HoursWorked INTEGER, UserType TEXT, Password TEXT, Username TEXT)")
connection.commit()

for i in range(1, 101):
    data_FirstName = "FirstName{0}".format(i)
    data_SecondName = "SecondName{0}".format(i)
    data_Age = random.randint(18, 66)
    data_StreetName = "StreetName{0}".format(random.randint(1, 101))
    data_PostCode = random.randint(10000, 99999)
    data_City = "City{0}".format(random.randint(1, 51))
    data_HouseNumber = random.randint(1, 25)
    data_Salary = random.randint(2000, 5001)
    data_HoursWorked = random.randint(5, 11)
    data_UserType = random.choice(["Admin", "User"])
    data_password = "Password{0}".format(i)
    data_username = "Username{0}".format(i)
    connection_cursor.execute("INSERT INTO userTable VALUES('{0}', '{1}', {2}, '{3}', {4}, '{5}', {6}, {7}, {8}, '{9}', '{10}', '{11}')".format(
        data_FirstName, data_SecondName, data_Age, data_StreetName, data_PostCode, data_City, data_HouseNumber, data_Salary, data_HoursWorked, data_UserType, data_password, data_username))
connection.commit()

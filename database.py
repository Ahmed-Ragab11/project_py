
import sqlite3 

mydb = sqlite3.connect('my_db.sqlite',detect_types=sqlite3.PARSE_DECLTYPES)
mydb.row_factory = sqlite3.Row
mycursor = mydb.cursor()

    

mydb = sqlite3.connect('my_db.sqlite',detect_types=sqlite3.PARSE_DECLTYPES)
mycursor = mydb.cursor()
mycursor.execute("""DROP TABLE IF EXISTS Doctor;""")
mycursor.execute("""DROP TABLE IF EXISTS Nurse;""")
mycursor.execute("""DROP TABLE IF EXISTS Patient;""")

mycursor.execute(
    "CREATE TABLE Doctor (DOC_ID INT NOT NULL, DOC_Fname VARCHAR(255), DOC_Lname VARCHAR(255), DOC_SSN INT, DOC_Email VARCHAR(255), DOC_Password VARCHAR(255), DOC_Specialisation VARCHAR(255), DOC_PhoneNo INT, PRIMARY KEY(DOC_ID))")

mycursor.execute(
    "CREATE TABLE Nurse (Nurse_ID INT NOT NULL, Nurse_Fname VARCHAR(255), Nurse_Lname VARCHAR(255), Nurse_SSN INT, Nurse_Email VARCHAR(255), Nurse_Password VARCHAR(255), Nurse_PhoneNo INT, PRIMARY KEY(Nurse_ID))")

mycursor.execute(
    "CREATE TABLE Patient (PAT_ID INT NOT NULL, PAT_Fname VARCHAR(255), PAT_Lname VARCHAR(255), PAT_SSN INT, PAT_Email VARCHAR(255), PAT_Password VARCHAR(255), PAT_RoomNo INT, PAT_PhoneNo INT, PRIMARY KEY(PAT_ID))")



##

###
sql = "INSERT INTO Doctor (DOC_ID, DOC_Fname, DOC_Lname, DOC_SSN, DOC_Email, DOC_Password, DOC_Specialisation, DOC_PhoneNo) VALUES ('1', 'Ayman', 'Adel', '26409', 'aman.adel@yahoo.com','12345678900', 'Radiology', '01067841235')"

sql1 = "INSERT INTO Doctor (DOC_ID, DOC_Fname, DOC_Lname, DOC_SSN, DOC_Email, DOC_Password, DOC_Specialisation, DOC_PhoneNo) VALUES ('2', 'Ezzat', 'Mohamed', '27305', 'ezzat.mohamed@yahoo.com','12345', 'Surgey', '01267841235')"
# val = [
#     ('1', 'Ayman', 'Adel', '26409', 'aman.adel@yahoo.com',
#      '12345678900', 'Radiology', '01067841235'),
#     ('2', 'Ezzat', 'Mohamed', '27305', 'ezzat.mohamed@yahoo.com',
#      '12345', 'Surgey', '01267841235'),
#     ('3', 'Essam', 'Adel', '26608', 'essam.adel@gmail.com',
#      '78900', 'Medicine', '01167841235'),
#     ('4', 'Tamer', 'Ahmed', '2640', 'tamer.ahmed@icloud.com',
#      '000000', 'Radiology', '01567841235'),
# ]
# mycursor.executemany(sql, val)
mycursor.execute(sql)
mycursor.execute(sql1)

mydb.commit()

####
sql = "INSERT INTO Patient (PAT_ID, PAT_Fname, PAT_Lname, PAT_SSN, PAT_Email, PAT_Password, PAT_RoomNo, PAT_PhoneNo) VALUES ('1', 'Aly', 'Ibrahim', '2851','aly@hotmail.com', 'aly1458693', '3201', '01008939915')"
mycursor.execute(sql)
mydb.commit()


# ##
# sql = "INSERT INTO Patient (PAT_ID, PAT_Fname, PAT_Lname, PAT_SSN, PAT_Email, PAT_Password, PAT_RoomNo, PAT_PhoneNo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
# val = [
#     ('1', 'Aly', 'Ibrahim', '2851',
#      'aly@hotmail.com', 'aly1458693', '3201', '01008939915'),
#     ('2', 'Khaled', 'Aly', '28511',
#      'khaled@yahoo.com', '265165165', '18205', '01206480119'),
#     ('3', 'Ahmed', 'Mossa', '25501',
#      'ahmed@gmail.com', 'sacsa653135', '20503', '01062670067'),

# ]

# mycursor.executemany(sql, val)
# mydb.commit()


###

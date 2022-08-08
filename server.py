import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from flask import flash, render_template, jsonify

mydb = sqlite3.connect('my_db.sqlite',detect_types=sqlite3.PARSE_DECLTYPES,check_same_thread=False) # conneccting to the database
mydb.row_factory = sqlite3.Row
mycursor = mydb.cursor()



app = Flask(__name__)


@app.route('/')
def home():
    data = ""
    return render_template("home.html", data=data)


@app.route('/home')
def index():
    data = ""
    return render_template("home.html", data=data)

# ------------------------ Signup ----------------------- #

@app.route('/addpatient', methods=['POST', 'GET'])
def addpatient():
    if request.method == "POST":  # check if there is post data
        pfname = request.form['pfnme']
        plname = request.form['pLname']
        pssn = request.form['pssn']
        pid = request.form['pID']
        pemail = request.form['pemail']
        ppassword = request.form['ppsw']
        rno = request.form['roomnumber']
        pno = request.form['ptelephone']
        print(pfname)
        sql = "INSERT INTO Patient (PAT_Fname, PAT_Lname, PAT_SSN, PAT_ID, PAT_Email,  PAT_Password, PAT_RoomNo, PAT_PhoneNo) VALUES ('{pfname}', '{plname}', '{pssn}', '{pid}', '{pemail}', '{ppassword}','{rno}', '{pno}')"
        val = (pfname, plname, pssn, pid, pemail, ppassword, rno, pno)
        mycursor.execute(sql, val)
        mydb.commit()
    return render_template('patientsignup.html')


@app.route('/adddoctor', methods=['POST', 'GET'])
def adddoctor():
    if request.method == "POST":  # check if there is post data
        fname = request.form['fnme']
        lname = request.form['Lname']
        ssn = request.form['ssn']
        did = request.form['ID']
        email = request.form['email']
        password = request.form['psw']
        specialization = request.form['Specialization']
        no = request.form['telephone']
        print(fname)
        sql = f"""INSERT INTO Doctor (DOC_Fname, DOC_Lname, DOC_SSN, DOC_ID, DOC_Email,  DOC_Password, DOC_Specialisation, DOC_PhoneNo) VALUES ('{fname}', '{lname}', '{ssn}', '{did}', '{email}', '{password}', '{specialization}', '{no}')"""
        mycursor.execute(sql)
        mydb.commit()
    return render_template('doctorsignup.html')


# ------------------------- End of Signup ------------------ #

# ------------------------ Login ---------------------- #
@app.route("/login/<string:prof>", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login(prof=1):
    if request.method == "POST":
        global userid
        global select
        userid = request.form["lID"]
        userpassword = request.form["lpsw"]
        select = request.form.get('type')

        if select == "doctor":
            sql = f"""SELECT  DOC_Fname, DOC_Password  FROM Doctor  Where DOC_ID='{userid}'"""
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            print("**********************************")
            print(myresult)
            prof = "doctorProfile"
            myresult = myresult
            if myresult[1] == userpassword:
                return render_template('home.html', data=myresult)
            else:
                return render_template('alert.html')

        elif select == "patient":
            sql = f"""SELECT  PAT_Fname, PAT_Password  FROM Patient  Where PAT_ID='{userid}'"""
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            print("**********************************")
            print(myresult)
            prof = "patientProfile"
            myresult = myresult 
            if myresult[1] == userpassword:
                return render_template('home.html', data=myresult)
            else:
                return render_template('alert.html')

    else:
        return render_template('loginuser.html')
# ------------------------ End of Login ----------------- #

# ----------------------- Contact Us ---------------------- #
@app.route('/contactus', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        cNo = 3
        pat_code = request.form["pat_code"]
        msg = request.form["message"]
        sql = f"""INSERT INTO Complain (Comp_No, PAT_Code, Comp_Msg) VALUES ('{cNo}', '{pat_code}','{msg}')"""
        mycursor.execute(sql)
        mydb.commit()
        return render_template("index.html")
    else:
        return render_template("contact.html")
# ----------------------- End of Contact Us ---------------------- #

# ---------------------------  PATIENT ---------------------- #
@app.route('/viewPatient')
def viewPatient():
    mycursor.execute("SELECT * FROM Patient")
    row_headers = [x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    patientData = {
        'message': "data retrieved",
        'rec': myresult,
        'header': row_headers
    }
    return render_template('viewPatient.html', data=patientData)
# ---------------------------  End of  PATIENT ---------------------- #

# ---------------------- Doctors -------------------- #

@app.route('/viewDoctor')
def viewDoctor():
    if request.method == 'POST':
        return render_template('index.html')
    else:
        mycursor.execute("SELECT * FROM Doctor")
        # this will extract row headers
        row_headers = [x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        doctorData = {
            'message': "data retrieved",
            'rec': myresult,
            'header': row_headers
        }
        return render_template('viewDoctor.html', data=doctorData)

# ---------------------- End of Doctors -------------------- #

@app.route('/myprofile')
def my_profile():

    if select == 'doctor':
        id = userid
        sql = f"""SELECT * FROM Doctor WHERE DOC_ID = '{id}'"""
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        return render_template('doctorProfile.html', data=myresult)

    elif  select == 'patient':
        id = userid
        sql = f"""SELECT * FROM Patient WHERE PAT_ID = '{id}'"""
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        return render_template('patientProfile.html', data=myresult)

if __name__ == '__main__':
    userid = ''
    app.run()

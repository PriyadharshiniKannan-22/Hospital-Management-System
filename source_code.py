import pymysql

def selection():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='Priya@2005', database='hospital')
    cursor = db.cursor()
    print('-----------------------------------WELCOME TO HOSPITAL MANAGEMENT-----------------------------------')
    print("1.PATIENT")
    print("2.STAFF")
    print("3.APPOINTMENT")
    ch=int(input("Enter your choice (1-3):"))
    if ch==1:
        print('WELCOME TO PATIENT MANAGEMENT')
        print('a.NEW PATIENT DETAILS')
        print('b.UPDATE PATIENT DETAILS')
        print('c.DELETE PATIENT DETAILS')
        c=input("Enter your choice (a-c):")
        print('Initially the details are..')
        display1()
        if c=='a':
            insert1()
            print('Modified details are..')
            display1()
        elif c=='b':
            update1()
            print('Modified details are..')
            display1()
        elif c=='c':
            delete1()
            print('Modified details are..')
            display1()
        else:
            print('Enter correct choice...!!')
            selection()
    elif ch==2:
        print('WELCOME TO ADMIN MANAGEMENT')
        print('a.NEW STAFF DETAILS')
        print('b.UPDATE STAFF DETAILS')
        print('c.DELETE STAFF DETAILS')
        c=input("Enter your choice (a-c) : ")
        print('Initially the details are..')
        display2()
        if c=='a':
            insert2()
            print('Modified details are..')
            display2()
        elif c=='b':
            update2()
            print('Modified details are..')
            display2()
        elif c=='c':
            delete2()
            print('Modified details are..')
            display2()
        else:
            print('Enter correct choice...!!')
            selection() 
    elif ch==3:
        print('WELCOME TO APPOINTMENT MANAGEMENT')
        print('a.NEW STAFF DETAILS')
        print('b.UPDATE STAFF DETAILS')
        print('c.EXEMPT STAFF DETAILS')
        c=input("Enter your choice(a-c) : ")
        print('Initially the details are..')
        display3()
        if c=='a':
            insert3()
            print('Modified details are..')
            display3()
        elif c=='b':
            update3()
            print('Modified details are..')
            display3()
        elif c=='c':
            delete3()
            print('Modified details are..')
            display3()
        else:
            print('Enter correct choice...!!')
            selection()
    else:
        print('Enter correct choice...!!')
        selection()

def insert1():
    patient_id=input("Enter patient id: ")
    f_name=input("Enter first name: ")
    l_name=input("Enter last name: ")
    gender=input("Enter gender(M/F): ")
    phno=input("Enter phone number: ")
    db =pymysql.connect(user='root',password='Priya@2005',host='localhost',database='hospital')
    cursor = db.cursor()
    sql="INSERT INTO patient(patient_id,f_name,l_name,gender,phno) VALUES ( '%s','%s','%s','%s','%s')"%(patient_id,f_name,l_name,gender,phno)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def display1():
    try:
        db =pymysql.connect(user='root',password='Priya@2005',host='localhost',database='hospital')
        cursor = db.cursor()
        sql = "SELECT * FROM patient"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            patient_id= c[0]
            f_name= c[1]
            l_name=c[2]
            gender=c[3]
            phno=c[4]
        print("(patient_id=%s,f_name=%s,l_name=%s,gender=%s,phno=%s)"% (patient_id,f_name,l_name,gender,phno))
    except:
        print ("Error: unable to fetch data")
        db.close()

def update1():
    try:
        db =pymysql.connect(user='root',password='Priya@2005',host='localhost',database='hospital')
        cursor = db.cursor()
        sql = "SELECT * FROM patient"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            patient_id= c[0]
            f_name= c[1]
            l_name=c[2]
            gender=c[3]
            phno=c[4]
    except:
        print ("Error: unable to fetch data")
        print()
    tempst=input("Enter first name : ")
    temp=input("Enter new patient id : ")
    try:
        sql = "Update patient set patient_id=%s where f_name='%s'" % (temp,tempst)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print (e)
        db.close()

def delete1():
    try:
        db=pymysql.connect(user='root',password='Priya@2005',host='localhost',database='hospital')
        cursor = db.cursor()
        sql = "SELECT * FROM patient"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            patient_id= c[0]
            f_name= c[1]
            l_name=c[2]
            gender=c[3]
            phno=c[4]
    except:
        print ("Error: unable to fetch data")
    temp=int(input("\nEnter patient_id to be deleted : "))
    try:
        sql = "delete from patient where patient_id='%s'" %(temp)
        ans=input("Are you sure you want to delete the record(y/n) : ")
        if ans=='y' or ans=='Y':
            cursor.execute(sql)
            db.commit()
    except Exception as e:
        print (e)
        db.close()

def insert2():
    s_id=input("Enter the staff id: ")
    s_name=input("Enter the staff name : ")
    dept=input("Enter the department : ")
    ph_no=input("Enter the phone number : ")
    db =pymysql.connect(user='root',password='Priya@2005',host='localhost',database='hospital')
    cursor = db.cursor()
    sql="INSERT INTO staff(s_id,s_name,dept,ph_no) VALUES ('%s' ,'%s','%s','%s')"%(s_id,s_name,dept,ph_no)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def display2():
    try:
        db =pymysql.connect(user='root',password='Priya@2005',host='localhost',database='hospital')
        cursor = db.cursor()
        sql = "SELECT * FROM staff"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            s_id = c[0]
            s_name= c[1]
            dept=c[2]
            ph_no=c[3]
        print ("(s_id=%s,s_name=%s,dept=%s,ph_no=%s)" %(s_id,s_name,dept,ph_no))
    except:
        print ("Error: unable to fetch data")
        db.close()

def update2():
    try:
        db =pymysql.connect(user='root',password='Priya@2005',host='localhost',database='hospital')
        cursor = db.cursor()
        sql = "SELECT * FROM staff"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            s_id = c[0]
            s_name= c[1]
            dept=c[2]
            ph_no=c[3]
        print ("(s_id=%s,s_name=%s,dept=%s,ph_no=%s)" %(s_id,s_name,dept,ph_no))
    except:
        print ("Error: unable to fetch data")
        print()
        tempst=input("Enter Staff name: ")
        temp=input("Enter Staff id: ")
    try:
        sql = "Update staff set s_id='%s' where s_name='%s'" %(temp,tempst)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print (e)
        db.close()

def delete2():
    try:
        db =pymysql.connect(user='root',password='Priya@2005',host='localhost',database='hospital')
        cursor = db.cursor()
        sql = "SELECT * FROM staff"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            s_id = c[0]
            s_name= c[1]
            dept=c[2]
            ph_no=c[3]
        print ("(s_id=%s,s_name=%s,dept=%s,ph_no=%s)" %(s_id,s_name,dept,ph_no))
    except:
        print ("Error: unable to fetch data")
        temp=int(input("\nEnter s_id to be deleted : "))
    try:
        sql = "delete from staff where s_id='%s'" % (temp)
        ans=input("Are you sure you want to delete the record(y/n) : ")
        if ans=='y' or ans=='Y':
            cursor.execute(sql)
            db.commit()
    except Exception as e:
        print (e)
        db.close()

def insert3():
    s_id=input("Enter Staff id: ")
    patient_id=input("Enter patient id: ")
    department= input("Enter department: ")
    a_date=input("Enter date of appointment: ")
    a_time=float(input("Enter time of appointment: "))
    db =pymysql.connect(user='root',password='Priya@2005',host='localhost',database='hospital')
    cursor = db.cursor()
    sql="INSERT INTO appointment(s_id,patient_id,department,a_date,a_time) VALUES ( '%s','%s','%s','%s,%s')"%(s_id,patient_id,department,a_date,a_time)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def display3():
    try:
        db =pymysql.connect(user='root',password='Priya@2005',host='localhost',database='hospital')
        cursor = db.cursor()
        sql = "SELECT * FROM appointment"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            s_id= c[0]
            patient_id=c[1]
            department=c[2]
            a_date=c[3]
            a_time=c[4]
        print("(s_id=%s,patient_id=%s,department=%s,a_date=%s,a_time=%s) " %(s_id,patient_id,department,a_date,a_time))
    except:
        print("Error: unable to fetch data")
    db.close()
    
def update3():
    try:
        db=pymysql.connect(user='root',password='Priya@2005',host='localhost',database='hospital')
        cursor = db.cursor()
        sql = "SELECT * FROM appointment"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            s_id= c[0]
            patient_id=c[1]
            department=c[2]
            a_date=c[3]
            a_time=c[4]
        print("(s_id=%s,patient_id=%s,department=%s,a_date=%s,a_time=%s) " %(s_id,patient_id,department,a_date,a_time))
    except:
        print ("Error: unable to fetch data")
        print()
        tempst=input("Enter patient id : ")
        temp=input("Enter new appointment time : ")
    try:
        sql = "Update appointment set a_time=%s where patient_id='%s'" % (temp,tempst)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print (e)
        db.close()

def delete3():
    try:
        db =pymysql.connect(user='root',password='Priya@2005',host='localhost',database='hospital')
        cursor = db.cursor()
        sql = "SELECT * FROM appointment"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            s_id= c[0]
            patient_id=c[1]
            department=c[2]
            a_date=c[3]
            a_time=c[4]
        print("(s_id=%s,patient_id=%s,department=%s,a_date=%s,a_time=%s) " %(s_id,patient_id,department,a_date,a_time))
    except:
        print ("Error: unable to fetch data")
        temp=input("\nEnter s_id to be deleted : ")
    try:
        sql = "delete from appointment where s_id='%s'" % (temp)
        ans=input("Are you sure you want to delete the record(y/n) : ")
        if ans=='y' or ans=='Y':
            cursor.execute(sql)
            db.commit()
    except Exception as e:
        print (e)
        db.close()

selection()
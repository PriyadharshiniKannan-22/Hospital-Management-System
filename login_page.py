import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', password='Priya@2005', database='hospital')
cur = conn.cursor()
'''cur.execute("create table admin(username varchar(25) primary key, passwrd varchar(25) not null)")'''

print("=========================WELCOME TO START HOSPITAL MANAGEMENT SYSTEM=========================")

import datetime as dt
print(dt.datetime.now())
def login():
    print("1.Register")
    print()
    print("2.Login")
    print()
    n=int(input("enter your choice="))
    print()
    if n==1:
        name=input("Enter a Username=")
        print()
        passwd=(input("Enter a four digit password="))
        print()
        Qry="INSERT INTO admin(username,passwrd) values (%s,%s)" 
        values=(name,passwd)
        cur.execute(Qry,values) 
        conn.commit()
        print()
        print("USER successfully created") 
        login()
    if n==2:
        name=input("Enter a Username=")
        print()
        passwd=(input("Enter a four digit password="))
        V_Sql_Sel="select * from admin where username=%s and passwrd=%s" 
        values=(name,passwd)
        cur.execute(V_Sql_Sel,values) 
        result=cur.fetchall()
        print(result)
        if cur.rowcount==0:
            print()
            print("Invalid username or password")
        else:
            print("User entered successfully")
login()
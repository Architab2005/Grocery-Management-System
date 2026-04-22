import mysql.connector as sql
from config import DB_CONFIG

conn = sql.connect(**DB_CONFIG)
#c.execute('create table customer_details(phone_no int(13),cust_name varchar(25),cost float(10))')
#print('table created')
#c.execute('create table product_details(product_name varchar(25),product_cost float(10))')
#print('table created')
#c.execute('create table staff_details(staff_name varchar(25),staff_work varchar(10),staff_age int(3), staff_salary float(10),phone_no int(13))')
#print('table created')
import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='1234',database='grocerymanagementsystem')
if conn.is_connected():
    print('successfully connected')
c=conn.cursor()
print('grocery shop management system')
print('1.Login')
print('2.Logout')
choice=int(input('enter your choice:'))
if choice==1:
    user_name=input('enter your user name=')
    password=input('enter your password=')
    while user_name=='asql' and password=='1234':
        print('connected successfully')
        print('Grocery Management')
        print('1.Customer details')
        print('2.Product details')
        print('3.Staff details')
        print('4.View all Customer details')
        print('5.View all Product details')
        print('6.View all Staff details')
        print('7.View one Customer details')
        print('8.see one product details')
        print('9.see one staff details')
        print('10.Stock')
        print('11.exit')
        choice=int(input('enter the choice'))
        if choice==1:
            cust_name=input('enter your name=')
            phone_no=int(input('enter your  phone number='))
            cost=float(input('enter your cost='))
            sql_insert="insert into customer_details values("+str(phone_no)+",'"+(cust_name)+"',"+str(cost)+")"
            c.execute(sql_insert)
            conn.commit()
            print('data is updated')
            
        elif choice==2:
            product_name=input('enter  product name=')
            product_cost=float(input('enter the cost='))
            sql_insert="insert into product_details values(""'"+(product_name)+"',"+str(product_cost)+")"
            c.execute(sql_insert)
            conn.commit()
            print('data is updated')
 
 
        elif choice==3:
            staff_name=input('enter your name=')
            staff_work=input('enter your work=')
            staff_age=int(input('enter your  age='))
            staff_salary=float(input('enter your salary='))
            phone_no =int(input('enter your  phone number='))
            sql_insert="insert into worker_details values(" "'"+(staff_name)+"'," "'"+(staff_work)+"',"+str(staff_age)+","+str(staff_salary)+","+str(phone_no)+ ")"
            c.execute(sql_insert)
            conn.commit()
            print('data is updated')
 
 
        elif choice==4:
            t=conn.cursor()
            t.execute('select*from customer_details')
            record=t.fetchall()
            for i in record:
                print(i)
                
        elif choice==5:
            t=conn.cursor()
            t.execute('select*from product_details')
            record=t.fetchall()
            for i in record:
                print(i)
 
        elif choice==6:
            t=conn.cursor()
            t.execute('select*from worker_details')
            record=t.fetchall()
            for i in record:
                print(i)
                
                
        elif choice==7:
            a=input('enter your name')
            t='select*from customer_details where cust_name=("{}")'.format(a)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print(v)
      
                 
        elif choice==8:
            a=input('enter your product_name')
            t='select*from product_details where product_name=("{}")'.format(a)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print(v)
        elif choice==9:
            c=conn.cursor()
            c.execute("SELECT * FROM worker_details")
            result=c.fetchone()
            print(result)
        elif choice==10:
            print('******************************************')
            f=open('test.txt','r')
            data=f.read()
            print(data)
            f.close()
            print('******************************************')
        elif choice==11:
            print("Do you want to continue(y/n):")
            exit()          
    else:
        print('wrong password, try again ')
if choice==2:
    exit()





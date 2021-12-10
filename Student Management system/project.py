import mysql.connector
import logging
import sshtunnel
from sshtunnel import SSHTunnelForwarder

ssh_host = '192.168.43.63'
ssh_username = 'rushi'
ssh_password = 'rushi12345'
database_username = 'root'
database_password = 'Rushitoshatwad@12345'
database_name = 'testdb'
localhost = '127.0.0.1'

def open_ssh_tunnel(verbose=False):

    if verbose:
        sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG
    
    global tunnel
    tunnel = SSHTunnelForwarder(
        (ssh_host, 22),
        ssh_username=ssh_username,
        ssh_password=ssh_password,
        remote_bind_address = ('127.0.0.1', 3306)
    )

    tunnel.start()

def mysql_connect():
    global connection
    
    connection = mysql.connector.connect(
        host='127.0.0.1',
        user=database_username,
        passwd=database_password,
        db=database_name,
        port=tunnel.local_bind_port
    )

def mysql_disconnect():
    
    connection.close()

def close_ssh_tunnel():

    tunnel.close



# Define global variables
student_database = database_name


def display_menu():
    print("--------------------------------------")
    print(" Welcome to Student Management System")
    print("---------------------------------------")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Quit")

def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")

    Roll = input("Enter_roll_no: ")
    Name = input("Enter_name: ")
    Age = input("ENter_age: ")
    Email = input("Enter_email: ")
    Phone = input("Enter_phone: ")


    open_ssh_tunnel()
    mysql_connect()
    mycursor = connection.cursor()
    sql = "INSERT INTO stud_info VALUES(%s, %s, %s, %s, %s)"
    val = (Roll, Name, Age, Email, Phone)
    mycursor.execute(sql, val)
    connection.commit()
    print(mycursor.execute(sql, val))
    mysql_disconnect()
    close_ssh_tunnel()


def view_students():
    open_ssh_tunnel()
    mysql_connect()
    mycursor = connection.cursor()
    sql = "SELECT Name FROM testdb.stud_info"
    mycursor.execute(sql)
    for x in mycursor:
        print(x)
    mysql_disconnect()
    close_ssh_tunnel()
    



def update_student():
    print("""Enter_operation:
             1) Update Age
             2) Update Email
             3) Update Phone Number""")

    resp = input("Enter_operaton: ")

    if resp == '1':
        Name = input("Enter_name: ")
        Age = input("Enter_updated_age: ")
        open_ssh_tunnel()
        mysql_connect()
        mycursor = connection.cursor()
        sql = "UPDATE stud_info SET Age = %s WHERE Name = %s"
        val = (Name, Age)
        mycursor.execute(sql, val)
        connection.commit()
        print(mycursor.execute(sql, val))
        mysql_disconnect()
        close_ssh_tunnel()
    elif resp == '2':
        Name = input("Enter_name: ")
        Email = input("Enter_updated_Email: ")
        open_ssh_tunnel()
        mysql_connect()
        mycursor = connection.cursor()
        sql = "UPDATE stud_info SET Age = %s WHERE Name = %s"
        val = (Name, Email)
        mycursor.execute(sql, val)
        connection.commit()
        print(mycursor.execute(sql, val))
        mysql_disconnect()
        close_ssh_tunnel()
        
    elif resp == '3':
        Name = input("Enter_name: ")
        Phone = input("Enter_updated_Phone_number: ")
        open_ssh_tunnel()
        mysql_connect()
        mycursor = connection.cursor()
        sql = "UPDATE stud_info SET Age = %s WHERE Name = %s"
        val = (Name, Phone)
        mycursor.execute(sql, val)
        connection.commit()
        print(mycursor.execute(sql, val))
        mysql_disconnect()
        close_ssh_tunnel()
    else:
        quit()
    


def delete_student():
    Name = input("Enter_name: ")
    open_ssh_tunnel()
    mysql_connect()
    mycursor = connection.cursor()
    sql = "DELETE FROM stud_info WHERE Name = %s"
    mycursor.execute(sql, Name)
    connection.commit()
    print(mycursor.execute(sql, Name))
    mysql_disconnect()
    close_ssh_tunnel()

while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    else:
        break

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")

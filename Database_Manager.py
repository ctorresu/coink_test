import sqlite3
import os

def createDB():
    DB = sqlite3.connect("database/customers.db")
    DB.commit()
    DB.close()

def createTable():
    DB = sqlite3.connect("database/customers.db")
    cursor = DB.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS table_customer (
            name text,
            email text, 
            city text
        )"""
    )
    DB.commit()
    DB.close()

def insertRow(name, email, city):
    DB = sqlite3.connect("database/customers.db")
    cursor = DB.cursor()
    instruction = f"INSERT INTO table_customer VALUES ('{name}', '{email}','{city}')"
    cursor.execute(instruction)
    DB.commit()
    DB.close()

def readrows(table_name):
    DB = sqlite3.connect("database/customers.db")
    cursor = DB.cursor()
    instruction = f"SELECT * FROM '{table_name}' "
    cursor.execute(instruction)
    datos = cursor.fetchall()
    print(datos)
    DB.commit()
    DB.close()

def insertManyRows(customer_list):
    for custormer in customer_list:

        name, email, city = custormer[0], custormer[1], custormer[2]
        DB = sqlite3.connect("database/customers.db")
        
        cursor = DB.cursor()
        instruction = f"INSERT INTO table_customers VALUES ('{name}','{email}','{city}')"
        cursor.execute(instruction)
        DB.commit()
        DB.close()

def delete_dates(name):
    DB = sqlite3.connect("database/customers.db")
    instruction = f"DELETE from table_customer where name={name}"
    cursor = DB.cursor()
    cursor.execute(instruction)
    DB.commit()
    DB.close()

def check_dates(name, email, city):
    while name=="" or email=="" or city=="":
        return ("La información que ingresaste no es válida")  
    return ("Anyone")

createDB()
createTable()

if __name__=="__main__":
    readrows("table_customer")

    list_new_users=[["Cristian","Gonzalez","Paipa"],
                    ["Andrea","Castillo", "Pereira"],
                    ["Gianluca","Machi","Roms"]]
    
    # insertManyRows(list_new_users)

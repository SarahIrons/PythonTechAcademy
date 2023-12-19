##DATABASES AND PYTHON CHALLENGE
##Complete these actions:
##1. Create a database table in RAM named Roster that includes the fields ‘Name’, ‘Species’ and ‘IQ.’
##2. Populate your new table with the following values:
##1 Jean-Baptiste Zorg, Human, 122
##2 Korben Dallas, Meat Popsicle, 100
##3 Ak'not, Mangalore, -5
##3. Update the Species of Korben Dallas to be Human.
##4. Display the names and IQs of everyone in the table who is classified as Human.

import sqlite3
from sqlite3 import Error

def create_connection ():
    """ create a database connection to a database that resides
        in the memory
    """
conn = sqlite3.connect(':memory:')
if conn:  
    print("Connection OK")
            
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()


# ----Example Python Program to create tables in-memory databases----https://pythontic.com/# Import the sqlite3 module
import sqlite3

# Create database connection to an in-memory database
conn= sqlite3.connect(":memory:")

# Obtain a cursor object
cursor = conn.cursor()

# Create a table in the in-memory database
createTable = "CREATE TABLE ROSTER(Name varchar(25), Species varchar(25), IQ varchar(4))"
cursor.execute (createTable)

 #below function for inserting the table and multi entries; taking following code from pynative.com#

def insertMultipleRecords(recordList):
        sqlite_insert_query ="""INSERT INTO ROSTER(Name, Species, IQ) VALUES (?, ?, ?);"""   
        cursor.executemany(sqlite_insert_query, recordList)
        conn.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into ROSTER")
        conn.commit()
        

recordsToInsert = [("Jean-Baptiste Zorg", "Human", "122"),("Korben Dallas", "Meat Popsicle", "100"),("Ak'not", "Mangalore", "-5")]

insertMultipleRecords(recordsToInsert)
cursor.execute("select * from SQLite_master where type=\"table\"")
print("Tables available in the in-memory database(main):")
tables = cursor.fetchall()
for table in tables:
    print("------------------------------------------------------")

    print("DB Object Name: %s"%(table[0]))

    print("Name of the database object: %s"%(table[1]))

    print("Table Name: %s"%(table[2]))

    print("Root page: %s"%(table[3]))

    print("SQL statement: %s"%(table[4]))

    print("------------------------------------------------------")


def print_roster ():
    cursor.execute('SELECT * FROM ROSTER')
    result =cursor.fetchall()
    for row in result:
        print(row)
        print("\n")

def print_row_by_name(passedName):
        cursor.execute("SELECT  *  FROM Roster WHERE Name = '{name}' ".format(name=passedName))
        result =cursor.fetchall()
        for row in result:
            print(row)
            print("\n")

        
print_row_by_name('Korben Dallas')
# Updating the record :"Update the Species of Korben Dallas to be Human."
def sql_update_korben():
        sql_update_query  = "Update ROSTER set Species = 'Human' where Name = 'Korben Dallas'"
        cursor.execute(sql_update_query)
        conn.commit()
        print("Record updated successfully. ")
        
sql_update_korben()
print_row_by_name('Korben Dallas')

#Display the names and IQs of everyone in the table who is classified as Human    
def sql_list_humans():
    cursor.execute("SELECT Name, IQ FROM ROSTER where Species ='Human'" )
    for i in cursor:
        print(i)

sql_list_humans()
conn.close()






if __name__ == '__main__':
    create_connection()
   

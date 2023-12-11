#!/usr/bin/python
# -*- coding: utf-8 -*-
""" Python version 3.11.5 64-bit
Author: Sarah Irons
Purpose: Tech Academy Boot Camp Python Course Demonstrating Tkinter GUI module, using Tkinter parent and child relationships. 
this code is tested to run with Windows 10.
STUDENT TRACKING ASSIGNMENT """





import os
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox

import Student_Tracking_main
import Student_Tracking_GUI





databaseString='db_Student_Tracker.db'

def center_window(self,w,h):# pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
        # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) -(w/2))
    y = int((screen_height/2)-(h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo



def ask_quit(self): 
    if messagebox.askokcancel("Exit program","Ok to exit application?"):
        #this closes the app
        self.master.destroy()
        os._exit(0)


        #++++++++++++++++++++++
def create_db(self):
    conn = sqlite3.connect(databaseString)
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_students(ID INTEGER PRIMARY KEY AUTOINCREMENT, col_fname TEXT, col_lname TEXT, col_fullname TEXT,col_phone TEXT,col_email TEXT, col_course TEXT);")

        conn.commit()
    conn.close()
    first_run(self)


def first_run(self): 
    conn = sqlite3.connect(databaseString)
    with conn: 
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_students(col_fname,col_lname,col_fullname,col_phone,col_email,col_course)VALUES(?,?,?,?,?,?)""",('Jane','Smith','Jane Smith','123-555-0159','jane@email.com','Software Dev 101'))
            conn.commit()
    conn.close() 


def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_students""")
    count = cur.fetchone()[0]
    return cur,count


#select item in listbox
def onSelect(self,event):
    #calling the event is the self.lstList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect(databaseString)
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email,col_course FROM tbl_students WHERE col_fullname =(?)""",[value])
        varBody = cursor.fetchall()
        #this returns a tuple & we can slice it into 4 parts using data during the iteration
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_course.delete(0,END)
            self.txt_course.insert(0,data[4])

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    var_course = self.txt_course.get()
    #normalize the data to keep it consistent in the database
    var_fname = var_fname.strip() #this will remove any blank spaces before/after the user's entry
    var_lname = var_lname.strip()
    var_fname = var_fname.title() #cap first letter of name
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname))
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if not "@" or not "." in var_email: 
        print('Incorrect email format!')
    conn = sqlite3.connect(databaseString)
    with conn:
        cursor = conn.cursor()
        #check the db for the full name
        cursor.execute("""SELECT COUNT (col_fullname) FROM tbl_students WHERE col_fullname = '{}'""".format(var_fullname))
        count = cursor.fetchone()[0]
        chkName = count
        if chkName == 0: #if this is 0 then there is no entry of the fullname and we can add new student
            print("chkName:{}".format(chkName))
            cursor.execute("""INSERT INTO tbl_students(col_fname,col_lname,col_fullname,col_phone,col_email,col_course)VALUES(?,?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email,var_course)) #update listbox with the new full name 
            self.lstList1.insert(END, var_fullname)
            onClear(self) #call the function to clear all of the text boxes
        else:
            messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name or please refer to the existing student record and modify it.".format(var_fullname))
            onClear(self) #call function to clear all the text boxes
    conn.commit()
    conn.close()



def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) #listbox's selected value
    conn = sqlite3.connect(databaseString)
    with conn:
        cur = conn.cursor()
        #check count to ensure that thyis is not the last record in the database; cannot delete the last record or we will get an error.
#
        cur.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel
            ("Delete Confirmation", "All information associated with ({})\n will be permantently deleted from the database. \n Proceed with the deletion request?".format(var_select))
            conn = sqlite3.connect (databaseString)
            with conn:
                cursor = conn.cursor()
                cursor.execute("""DELETE FROM tbl_students WHERE col_fullname = '{}'""".format(var_select))
            onDeleted(self) #call the function to clear all the text boxes and the selected indext of listbox. Onrefresh, will update the listbox of the changes.
            conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "{} is the last record in the database and cannot be deleted at this time.\nPlease add another record first before you can delete({}).".format(var_select,var_select))       
    conn.close()

def onDeleted(self):
    #clear the text in text boxes
    self.txt_fname.delete(0,END)   
    self.txt_lname.delete(0,END)          
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)
    ##    onRefresh(self) # update the listbox of the changes
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)

def onRefresh(self):

    self.lstList1.delete(0,END)
    conn = sqlite3.connect(databaseString)
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*)FROM tbl_students""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count: 
            cursor.execute("""SELECT col_fullname FROM tbl_students""")
            varList = cursor.fetchall()[i]
            for item in varList:
                    self.lstList1.insert(0,str(item))
                    i = i + 1
    conn.close()


def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0] # index of the list selection
        var_value = self.lstList1.get(var_select) # list selection's text value
    except:
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the Update request.")
        return
     # The user will only be alowed to update changes for phone and emails.
    # For name changes, the user will need to delete the entire record and start over.
    var_phone = self.txt_phone.get().strip() # normalize the data to maintain database integrity
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get()
    if (len(var_phone) > 0) and (len(var_email) > 0): # ensure that there is data present
        conn = sqlite3.connect(databaseString)
        with conn:
            cur = conn.cursor()
            # count records to see if the user's changes are already in
            # the database...meaning, there are no changes to update.

            cur.execute("""SELECT COUNT(col_phone) FROM tbl_students WHERE col_phone = '{}'""".format(var_phone))
            count = cur.fetchone()[0]
            print(count)

            cur.execute("""SELECT COUNT(col_email) FROM tbl_students WHERE col_email = '{}'""".format(var_email))
            count2 = cur.fetchone()[0]
            print(count2)

            cur.execute("""SELECT COUNT(col_course) FROM tbl_students WHERE col_course = '{}'""".format(var_course))
            count3 = cur.fetchone()[0]
            print(count3)


            if count == 0 or count2 == 0 or count3 == 0: # if proposed changes are not already in the database, then proceed
                response = messagebox.askokcancel("Update Request","The following data:\nphone: ({0})\nemail: ({1})\ncourse: ({2})\n Will be implemented for ({3}). \n\nProceed with the update request?".format(var_phone,var_email,var_course,var_value))
                print(response)
                if response:
                    conn = sqlite3.connect(databaseString)
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_students SET 
                        col_phone = '{0}',col_email = '{1}',
                        col_course = '{2}' WHERE col_fullname = '{3}'""".format(var_phone,var_email,var_course,var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request","No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected","({0}),({1}) and ({2}) \nalready exist in the database for this name. \n\nYour update request has been cancelled.".format(var_phone,var_email,var_course))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing information","Please select a name from the list. \nThen edit the phone or email information.")
    onClear(self)


if __name__ == "__main__":
    pass

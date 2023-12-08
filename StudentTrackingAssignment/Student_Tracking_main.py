#!/usr/bin/python
# -*- coding: utf-8 -*-
"""     # -*- coding: utf-8 -*-
    # This sets the charset if it is present on the first two lines of the file.""" 
""" Python version 3.11.5 64-bit
Author: Sarah Irons
Purpose: Tech Academy Boot Camp Python Course Demonstrating Tkinter GUI module, using Tkinter parent and child relationships. 
this code is tested to run with Windows 10.
STUDENT TRACKING ASSIGNMENT """ 
from tkinter import *
import tkinter as tk
from tkinter import messagebox




import Student_Tracking_GUI
import Student_Tracking_func




class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)


        self.master = master
        self.master.minsize(500,500)
        self.master.maxsize(500,500)
        #the Centerwindow method will center the app on the user's screen
        Student_Tracking_func.center_window(self,500,300)
        self.master.title('Student Tracker')
        self.master.configure(bg="#f0f0f0")
        #this protocol method is built in to tk to catch if the user clicks the upper corner red X on windows OS.

        ("WM_DELETE_WINDOW",lambda: Student_Tracking_func.ask_quit(self))
        arg = self.master

        #load in the GUI widgets from a separate module to keep code clutter free

        Student_Tracking_GUI.load_gui(self)

        #instantiate the tkinter menu dropdown object; this is the menu that will appear at top of window

        menubar = Menu(self.master)
        filemenu = Menu(menubar,tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit",underline=1,accelerator="Ctrl+Q",command=lambda: Student_Tracking_func.ask_quit(self))
        menubar.add_cascade(label="File",underline=0,menu=filemenu)
        helpmenu = Menu(menubar,tearoff=0) #defines the particular dropdown column and tearoff=0 means don't separate from menubar.
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About")
        menubar.add_cascade(label="Help")

        self.master.config(menu=menubar,borderwidth='1')




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

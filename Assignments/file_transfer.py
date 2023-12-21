import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import timedelta, datetime
from pathlib import Path
print(Path.home())
import time



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #sets title of GUI window
        self.master.title("File Transfer")

         ## GUI 
        self.sourceDir_btn = Button (text="Select Source", width=20, command=self.sourceDir)
            
        #positions source button in GUI using tkinter grid
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10),pady=(30,0))
            
        #creates entry for source directory selections
        self.source_dir = Entry(width=75)
         #positions entry in GUI using grid padx and pady are same as button to ensure they'll line up
        self.source_dir.grid(row=0, column=1,columnspan=2,padx=(20,10),pady=(30,0))

        #creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #positions the button in GUI on tk grid on next row under the source button
        self.destDir_btn.grid(row=1, column=0,padx=(20,10),pady=(15,10))

        #creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #positions entry in GUI using tk grid padx and pady are same as the button to ensure they will line up
        self.destination_dir.grid(row=1,column=1,columnspan=2,padx=(20,10),pady=(15,10))

        #creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width= 20, command=self.transferFiles)
        #positions transfer file button
        self.transfer_btn.grid(row=2,column=1,padx=(200,0),pady=(0,15))

        #creates an exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #positions the exit button
        self.exit_btn.grid(row=2,column=2,padx=(10,40),pady=(0,15))

    ## Functions
    #creates function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #the delete(0,END) will clear the content that is inserted in the entry widget. this allows the path to be inserted into the entry widget properly.
        
        self.source_dir.delete(0,END)
        #the insert method will insert the user selection to source_dir Entry
        self.source_dir.insert(0,selectSourceDir)

            #creates button to select files from source directory
        
        
    #creates function to select destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        #the delete will clear the content inserted into widget; the insert will insert user selection
        self.destination_dir.delete(0,END)
        self.destination_dir.insert(0, selectDestDir)



    
    def transferFiles(self):
        #https://gist.github.com/MatthewAndres/25719ef89622f6666fa5#file-copy-files-1-L26
    #gets source directory
        source = self.source_dir.get()
        #gets destination directory
        destination = self.destination_dir.get()
        #gets list of files in source directory
        source_files = os.listdir(source)

        for fileName in source_files:
            filePathName = source + "/" + fileName
            filetimestamp = os.path.getmtime(filePathName)
            modifyDate = datetime.fromtimestamp(filetimestamp)
            todaysDate = datetime.today()
            fileMoveByDate = modifyDate + timedelta(days=1)
            #check date if newer than 24 hours
            #if older than 24 hours do not move(pass)
            if fileMoveByDate > todaysDate:
                #moves each file from source to the destination
                shutil.move(filePathName, destination)
                print(fileName + 'was successfully transferred.')
                    # Create list of text filenames in Origin folder
            
    def exit_program (self):
        #root is the main GUI window, the tKinter destroy method tells python to terminate root.mainloop and all widgets inside the GUI window 
        root.destroy()


if __name__=="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


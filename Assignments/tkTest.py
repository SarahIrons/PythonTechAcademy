#Import the required Libraries
from tkinter import *
from tkinter import ttk
import webbrowser


#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x250")

def customHTMLGenerator():
   global userInput
   string = userInput.get()
   createHTML(string)

def createHTML(htmlText = 'This text can be changed'):
    htmlFile = open("index.html","w")
    htmlContent = ("<html>\n<body>\n<h1>"+ htmlText + "</h1>\n</body>\n</html>")
    htmlFile.write(htmlContent)
    htmlFile.close()
    webbrowser.open_new_tab("index.html")


#Create an Entry widget to accept User Input
userInput = Entry(win, width= 40)
userInput.focus_set()
userInput.pack()

ttk.Button(win, text= "Default",width= 20, command= createHTML).pack(pady=20)

ttk.Button(win, text= "Custom",width= 20, command= customHTMLGenerator).pack(pady=20)

if __name__=="__main__":
    win.mainloop()
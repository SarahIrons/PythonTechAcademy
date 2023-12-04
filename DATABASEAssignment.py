import sqlite3
conn = sqlite3.connect('test01.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
col_filename TEXT)")
    conn.commit()
conn = sqlite3.connect('test01.db')
fileList = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.png','World.txt','data.pdf','myPhoto.jpg')

##loop through each object in the tuple to find file names that end in 'txt'
for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            #the value for each row will be one name out of the tuple therefore (x, ) will denote  one element tuple for each name ending with 'txt'.
            cur.execute("INSERT INTO tbl_fileList (col_filename) VALUES (?)",(x,))
            print(x)


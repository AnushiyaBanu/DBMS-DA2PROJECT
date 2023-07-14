import mysql.connector

    # Connect to MySQL server
con = mysql.connector.connect(host="localhost",user="root",
        passwd="anu123",
        database = "library1")

    # Create a cursor object to execute SQL queries
cursor = con.cursor()

    # Create the movie1 database
    #cursor.execute("CREATE DATABASE IF NOT EXISTS library1")

    # Switch to the movie1 database
    #cursor.execute("USE library1")

    # Create the 'book' table
cursor.execute("""
        CREATE TABLE IF NOT EXISTS book (
            id INT ,
            Book_ID VARCHAR(255),
            Book_Name VARCHAR(255),
            Bookrelease_Date VARCHAR(255),
            Author VARCHAR(255),
            Genre VARCHAR(255),
            Availability VARCHAR(255),
            Pages VARCHAR(255),
            Rating VARCHAR(255)
        )
    """)

    # Commit the changes and close the connection
con.commit()

# Call the create_database function to create the database and table
def AddBookRec(Book_ID,Book_Name,bookrelease_Date,Author,Genre,Availability,Pages,Rating):   
    cur=con.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s)", (Book_ID,Book_Name,bookrelease_Date,Author,Genre,Availability,Pages,Rating))
    con.commit()
    con.close()

def ViewBookData():
    cur=con.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    con.close()    
    return rows

def DeleteBookRec(id):       
    cur=con.cursor()
    cur.execute("DELETE FROM book WHERE id=%s", (id,))
    con.commit()
    con.close()  

def SearchBookData(Book_ID="",Book_Name="",bookrelease_Date="",Author="",Genre="",Availability="",Pages="",Rating=""):    
    cur=con.cursor()
    cur.execute("SELECT * FROM book WHERE Book_ID=%s OR Book_Name=%s OR bookrelease_Date=%s OR Author=%s OR Genre=%s OR Availability=%s OR Pages=%s OR Rating=%s",(Book_ID,Book_Name,bookrelease_Date,Author,Genre,Availability,Pages,Rating))
    rows=cur.fetchall()
    con.close()    
    return rows

def UpdateMovieData(id,Book_ID="",Book_Name="",bookrelease_Date="",Author="",Genre="",Availability="",Pages="",Rating=""):    
    cur=con.cursor()
    cur.execute("UPDATE book SET Book_ID=%s,Book_Name=%s,bookrelease_Date=%s,Author=%s,Genre=%s,Availability=%s,Pages=%s,Rating=%s WHERE id=%s",(Book_ID,Book_Name,bookrelease_Date,Author,Genre,Availability,Pages,Rating,id))
    con.commit()
    con.close()

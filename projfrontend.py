#Frontend

from tkinter import *
import tkinter.messagebox
import projectdb

class libraryclass:
	def __init__(self, root):
		self.root=root
		self.root.title("Online Library Management System")
		self.root.geometry("1350x750+0+0")
		self.root.config(bg="black")

		Book_Name=StringVar()
		Book_ID=StringVar()
		Bookrelease_Date=StringVar()
		Author=StringVar()
		Genre=StringVar()
		Availability=StringVar()
		Pages=StringVar()
		Rating=StringVar()

		#Functions
		def iExit():
			iExit=tkinter.messagebox.askyesno("Online Library Management System", "Are you sure?")
			if iExit>0:
				root.destroy()
			return

		def clcdata():
			self.txtBook_ID.delete(0,END)
			self.txtBook_Name.delete(0,END)
			self.txtBookrelease_Date.delete(0,END)
			self.txtAuthor.delete(0,END)
			self.txtGenre.delete(0,END)
			self.txtAvailability.delete(0,END)
			self.txtPages.delete(0,END)
			self.txtRating.delete(0,END)

		def adddata():
			if(len(Book_ID.get())!=0):
				projectdb.AddBookRec(Book_ID.get(),Book_Name.get(),Bookrelease_Date.get(),Author.get(),Genre.get(),Availability.get(),Pages.get(),Rating.get())
				BookList.delete(0,END)
				BookList.insert(END,(Book_ID.get(),Book_Name.get(),Bookrelease_Date.get(),Author.get(),Genre.get(),Availability.get(),Pages.get(),Rating.get()))

		def disdata():
			BookList.delete(0,END)
			for row in projectdb.ViewBookData():
				BookList.insert(END, row, str(""))

		def bookrec(event):
			global sd
			searchbook=BookList.curselection()[0]
			sd=BookList.get(searchbook)

			self.txtBook_ID.delete(0,END)
			self.txtBook_ID.insert(END,sd[1])
			self.txtBook_Name.delete(0,END)
			self.txtBook_Name.insert(END,sd[2])
			self.txtBookrelease_Date.delete(0,END)
			self.txtBookrelease_Date.insert(END,sd[3])
			self.txtAuthor.delete(0,END)
			self.txtAuthor.insert(END,sd[4])
			self.txtGenre.delete(0,END)
			self.txtGenre.insert(END,sd[5])
			self.txtAvailability.delete(0,END)
			self.txtAvailability.insert(END,sd[6])
			self.txtPages.delete(0,END)
			self.txtPages.insert(END,sd[7])
			self.txtRating.delete(0,END)
			self.txtRating.insert(END,sd[8])

		def deldata():
			if(len(Book_ID.get())!=0):
				projectdb.DeleteBookRec(sd[0])
				clcdata()
				disdata()

		def searchdb():
			BookList.delete(0,END)
			for row in projectdb.SearchBookData(Book_ID.get(),Book_Name.get(),Bookrelease_Date.get(),Author.get(),Genre.get(),Availability.get(),Pages.get(),Rating.get()):
				BookList.insert(END, row, str(""))

		def updata():
			if(len(Book_ID.get())!=0):
				projectdb.DeleteBookRec(sd[0])
			if(len(Book_ID.get())!=0):
				projectdb.AddBookRec(Book_ID.get(),Book_Name.get(),Bookrelease_Date.get(),Author.get(),Genre.get(),Availability.get(),Pages.get(),Rating.get())
				BookList.delete(0,END)
				BookList.insert(END,(Book_ID.get(),Book_Name.get(),Bookrelease_Date.get(),Author.get(),Genre.get(),Availability.get(),Pages.get(),Rating.get()))

		#Frames
		MainFrame=Frame(self.root, bg="black")
		MainFrame.grid()

		TFrame=Frame(MainFrame, bd=5, padx=54, pady=8, bg="black", relief=RIDGE)
		TFrame.pack(side=TOP)

		self.TFrame=Label(TFrame, font=('Arial', 25, 'bold'), text="ONLINE LIBRARY MANAGEMENT SYSTEM", bg="black", fg="pink")
		self.TFrame.grid() 

		BFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="black", relief=RIDGE)
		BFrame.pack(side=BOTTOM)

		DFrame=Frame(MainFrame, bd=2, width=1300, height=400, padx=20, pady=20, bg="black", relief=RIDGE)
		DFrame.pack(side=BOTTOM)

		DFrameL=LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, bg="black", relief=RIDGE, font=('Arial', 20, 'bold'), text="Book Info_\n", fg="white")
		DFrameL.pack(side=LEFT)

		DFrameR=LabelFrame(DFrame, bd=2, width=450, height=300, padx=31, pady=3, bg="black", relief=RIDGE, font=('Arial', 20, 'bold'), text="Book Details_\n", fg="white")
		DFrameR.pack(side=RIGHT)

		#Labels & Entry Box

		self.lblBook_ID=Label(DFrameL, font=('Arial', 18, 'bold'), text="Book ID:", padx=2, pady=2, bg="black", fg="pink")
		self.lblBook_ID.grid(row=0, column=0, sticky=W)
		self.txtBook_ID=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Book_ID, width=39, bg="black", fg="white")
		self.txtBook_ID.grid(row=0, column=1) 

		self.lblBook_Name=Label(DFrameL, font=('Arial', 18, 'bold'), text="Book Name:", padx=2, pady=2, bg="black", fg="pink")
		self.lblBook_Name.grid(row=1, column=0, sticky=W) 
		self.txtBook_Name=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Book_Name, width=39, bg="black", fg="white")
		self.txtBook_Name.grid(row=1, column=1)

		self.lblBookrelease_Date=Label(DFrameL, font=('Arial', 18, 'bold'), text="Book Release Date:", padx=2, pady=2, bg="black", fg="pink")
		self.lblBookrelease_Date.grid(row=2, column=0, sticky=W) 
		self.txtBookrelease_Date=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Bookrelease_Date, width=39, bg="black", fg="white")
		self.txtBookrelease_Date.grid(row=2, column=1)

		self.lblAuthor=Label(DFrameL, font=('Arial', 18, 'bold'), text="Author:", padx=2, pady=2, bg="black", fg="pink")
		self.lblAuthor.grid(row=3, column=0, sticky=W) 
		self.txtAuthor=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Author, width=39, bg="black", fg="white")
		self.txtAuthor.grid(row=3, column=1)

		self.lblGenre=Label(DFrameL, font=('Arial', 18, 'bold'), text="Genre:", padx=2, pady=2, bg="black", fg="pink")
		self.lblGenre.grid(row=4, column=0, sticky=W) 
		self.txtGenre=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Genre, width=39, bg="black", fg="white")
		self.txtGenre.grid(row=4, column=1)

		self.lblAvailability=Label(DFrameL, font=('Arial', 18, 'bold'), text="Availability :", padx=2, pady=2, bg="black", fg="pink")
		self.lblAvailability.grid(row=5, column=0, sticky=W) 
		self.txtAvailability=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Availability, width=39, bg="black", fg="white")
		self.txtAvailability.grid(row=5, column=1)

		self.lblPages=Label(DFrameL, font=('Arial', 18, 'bold'), text="Pages:", padx=2, pady=2, bg="black", fg="pink")
		self.lblPages.grid(row=6, column=0, sticky=W) 
		self.txtPages=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Pages, width=39, bg="black", fg="white")
		self.txtPages.grid(row=6, column=1)

		self.lblRating=Label(DFrameL, font=('Arial', 18, 'bold'), text="Rating (Out of 5):", padx=2, pady=2, bg="black", fg="pink")
		self.lblRating.grid(row=7, column=0, sticky=W) 
		self.txtRating=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Rating, width=39, bg="black", fg="white")
		self.txtRating.grid(row=7, column=1)

		#ListBox & ScrollBar
		sb=Scrollbar(DFrameR)
		sb.grid(row=0, column=1, sticky='ns')

		BookList=Listbox(DFrameR, width=41, height=16, font=('Arial', 12, 'bold'), bg="black", fg="white", yscrollcommand=sb.set)
		BookList.bind('<<ListboxSelect>>', bookrec)
		BookList.grid(row=0, column=0, padx=8)
		sb.config(command=BookList.yview)

		#Buttons
		self.btnadd=Button(BFrame, text="Add New", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="pink", command=adddata)
		self.btnadd.grid(row=0, column=0)

		self.btndis=Button(BFrame, text="Display", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="pink", command=disdata)
		self.btndis.grid(row=0, column=1)

		self.btnclc=Button(BFrame, text="Clear", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="pink", command=clcdata)
		self.btnclc.grid(row=0, column=2)

		self.btnse=Button(BFrame, text="Search", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="pink", command=searchdb)
		self.btnse.grid(row=0, column=3)

		self.btndel=Button(BFrame, text="Delete", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="pink", command=deldata)
		self.btndel.grid(row=0, column=4)

		self.btnup=Button(BFrame, text="Update", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="pink", command=updata)
		self.btnup.grid(row=0, column=5)

		self.btnx=Button(BFrame, text="Exit", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="pink", command=iExit)
		self.btnx.grid(row=0, column=6)


if __name__=='__main__':
	root=Tk()
	datbase=libraryclass(root)
	root.mainloop()

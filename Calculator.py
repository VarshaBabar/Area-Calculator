from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from math import pi , pow

root = Tk()
root.title("AREA CALCULATOR")
root.geometry("800x700+50+50")
t = ("Century" , 40 , "bold" , "italic")
f = ("Arial" , 20 , "bold" , "italic")

def f1():
	Rectangle.deiconify()
	root.withdraw()
def f2():
	root.deiconify()
	Rectangle.withdraw()

def f3():
	Triangle.deiconify()
	root.withdraw()
def f4():
	root.deiconify()
	Triangle.withdraw()

def f5():
	Square.deiconify()
	root.withdraw()
def f6():
	root.deiconify()
	Square.withdraw()

def f7():
	Circle.deiconify()
	root.withdraw()
def f8():
	root.deiconify()
	Circle.withdraw()



lab =Label(root , text = "AREA CALCULATOR" , font = t)
lab.pack(pady = 50)

labtitle =Label(root , text = "Select the shape of Area " , font = f)
labtitle.place(x = 200 , y = 200)

btnRect = Button(root , text = "Rectangle" , font = f ,width = 15, command = f1)
btnRect.place(x = 300 , y = 300)

btnTri = Button(root , text = "Triangle  " , font = f ,width = 15, command = f3)
btnTri.place(x = 300 , y = 400)

btnSqr = Button(root , text = "  Square  " , font = f ,width = 15, command = f5)
btnSqr.place(x = 300 , y = 500)

btncir = Button(root , text = "  Circle   " , font = f ,width = 15, command = f7)
btncir.place(x = 300 , y = 600)

def show():
	L = as_entLen.get()
	W = as_entWid.get()
	try:
		L = float(as_entLen.get())
		W = float(as_entWid.get())
		if (L > 0.0) and (W > 0.0):
			Area = L * W
			ans = round(Area , 2)
			as_Ans.configure(text = ans)
			as_entLen.delete(0 , END)
			as_entWid.delete(0 , END)
			as_entLen.focus()
		else:
			showerror("issue" , "input cannot be negative")
			as_entLen.delete(0 , END)
			as_entWid.delete(0 , END)
			as_entLen.focus()

	except ValueError :
		showerror("issue" ,"Invalid input")
		as_entLen.delete(0 , END)
		as_entWid.delete(0 , END)
		as_entLen.focus()

	except Exception as e:
		showerror("issue" ,"Invalid input")
		as_entLen.delete(0 , END)
		as_entWid.delete(0 , END)
		as_entLen.focus()

"""def clr():
	as_entLen.delete(0 , END)
	as_entWid.delete(0 , END)
	#as_Ans.destroy()
	as_entLen.focus()"""


Rectangle = Toplevel(root)
Rectangle.title("Area of Rectangle")
Rectangle.geometry("800x700+50+50")

as_lab = Label(Rectangle , text = "Area of Rectangle" , font = t)
as_lab.place(x = 70, y =20)

as_labLen = Label(Rectangle , text = "Length (l)" , font = f)
as_labLen.place(x = 50 , y = 100)

as_entLen = Entry(Rectangle , font = f ,width = 13)
as_entLen.place(x = 200 , y = 100)

as_labWid = Label(Rectangle , text = "Width (w)" , font = f)
as_labWid.place(x = 50 , y = 200)

as_entWid = Entry(Rectangle , font = f ,width = 13)
as_entWid.place(x = 200 , y = 200)

as_Ans = Label(Rectangle  , font = f)
as_Ans.place(x = 300, y =300)

as_btnCal = Button(Rectangle , text = "Calculate" , font = f ,width = 10 , command = show)
as_btnCal.place(x = 50 , y = 300)

"""as_btnClr = Button(Rectangle , text = "Clear" , font = f ,width = 10 , command = clr)
as_btnClr.place(x = 250 , y = 400)"""

as_btn = Button(Rectangle , text = "Back" , font = f ,width = 10 , command = f2)
as_btn.place(x = 50 , y = 400)

Rectangle.withdraw()




def show1():
	a = as_entEg1.get()
	b = as_entEg2.get()
	c = as_entEg3.get()
	try:
		a = float(as_entEg1.get())
		b = float(as_entEg2.get())
		c = float(as_entEg3.get())
		if (a > 0.0) and (b > 0.0) and (c > 0.0):
			s = (a +b +c)/2
			Area = (s*(s-a)*(s-b)*(s-c))** 0.5
			ans = round(Area , 2)
			as_Ans1.configure(text = ans)
			as_entEg1.delete(0 , END)
			as_entEg2.delete(0 , END)
			as_entEg3.delete(0 , END)
			as_entEg1.focus()
		else:
			showerror("issue" , "input cannot be negative")
			as_entEg1.delete(0 , END)
			as_entEg2.delete(0 , END)
			as_entEg3.delete(0 , END)
			as_entEg1.focus()
	except ValueError :
		showerror("issue" ,"Invalid input")
		as_entEg1.delete(0 , END)
		as_entEg2.delete(0 , END)
		as_entEg3.delete(0 , END)
		as_entEg1.focus()
	except Exception as e:
		showerror("issue" ,"Invalid input")	
		as_entEg1.delete(0 , END)
		as_entEg2.delete(0 , END)
		as_entEg3.delete(0 , END)
		as_entEg1.focus()

"""def clr1():
	as_entEg1.delete(0 , END)
	as_entEg2.delete(0 , END)
	as_entEg3.delete(0 , END)
	as_entEg1.focus()
	#as_Ans1.destroy()"""



Triangle = Toplevel(root)
Triangle.title("Area of Triangle")
Triangle.geometry("800x700+50+50")

as_lab = Label(Triangle , text = "Area of Triangle" , font = t)
as_lab.pack(pady = 50)

as_labEg1 = Label(Triangle , text = "Edge 1(a)" , font = f)
as_labEg1.place(x = 50 , y = 150)

as_labEg2 = Label(Triangle , text = "Edge 2(b)" , font = f)
as_labEg2.place(x = 50 , y = 250)

as_labEg3 = Label(Triangle , text = "Edge 3(c)" , font = f)
as_labEg3.place(x = 50 , y = 350)

as_entEg1 = Entry(Triangle , font = f , width = 13)
as_entEg1.place(x = 200 , y = 150)

as_entEg2 = Entry(Triangle , font = f ,width = 13)
as_entEg2.place(x = 200 , y = 250)

as_entEg3 = Entry(Triangle , font = f ,width = 13)
as_entEg3.place(x = 200 , y = 350)

as_btnCal1 = Button(Triangle , text = "Calculate" , font = f ,command = show1)
as_btnCal1.place(x = 50 , y = 450)

as_Ans1 = Label(Triangle  , font = f)
as_Ans1.place(x = 250, y =450)

"""as_btnClr1 = Button(Triangle , text = "Clear" , font = f , command = clr1 )
as_btnClr1.place(x = 250 , y = 550)"""

as_btn = Button(Triangle , text = "Back" , font = f , command = f4)
as_btn.place(x = 50 , y = 550)

Triangle.withdraw()


def show2():
	L = as_entSide.get()
	try:
		L = float(as_entSide.get())
		if (L > 0.0):
			Area = L * L
			ans = round(Area , 2)
			as_Ans2.configure(text = ans)
			as_entSide.delete(0 , END)
			as_entSide.focus()
		else:
			showerror("issue" , "input cannot be negative")
			as_entSide.delete(0 , END)
			as_entSide.focus()
	except ValueError :
		showerror("issue" ,"Invalid input")
		as_entSide.delete(0 , END)
		as_entSide.focus()
	except Exception as e:
		showerror("issue" ,"Invalid input")	
		as_entSide.delete(0 , END)
		as_entSide.focus()

"""def clr2():
	as_entSide.delete(0 , END)
	as_entSide.focus()
	#as_Ans2.destroy()"""



Square = Toplevel(root)
Square.title("Area of Square")
Square.geometry("800x700+50+50")

as_lab = Label(Square , text = "Area of Square" , font = t)
as_lab.place(x = 200, y =50)

as_labSide = Label(Square , text = "Side (l)" , font = f)
as_labSide.place(x = 50 , y = 150)

as_entSide = Entry(Square , font = f , width = 13)
as_entSide.place(x = 200 , y = 150)

as_Ans2 = Label(Square  , font = f)
as_Ans2.place(x = 220, y =250)

as_btnCal2 = Button(Square , text = "Calculate" , font = f , command = show2)
as_btnCal2.place(x = 50 , y = 250)

"""as_btnClr2 = Button(Square , text = "Clear" , font = f ,command = clr2)
as_btnClr2.place(x = 220 , y = 330)"""

as_btn = Button(Square , text = "Back" , font = f , command = f6)
as_btn.place(x = 50 , y = 330)

Square.withdraw()


def show3():
	R = as_entRd.get()
	try:
		R = float(as_entRd.get())
		if (R > 0.0):
			Area = pi * pow(R,2)
			ans = round(Area , 2)
			as_Ans3.configure(text = ans)
			R = as_entRd.delete(0 , END)
			as_entRd.focus()
		else:
			showerror("issue" , "input cannot be negative")
			R = as_entRd.delete(0 , END)
			as_entRd.focus()
	except ValueError :
		showerror("issue" ,"Invalid input")
		R = as_entRd.delete(0 , END)
		as_entRd.focus()
	except Exception as e:
		showerror("issue" ,"Invalid input")	
		R = as_entRd.delete(0 , END)
		as_entRd.focus()

"""def clr3():
	R = as_entRd.delete(0 , END)
	as_entRd.focus()
	as_Ans3.destroy()"""


Circle = Toplevel(root)
Circle.title("Area of Circle")
Circle.geometry("800x700+50+50")

as_lab = Label(Circle , text = "Area of Circle" , font = t)
as_lab.place(x = 200, y =50)

as_labRd = Label(Circle , text = "Radius (r)" , font = f)
as_labRd.place(x = 50 , y = 150)

as_entRd = Entry(Circle , font = f , width = 13)
as_entRd.place(x = 200 , y = 150)

as_Ans3 = Label(Circle , font = f)
as_Ans3.place(x = 220 , y = 250)

as_btnCal3 = Button(Circle , text = "Calculate" , font = f , command = show3)
as_btnCal3.place(x = 50 , y = 250)

"""as_btnClr3 = Button(Circle , text = "Clear" , font = f , command = clr3)
as_btnClr3.place(x = 220 , y = 330)"""

as_btn = Button(Circle , text = "Back" , font = f , command = f8)
as_btn.place(x = 50 , y = 330)


Circle.withdraw()

def confirmExit():
	if askyesno('Exit' , 'Do you want to exit?'):
		root.destroy()
root.protocol('WM_DELETE_WINDOW' , confirmExit) 

root.mainloop()




























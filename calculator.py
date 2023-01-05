from tkinter import *

root = Tk()

# basic chracterstics of the app
root.title('PY-CALCULATOR')
root.geometry('230x295')
icon = PhotoImage(file = 'calculator.png')
root.iconphoto(False, icon)


func = None

# functions that calculates,clears or displays numbers
def add(num):
	pre = e.get()
	e.delete(0,END)
	e.insert(0,pre+num )

def addition(num):
	
	global f_num
	f_num = num 
	e.delete(0, END)
	global func
	func = 'add'

def subtraction(num):
	e.delete(0, END)
	global f_num
	f_num = num 
	global func
	func = 'sub'

def multiplication(num):
	e.delete(0, END)
	global f_num
	f_num = num 
	global func
	func = 'mult'

def division(num):
	e.delete(0, END)
	global f_num
	f_num = num 
	global func
	func = 'div'

def equal(num):
	
	s_num = num 
	e.delete(0, END)

	if func == 'add':
		e.insert(0,int(float(f_num)) + int(s_num))


	if func=='sub':
		e.insert(0, str(int(float(f_num)) - int(s_num)))

	if func=='mult':
		e.insert(0, str(int(float(f_num)) * int(s_num)))

	if func=='div':
		if s_num == "0":
			e.insert(0, "ZERO DIVISION ERROR")
		else:
			e.insert(0, str(int(float(f_num)) / int(s_num)))

def clear():
	e.delete(0, END)
	global func
	func = None

# app widgets
e = Entry(root, width = 35, borderwidth = 10)
e.grid(row = 0, column = 0, columnspan = 4)

btn1 = Button(root,text = '1',padx=20,pady=20, command =lambda :add('1'))
btn1.grid(row = 1, column = 0)

btn2 = Button(root,text = '2',padx=20,pady=20, command =lambda :add('2'))
btn2.grid(row = 1, column = 1)

btn3 = Button(root,text = '3',padx=20,pady=20, command =lambda :add('3'))
btn3.grid(row = 1, column = 2)

btn4 = Button(root,text = '4',padx=20,pady=20, command =lambda :add('4'))
btn4.grid(row = 2, column = 0)

btn5 = Button(root,text = '5',padx=20,pady=20, command =lambda :add('5'))
btn5.grid(row = 2, column = 1)

btn6 = Button(root,text = '6',padx=20,pady=20, command =lambda :add('6'))
btn6.grid(row = 2, column = 2)

btn7 = Button(root,text = '7',padx=20,pady=20, command =lambda :add('7'))
btn7.grid(row = 3, column = 0)

btn8 = Button(root,text = '8',padx=20,pady=20, command =lambda :add('8'))
btn8.grid(row = 3, column = 1)

btn9 = Button(root,text = '9',padx=20,pady=20, command =lambda :add('9'))
btn9.grid(row = 3, column = 2)

btn0 = Button(root,text = '0',padx=20,pady=20, command =lambda :add('0'))
btn0.grid(row = 4, column = 0)

btnADD = Button(root,text = '+',padx=20,pady=20, command =lambda :addition(e.get()))
btnADD.grid(row = 1, column = 3)

btnSUB = Button(root,text = '-',padx=20,pady=20, command =lambda :subtraction(e.get()))
btnSUB.grid(row = 2, column = 3)

btnMULT = Button(root,text = 'X',padx=20,pady=20, command =lambda :multiplication(e.get()))
btnMULT.grid(row = 4, column = 1)

btnDIV = Button(root,text = '/',padx=20,pady=20, command =lambda :division(e.get()))
btnDIV.grid(row = 4, column = 2)

btnEQUAL = Button(root,text = '=',padx=20,pady=20, command =lambda :equal(e.get()))
btnEQUAL.grid(row = 4, column = 3)

btnCLEAR = Button(root,text = 'C',padx=20,pady=20, command =lambda :clear())
btnCLEAR.grid(row = 3, column = 3)


root.mainloop()

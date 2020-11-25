from tkinter import *
root=Tk()
root.title("SIMPLE CALCULATOR")
root.configure(bg="light green")
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def press(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def clear():
    e.delete(0,END)

def add():
    first_number=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_number)
    e.delete(0,END)

def minus():
    first_number=e.get()
    global f_num
    global math
    math="minus"
    f_num=int(first_number)
    e.delete(0,END)

def multiply():
    first_number=e.get()
    global f_num
    global math
    math="multiply"
    f_num=int(first_number)
    e.delete(0,END)

def divide():
    first_number=e.get()
    global f_num
    global math
    math="divide"
    f_num=int(first_number)
    e.delete(0,END)

def equal():
    second_no=e.get()
    e.delete(0,END)

    if(math=="addition"):
        e.insert(0,f_num + int(second_no))
    if(math=="minus"):
        e.insert(0,f_num - int(second_no))
    if(math=="multiply"):
        e.insert(0,f_num * int(second_no))
    try:
        if(math=="divide"):
           e.insert(0,f_num / int(second_no))
    except ZeroDivisionError:
        e.insert(0," MATH ERROR : CAN'T DIVIDE BY ZERO")



button_1=Button(text=' 1 ', fg='black', bg='red',command=lambda: press(1), height=2, width=7) 
button_1.grid(row=3,column=0)
button_2=Button(text=' 2 ', fg='black', bg='red',command=lambda: press(2), height=2, width=7) 
button_2.grid(row=3,column=1)
button_3=Button(text=' 3', fg='black', bg='red',command=lambda: press(3), height=2, width=7) 
button_3.grid(row=3,column=2)
button_4=Button(text=' 4 ', fg='black', bg='red',command=lambda: press(4), height=2, width=7) 
button_4.grid(row=2,column=0)
button_5=Button(text=' 5 ', fg='black', bg='red',command=lambda: press(5), height=2, width=7) 
button_5.grid(row=2,column=1)
button_6=Button(text=' 6 ', fg='black', bg='red',command=lambda: press(6), height=2, width=7) 
button_6.grid(row=2,column=2)
button_7=Button(text=' 7 ', fg='black', bg='red',command=lambda: press(7), height=2, width=7) 
button_7.grid(row=1,column=0)
button_8=Button(text=' 8 ', fg='black', bg='red',command=lambda: press(8), height=2, width=7) 
button_8.grid(row=1,column=1)
button_9=Button(text=' 9 ', fg='black', bg='red',command=lambda: press(9), height=2, width=7) 
button_9.grid(row=1,column=2)
button_0=Button(text=' 0 ', fg='black', bg='red',command=lambda: press(0),height=2, width=7) 
button_0.grid(row=4,column=1)
button_clear=Button(text=' clear', fg='black', bg='light blue',command=clear, height=2, width=7) 
button_clear.grid(row=6,column=2)
button_equal=Button(text=' equal= ', fg='black', bg='light blue',command=equal, height=2, width=7) 
button_equal.grid(row=6,column=1)
button_add=Button(text=' + ', fg='black', bg='yellow',command= add, height=2, width=7) 
button_add.grid(row=5,column=0)
button_minus=Button(text=' -', fg='black', bg='yellow',command=minus, height=2, width=7) 
button_minus.grid(row=5,column=1)
button_multiply=Button(text=' X', fg='black', bg='yellow',command=multiply, height=2, width=7) 
button_multiply.grid(row=5,column=2)
button_divide=Button(text=' / ', fg='black', bg='yellow',command=divide, height=2, width=7) 
button_divide.grid(row=6,column=0)

root.mainloop()

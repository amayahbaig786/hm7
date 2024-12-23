import tkinter as tk

window = tk.Tk()
window.geometry("300x300")


expression = ""

def empty():
    global expression
    expression = ""
    v.set("")
    

def click(number):
    global expression
    expression = expression+str(number)
    v.set(expression)

v = tk.StringVar()

def result():
    s = str(eval(expression))
    v.set(s)


seven = tk.Button(window, text= "7", background = "white", fg = "black", command = lambda:click(7))
seven.place(x=20,y=60)

eight = tk.Button(window, text= "8", background = "white", fg = "black",command = lambda:click(8))
eight.place(x=65,y=60)

nine = tk.Button(window, text= "9", background = "white", fg = "black",command = lambda:click(9))
nine.place(x=112,y=60)

four = tk.Button(window, text= "4", background = "white", fg = "black",command = lambda:click(4))
four.place(x=20,y=100)

five = tk.Button(window, text= "5", background = "white", fg = "black",command = lambda:click(5))
five.place(x=66,y=100)

six = tk.Button(window, text= "6", background = "white", fg = "black",command = lambda:click(6))
six.place(x=112,y=100)

one = tk.Button(window, text= "1", background = "white", fg = "black",command = lambda:click(1))
one.place(x=21,y=140)

two = tk.Button(window, text= "2", background = "white", fg = "black",command = lambda:click(2))
two.place(x=66,y=140)

three = tk.Button(window, text= "3", background = "white", fg = "black",command = lambda:click(3))
three.place(x=115,y=140)

zero = tk.Button(window, text= "0", background = "white", fg = "black",command = lambda:click(0))
zero.place(x=20,y=180)

ce = tk.Button(window, text= "ce", activebackground="orange", fg = "black", command = empty)
ce.place(x=66,y=180)

equal = tk.Button(window, text= "=", background = "white", fg = "black", command = result)
equal.place(x=118,y=180)

plus = tk.Button(window, text= "+", background = "white", fg = "black",command = lambda:click("+"))
plus.place(x=165,y=180)

minus = tk.Button(window, text= "-", background = "white", fg = "black",command = lambda:click("-"))
minus.place(x=165,y=140)

times = tk.Button(window, text= "x", background = "white", fg = "black",command = lambda:click("x"))
times.place(x=165,y=100)

dash = tk.Button(window, text= "/", background = "white", fg = "black",command = lambda:click("/"))
dash.place(x=165,y=60)

Label = tk.Label(window, text = "Python Calculator", background = "Black")
Label.place(x=10,y=10)

box = tk.Entry(window,width=20,textvariable = v)
box.place(x=15,y=35)




window.mainloop()




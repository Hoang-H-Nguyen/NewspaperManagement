#Import the required libraries
from tkinter import *

# from matplotlib.pyplot import title
# #Create an instance of tkinter frame
win = Tk()
# #Set the geometry of frame
# win.geometry("650x250")
# #Define a function to clear the Entry Widget Content
# def clear_text():
#    text.delete(0, END)
# #Create a entry widget
# text= Entry(win, width=40)
# text.pack()
# #Create a button to clear the Entry Widget
# Button(win,text="Clear", command=clear_text, font=('Helvetica bold',10)).pack(pady=5)

# win.mainloop()

text2 = Entry(win, width=40).pack()
text3 = Entry(win, width=40).place(x=159, y=15, width=400, height=21)
print(type(text3))
print(type(text2))




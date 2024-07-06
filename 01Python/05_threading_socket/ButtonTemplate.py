from tkinter import *

window = Tk()
window.geometry("170x80+450+250")

button1 = Button(window,text='Button 1',command=lambda: print('Button 1')).grid(row=0,column=1)
button2 = Button(window,text='Button 2',command=lambda: print('Button 2')).grid(row=1,column=0)
button3 = Button(window,text='Button 3',command=lambda: print('Button 3')).grid(row=1,column=2)
button4 = Button(window,text='Button 4',command=lambda: print('Button 4')).grid(row=2,column=1)
window.mainloop()
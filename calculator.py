from tkinter import *
import tkinter.messagebox
r=Tk()
r.title("Calculator")
r.geometry("400x600")
#r.minsize(200,300)
#r.maxsize(400,500)
r.resizable(0,0)
#def show():
 #   tkinter.messagebox.showinfo('david','good')
o=''
te=StringVar()
tx=Entry(r,font=('arial',20,'bold'),bg='yellow',bd=40,textvariable=te,justify='right').grid(columnspan=4)
b7=Button(r,padx=16,pady=16,text='7',fg='black',font=('arial',20,'bold'),bd=10,command=lambda:fn(7)).grid(row=1)
b8=Button(r,padx=16,pady=16,text='8',bd=10,font=('arial',20,'bold'),command=lambda:fn(8)).grid(row=1,column=1)
b9=Button(r,padx=16,pady=16,text='9',bd=10,font=('arial',20,'bold'),command=lambda:fn(9)).grid(row=1,column=2)
badd=Button(r,padx=16,pady=16,text='+',bd=10,font=('arial',20,'bold'),command=lambda:fn('+')).grid(row=1,column=3)

b4=Button(r,padx=16,pady=16,text='4',bd=10,font=('arial',20,'bold'),command=lambda:fn(4)).grid(row=2)
b5=Button(r,padx=16,pady=16,text='5',bd=10,font=('arial',20,'bold'),command=lambda:fn(5)).grid(row=2,column=1)
b6=Button(r,padx=16,pady=16,text='6',bd=10,font=('arial',20,'bold'),command=lambda:fn(6)).grid(row=2,column=2)
bsub=Button(r,padx=16,pady=16,text='-',bd=10,font=('arial',20,'bold'),command=lambda:fn('-')).grid(row=2,column=3)

b1=Button(r,padx=16,pady=16,text='1',bd=10,font=('arial',20,'bold'),command=lambda:fn(1)).grid(row=3)
b2=Button(r,padx=16,pady=16,text='2',bd=10,font=('arial',20,'bold'),command=lambda:fn(2)).grid(row=3,column=1)
b3=Button(r,padx=16,pady=16,text='3',bd=10,font=('arial',20,'bold'),command=lambda:fn(3)).grid(row=3,column=2)
bmul=Button(r,padx=16,pady=16,text='*',bd=10,font=('arial',20,'bold'),command=lambda:fn('*')).grid(row=3,column=3)

b0=Button(r,padx=16,pady=16,text='0',bd=10,font=('arial',20,'bold'),command=lambda:fn(0)).grid(row=4)
bclear=Button(r,padx=16,pady=16,text='C',bd=10,font=('arial',20,'bold'),command=lambda:cl()).grid(row=4,column=1)
bequal=Button(r,padx=16,pady=16,text='=',bd=10,font=('arial',20,'bold'),command=lambda:eq()).grid(row=4,column=2)
bdiv=Button(r,padx=16,pady=16,text='/',bd=10,font=('arial',20,'bold'),command=lambda:fn('/')).grid(row=4,column=3)


def fn(n):
    global o
    o=o+str(n)
    te.set(o)
def cl():
    global o
    o=''
    te.set('')
def eq():
    global o
    t=str(eval(o))
    te.set(t)
    o=''
    














#b=Button(r,text='click',bg='yellow',bd='20',fg='red',command=show)
#b.pack(side=TOP)
r.mainloop()

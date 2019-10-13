from tkinter import *

def hello():
    x=i.get() 
    if x== 1:
        label.configure(background="red",text="You selected the option {}".format(x))
        rbtn_red.configure(foreground="red")
    if x== 2:
        label.configure(background="green",text="You selected the option {}".format(x))
        rbtn_green.configure(foreground="green")
    if x== 3:
        label.configure(background="blue",text="You selected the option {}".format(x))
        rbtn_blue.configure(foreground="blue")
    
    
app = Tk()
app.geometry("200x200")

i=IntVar()
rbtn_red=Radiobutton(text="Red", variable=i,value=1,command=hello, )
rbtn_green=Radiobutton(text="Green", variable=i,value=2,command=hello,)
rbtn_blue=Radiobutton(text="Blue",variable=i,value=3,command=hello)

label = Label()
#Place
rbtn_red.place(relx=0.1, rely=0.3 , anchor="w")
label.place(relx=0.1, rely=0.8 , anchor="w")
rbtn_green.place(relx=0.1, rely=0.4 , anchor="w")
rbtn_blue.place(relx=0.1, rely=0.5 , anchor="w")

app.mainloop()

from tkinter import *

def clicked():
    print ("Successful")

app = Tk()
app.title("Raizen Sangalang")
app.geometry("
             200x400")
 
button1 = Button(app,text= "Submit", command= clicked)
button1.pack(side="top")
app.mainloop()

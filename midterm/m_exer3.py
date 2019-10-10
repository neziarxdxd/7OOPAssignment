from tkinter import *
'''
the are three radio button
selecting one of the buttons changes the text of the lable
changethe color of the button is well as the text for the suitable changes
choice three color 
'''


def clicked():
    
    x = str(entry.get())
    
    

       
    if x=="" or (x.isspace()):
        button.configure(background="red")
        label.configure(text=x)
            
                
    else:
        button.configure(background="white",command=clear,text="clear")
        label.configure(text=x)
def clear():
    x=entry.get()
    entry.delete(0,len(x))
    button.configure(background="white",text="Copy Text",command=clicked)
    label.configure(text="")
    
        
    
   
       


app = Tk()
app.title("Raizen Sangalang")
app.geometry("200x200")
entry= Entry(app)
button= Button(app,text="copy text",command=clicked,background="white")
label = Label(app,text="Text display here")
entry.place(relx=0.5, rely=0.3 , anchor="center")
button.place(relx=0.5, rely=0.5 , anchor="center")
label.place(relx=0.5, rely=0.7 , anchor="center")
app.mainloop()

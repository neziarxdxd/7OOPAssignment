from tkinter import *
'''
the are three radio button
selecting one of the buttons changes the text of the lable
changethe color of the button is well as the text for the suitable changes
choice three color 
'''



        
    
   
       


app = Tk()
app.title("Raizen Sangalang")
app.geometry("200x400")
entry= Entry(app)
radio1= Radiobutton(app,text="red" ,active=False)
# radio2= Radiobutton(app,text="red")
# radio3= Radiobutton(app,text="red")
radio1.pack()
radio2.pack()
radio3.pack()
app.mainloop()

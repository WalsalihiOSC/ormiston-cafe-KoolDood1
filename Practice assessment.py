#CSC Practice assessment app/coded design, Andre


from tkinter import *

class interface:
    def __init__(self, parent):

     self.startframe = Frame(parent, highlightbackground= "black", highlightthickness=1, width=575, height=350)
     self.startframe.place(x=287.5, y=175)
     self.startframe.pack_propagate(False)

     startlabel = Label(self.startframe, text="Ormiston cafe orders")
     startlabel.config(font=("Courier", 28))
     startlabel.pack(anchor=CENTER, padx=50, pady=100)
     
     startbutton = Button(self.startframe, text="Start!", height=5, width=20, command = self.close_frame)
     startbutton.config(relief=SOLID)
     startbutton.pack(anchor=CENTER)
    
    def close_frame(self):
        self.startframe.destroy()
        Menu(root)

class Menu:
    def __init__(self):
        pass

class Data:
    def __init__(self):
        pass
     
    
if __name__ =="__main__":
    root = Tk()
    gui = interface(root)
    root.geometry("1150x700")
    root.resizable(False, False)
    root.title("Ormiston cafe app")
    root.mainloop()
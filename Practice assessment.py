
#CSC Practice assessment app/coded design, Andre

from tkinter import *

#Data encapsulate later
categories = ['Burger','With rice','Salads','Desserts','Drinks']
burgers = ['Chicken Burger', 'Beef Burger', 'Butte Chicken Burger', 'Lamb Burger', 'Chilli burger', 'Legendary Burger']


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
    def __init__(self, parent):
        #Main 3 sections
        self.categoryframe = Frame(parent, highlightbackground="black", highlightthickness=1, bg="beige", height=700, width=333)
        self.categoryframe.grid(column=0, row=0)
        self.categoryframe.grid_propagate(False)
        
        self.mainframe = Frame(parent, highlightbackground="black", highlightthickness=1, bg="beige", height=700, width=550)
        self.mainframe.grid(column=1, row=0)
        self.mainframe.grid_propagate(False)

        self.orderframe = Frame(parent, highlightbackground="black", highlightthickness=1, bg="beige", height=700, width=270)
        self.orderframe.grid(column=2, row=0)
        self.orderframe.pack_propagate(False)

        # These are buttons created with a loop using the list of strings and placed with grid geometry
        rcount = 0 #Starting Row count
        for item in categories:
            button = item
            gridbuttons = Button(self.categoryframe, 
                                 text=button)
            gridbuttons.grid(sticky = W+E, row = rcount, padx=20)
            rcount += 1
            
        
        horizontal = 0 #Same as before, represents the starting placement position
        vertical = 0
        
        for name in burgers: 
            menuframes = Frame(self.mainframe, highlightbackground="black", highlightthickness=1)
            menuframes.grid(column=horizontal, row=vertical, padx=10, pady=10)
            #Add pictures into here
            itemlabel = Label(menuframes, text= name)
            itemlabel.pack()
            horizontal += 1
        
            if horizontal == 3:
                horizontal = 0
                vertical = +1
                vertical = vertical+1

        #Order confirmation widget
        displayorder = Frame(self.orderframe, highlightbackground="black", highlightthickness=1, height= 400, width=160)
        displayorder.grid_propagate(False)
        displayorder.pack(padx=5,pady=15)
        ordertext = Label(displayorder, text= "Order confrimation")
        ordertext.config(font=("Courier", 9))
        ordertext.grid(row=0, column=0,pady=10,padx=10)
  




#Data class
class Data:
    def __init__(self):
        pass
     
    
if __name__ =="__main__":
    root = Tk()
    gui = interface(root)
    root.geometry("1150x700")
    root.resizable(False, False)#Maybe adjust resize
    root.title("Ormiston cafe app")
    root.mainloop()
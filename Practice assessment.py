#CSC Practice assessment app/coded,functional UI, Andre


from tkinter import *
from PIL import ImageTk, Image



class interface:
    def __init__(self, parent): #Starting frames 
     self.startframe = Frame(parent, bg="beige", highlightbackground= "black", highlightthickness=1, width=575, height=350)
     self.startframe.place(x=287.5, y=175)
     self.startframe.pack_propagate(False)

     startlabel = Label(self.startframe, text="Ormiston cafe orders", bg="beige")
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
        self.d = Data() #Reference to data class
        #Main 3 sections(frames)
        self.categoryframe = Frame(parent, highlightbackground="black", highlightthickness=1, bg="beige", height=700, width=333)
        self.categoryframe.grid(column=0, row=0)
        self.categoryframe.grid_propagate(False)
        
        self.mainframe = Frame(parent, highlightbackground="black", highlightthickness=1, bg="beige", height=700, width=550)
        self.mainframe.grid(column=1, row=0)
        self.mainframe.grid_propagate(False)

        self.orderframe = Frame(parent, highlightbackground="black", highlightthickness=1, bg="beige", height=700, width=270)
        self.orderframe.grid(column=2, row=0)
        self.orderframe.pack_propagate(False)

        #Order confirmation window
        self.displayorder = Frame(self.orderframe, highlightbackground="black", highlightthickness=1, height= 400, width=160)
        self.displayorder.pack_propagate(False)
        self.displayorder.pack(padx=5,pady=15)
        ordertext = Label(self.displayorder, text= "Order Confirmation")
        ordertext.config(font=("Courier", 9))
        ordertext.pack(pady=10,padx=10)

        #Add clear button and checkout button
        clearlist = Button(self.orderframe, text="Clear", command= self.clearlist)
        checkout = Button(self.orderframe, text="Checkout", command=self.checkoutfunc)
        clearlist.pack(padx=5, pady=10)
        checkout.pack(padx=5, pady=10)


        #Scrollbar for order window
        canvas = Canvas(self.displayorder)
        scrollbar = Scrollbar(canvas, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas)

        self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill=BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")
        
        
        

        # These are buttons created with a loop using the list of strings from the data class and placed with grid geometry
        rcount = 0 #Starting Row count
        for button in self.d.categories:
            gridbuttons = Button(self.categoryframe, 
                                 text=button, command=lambda button=button: self.menupick(button))
            gridbuttons.grid(sticky = W+E, row = rcount, padx=20, pady=5)
            rcount += 1

    def menupick(self, category):
        self.d.selected = category
        self.menugeneration()
        

    def menugeneration(self):
        for child in self.mainframe.winfo_children():
            child.destroy()

        if self.d.selected == 'Burger':
            horizontal = 0 #Same as before, represents the starting placement position
            vertical = 0

            items = self.d.burgers     #Below is loop to create menu frames
            for index in range(len(items)): 
                name = items[index]
                price = self.d.burgerprice[index]

                menuframes = Frame(self.mainframe, highlightbackground="black", highlightthickness=1)#Maybe adjust size
                menuframes.grid(column=horizontal, row=vertical, padx=10, pady=10)
                itemlabel = Label(menuframes, text= name) 
                itemprice = Label(menuframes, text= self.d.burgerprice[index])
                itembutton = Button(menuframes, text= "Add", command=lambda name=name, price=price: self.addorder(name, price))
            
                itemlabel.pack()
                itemprice.pack()
                itembutton.pack()
                horizontal += 1
                
                if horizontal == 3:
                    horizontal = 0
                    vertical = +1
                    vertical = vertical+1
        elif self.d.selected == 'With rice':
            horizontal = 0 
            vertical = 0

            items = self.d.withrice
            for index in range(len(items)): 
                name = items[index]
                price = self.d.withriceprice[index]
                
                menuframes = Frame(self.mainframe, highlightbackground="black", highlightthickness=1)
                menuframes.grid(column=horizontal, row=vertical, padx=10, pady=10)
                itemlabel = Label(menuframes, text= name) 
                itemprice = Label(menuframes, text= self.d.withriceprice[index])
                itembutton = Button(menuframes, text= "Add", command=lambda name=name, price=price: self.addorder(name, price))

                itemlabel.pack()
                itemprice.pack()
                itembutton.pack()
                horizontal += 1
                
                if horizontal == 3:
                    horizontal = 0
                    vertical = +1
                    vertical = vertical+1  
        elif self.d.selected == 'Salads':
            horizontal = 0 
            vertical = 0

            items = self.d.salads
            for index in range(len(items)): 
                name = items[index]
                price = self.d.saladprice[index]

                menuframes = Frame(self.mainframe, highlightbackground="black", highlightthickness=1)
                menuframes.grid(column=horizontal, row=vertical, padx=10, pady=10)
                itemlabel = Label(menuframes, text= name) 
                itemprice = Label(menuframes, text= self.d.saladprice[index])
                itembutton = Button(menuframes, text= "Add", command=lambda name=name, price=price: self.addorder(name, price))

                itemlabel.pack()
                itemprice.pack()
                itembutton.pack()
                horizontal += 1
                
                if horizontal == 3:
                    horizontal = 0
                    vertical = +1
                    vertical = vertical+1
        elif self.d.selected == 'Desserts':
            horizontal = 0 #
            vertical = 0

            items = self.d.desserts
            for index in range(len(items)): 
                name = items[index]
                price = self.d.dessertprice[index]

                menuframes = Frame(self.mainframe, highlightbackground="black", highlightthickness=1)
                menuframes.grid(column=horizontal, row=vertical, padx=10, pady=10)
                itemlabel = Label(menuframes, text= name) 
                itemprice = Label(menuframes, text= self.d.dessertprice[index])
                itembutton = Button(menuframes, text= "Add", command=lambda name=name, price=price: self.addorder(name, price))

                itemlabel.pack()
                itemprice.pack()
                itembutton.pack()
                horizontal += 1
                
                if horizontal == 3:
                    horizontal = 0
                    vertical = +1
                    vertical = vertical+1
        elif self.d.selected == 'Drinks':
            horizontal = 0 
            vertical = 0

            items = self.d.drinks
            for index in range(len(items)): 
                name = items[index]
                price = self.d.drinkprice[index]

                menuframes = Frame(self.mainframe, highlightbackground="black", highlightthickness=1)
                menuframes.grid(column=horizontal, row=vertical, padx=10, pady=10)
                itemlabel = Label(menuframes, text= name) 
                itemprice = Label(menuframes, text= self.d.drinkprice[index])
                itembutton = Button(menuframes, text= "Add", command=lambda name=name, price=price: self.addorder(name, price))
                
                itemlabel.pack()
                itemprice.pack()
                itembutton.pack()
                horizontal += 1
                
                if horizontal == 3:
                    horizontal = 0
                    vertical = +1
                    vertical = vertical+1
        else:
            pass

    def addorder(self, item, price): #Function that runs when you press add button
        self.d.total += price
        writeorder = Label(self.scrollable_frame, text= item)
        writeorder.pack(padx= 10)


    def clearlist(self): #Clears order list
        for child in self.scrollable_frame.winfo_children():
            child.destroy()
        self.d.total = 0
        

    def checkoutfunc(self): #Creates checkout screen and deletes other frames
        self.categoryframe.destroy()
        self.mainframe.destroy()
        self.orderframe.destroy()
        self.totaldue = Label(text= "${}".format(self.d.total))
        self.pay = Button(root, text="Pay", command= self.reset)
        self.totaldue.pack(padx=20, pady=10)
        self.pay.pack(padx=20, pady=20)

    def reset(self): #Function button on checkout screen that resets program when pressed
        self.d.total = 0
        self.totaldue.destroy()
        self.pay.destroy()
        interface(root)



#Data class
class Data:
    def __init__(self):
        self.selected = StringVar()
        
        self.categories = ['Burger','With rice','Salads','Desserts','Drinks']
        self.total = 0
        
        
        self.burgers = ['Chicken Burger', 'Beef Burger', 'Fried Chicken Burger', 'Lamb Burger', 'Chilli burger', 'Legendary Burger']
        self.burgerpicture = ['bur1.png', 'bur2.png', 'bur3.png', 'bur4.png', 'bur5.png', 'bur6.png']
        self.burgerprice = [6.00, 6.50, 7.00, 7.00, 7.50, 10]

        self.withrice = ['Butter Chicken', 'Teriyaki Chicken', 'Lamb curry', 'Potato curry', 'Chicken Katsu', 'Risotto'] 
        self.withriceprice = [5.50, 6.00, 6.50, 5.00, 5.50, 6.00]

        self.salads = ['Caesar salad', 'Greek salad', 'Italian salad', 'Egg salad', 'Fruit salad', 'Vegetable salad']
        self.saladprice = [5.50, 5.00, 5.00, 4.50, 4.00, 4.50]

        self.desserts = ['Caramel slice', 'Chocolate slice', 'Moosie', 'Ice pop', 'Brownie', 'Ice cream sandwich']
        self.dessertprice = [3.50, 3.50, 2.00, 1.50, 3.50, 4.00]

        self.drinks = ['Lipton ice tea', 'Up n go', 'Calci yum', 'Barista bros mocha', 'Anchor milk', 'Barista Bros espresso']
        self.drinkprice = [4.50, 2.50, 2.00, 4.50, 2.00, 5.00]

     
    
#Run
if __name__ =="__main__":
    root = Tk()
    gui = interface(root)
    root.geometry("1150x700")
    root.resizable(False, False)
    root.title("Ormiston cafe app")
    root.mainloop()

from tkinter import*
import tkinter as tk

def f5():
    global f5_frame 
    
    f2_frame.grid_remove()
    f3_frame.grid_remove()
    f4_frame.grid_remove()
    f1_frame.grid_remove()    

    f5_frame = LabelFrame(root, height="200", width="350", bd=5)
    f5_frame.grid(row=1, column=0, padx=0)
    
    Potato_Chips = Button(f5_frame, text="Potato Chips ", width=12, height=1, bd=3)
    Popcorn  = Button(f5_frame, text="Popcorn", width=12, height=1, bd=3)
    Chips  = Button(f5_frame, text="Chips ", width=12, height=1, bd=3)
    Noodle_Snack = Button(f5_frame, text="Noodle Snack", width=12, height=1, bd=3)
    
    Afghan_Cookies = Button(f5_frame, text="Afghan Cookies", width=28, height=1, bd=3)
    Mrs_Higgins_Chocolate_Chip_Cookies = Button(f5_frame, text="Mrs Higgins Chocolate Chip Cookies ", width=28, height=1, bd=3)
    Chocolate_Fudge_Brownie = Button(f5_frame, text="Chocolate Fudge Brownie", width=28, height=1, bd=3)
    Rice_Crackers = Button(f5_frame, text="Rice Crackers", width=28, height=1, bd=3)
    
    Potato_Chips.grid(row=0, column=0, pady=3, padx=5)
    Popcorn.grid(row=1, column=0, pady=3, padx=5)
    Chips.grid(row=2, column=0, pady=3, padx=5)
    Noodle_Snack.grid(row=3, column=0, pady=3, padx=5) 
    
    Afghan_Cookies.grid(row=0, column=1, pady=3, padx=5)
    Mrs_Higgins_Chocolate_Chip_Cookies.grid(row=1, column=1, pady=3, padx=5)
    Chocolate_Fudge_Brownie.grid(row=2, column=1, pady=3, padx=5)
    Rice_Crackers.grid(row=3, column=1, pady=3, padx=5)
    
    
def f4(): 
    global f4_frame 
    
    f2_frame.grid_remove()
    f3_frame.grid_remove()
    f1_frame.grid_remove()
    f5_frame.grid_remove()    
    
    f4_frame = LabelFrame(root, height="200", width="350", bd=5)
    f4_frame.grid(row=1, column=0, padx=0)
    
    Hot_Noodles = Button(f4_frame, text="Hot Noodles", width=15, height=1, bd=3)
    Spaghetti_Bun = Button(f4_frame, text="Spaghetti Bun", width=15, height=1, bd=3)
    Hash_Brown  = Button(f4_frame, text="Hash Brown", width=15, height=1, bd=3)
    Garlic_Bread = Button(f4_frame, text="Garlic Bread ", width=15, height=1, bd=3)
    Hot_Dog = Button(f4_frame, text="Hot Dog", width=15, height=1, bd=3)
    
    Steam_Bun  = Button(f4_frame, text="Steam Bun", width=15, height=1, bd=3)
    Pie = Button(f4_frame, text="Pie ", width=15, height=1, bd=3)
    Sausage_Roll = Button(f4_frame, text="Sausage Roll", width=15, height=1, bd=3)
    Pizza = Button(f4_frame, text="Pizza", width=15, height=1, bd=3)
    Pizza_Bread = Button(f4_frame, text="Pizza Bread", width=15, height=1, bd=3)
    
    
    Hot_Noodles.grid(row=0, column=0, padx=0)
    Spaghetti_Bun.grid(row=1, column=0, padx=0)    
    Hash_Brown.grid(row=2, column=0, padx=0)    
    Garlic_Bread.grid(row=3, column=0, padx=0)    
    Hot_Dog.grid(row=4, column=0, padx=0)    
    
    Steam_Bun.grid(row=0, column=1, padx=0)    
    Pie.grid(row=1, column=1, padx=0)    
    Sausage_Roll.grid(row=2, column=1, padx=0)    
    Pizza.grid(row=3, column=1, padx=0)    
    Pizza_Bread.grid(row=4, column=1, padx=0)    
    
    
    
    

def f3():
    global f3_frame 
    

    f2_frame.grid_remove()
    f1_frame.grid_remove()
    f4_frame.grid_remove()
    f5_frame.grid_remove()    
    
    f3_frame = LabelFrame(root, height="200", width="350", bd=5)
    f3_frame.grid(row=1, column=0, padx=0)    
    
    Water = Button(f3_frame, text="Water", width=15, height=1, bd=3)
    Frozen = Button(f3_frame, text="Frozen", width=15, height=1, bd=3)
    Milk = Button(f3_frame, text="Milk", width=15, height=1, bd=3)
    Ice_Tea = Button(f3_frame, text="Ice Tea", width=15, height=1, bd=3)
    Barista_Bros = Button(f3_frame, text="Barista Bros", width=15, height=1, bd=3)
    Hot_Chocolate = Button(f3_frame, text="Hot Chocolate", width=15, height=1, bd=3)
    
    Water.grid(row=0, column=0, padx=0)
    Frozen.grid(row=1, column=0, padx=0)
    Milk.grid(row=2, column=0, padx=0)
    Ice_Tea.grid(row=0, column=1, padx=0)
    Barista_Bros.grid(row=1, column=1, padx=0)
    Hot_Chocolate.grid(row=2, column=1, padx=0)
    

def f2():
    global f2_frame 
    
    def mon():
        f22_frame = LabelFrame(root, height="200", width="350", bd=5)
        f22_frame.grid(row=1, column=0, padx=0)
        
    f1_frame.grid_remove()
    f3_frame.grid_remove()
    f4_frame.grid_remove()
    f5_frame.grid_remove()    
    
    f2_frame = LabelFrame(root, height="200", width="350", bd=5)
    f2_frame.grid(row=1, column=0, padx=0)  
    
    MON = Button(f2_frame, text="monday", width=15, height=1, bd=3)
    TUE = Button(f2_frame, text="tuesday", width=15, height=1, bd=3)
    WED = Button(f2_frame, text="wednesday", width=15, height=1, bd=3)
    THU = Button(f2_frame, text="thursday", width=15, height=1, bd=3)
    FRI = Button(f2_frame, text="friday", width=15, height=1, bd=3)
    
    MON.grid(row=0, column=0, pady=3, padx=5)
    TUE.grid(row=1, column=0, pady=3, padx=5)
    WED.grid(row=2, column=0, pady=3, padx=5)
    THU.grid(row=3, column=0, pady=3, padx=5)
    FRI.grid(row=4, column=0, pady=3, padx=5)
    
    
def f1():
    global f1_frame
    
    f2_frame.grid_remove()
    f3_frame.grid_remove()
    f4_frame.grid_remove()
    f5_frame.grid_remove()
    
    f1_frame = LabelFrame(root, height="200", width="350", bd=5)
    f1_frame.grid(row=1, column=0, padx=0)
    
    Fresh_Fruits = Button(f1_frame, text="Fresh Fruits", width=15, height=1, bd=3)
    Fresh_Fruit_Salad = Button(f1_frame, text="Fresh Fruit Salad", width=15, height=1, bd=3)
    Salads = Button(f1_frame, text="Salads", width=15, height=1, bd=3) 
    Sandwiches = Button(f1_frame, text="Sandwiches", width=15, height=1, bd=3) 
    Chicken_Sub = Button(f1_frame, text="Chicken Sub", width=15, height=1, bd=3)
    Wraps = Button(f1_frame, text="Wraps", width=15, height=1, bd=3) 
    Pizza_Bread = Button(f1_frame, text="Pizza Bread", width=15, height=1, bd=3)
    Soup_of_the_Day  = Button(f1_frame, text="Soup of the Day", width=15, height=1, bd=3)
    
    
    Fresh_Fruits.grid(row=0, column=0, pady=3, padx=5)
    Fresh_Fruit_Salad.grid(row=1, column=0, pady=3, padx=5)    
    Salads.grid(row=2, column=0, pady=3, padx=5)    
    Sandwiches.grid(row=3, column=0, pady=3, padx=5)    
    Chicken_Sub.grid(row=0, column=1, pady=3, padx=5)    
    Wraps.grid(row=1, column=1, pady=3, padx=5)
    Pizza_Bread.grid(row=2, column=1, pady=3, padx=5)  
    Soup_of_the_Day.grid(row=3, column=1, pady=3, padx=5)   


def menu():
    
    #################################################################################
    # menu frame, this frame is for menu and selection of items
    menu_frame = LabelFrame(root,  padx=0, pady=0, borderwidth = 5)
    menu_frame.grid(row=0, column=0, columnspan=3) 
  
    website_title = Label(menu_frame, text="BDSC CAFE", padx=5, pady=5, font=("Times", "20", "bold"))
    website_title.grid(row=0, column=0, columnspan=5)
    
    
    HEALTHY_CHOICES = Button(menu_frame, text="healthy choices", width=12, height=1, command=f1)
    MEAL_OF_THE_DAY = Button(menu_frame, text="Meal of the day", width=12, height=1, command=f2)
    DRINKS = Button(menu_frame, text="drinks", width=12, height=1, command=f3)
    HOT_LUNCHES = Button(menu_frame, text="Hot lunch", width=12, height=1, command=f4)
    SNACKS = Button(menu_frame, text="snacks", width=12, height=1, command=f5)   
    
    
    HEALTHY_CHOICES.grid(row=1, column=0, pady=0, padx=2)
    MEAL_OF_THE_DAY.grid(row=1, column=1, pady=0, padx=2)
    DRINKS.grid(row=1, column=2, pady=0, padx=2)
    HOT_LUNCHES.grid(row=1, column=3, pady=0, padx=2)
    SNACKS.grid(row=1, column=4, pady=0, padx=2)
    
    
    
    ####################################### for looks#########################################
    extra_1 = LabelFrame(root, height="200", width="350", borderwidth = 5)
    extra_1.grid(row=1, column=0, padx=0)
    f1()
    extra_2 = LabelFrame(root, height="200", width="150", borderwidth = 5)
    extra_2.grid(row=1, column=2)
    
    
    #####################################################################################
    #Buttons Frame, this frame is for function frames
    Buttons_frame = LabelFrame(root, height="40", width="450", borderwidth = 5)
    Buttons_frame.grid(row=2, column=0, columnspan=3)
    
    #off screen button codes
    add_item_BTN = Button(Buttons_frame, text="add item", width=8, height=1, anchor=W, font=("Times", "20", "bold"),bd=5)
    remove_item_BTN = Button(Buttons_frame, text="remove item", width=10, height=1, anchor=W, font=("Times", "20", "bold"),bd=5)
    purchess_item_BTN = Button(Buttons_frame, text="purchess", width=8, height=1, anchor=W, font=("Times", "20", "bold"),bd=5)
    
    #on screen button codes
    add_item_BTN.grid(row=0, column=0, pady=5, padx=5)
    remove_item_BTN.grid(row=0, column=1, pady=5, padx=5)
    purchess_item_BTN.grid(row=0, column=2, pady=5, padx=5)
    

root = Tk()
root.title("BDSC_CAFE")

################################## the menu frame #####################################
f1_frame = Frame(root)
f2_frame = Frame(root)

f22_frame = Frame(root)

f3_frame = Frame(root)
f4_frame = Frame(root)
f5_frame = Frame(root)
#######################################################################################\

menu()

root.mainloop()
from tkinter import*
import tkinter as tk

def frames_remove():
    f1.grid_remove()
    f2.grid_remove()
    f3.grid_remove()
    f4.grid_remove()
    f5.grid_remove()
    f6.grid_remove()
    f7.grid_remove()
    f8.grid_remove()
    f9.grid_remove()
    f10.grid_remove()
    f11.grid_remove()
    f12.grid_remove()
    f13.grid_remove()
    f14.grid_remove()
    f15.grid_remove()
    f16.grid_remove()
    f17.grid_remove()
    f18.grid_remove()
    f19.grid_remove()
    f20.grid_remove()
    f21.grid_remove()
    f22.grid_remove()
    f23.grid_remove()
    f24.grid_remove()
    f25.grid_remove()
    f26.grid_remove()
    f27.grid_remove()
    f28.grid_remove()
    f29.grid_remove()
    f30.grid_remove()
    f31.grid_remove()
    f32.grid_remove()
    f33.grid_remove()
    f34.grid_remove()
    f35.grid_remove()
    f36.grid_remove()
    f37.grid_remove()
    f38.grid_remove()
    f39.grid_remove()
    f40.grid_remove()
    
    
################################## Healty chocies###############################    
def FF():
    frames_remove()
    global f1       
    
    f1 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f1.grid(row=1, column=1)
    
    FF_checkbutton=Checkbutton(f1, text= "Fresh Fruits")
    FF_amount=Label(f1, text= "entre amount below")
    FF_entry=Entry(f1, text= "Fresh Fruits")    
    
    FF_checkbutton.grid(row=1)
    FF_amount.grid(row=2)
    FF_entry.grid(row=3)
    
def FFS():
    frames_remove()
    global f2        
    
    f2 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f2.grid(row=1, column=1) 
    
    FFS_label=Label(f2, text= "Fresh Fruit Salad")
    summer=Checkbutton(f2, text= "is it summer? ")    
    FFS_checkbutton=Checkbutton(f2, text= "Fresh Fruit Salad")
    FFS_amount=Label(f2, text= "entre amount below")
    FFS_entry=Entry(f2)    
    

    summer.grid(row=0)
    FFS_checkbutton.grid(row=1)
    FFS_amount.grid(row=2)
    FFS_entry.grid(row=3)
    
def S():
    frames_remove()
    global f3        
    
    f3 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f3.grid(row=1, column=1) 
    
    S_checkbutton=Checkbutton(f3,  text= "Salads ")
    S_amount=Label(f3, text= "entre amount below")
    S_entry=Entry(f3,)    

    S_checkbutton.grid(row=1)
    S_amount.grid(row=2)
    S_entry.grid(row=3)  

def SW():
    frames_remove()
    global f4        
    
    f4 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f4.grid(row=1, column=1) 
    
    SW_label=Label(f4, text= "Sandwiches")
    
    
    SW_label.grid(row=0) 

def CS():
    frames_remove()
    global f5        
    
    f5 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f5.grid(row=1, column=1) 
    
    CS_label=Label(f5, text= " Chicken Sub")
    
    
    CS_label.grid(row=0)     
    
def Ww():
    frames_remove()
    global f6        
    
    
    f6 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f6.grid(row=1, column=1) 
    
    Ww_label=Label(f6, text= "Wraps")
    
    
    Ww_label.grid(row=0)     

def PB():
    frames_remove()
    global f7        
    
    f7 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f7.grid(row=1, column=1) 
    
    PB_label=Label(f7, text= "Pizza Bread")
    
    
    PB_label.grid(row=0) 

def SOTD():
    frames_remove()
    global f8        
    
    f8 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f8.grid(row=1, column=1) 
    
    STOD_label=Label(f8, text= "Soup of the Day")
    
    
    STOD_label.grid(row=0)   

################################## drinks ################################
def Wa():
    frames_remove()
    global f9        
    
    f9 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f9.grid(row=1, column=1) 
    
    Wa_label=Label(f9, text="Water")
    
    
    Wa_label.grid(row=0)    
def F():
    frames_remove()
    global f10        
    
    f10 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f10.grid(row=1, column=1) 
    
    F_label=Label(f10, text= "Frozen")
    
    
    F_label.grid(row=0)  

def M():
    frames_remove()
    global f11        
    
    f11 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f11.grid(row=1, column=1) 
    
    M_label=Label(f11, text= "Milk")
    
    
    M_label.grid(row=0)   
    
def IT():
    frames_remove()
    global f12        
    
    f12 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f12.grid(row=1, column=1) 
    
    IT_label=Label(f12, text= "Ice Tea")
    
    
    IT_label.grid(row=0)      

def BB():
    frames_remove()
    global f13        
    
    f13 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f13.grid(row=1, column=1) 
    
    BB_label=Label(f13, text= "Barista Bros")
    
    
    BB_label.grid(row=0)   

def HC():
    frames_remove()
    global f14       
    
    f14 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f14.grid(row=1, column=1) 
    
    HC_label=Label(f14, text= "Hot Chocolate")
    
    
    HC_label.grid(row=0)     
################################# snacks ######################################

def PC():
    frames_remove()
    global f15       
    
    f15 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f15.grid(row=1, column=1) 
    
    PC_label=Label(f15, text= "Potato Chips")
    
    
    PC_label.grid(row=0)     

def POPC():
    frames_remove()
    global f16        
        
    f16 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f16.grid(row=1, column=1) 
    
    POPC_label=Label(f16, text= "Popcorn")
    
    
    POPC_label.grid(row=0)  
    
def C():
    frames_remove()
    global f17        
    
    f17 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f17.grid(row=1, column=1) 
    
    c_label=Label(f17, text= "Chips")
    
    
    c_label.grid(row=0) 

def NC():
    frames_remove()
    global f18        
       
    f18 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f18.grid(row=1, column=1) 
  
    NC_label=Label(f18, text= "Noodle Snack")
    
    
    NC_label.grid(row=0)    
    
def AC():
    frames_remove()
    global f19        
          
    f19 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f19.grid(row=1, column=1) 
    
    AC_label=Label(f19, text= "Afghan Cookies")
    
    
    AC_label.grid(row=0)     
def MHCCC():
    frames_remove()
    global f20        
    
    
    f20 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f20.grid(row=1, column=1) 
    
    MHCCC_label=Label(f20, text= "Mrs Higgins Chocolate Chip Cookies")
    
    
    MHCCC_label.grid(row=0)
    
def CFB():
    frames_remove()
    global f21        
       
    f21 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f21.grid(row=1, column=1) 
    
    CFB_label=Label(f21, text= "Chocolate Fudge Brownie")
    
    
    CFB_label.grid(row=0)

def RC():
    frames_remove()
    global f22     
    
        
    f22 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f22.grid(row=1, column=1) 
    
    RC_label=Label(f22, text= "Rice Crackers")
    
    
    RC_label.grid(row=0)  
################################# HOT LUNCHES ##############################
def HN():
    frames_remove()
    global f23        
    
    f23 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f23.grid(row=1, column=1) 
    
    HN_label=Label(f23, text= "Hot Noodles")
    
    
    HN_label.grid(row=0)

def SB():
    frames_remove()
    global f24    
    
    f24 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f24.grid(row=1, column=1) 
    
    SB_label=Label(f24, text= "Spaghetti Bun")
    
    
    SB_label.grid(row=0)     

def HB():
    frames_remove()
    global f25        
    
    f25 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f25.grid(row=1, column=1) 
    
    HB_label=Label(f25, text= "Hash Brown")
    
    
    HB_label.grid(row=0) 

def GB():
    frames_remove()
    global f26       
            
    f26 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f26.grid(row=1, column=1) 
    
    GB_label=Label(f26, text= "Garlic Bread")
    
    
    GB_label.grid(row=0)     
    
def HD():
    frames_remove()
    global f27
    
    f27 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f27.grid(row=1, column=1) 
    
    HD_label=Label(f27, text= "Hot Dog")
    
    
    HD_label.grid(row=0)     
def SB():
    frames_remove()
    global f28        
    
    f28 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f28.grid(row=1, column=1) 
    
    SB_label=Label(f28, text= "Steam Bun")
    
    
    SB_label.grid(row=0) 
    
def P():
    frames_remove()
    global f29
    
    
    f29 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f29.grid(row=1, column=1) 
    
    P_label=Label(f29, text= "Pie")
    
    
    P_label.grid(row=0) 
    
def SR():
    frames_remove()
    global f30
    
    f30 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f30.grid(row=1, column=1) 
    
    SR_label=Label(f30, text= "Sausage Roll")
    
    
    SR_label.grid(row=0)     

def Pizza():
    frames_remove()
    global f31
            
    f31 = LabelFrame(root, padx=0, pady=0, borderwidth = 5)
    f31.grid(row=1, column=1) 
    
    Pizza_label=Label(f31, text= "Pizza")
    
    
    Pizza_label.grid(row=0) 
####################### pizza bread


########################################## menu frames #############################    
def f_5():
    global f5_frame 
    
    f2_frame.grid_remove()
    f3_frame.grid_remove()
    f4_frame.grid_remove()
    f1_frame.grid_remove()    

    f5_frame = LabelFrame(root, height="200", width="350", bd=5)
    f5_frame.grid(row=1, column=0, padx=0)
    
    Potato_Chips = Button(f5_frame, text="Potato Chips ", width=12, height=1, bd=3, command=PC)
    Popcorn  = Button(f5_frame, text="Popcorn", width=12, height=1, bd=3, command=POPC)
    Chips  = Button(f5_frame, text="Chips ", width=12, height=1, bd=3, command=C)
    Noodle_Snack = Button(f5_frame, text="Noodle Snack", width=12, height=1, bd=3, command=NC)
    
    Afghan_Cookies = Button(f5_frame, text="Afghan Cookies", width=28, height=1, bd=3, command=AC)
    Mrs_Higgins_Chocolate_Chip_Cookies = Button(f5_frame, text="Mrs Higgins Chocolate Chip Cookies ", width=28, height=1, bd=3, command=MHCCC)
    Chocolate_Fudge_Brownie = Button(f5_frame, text="Chocolate Fudge Brownie", width=28, height=1, bd=3, command=CFB)
    Rice_Crackers = Button(f5_frame, text="Rice Crackers", width=28, height=1, bd=3, command=RC)
    
    Potato_Chips.grid(row=0, column=0, pady=3, padx=5)
    Popcorn.grid(row=1, column=0, pady=3, padx=5)
    Chips.grid(row=2, column=0, pady=3, padx=5)
    Noodle_Snack.grid(row=3, column=0, pady=3, padx=5) 
    
    Afghan_Cookies.grid(row=0, column=1, pady=3, padx=5)
    Mrs_Higgins_Chocolate_Chip_Cookies.grid(row=1, column=1, pady=3, padx=5)
    Chocolate_Fudge_Brownie.grid(row=2, column=1, pady=3, padx=5)
    Rice_Crackers.grid(row=3, column=1, pady=3, padx=5)
    
    
def f_4(): 
    global f4_frame 
    
    f2_frame.grid_remove()
    f3_frame.grid_remove()
    f1_frame.grid_remove()
    f5_frame.grid_remove()    
    
    f4_frame = LabelFrame(root, height="200", width="350", bd=5)
    f4_frame.grid(row=1, column=0, padx=0)
    
    Hot_Noodles = Button(f4_frame, text="Hot Noodles", width=15, height=1, bd=3, command=HN)
    Spaghetti_Bun = Button(f4_frame, text="Spaghetti Bun", width=15, height=1, bd=3, command=SB)
    Hash_Brown  = Button(f4_frame, text="Hash Brown", width=15, height=1, bd=3, command=HB)
    Garlic_Bread = Button(f4_frame, text="Garlic Bread ", width=15, height=1, bd=3, command=GB)
    Hot_Dog = Button(f4_frame, text="Hot Dog", width=15, height=1, bd=3, command=HD)
    
    Steam_Bun  = Button(f4_frame, text="Steam Bun", width=15, height=1, bd=3, command=SB)
    Pie = Button(f4_frame, text="Pie ", width=15, height=1, bd=3, command=P)
    Sausage_Roll = Button(f4_frame, text="Sausage Roll", width=15, height=1, bd=3, command=SR)
    Pizza_BTN = Button(f4_frame, text="Pizza", width=15, height=1, bd=3, command=Pizza)
    Pizza_Bread = Button(f4_frame, text="Pizza Bread", width=15, height=1, bd=3, command=PB)
      
    Hot_Noodles.grid(row=0, column=0, padx=0)
    Spaghetti_Bun.grid(row=1, column=0, padx=0)    
    Hash_Brown.grid(row=2, column=0, padx=0)    
    Garlic_Bread.grid(row=3, column=0, padx=0)    
    Hot_Dog.grid(row=4, column=0, padx=0)    
    
    Steam_Bun.grid(row=0, column=1, padx=0)    
    Pie.grid(row=1, column=1, padx=0)    
    Sausage_Roll.grid(row=2, column=1, padx=0)    
    Pizza_BTN.grid(row=3, column=1, padx=0)    
    Pizza_Bread.grid(row=4, column=1, padx=0)    

def f_3():
    global f3_frame 
    
    f2_frame.grid_remove()
    f1_frame.grid_remove()
    f4_frame.grid_remove()
    f5_frame.grid_remove()    
    
    f3_frame = LabelFrame(root, height="200", width="350", bd=5)
    f3_frame.grid(row=1, column=0, padx=0)    
    
    Water = Button(f3_frame, text="Water", width=15, height=1, bd=3, command=Wa)
    Frozen = Button(f3_frame, text="Frozen", width=15, height=1, bd=3, command=F)
    Milk = Button(f3_frame, text="Milk", width=15, height=1, bd=3, command=M)
    Ice_Tea = Button(f3_frame, text="Ice Tea", width=15, height=1, bd=3, command=IT)
    Barista_Bros = Button(f3_frame, text="Barista Bros", width=15, height=1, bd=3, command=BB)
    Hot_Chocolate = Button(f3_frame, text="Hot Chocolate", width=15, height=1, bd=3, command=HC)
    
    Water.grid(row=0, column=0, padx=0)
    Frozen.grid(row=1, column=0, padx=0)
    Milk.grid(row=2, column=0, padx=0)
    Ice_Tea.grid(row=0, column=1, padx=0)
    Barista_Bros.grid(row=1, column=1, padx=0)
    Hot_Chocolate.grid(row=2, column=1, padx=0)
    

def f_2():
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
    
    
def f_1():
    global f1_frame
    
    f2_frame.grid_remove()
    f3_frame.grid_remove()
    f4_frame.grid_remove()
    f5_frame.grid_remove()
    
    f1_frame = LabelFrame(root, height="200", width="350", bd=5)
    f1_frame.grid(row=1, column=0, padx=0)
    
    Fresh_Fruits = Button(f1_frame, text="Fresh Fruits", width=15, height=1, bd=3, command=FF)
    Fresh_Fruit_Salad = Button(f1_frame, text="Fresh Fruit Salad", width=15, height=1, bd=3, command=FFS)
    Salads = Button(f1_frame, text="Salads", width=15, height=1, bd=3, command=S) 
    Sandwiches = Button(f1_frame, text="Sandwiches", width=15, height=1, bd=3, command=SW) 
    Chicken_Sub = Button(f1_frame, text="Chicken Sub", width=15, height=1, bd=3, command=CS)
    Wraps = Button(f1_frame, text="Wraps", width=15, height=1, bd=3, command=Ww) 
    Pizza_Bread = Button(f1_frame, text="Pizza Bread", width=15, height=1, bd=3, command=PB)
    Soup_of_the_Day  = Button(f1_frame, text="Soup of the Day", width=15, height=1, bd=3, command=SOTD)
    
    
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
    
    HEALTHY_CHOICES = Button(menu_frame, text="healthy choices", width=12, height=1, command=f_1)
    MEAL_OF_THE_DAY = Button(menu_frame, text="Meal of the day", width=12, height=1, command=f_2)
    DRINKS = Button(menu_frame, text="drinks", width=12, height=1, command=f_3)
    HOT_LUNCHES = Button(menu_frame, text="Hot lunch", width=12, height=1, command=f_4)
    SNACKS = Button(menu_frame, text="snacks", width=12, height=1, command=f_5)   
        
    HEALTHY_CHOICES.grid(row=1, column=0, pady=0, padx=2)
    MEAL_OF_THE_DAY.grid(row=1, column=1, pady=0, padx=2)
    DRINKS.grid(row=1, column=2, pady=0, padx=2)
    HOT_LUNCHES.grid(row=1, column=3, pady=0, padx=2)
    SNACKS.grid(row=1, column=4, pady=0, padx=2)

    ####################################### for looks#########################################
    extra_1 = LabelFrame(root, height="200", width="350", borderwidth = 5)
    extra_1.grid(row=1, column=0, padx=0)
    f_1()
    extra_2 = LabelFrame(root, height="200", width="150", borderwidth = 5)
    extra_2.grid(row=1, column=1)    
    FF()
    #####################################################################################
    #Buttons Frame, this frame is for function frames
    Buttons_frame = LabelFrame(root, height="40", width="450", borderwidth = 5)
    Buttons_frame.grid(row=2, column=0, columnspan=3)
    
    #off screen button codes
    add_item_BTN = Button(Buttons_frame, text="add item", width=8, height=1, font=("Times", "20", "bold"),bd=5)
    remove_item_BTN = Button(Buttons_frame, text="remove item", width=10, height=1, font=("Times", "20", "bold"),bd=5)
    purchess_item_BTN = Button(Buttons_frame, text="purchess", width=8, height=1, font=("Times", "20", "bold"),bd=5)
    
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

###################################### declare food frames #####################
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)
f6 = Frame(root)
f7 = Frame(root)
f8 = Frame(root)
f9 = Frame(root)
f10 = Frame(root)
f11 = Frame(root)
f12 = Frame(root)
f13 = Frame(root)
f14 = Frame(root)
f15 = Frame(root)
f16 = Frame(root)
f17 = Frame(root)
f18 = Frame(root)
f19 = Frame(root)
f20 = Frame(root)
f21 = Frame(root)
f22 = Frame(root)
f23 = Frame(root)
f24 = Frame(root)
f25 = Frame(root)
f26 = Frame(root)
f27 = Frame(root)
f28 = Frame(root)
f29 = Frame(root)
f30 = Frame(root)
f31 = Frame(root)
f32 = Frame(root)
f33 = Frame(root)
f34 = Frame(root)
f35 = Frame(root)
f36 = Frame(root)
f37 = Frame(root)
f38 = Frame(root)
f39 = Frame(root)
f40 = Frame(root)

menu()

root.mainloop()
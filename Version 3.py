from tkinter import *
import sqlite3
from tkinter import Label

conn = sqlite3.connect('BDSC_Students.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Student (firstname text, lastname text, age text, username text, password text)")
conn.commit()
conn.close()


################################################################################
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


###############################################################################


###############################################################################
def check_FF():
    if (variable1.get() == 1):
        FF_entry.configure(state=NORMAL)
        varFF.set("")
    elif (variable1.get() == 0):
        FF_entry.configure(state=DISABLED)
        varFF.set("0")


def check_FFS():
    if (variable2.get() == 1):
        FFS_entry.configure(state=NORMAL)
        varFFS.set("")
    elif (variable2.get() == 0):
        FFS_entry.configure(state=DISABLED)
        varFFS.set("0")


def check_S():
    if (variable3.get() == 1):
        S_entry.configure(state=NORMAL)
        varS.set("")
    elif (variable3.get() == 0):
        S_entry.configure(state=DISABLED)
        varS.set("0")


def check_SW():
    if (variable4.get() == 1):
        SW_entry.configure(state=NORMAL)
        varSW.set("")
    elif (variable4.get() == 0):
        SW_entry.configure(state=DISABLED)
        varSW.set("0")


def check_CS():
    if (variable5.get() == 1):
        CS_entry.configure(state=NORMAL)
        varCS.set("")
    elif (variable5.get() == 0):
        CS_entry.configure(state=DISABLED)
        varCS.set("0")


def check_Ww():
    if (variable6.get() == 1):
        Ww_entry.configure(state=NORMAL)
        varWw.set("")
    elif (variable6.get() == 0):
        Ww_entry.configure(state=DISABLED)
        varWw.set("0")


def check_PB():
    if (variable7.get() == 1):
        PB_entry.configure(state=NORMAL)
        varPB.set("")
    elif (variable7.get() == 0):
        PB_entry.configure(state=DISABLED)
        varPB.set("0")


def check_SOTD():
    if (variable8.get() == 1):
        SOTD_entry.configure(state=NORMAL)
        varSOTD.set("")
    elif (variable8.get() == 0):
        SOTD_entry.configure(state=DISABLED)
        varSOTD.set("0")


def check_Wa():
    if (variable9.get() == 1):
        Wa_entry.configure(state=NORMAL)
        varWa.set("")
    elif (variable9.get() == 0):
        Wa_entry.configure(state=DISABLED)
        varWa.set("0")


def check_F():
    if (variable10.get() == 1):
        F_entry.configure(state=NORMAL)
        varF.set("")
    elif (variable10.get() == 0):
        F_entry.configure(state=DISABLED)
        varF.set("0")


def check_M():
    if (variable11.get() == 1):
        M_entry.configure(state=NORMAL)
        varM.set("")
    elif (variable11.get() == 0):
        M_entry.configure(state=DISABLED)
        varM.set("0")


def check_IT():
    if (variable12.get() == 1):
        IT_entry.configure(state=NORMAL)
        varIT.set("")
    elif (variable12.get() == 0):
        IT_entry.configure(state=DISABLED)
        varIT.set("0")


def check_BB():
    if (variable13.get() == 1):
        BB_entry.configure(state=NORMAL)
        varBB.set("")
    elif (variable13.get() == 0):
        BB_entry.configure(state=DISABLED)
        varBB.set("0")


def check_HC():
    if (variable14.get() == 1):
        HC_entry.configure(state=NORMAL)
        varHC.set("")
    elif (variable14.get() == 0):
        HC_entry.configure(state=DISABLED)
        varHC.set("0")


def check_PC():
    if (variable15.get() == 1):
        PC_entry.configure(state=NORMAL)
        varPC.set("")
    elif (variable15.get() == 0):
        PC_entry.configure(state=DISABLED)
        varPC.set("0")


def check_POPC():
    if (variable16.get() == 1):
        POPC_entry.configure(state=NORMAL)
        varPOPC.set("")
    elif (variable16.get() == 0):
        POPC_entry.configure(state=DISABLED)
        varPOPC.set("0")


def check_C():
    if (variable17.get() == 1):
        C_entry.configure(state=NORMAL)
        varC.set("")
    elif (variable17.get() == 0):
        C_entry.configure(state=DISABLED)
        varC.set("0")


def check_NC():
    if (variable18.get() == 1):
        NC_entry.configure(state=NORMAL)
        varNC.set("")
    elif (variable18.get() == 0):
        NC_entry.configure(state=DISABLED)
        varNC.set("0")


def check_AC():
    if (variable19.get() == 1):
        AC_entry.configure(state=NORMAL)
        varAC.set("")
    elif (variable19.get() == 0):
        AC_entry.configure(state=DISABLED)
        varAC.set("0")


def check_MHCCC():
    if (variable20.get() == 1):
        MHCCC_entry.configure(state=NORMAL)
        varMHCCC.set("")
    elif (variable20.get() == 0):
        MHCCC_entry.configure(state=DISABLED)
        varMHCCC.set("0")


def check_CFB():
    if (variable21.get() == 1):
        CFB_entry.configure(state=NORMAL)
        varCFB.set("")
    elif (variable21.get() == 0):
        CFB_entry.configure(state=DISABLED)
        varCFB.set("0")


def check_RC():
    if (variable22.get() == 1):
        RC_entry.configure(state=NORMAL)
        varRC.set("")
    elif (variable22.get() == 0):
        RC_entry.configure(state=DISABLED)
        varRC.set("0")


def check_HN():
    if (variable23.get() == 1):
        HN_entry.configure(state=NORMAL)
        varHN.set("")
    elif (variable23.get() == 0):
        HN_entry.configure(state=DISABLED)
        varHN.set("0")


def check_SB():
    if (variable24.get() == 1):
        SB_entry.configure(state=NORMAL)
        varSB.set("")
    elif (variable24.get() == 0):
        SB_entry.configure(state=DISABLED)
        varSB.set("0")


def check_HB():
    if (variable25.get() == 1):
        HB_entry.configure(state=NORMAL)
        varHB.set("")
    elif (variable25.get() == 0):
        HB_entry.configure(state=DISABLED)
        varHB.set("0")


def check_GB():
    if (variable26.get() == 1):
        GB_entry.configure(state=NORMAL)
        varGB.set("")
    elif (variable26.get() == 0):
        GB_entry.configure(state=DISABLED)
        varGB.set("0")


def check_HD():
    if (variable27.get() == 1):
        HD_entry.configure(state=NORMAL)
        varHD.set("")
    elif (variable27.get() == 0):
        HD_entry.configure(state=DISABLED)
        varHD.set("0")


def check_Sb():
    if (variable28.get() == 1):
        SB.configure(state=NORMAL)
        varSb.set("")
    elif (variable28.get() == 0):
        SB_entry.configure(state=DISABLED)
        varSb.set("0")


def check_P():
    if (variable29.get() == 1):
        P_entry.configure(state=NORMAL)
        varP.set("")
    elif (variable29.get() == 0):
        P_entry.configure(state=DISABLED)
        varP.set("0")


def check_SR():
    if (variable30.get() == 1):
        SR_entry.configure(state=NORMAL)
        varSR.set("")
    elif (variable30.get() == 0):
        SR_entry.configure(state=DISABLED)
        varSR.set("0")


def check_Pizza():
    if (variable31.get() == 1):
        Pizza_entry.configure(state=NORMAL)
        varPizza.set("")
    elif (variable31.get() == 0):
        Pizza_entry.configure(state=DISABLED)
        varPizza.set("0")


################################## Healty chocies###############################

def FF():
    frames_remove()
    global f1
    global FF_entry

    f1 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f1.grid(row=1, column=1)

    FF_checkbutton = Checkbutton(f1, text="Fresh Fruits", variable=variable1, onvalue=1, offvalue=0, command=check_FF)
    price_label = Label(f1, text="price = $1")
    FF_entry = Entry(f1, textvariable=varFF, width=8, state=DISABLED)

    FF_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    FF_entry.grid(row=2)

def FFS():
    frames_remove()
    global f2
    global FFS_entry

    f2 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f2.grid(row=1, column=1)

    FFS_checkbutton = Checkbutton(f2, text="Fresh Fruit Salad", variable=variable2, onvalue=1, offvalue=0,
                                  command=check_FFS)
    price_label = Label(f2, text="price = $4.5")
    FFS_entry = Entry(f2, textvariable=varFFS, width=8, state=DISABLED)

    FFS_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    FFS_entry.grid(row=2)


def S():
    frames_remove()
    global f3
    global S_entry

    f3 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f3.grid(row=1, column=1)

    S_checkbutton = Checkbutton(f3, text="Salad", variable=variable3, onvalue=1, offvalue=0, command=check_S)
    price_label = Label(f3, text="price = $6")
    S_entry = Entry(f3, textvariable=varS, width=8, state=DISABLED)

    S_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    S_entry.grid(row=2)


def SW():
    frames_remove()
    global f4
    global SW_entry

    f4 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f4.grid(row=1, column=1)

    SW_checkbutton = Checkbutton(f4, text="Sandwich", variable=variable4, onvalue=1, offvalue=0, command=check_SW)
    price_label = Label(f4, text="price = $4")
    SW_entry = Entry(f4, textvariable=varSW, width=8, state=DISABLED)

    SW_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    SW_entry.grid(row=2)


def CS():
    frames_remove()
    global f5
    global CS_entry

    f5 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f5.grid(row=1, column=1)

    CS_checkbutton = Checkbutton(f5, text="Chicken Sub ", variable=variable5, onvalue=1, offvalue=0, command=check_CS)
    price_label = Label(f5, text="price = $4")
    CS_entry = Entry(f5, textvariable=varCS, width=8, state=DISABLED)

    CS_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    CS_entry.grid(row=2)


def Ww():
    frames_remove()
    global f6
    global Ww_entry
    f6 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f6.grid(row=1, column=1)

    Ww_checkbutton = Checkbutton(f6, text="Wraps", variable=variable6, onvalue=1, offvalue=0, command=check_Ww)
    price_label = Label(f6, text="price = $4.5")
    Ww_entry = Entry(f6, textvariable=varWw, width=8, state=DISABLED)

    Ww_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    Ww_entry.grid(row=2)


def PB():
    frames_remove()
    global f7
    global PB_entry

    f7 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f7.grid(row=1, column=1)

    PB_checkbutton = Checkbutton(f7, text="Pizza Bread", variable=variable7, onvalue=1, offvalue=0, command=check_PB)
    price_label = Label(f7, text="price = $3")
    PB_entry = Entry(f7, textvariable=varPB, width=8, state=DISABLED)

    PB_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    PB_entry.grid(row=2)


def SOTD():
    frames_remove()
    global f8
    global SOTD_entry

    f8 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f8.grid(row=1, column=1)

    SOTD_checkbutton = Checkbutton(f8, text="Soup of the day", variable=variable8, onvalue=1, offvalue=0,
                                   command=check_SOTD)
    price_label = Label(f8, text="price = $4")
    SOTD_entry = Entry(f8, textvariable=varSOTD, width=8, state=DISABLED)

    SOTD_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    SOTD_entry.grid(row=2)


################################## drinks ################################
def Wa():
    frames_remove()
    global f9
    global Wa_entry

    f9 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f9.grid(row=1, column=1)

    Wa_checkbutton = Checkbutton(f9, text="water", variable=variable9, onvalue=1, offvalue=0, command=check_Wa)
    price_label = Label(f9, text="price = $3")
    Wa_entry = Entry(f9, textvariable=varWa, width=8, state=DISABLED)

    Wa_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    Wa_entry.grid(row=2)


def F():
    frames_remove()
    global f10
    global F_entry

    f10 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f10.grid(row=1, column=1)

    F_checkbutton = Checkbutton(f10, text="Frozen", variable=variable10, onvalue=1, offvalue=0, command=check_F)
    price_label = Label(f10, text="price = $2")
    F_entry = Entry(f10, textvariable=varF, width=8, state=DISABLED)

    F_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    F_entry.grid(row=2)


def M():
    frames_remove()
    global f11
    global M_entry

    f11 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f11.grid(row=1, column=1)

    M_checkbutton = Checkbutton(f11, text="Milk", variable=variable11, onvalue=1, offvalue=0, command=check_M)
    price_label = Label(f11, text="price = $3")
    M_entry = Entry(f11, textvariable=varM, width=8, state=DISABLED)

    M_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    M_entry.grid(row=2)


def IT():
    frames_remove()
    global f12
    global IT_entry

    f12 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f12.grid(row=1, column=1)

    IT_checkbutton = Checkbutton(f12, text="Ice Tea", variable=variable12, onvalue=1, offvalue=0, command=check_IT)
    price_label = Label(f12, text="price = $4")
    IT_entry = Entry(f12, textvariable=varIT, width=8, state=DISABLED)

    IT_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    IT_entry.grid(row=2)


def BB():
    frames_remove()
    global f13
    global BB_entry

    f13 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f13.grid(row=1, column=1)

    BB_checkbutton = Checkbutton(f13, text="Barista Bros", variable=variable13, onvalue=1, offvalue=0, command=check_BB)
    price_label = Label(f13, text="price = $4")
    BB_entry = Entry(f13, textvariable=varBB, width=8, state=DISABLED)

    BB_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    BB_entry.grid(row=2)


def HC():
    frames_remove()
    global f14
    global HC_entry

    f14 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f14.grid(row=1, column=1)

    HC_checkbutton = Checkbutton(f14, text="Hot Chocolate", variable=variable14, onvalue=1, offvalue=0,
                                 command=check_HC)
    price_label = Label(f14, text="price = $2")
    HC_entry = Entry(f14, textvariable=varHC, width=8, state=DISABLED)

    HC_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    HC_entry.grid(row=2)


################################# snacks ######################################

def PC():
    frames_remove()
    global f15
    global PC_entry

    f15 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f15.grid(row=1, column=1)

    PC_checkbutton = Checkbutton(f15, text="Potato Chips", variable=variable15, onvalue=1, offvalue=0, command=check_PC)
    price_label = Label(f15, text="price = $2")
    PC_entry = Entry(f15, textvariable=varPC, width=8, state=DISABLED)

    PC_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    PC_entry.grid(row=2)


def POPC():
    frames_remove()
    global f16
    global POPC_entry

    f16 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f16.grid(row=1, column=1)

    POPC_checkbutton = Checkbutton(f16, text="Popcorn", variable=variable16, onvalue=1, offvalue=0, command=check_POPC)
    price_label = Label(f16, text="price = $2")
    POPC_entry = Entry(f16, textvariable=varPOPC, width=8, state=DISABLED)

    POPC_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    POPC_entry.grid(row=2)


def C():
    frames_remove()
    global f17
    global C_entry

    f17 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f17.grid(row=1, column=1)

    C_checkbutton = Checkbutton(f17, text="Chips", variable=variable17, onvalue=1, offvalue=0, command=check_C)
    price_label = Label(f17, text="price = $2")
    C_entry = Entry(f17, textvariable=varC, width=8, state=DISABLED)

    C_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    C_entry.grid(row=2)


def NC():
    frames_remove()
    global f18
    global NC_entry

    f18 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f18.grid(row=1, column=1)
    NC_checkbutton = Checkbutton(f18, text="Noodle Snack ", variable=variable18, onvalue=1, offvalue=0,
                                 command=check_NC)
    price_label = Label(f18, text="price = $1")
    NC_entry = Entry(f18, textvariable=varNC, width=8, state=DISABLED)

    NC_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    NC_entry.grid(row=2)


def AC():
    frames_remove()
    global f19
    global AC_entry

    f19 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f19.grid(row=1, column=1)

    AC_checkbutton = Checkbutton(f19, text="Afghan Cookies", variable=variable19, onvalue=1, offvalue=0,
                                 command=check_AC)
    price_label = Label(f19, text="price = $1")
    AC_entry = Entry(f19, textvariable=varAC, width=8, state=DISABLED)

    AC_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    AC_entry.grid(row=2)


def MHCCC():
    frames_remove()
    global f20
    global MHCCC_entry

    f20 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f20.grid(row=1, column=1)

    MHCCC_checkbutton = Checkbutton(f20, text="Mrs Higgins Chocolate Chip Cookies ", variable=variable20, onvalue=1,
                                    offvalue=0, command=check_MHCCC)
    price_label = Label(f20, text="price = $3")
    MHCCC_entry = Entry(f20, textvariable=varMHCCC, width=8, state=DISABLED)

    MHCCC_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    MHCCC_entry.grid(row=2)


def CFB():
    frames_remove()
    global f21
    global CFB_entry

    f21 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f21.grid(row=1, column=1)

    CFB_checkbutton = Checkbutton(f21, text="Chocolate Fudge Brownie", variable=variable21, onvalue=1, offvalue=0,
                                  command=check_CFB)
    price_label = Label(f21, text="price = $3")
    CFB_entry = Entry(f21, textvariable=varCFB, width=8, state=DISABLED)

    CFB_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    CFB_entry.grid(row=2)


def RC():
    frames_remove()
    global f22
    global RC_entry

    f22 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f22.grid(row=1, column=1)

    RC_checkbutton = Checkbutton(f22, text="Rice Crackers", variable=variable22, onvalue=1, offvalue=0,
                                 command=check_RC)
    price_label = Label(f22, text="price = $.50C")
    RC_entry = Entry(f22, textvariable=varRC, width=8, state=DISABLED)

    RC_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    RC_entry.grid(row=2)


################################# HOT LUNCHES ##############################
def HN():
    frames_remove()
    global f23
    global HN_entry

    f23 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f23.grid(row=1, column=1)

    HN_checkbutton = Checkbutton(f23, text="Pizza", variable=variable23, onvalue=1, offvalue=0, command=check_HN)
    price_label = Label(f23, text="price = $3.50")
    HN_entry = Entry(f23, textvariable=varHN, width=8, state=DISABLED)

    HN_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    HN_entry.grid(row=2)


def SB():
    frames_remove()
    global f24
    global SB_entry
    f24 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f24.grid(row=1, column=1)

    SB_checkbutton = Checkbutton(f24, text="Spaghetti Bun", variable=variable24, onvalue=1, offvalue=0,
                                 command=check_SB)
    price_label = Label(f24, text="price = $1.50")
    SB_entry = Entry(f24, textvariable=varSB, width=8, state=DISABLED)

    SB_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    SB_entry.grid(row=2)


def HB():
    frames_remove()
    global f25
    global HB_entry
    f25 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f25.grid(row=1, column=1)

    HB_checkbutton = Checkbutton(f25, text="Hash Brown", variable=variable25, onvalue=1, offvalue=0, command=check_HB)
    price_label = Label(f25, text="price = $1.50")
    HB_entry = Entry(f25, textvariable=varHB, width=8, state=DISABLED)

    HB_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    HB_entry.grid(row=2)


def GB():
    frames_remove()
    global f26
    global GB_entry
    f26 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f26.grid(row=1, column=1)

    GB_checkbutton = Checkbutton(f26, text="Garlic Bread ", variable=variable26, onvalue=1, offvalue=0,
                                 command=check_GB)
    price_label = Label(f26, text="price = $2")
    GB_entry = Entry(f26, textvariable=varGB, width=8, state=DISABLED)

    GB_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    GB_entry.grid(row=2)


def HD():
    frames_remove()
    global f27
    global HD_entry
    f27 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f27.grid(row=1, column=1)

    HD_checkbutton = Checkbutton(f27, text="Hot Dog", variable=variable27, onvalue=1, offvalue=0, command=check_HD)
    price_label = Label(f27, text="price = $3")
    HD_entry = Entry(f27, textvariable=varHD, width=8, state=DISABLED)

    HD_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    HD_entry.grid(row=2)


def Sb():
    frames_remove()
    global f28
    global Sb_entry
    f28 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f28.grid(row=1, column=1)

    Sb_checkbutton = Checkbutton(f28, text="Steam Bun", variable=variable28, onvalue=1, offvalue=0, command=check_Sb)
    price_label = Label(f28, text="price = $3.50")
    Sb_entry = Entry(f28, textvariable=varSb, width=8, state=DISABLED)

    Sb_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    Sb_entry.grid(row=2)


def P():
    frames_remove()
    global f29
    global P_entry
    f29 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f29.grid(row=1, column=1)

    P_checkbutton = Checkbutton(f29, text="Pie", variable=variable29, onvalue=1, offvalue=0, command=check_P)
    price_label = Label(f29, text="price = $.4.50")
    P_entry = Entry(f29, textvariable=varP, width=8, state=DISABLED)

    P_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    P_entry.grid(row=2)


def SR():
    frames_remove()
    global f30
    global SR_entry

    f30 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f30.grid(row=1, column=1)

    SR_checkbutton = Checkbutton(f30, text="Sausage Roll", variable=variable30, onvalue=1, offvalue=0, command=check_SR)
    price_label = Label(f30, text="price = $2")
    SR_entry = Entry(f30, textvariable=varSR, width=8, state=DISABLED)

    SR_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    SR_entry.grid(row=2)


def Pizza():
    frames_remove()
    global f31
    global Pizza_entry

    f31 = LabelFrame(root, padx=0, pady=0, borderwidth=5)
    f31.grid(row=1, column=1)

    Pizza_checkbutton = Checkbutton(f31, text="Pizza", variable=variable31, onvalue=1, offvalue=0, command=check_Pizza)
    price_label = Label(f31, text="price = $3")
    Pizza_entry = Entry(f31, textvariable=varPizza, width=8, state=DISABLED)

    Pizza_checkbutton.grid(row=0, sticky="W")
    price_label.grid(row=1)
    Pizza_entry.grid(row=2)


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
    Popcorn = Button(f5_frame, text="Popcorn", width=12, height=1, bd=3, command=POPC)
    Chips = Button(f5_frame, text="Chips ", width=12, height=1, bd=3, command=C)
    Noodle_Snack = Button(f5_frame, text="Noodle Snack", width=12, height=1, bd=3, command=NC)

    Afghan_Cookies = Button(f5_frame, text="Afghan Cookies", width=28, height=1, bd=3, command=AC)
    Mrs_Higgins_Chocolate_Chip_Cookies = Button(f5_frame, text="Mrs Higgins Chocolate Chip Cookies ", width=28,
                                                height=1, bd=3, command=MHCCC)
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
    Hash_Brown = Button(f4_frame, text="Hash Brown", width=15, height=1, bd=3, command=HB)
    Garlic_Bread = Button(f4_frame, text="Garlic Bread ", width=15, height=1, bd=3, command=GB)
    Hot_Dog = Button(f4_frame, text="Hot Dog", width=15, height=1, bd=3, command=HD)

    Steam_Bun = Button(f4_frame, text="Steam Bun", width=15, height=1, bd=3, command=SB)
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
    Soup_of_the_Day = Button(f1_frame, text="Soup of the Day", width=15, height=1, bd=3, command=SOTD)

    Fresh_Fruits.grid(row=0, column=0, pady=3, padx=5)
    Fresh_Fruit_Salad.grid(row=1, column=0, pady=3, padx=5)
    Salads.grid(row=2, column=0, pady=3, padx=5)
    Sandwiches.grid(row=3, column=0, pady=3, padx=5)
    Chicken_Sub.grid(row=0, column=1, pady=3, padx=5)
    Wraps.grid(row=1, column=1, pady=3, padx=5)
    Pizza_Bread.grid(row=2, column=1, pady=3, padx=5)
    Soup_of_the_Day.grid(row=3, column=1, pady=3, padx=5)

def CALC():
    item1 = float(FF_entry.get())
    item2 = float(FFS_entry.get())
    item3 = float(S_entry.get())
    item4 = float(SW_entry.get())
    item5 = float(CS_entry.get())
    item6 = float(Ww_entry.get())
    item7 = float(PB_entry.get())
    item8 = float(SOTD_entry.get())
    item9 = float(Wa_entry.get())
    item10 = float(F_entry.get())
    item11 = float(M_entry.get())
    item12 = float(IT_entry.get())
    item13 = float(BB_entry.get())
    item14 = float(HC_entry.get())
    item15 = float(PC_entry.get())
    item16 = float(POPC_entry.get())
    item17 = float(C_entry.get())
    item18 = float(NC_entry.get())
    item19 = float(AC_entry.get())
    item20 = float(MHCCC_entry.get())
    item21 = float(CFB_entry.get())
    item22 = float(RC_entry.get())
    item23 = float(HN_entry.get())
    item24 = float(SB_entry.get())
    item25 = float(HB_entry.get())
    item26 = float(GB_entry.get())
    item27 = float(HD_entry.get())
    item28 = float(Sb_entry.get())
    item29 = float(P_entry.get())
    item30 = float(SR_entry.get())
    item31 = float(Pizza_entry.get())

    total1 = ((item1 * 1) + (item2 * 4.5) + (item3 * 6) + (item4 * 4) + (item5 * 4) + (item6 * 4.5) + (item7 * 3) + (
                item8 * 4))
    total2 = ((item9 * 3) + (item10 * 2) + (item11 * 3) + (item12 * 4) + (item13 * 4) + (item14 * 2))
    total3 = ((item15 * 2) + (item16 * 2) + (item17 * 2) + (item18 * 1) + (item19 * 1) + (item20 * 3) + (item21 * 3) + (
                item22 * 0.5))
    total4 = ((item23 * 3.50) + (item24 * 1.5) + (item25 * 1.5) + (item26 * 2) + (item27 * 3) + (item28 * 3.50) + (
                item29 * 4.50) + (item30 * 2) + (item31 * 3))

    total = total1 + total2 + total3 + total4
    itt = str(total)

    total_label.config(text="{}".format(itt))


def menu():
    global total_label
    frame1.grid_remove()
    global menu_frame
    global purchess_frame
    global extra_1
    global extra_2
    global extra_3
    global Buttons_frame
    #################################################################################
    # menu frame, this frame is for menu and selection of items
    menu_frame = LabelFrame(root, padx=25, pady=6, borderwidth=5)
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
    extra_1 = LabelFrame(root, height="220", width="400", borderwidth=5)
    extra_1.grid(row=1, column=0, padx=0)
    f_1()
    extra_2 = LabelFrame(root, height="220", width="150", borderwidth=5)
    extra_2.grid(row=1, column=1)
    FF()
    FFS()
    S()
    SW()
    CS()
    Ww()
    PB()
    SOTD()
    Wa()
    F()
    M()
    IT()
    BB()
    HC()
    PC()
    POPC()
    C()
    NC()
    AC()
    MHCCC()
    CFB()
    RC()
    HN()
    SB()
    HB()
    GB()
    HD()
    Sb()
    P()
    SR()
    Pizza()
    frames_remove()
    FF()

    extra_3 = LabelFrame(root, height="95", width="150", borderwidth=5)
    extra_3.grid(row=2, column=1)

    purchess_frame = LabelFrame(root, borderwidth=5)
    purchess_frame.grid(row=2, column=1)

    total_label = Label(purchess_frame, text="", width=8, state=DISABLED)
    total_label.grid(row=0)
    #####################################################################################
    # Buttons Frame, this frame is for function frames
    Buttons_frame = LabelFrame(root, height="40", width="450", borderwidth=5)
    Buttons_frame.grid(row=2, column=0)

    # off screen button codes
    add_item_BTN = Button(Buttons_frame, text="Total", width=5, height=1, command=CALC,
                          font=("Times", "20", "bold"), bd=5)
    remove_item_BTN = Button(Buttons_frame, text="Reset selection", width=10, height=1, command=reset_items,
                             font=("Times", "20", "bold"), bd=5)
    purchess_item_BTN = Button(Buttons_frame, text="Exit", width=5, height=1, command=window_close,
                               font=("Times", "20", "bold"), bd=5)

    # on screen button codes
    add_item_BTN.grid(row=0, column=0, pady=5, padx=5)
    remove_item_BTN.grid(row=0, column=1, pady=5, padx=5)
    purchess_item_BTN.grid(row=0, column=2, pady=5, padx=5)


def reset_items():
    varFF.set("0")
    varFFS.set("0")
    varS.set("0")
    varSW.set("0")
    varCS.set("0")
    varWw.set("0")
    varPB.set("0")
    varSOTD.set("0")
    varWa.set("0")
    varF.set("0")
    varM.set("0")
    varIT.set("0")
    varBB.set("0")
    varHC.set("0")
    varPC.set("0")
    varPOPC.set("0")
    varC.set("0")
    varNC.set("0")
    varAC.set("0")
    varMHCCC.set("0")
    varCFB.set("0")
    varRC.set("0")
    varHN.set("0")
    varSB.set("0")
    varHB.set("0")
    varGB.set("0")
    varHD.set("0")
    varSb.set("0")
    varP.set("0")
    varSR.set("0")
    varPizza.set("0")
    ############################################################################

    FF_entry.configure(state=DISABLED)
    FFS_entry.configure(state=DISABLED)
    S_entry.configure(state=DISABLED)
    SW_entry.configure(state=DISABLED)
    CS_entry.configure(state=DISABLED)
    Ww_entry.configure(state=DISABLED)
    PB_entry.configure(state=DISABLED)
    SOTD_entry.configure(state=DISABLED)
    Wa_entry.configure(state=DISABLED)
    F_entry.configure(state=DISABLED)
    M_entry.configure(state=DISABLED)
    IT_entry.configure(state=DISABLED)
    BB_entry.configure(state=DISABLED)
    HC_entry.configure(state=DISABLED)
    PC_entry.configure(state=DISABLED)
    POPC_entry.configure(state=DISABLED)
    C_entry.configure(state=DISABLED)
    NC_entry.configure(state=DISABLED)
    AC_entry.configure(state=DISABLED)
    MHCCC_entry.configure(state=DISABLED)
    CFB_entry.configure(state=DISABLED)
    RC_entry.configure(state=DISABLED)
    HN_entry.configure(state=DISABLED)
    SB_entry.configure(state=DISABLED)
    HB_entry.configure(state=DISABLED)
    GB_entry.configure(state=DISABLED)
    HD_entry.configure(state=DISABLED)
    Sb_entry.configure(state=DISABLED)
    P_entry.configure(state=DISABLED)
    SR_entry.configure(state=DISABLED)
    Pizza_entry.configure(state=DISABLED)

    itt = ("")
    total_label.config(text="{}".format(itt))
def close_root1():
    root1.destroy()


def close_program():
    root.destroy()
    root1.destroy()


def window_close():
    global root1
    root1 = Tk()
    root1.title("BDSC_CAFE")

    close_frame = Frame(root1)

    close_frame = LabelFrame(root1, height="800", width="300", padx=10, pady=10)
    close_frame.grid(row=0, column=0)

    close_program_BTN = Button(close_frame, text="Close program", width=10, height=1, font=("Times", "8",), bd=5,
                               command=close_program)
    Back_frame_BTN = Button(close_frame, text="Back", width=5, height=1, font=("Times", "8",), bd=5,
                            command=close_root1)

    close_program_BTN.grid(row=0, column=2)
    Back_frame_BTN.grid(row=0, column=3)


################################################# SIGN UP AND SIGN IN ##################################################
def sign_in():
    username = email.get()  # Asks for username
    password = passWord.get()  # Asks for password

    conn = sqlite3.connect('BDSC_Students.db')
    c = conn.cursor()
    find_user = "SELECT *, oid FROM Student WHERE username = ? AND password = ?"
    # Validates inputs for account
    c.execute(find_user, [username, password])
    results = c.fetchall()  # Fetches values from database

    if results:  # Validates if the username/password is recognised
        """
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS {}(website text, usernames text, passwords text)".format(username))
        conn.commit()
        conn.close()
        """
        menu()
    else:
        feedback1.configure(text="username or password not correct", bg="red")


def sign_up():
    firstName = first_name.get()
    lastName = last_name.get()
    Age = age.get()
    Username = userName.get()
    Pass = password.get()

    conn = sqlite3.connect('BDSC_Students.db')
    c = conn.cursor()
    finduser = "SELECT * FROM Student WHERE username = ?"
    c.execute(finduser, [(Username)])  # Checks existence of username in database
    if c.fetchall():
        feedback.configure(text="username taken", bg="red")
    else:
        insertData = ('''INSERT INTO Student (firstname, lastname, age, username, password)
                        VALUES(?,?,?,?,?)''')  # Inserts new account into database
        c.execute(insertData, [firstName, lastName, Age, Username, Pass])
        feedback.configure(text="account created", bg="green")
        first_name.delete(0, END)
        last_name.delete(0, END)
        age.delete(0, END)
        userName.delete(0, END)
        password.delete(0, END)
        conPassword.delete(0, END)
        first_name.focus()

        conn.commit()
        conn.close()


############################################## BACKGROUND CHECKING CODE ################################################
def check_newaccount():
    num1 = (number1.get())
    # first name Check
    if first_name.get() == "":
        feedback.configure(text="please enter your name", bg="red")
        first_name.focus()
        first_name.delete(0, END)
    elif not first_name.get().isalpha():
        feedback.configure(text="first name cant have digit", bg="red")
        first_name.delete(0, END)
        first_name.focus()
    # last name Check
    elif last_name.get() == "":
        feedback.configure(text="please enter your last name", bg="red")
        last_name.focus()
        last_name.delete(0, END)
    elif not last_name.get().isalpha():
        feedback.configure(text="last name cant have digit", bg="red")
        last_name.delete(0, END)
        last_name.focus()
        # age check
    elif age.get() == "":
        feedback.configure(text="please enter your age ", bg="red")
        age.focus()
        age.delete(0, END)
    elif not age.get().isdigit():
        feedback.configure(text="age cant have alphabet", bg="red")
        age.focus()
        age.delete(0, END)
    elif float(num1) > 18:
        feedback.configure(text="you cant be older than 18", bg="red")
        age.focus()
        age.delete(0, END)
    elif float(num1) < 13:
        feedback.configure(text="you cant be younger than 13", bg="red")
        age.focus()
        age.delete(0, END)
    # userName check
    elif userName.get() == "":
        feedback.configure(text="please enter your Username", bg="red")
        userName.focus()
        userName.delete(0, END)
    # coming back to this

    # password check
    elif password.get() == "":
        feedback.configure(text="please enter your Password", bg="red")
        password.focus()
        password.delete(0, END)
    elif conPassword.get() == "":
        feedback.configure(text="please confirm Password", bg="red")
        password.focus()
        password.delete(0, END)
    elif str(conPassword.get()) != str(password.get()):
        feedback.configure(text="Passwords dont match", bg="red")
        conPassword.focus()
        conPassword.delete(0, END)
    else:
        sign_up()
##################################################### FRAMES ###########################################################
def new_account_frame():
    global first_name
    global last_name
    global age
    global userName
    global password
    global conPassword
    global frame2
    global feedback
    global number1

    frame1.grid_remove()

    frame2 = LabelFrame(root, height="800", width="300")
    frame2.grid(row=0, column=0)

    website_title = Label(frame2, text="BDSC CAFE", padx=5, pady=5, font=("Times", "20", "bold"))
    website_title.grid(row=0, columnspan=4)
    discription = Label(frame2, text="Create a new account to use BDSC CAFE")
    discription.grid(row=1, columnspan=4)

    # background Labels
    firstname_label = Label(frame2, text="First name ")
    lastname_label = Label(frame2, text="Last name ")
    age_label = Label(frame2, text="Age ")
    username_label = Label(frame2, text="Username ")
    password_label = Label(frame2, text="Password ")
    conPassword_label = Label(frame2, text="Confirm Password")

    # background Buttons
    sign_up = Button(frame2, text="Sign Up", width=8, height=1, command=check_newaccount)
    back = Button(frame2, text="Back", width=8, height=1, command=login_frame)

    # on screen Labels
    firstname_label.grid(row=2, column=0)
    lastname_label.grid(row=2, column=2)
    age_label.grid(row=4, column=0)
    username_label.grid(row=5, column=0)
    password_label.grid(row=6, column=0)
    conPassword_label.grid(row=7, column=0)

    # background Entry boxes
    first_name = Entry(frame2, width=18)
    last_name = Entry(frame2, width=10)
    age = Entry(frame2, textvariable=number1, width=18)
    userName = Entry(frame2, width=40)
    password = Entry(frame2, width=40)
    conPassword = Entry(frame2, width=40)

    # on screen Entry Boxes
    first_name.grid(row=2, column=1)
    last_name.grid(row=2, column=3)
    age.grid(row=4, column=1)
    userName.grid(row=5, column=1, columnspan=3)
    password.grid(row=6, column=1, columnspan=3)
    conPassword.grid(row=7, column=1, columnspan=3)

    # on screen Buttons
    sign_up.grid(row=8, column=3, pady=5)
    back.grid(row=8, column=0, pady=5)

    # feedback background
    feedback = Label(frame2, text="")

    # feedback on screen
    feedback.grid(row=8, column=1, columnspan=2)
def back_to_login():
    frame1.grid_remove()
    frame2.grid_remove()
    frame3.grid_remove()
    frame4.grid_remove()
    frame5.grid_remove()
    f1_frame.grid_remove()
    f2_frame.grid_remove()
    f3_frame.grid_remove()
    f4_frame.grid_remove()
    f5_frame.grid_remove()
    menu_frame.grid_remove()
    purchess_frame.grid_remove()
    extra_1.grid_remove()
    extra_2.grid_remove()
    extra_3.grid_remove()
    Buttons_frame.grid_remove()
def login_frame():
    global email
    global passWord
    global feedback1
    global frame1

    frames_remove()
    back_to_login()

    frame1 = LabelFrame(root, height="800", width="300")
    frame1.grid(row=0, column=0)

    website_title = Label(frame1, text="BDSC CAFE", padx=5, pady=5, font=("Times", "20", "bold"))
    website_title.grid(row=0, column=0)
    discription = Label(frame1, text="Welcome, Please enter username to access CAFE app", font=("Times", "9"))
    discription.grid(row=1, column=0)

    # off screen code
    email = Entry(frame1, width=30)
    passWord = Entry(frame1, width=30)
    login = Button(frame1, text="Login", width=30, command=sign_in)
    new_account = Button(frame1, text="Create New account", width=30, command=new_account_frame)

    # on screen codes
    email.grid(row=2, column=0, padx=20, pady=15)
    email.insert(0, "Write email here please")
    passWord.grid(row=3, column=0, padx=20)
    passWord.insert(0, "Write password here please")

    login.grid(row=4, column=0, pady=10)
    new_account.grid(row=5, column=0, pady=4)

    feedback1 = Label(frame1, text="")
    feedback1.grid(row=6, column=0)
################################################### Main_Loop ##########################################################

# loging frames
root = Tk()
root.title("BDSC_CAFE")
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)

number1 = StringVar()
# menu frames

################################## the menu frame #####################################
f1_frame = Frame(root)
f2_frame = Frame(root)
f22_frame = Frame(root)
f3_frame = Frame(root)
f4_frame = Frame(root)
f5_frame = Frame(root)

menu_frame = Frame(root)
purchess_frame = Frame(root)
extra_1 = Frame(root)
extra_2 = Frame(root)
extra_3 = Frame(root)
Buttons_frame = Frame(root)
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

variable1 = IntVar()
variable2 = IntVar()
variable3 = IntVar()
variable4 = IntVar()
variable5 = IntVar()
variable6 = IntVar()
variable7 = IntVar()
variable8 = IntVar()
variable9 = IntVar()
variable10 = IntVar()
variable11 = IntVar()
variable12 = IntVar()
variable13 = IntVar()
variable14 = IntVar()
variable15 = IntVar()
variable16 = IntVar()
variable17 = IntVar()
variable18 = IntVar()
variable19 = IntVar()
variable20 = IntVar()
variable21 = IntVar()
variable22 = IntVar()
variable23 = IntVar()
variable24 = IntVar()
variable25 = IntVar()
variable26 = IntVar()
variable27 = IntVar()
variable28 = IntVar()
variable29 = IntVar()
variable30 = IntVar()
variable31 = IntVar()

variable1.set(0)
variable2.set(0)
variable3.set(0)
variable4.set(0)
variable5.set(0)
variable6.set(0)
variable7.set(0)
variable8.set(0)
variable9.set(0)
variable10.set(0)
variable11.set(0)
variable12.set(0)
variable13.set(0)
variable14.set(0)
variable15.set(0)
variable16.set(0)
variable17.set(0)
variable18.set(0)
variable19.set(0)
variable20.set(0)
variable21.set(0)
variable22.set(0)
variable23.set(0)
variable24.set(0)
variable25.set(0)
variable26.set(0)
variable27.set(0)
variable28.set(0)
variable29.set(0)
variable30.set(0)
variable31.set(0)

varFF = StringVar()
varFFS = StringVar()
varS = StringVar()
varSW = StringVar()
varCS = StringVar()
varWw = StringVar()
varPB = StringVar()
varSOTD = StringVar()
varWa = StringVar()
varF = StringVar()
varM = StringVar()
varIT = StringVar()
varBB = StringVar()
varHC = StringVar()
varPC = StringVar()
varPOPC = StringVar()
varC = StringVar()
varNC = StringVar()
varAC = StringVar()
varMHCCC = StringVar()
varCFB = StringVar()
varRC = StringVar()
varHN = StringVar()
varSB = StringVar()
varHB = StringVar()
varGB = StringVar()
varHD = StringVar()
varSb = StringVar()
varP = StringVar()
varSR = StringVar()
varPizza = StringVar()

varFF.set("0")
varFFS.set("0")
varS.set("0")
varSW.set("0")
varCS.set("0")
varWw.set("0")
varPB.set("0")
varSOTD.set("0")
varWa.set("0")
varF.set("0")
varM.set("0")
varIT.set("0")
varBB.set("0")
varHC.set("0")
varPC.set("0")
varPOPC.set("0")
varC.set("0")
varNC.set("0")
varAC.set("0")
varMHCCC.set("0")
varCFB.set("0")
varRC.set("0")
varHN.set("0")
varSB.set("0")
varHB.set("0")
varGB.set("0")
varHD.set("0")
varSb.set("0")
varP.set("0")
varSR.set("0")
varPizza.set("0")

total = StringVar()
total.set("0")

vartotal = StringVar()

login_frame()

root.mainloop()

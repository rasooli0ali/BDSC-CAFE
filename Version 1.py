from tkinter import *
import sqlite3

conn = sqlite3.connect('BDSC_Students.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Student (firstname text, lastname text, age text, username text, password text)")
conn.commit()
conn.close()


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
        feedback1.configure(text="Logged in", bg="green")
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
    age_label = Label(frame2, text = "Age ")
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


def login_frame():
    global email
    global passWord
    global feedback1
    global frame1
    
    frame2.grid_remove()
    
    frame1 = LabelFrame(root, height="800", width="300")
    frame1.grid(row=0, column=0)
    
    website_title = Label(frame1, text="BDSC 2DIP", padx=5, pady=5, font=("Times", "20", "bold"))
    website_title.grid(row=0, column=0)
    discription = Label(frame1, text="this app is for 2DIP class login")
    discription.grid(row=1, column=0)

    # off screen code
    email = Entry(frame1, width=30)
    passWord = Entry(frame1, width=30)
    login = Button(frame1, text="Login", width=30, command=sign_in)
    new_account = Button(frame1, text="Create New account", width=30, command=new_account_frame)

    # on screen codes
    email.grid(row=2, column=0, padx=20, pady=15)
    email.insert(0, "Write username here please")
    passWord.grid(row=3, column=0, padx=20)
    passWord.insert(0, "Write password here please")

    login.grid(row=4, column=0, pady=10)
    new_account.grid(row=5, column=0, pady=4)

    feedback1 = Label(frame1, text="")
    feedback1.grid(row=6, column=0)


################################################### Main_Loop ##########################################################
#loging frames
root = Tk()
root.title("BDSC_CAFE")
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)

number1 = StringVar()
#menu frames

################################## the menu frame #####################################
login_frame()

root.mainloop()
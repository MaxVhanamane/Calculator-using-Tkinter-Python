from tkinter import *
# This is to show message when user gives wrong input
from tkinter.messagebox import *
# from PIL import Image, ImageTk 
import math 
# useful repeating variables
# We are gonna use font many times in program so its better to assign it to a variable and use it
font = "lucida 15 bold"


# imp functions

def clickaction(event):
    # This will help to get text value on button
    val = event.widget.cget("text")
    
    if val == "x":
        text.insert(END, "*")
        return
    # here the text is variable name which i have defined while creating entry field...
    # by using insert function now i can show that btn text on screen
    # Here END is index value i.e when i press 7 and then 9 now that index will decide where should that 9 to be shown i.e 79 or 97
    # END means show it after 7  above 3 lines are talking about text.insert(END, val)

    elif val == "=":
        try:
            # This will give you the expression which was written before pressing =
            get_expression = text.get()
            # print(get_expression)
            # This function will solve the expression this is inbuilt function in Tkinter
            solving_expression = eval(get_expression)
            # print(solving_expression)
            # till now it will show expression and = on screen but when i press equal button i dont want to see expression and
            # equal button like this eg.3+4=  i want direct result i.e 7 to do that
            text.delete(0, END)  # it will delete everythin which is on screen
            text.insert(0, solving_expression)
            # after inserting answer i will return the function else it will insert below lines
        except Exception as e:
            showerror("Error", "Invalid input")
        return
    # To clear all data on screen
    elif val == "C":
        text.delete(0, END)
        return
        # Agar mai return na likhu toh val ki value yaha pe hogi C jo niche jage insert hogi aur screen pe dikhegi to avoid that function ko
        # yahi se return karo

    # To clear one digit at a time
    elif val == "⌫":
        get_data = text.get()  # get all data which is in text field
        # Take all data except last digit and assign it to modify_data
        modify_data = get_data[0:len(get_data)-1]
        text.delete(0, END)  # delete everything on screen
        # insert the data which is in modify data at index 0
        text.insert(0, modify_data)
        return

    text.insert(END, val)

# creating a window


root = Tk()
root.title("Calculator")
root.geometry("400x600")
root.config(bg="pink")
# to change root background
# root.configure(background="grey")


# To change its icon ....the file should be in .ico format
root.iconbitmap("image/calicon.ico")

# adding textfield
# To change height of entry widget we have to increase font size there is no other option
text = Entry(root, font="lucida 25 bold", justify=CENTER)
text.pack(side=TOP, pady=10, padx=5, fill=X)

# frame is like div container
# creating one frame to put buttons inside that frame
buttonframe = Frame(root)
buttonframe.pack(side=TOP)

# adding buttons in frame(buttonframe)
# by using grid geometry we can devide our root window or frame in rows and column so that we could
# put cal buttons in it properly
# in grid we use concept of excel (0,0)th cell (0,1)th cell.....
# creating 1 to 9 button
initial_value = 9
for i in range(0, 3):
    for j in range(2, -1, -1):
        btn = Button(buttonframe, text=initial_value, font=font, width=5, height=3, pady=5, relief="ridge",
                     activebackground="grey", activeforeground="white",bg="pink")
        btn.grid(row=i, column=j, padx=2, pady=2)

        btn.bind('<Button-1>', clickaction)
        initial_value -= 1
        # binding 1 to 9 buttons so i could fetch the data in that button
        # here <Button-1> means when i take my cursor on some button and right click on it it should call some function


# creating other buttons
# while creating 1 to 9 buttons i used one liner i.e Button().grid()
# we can assign variable and then we can perform operation as shown below
Zerobtn = Button(buttonframe, text="0", font=font, width=5, height=3, pady=5,
                 relief="ridge", activebackground="grey", activeforeground="white",bg="pink")
Zerobtn.grid(row=3, column=1, padx=2, pady=2)

# creating equal button using one liner code
# when u create one liner code it will create problem while binding so its better to assign it to some variable
# Button(buttonframe, text="=", font=font, width=5, height=3, pady=5, relief="ridge",
#        activebackground="grey", activeforeground="white").grid(row=3, column=2, padx=2, pady=2)

equalbtn = Button(buttonframe, text="=", font=font, width=5, height=3, pady=5, relief="ridge",
                  activebackground="grey", activeforeground="white",bg="pink")
equalbtn.grid(row=3, column=2, padx=2, pady=2)

# creating dot button
dotbtn = Button(buttonframe, text=".", font=font, width=5, height=3, pady=5,
                relief="ridge", activebackground="grey", activeforeground="white",bg="pink")
dotbtn.grid(row=3, column=0, padx=2, pady=2)


# creating operation buttons +,-,=,/
divisionbtn = Button(buttonframe, text="/", font=font, width=5, height=3, pady=5,
                     relief="ridge", activebackground="grey", activeforeground="white",bg="pink")
divisionbtn.grid(row=0, column=3, padx=2, pady=2)

multiplicationbtn = Button(buttonframe, text="x", font=font, width=5, height=3, pady=5,
                           relief="ridge", activebackground="grey", activeforeground="white",bg="pink")
multiplicationbtn.grid(row=1, column=3, padx=2, pady=2)

substractionbtn = Button(buttonframe, text="-", font=font, width=5, height=3, pady=5,
                         relief="ridge", activebackground="grey", activeforeground="white",bg="pink")
substractionbtn.grid(row=2, column=3, padx=2, pady=2)

additionbtn = Button(buttonframe, text="+", font=font, width=5, height=3, pady=5,
                     relief="ridge", activebackground="grey", activeforeground="white",bg="pink")
additionbtn.grid(row=3, column=3, padx=2, pady=2)

# creating clear and back btn
# To cobine 2 columns we can use columnspan=2
clearbtn = Button(buttonframe, text="⌫", font=font, width=11, height=2, pady=5,
                  relief="ridge", activebackground="grey", activeforeground="white",bg="pink")
clearbtn.grid(row=4, column=0, padx=1, pady=2, columnspan=2)

allclearbtn = Button(buttonframe, text="C", font=font, width=11, height=2, pady=5,
                     relief="ridge", activebackground="grey", activeforeground="white",bg="pink")
allclearbtn.grid(row=4, column=2, padx=1, pady=2, columnspan=2)

# binding all remaining buttons
equalbtn.bind('<Button-1>', clickaction)
Zerobtn.bind('<Button-1>', clickaction)
dotbtn.bind('<Button-1>', clickaction)
divisionbtn.bind('<Button-1>', clickaction)
multiplicationbtn.bind('<Button-1>', clickaction)
substractionbtn.bind('<Button-1>', clickaction)
additionbtn.bind('<Button-1>', clickaction)
clearbtn.bind('<Button-1>', clickaction)
allclearbtn.bind('<Button-1>', clickaction)


# Coding for scintific calculator ................

# creating frame for sci cal
sciFrame = Frame(root)


sqrt = Button(sciFrame, text="√", font=font, width=5, height=2, pady=5,
              relief="ridge", activebackground="grey", activeforeground="white",bg="orange")
sqrt.grid(row=0, column=0, padx=2, pady=2)

power = Button(sciFrame, text="^", font=font, width=5, height=2, pady=5,
               relief="ridge", activebackground="grey", activeforeground="white",bg="orange")
power.grid(row=0, column=1, padx=2, pady=2)

factorialbtn = Button(sciFrame, text="x!", font=font, width=5, height=2, pady=5, relief="ridge",
                      activebackground="grey", activeforeground="white",bg="orange")
factorialbtn.grid(row=0, column=2, padx=2, pady=2)


radbtn = Button(sciFrame, text="Rad", font=font, width=5, height=2, pady=5, relief="ridge",
                activebackground="grey", activeforeground="white",bg="orange")
radbtn.grid(row=0, column=3, padx=2, pady=2)

sinbtn = Button(sciFrame, text="sin", font=font, width=5, height=2, pady=5, relief="ridge",
                activebackground="grey", activeforeground="white",bg="orange")
sinbtn.grid(row=1, column=0, padx=2, pady=2)

cosbtn = Button(sciFrame, text="cos", font=font, width=5, height=2, pady=5, relief="ridge",
                activebackground="grey", activeforeground="white",bg="orange")
cosbtn.grid(row=1, column=1, padx=2, pady=2)

tanbtn = Button(sciFrame, text="tan", font=font, width=5, height=2, pady=5, relief="ridge",
                activebackground="grey", activeforeground="white",bg="orange")
tanbtn.grid(row=1, column=2, padx=2, pady=2)

degbtn = Button(sciFrame, text="Deg", font=font, width=5, height=2, pady=5, relief="ridge",
                activebackground="grey", activeforeground="white",bg="orange")
degbtn.grid(row=1, column=3, padx=2, pady=2)


# Creating functions write function before binding else it will throw an error NameError: name 'sci_cal' is not defined
def sci_cal(event):
    val = event.widget.cget("text") #To get text
    # print(val)
    expression=text.get() #To get value
    # print(expression)

    if val=="Deg":
        ans=math.degrees(float(expression))
        
    elif val=="Rad":
        ans=math.radians(float(expression[0]),2)
        # text.delete(0, END)  # it will delete everythin which is on screen
        # text.insert(0,b)

    elif val=="sin":
        ans=math.sin(math.radians(float(expression))) #Sin takes value in rad so we r converting degree into rad
        # text.delete(0, END)  
        # text.insert(0,c)

    elif val=="cos":
        ans=math.cos(math.radians(float(expression)))
        # text.delete(0, END)  
        # text.insert(0,d)

    elif val=="tan":
        ans=math.tan(math.radians(float(expression)))
        # text.delete(0, END)  
        # text.insert(0,d)

    elif val=="√":
        ans=math.sqrt(float(expression))
        # text.delete(0, END)  
        # text.insert(0,e)

    elif val=="^":
        text.insert(END, "**") 
        return

    elif val=="=":
        ans=math.pow(float(expression),2)
        # text.delete(0, END)  
        # text.insert(0,e)

    elif val=="x!":
        ans=math.factorial(float(expression))
        # text.delete(0, END)  
        # text.insert(0,f)
    text.delete(0, END)  # it will delete everythin which is on screen
    text.insert(0,ans) #it will insert value of a at index 0

# binding all buttons
sqrt.bind('<Button-1>', sci_cal)
power.bind('<Button-1>', sci_cal)
factorialbtn.bind('<Button-1>', sci_cal)
radbtn.bind('<Button-1>', sci_cal)
sinbtn.bind('<Button-1>', sci_cal)
cosbtn.bind('<Button-1>', sci_cal)
tanbtn.bind('<Button-1>', sci_cal)
degbtn.bind('<Button-1>', sci_cal)

#Making keyboard button fuctioning its bit tricky concept
def keybrdequalbtn(event):
    getvalue = Event() #creating event object
    getvalue.widget=equalbtn #assigning equal button 
    clickaction(getvalue)


text.bind('<Return>',keybrdequalbtn)

x = "Normal Mode"


def ScientificCal_click():
    global x
    x = modename.entrycget(0, "label")
    if x == "Normal Mode":
        modename.add_command(label="Scientific Cal",
                             command=ScientificCal_click)  # adding options
        # concept : self.filemenu2.delete(0) # deletes first item in menu
        modename.delete(0)
        # self.filemenu2.delete("Stop") $ delete item with the label "Stop"
        sciFrame.pack_forget()
        root.geometry("400x600")

    else:
        modename.add_command(label="Normal Mode",
                             command=ScientificCal_click)  # adding options
        modename.delete(0)
        buttonframe.pack_forget()
        sciFrame.pack(side=TOP)
        buttonframe.pack(side=TOP)
        root.geometry("400x750")


# adding menubar
menubar = Menu(root, font="lucida 10 bold")  # root ke andar ek menu banao
# adding options/modes in Menu
# aur ek menu banao jo menubar be hoga ....tearoff removes dotted line
modename = Menu(menubar, font="lucida 10 bold", tearoff=0)
modename.add_command(label="Scientific Cal",
                     command=ScientificCal_click)  # adding options
# if u dont cascade it wont show it on screen
menubar.add_cascade(label="Mode", menu=modename)
root.config(menu=menubar)


root.mainloop()



#If u want to convert .py file to .exe file...............
#While converting this .py file to .exe use command pyinstaller --onefile main.py(whatever ur filename is ) 
#If u use above command it will convert it into exe file but when u open that exe file it will open ur file along with black console in background 
#To get rid of that console use (-w)...pyinstaller --onefile -w main.py it will solve the problem now it will open only ur application
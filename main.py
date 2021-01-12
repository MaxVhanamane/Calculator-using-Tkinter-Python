from tkinter import *
# This is to show message when user gives wrong input
from tkinter.messagebox import *
# from PIL import Image, ImageTk  (use this if you want to add images in your gui)
import math 
# useful repeating variables
# We are gonna use font multiple times in program so its better to assign it to a variable and use it
font = "lucida 15 bold"

# Important functions

def clickaction(event):
    # This will help to get text value which is on buttons
    val = event.widget.cget("text") #Storing text value in variable (val)
    
    if val == "x":   #In gui we have used alphabet x for multiplication but when we pass that to math module it wont uderstand so we are converting it into *
        text.insert(END, "*") #Whenerver you press x on gui it will isert * instead of x
        return
    # Here the text is variable name which i have defined while creating entry field...
    # Here END is index value i.e when i press 7 and then 9... that index value will decide where should that 9 to be shown i.e at the END 79 or somewhere else in this case at start 97
    # In the above eg. END means show it after 7  above 2 lines are talking about text.insert(END, val)

    elif val == "=":
        try:
            # This will give you the expression which was written before pressing =
            get_expression = text.get()
            # print(get_expression) #(Just for uderstanding)
            # This function will solve the expression this is inbuilt function in Python/Tkinter
            solving_expression = eval(get_expression)
            # print(solving_expression)  #(Just for uderstanding)
            # Upto above code it will show expression and equal to sign (=) on screen but when I press equal button I don't want to see expression and
            # equal button like this eg.3+4=  i want direct result i.e 7 to do that
            text.delete(0, END)  # It will delete everything which is on screen
            text.insert(0, solving_expression) #This will insert/show solved expression on screen
            # after inserting answer i will return the function else it will insert lines which are after this if else statement
        except Exception as e:
            showerror("Error", "Invalid input")
        return
    # To clear all data on screen i.e making clear button fuctioning
    elif val == "C":
        text.delete(0, END)
        return
        # Agar mai return na likhu toh val ki value yaha pe hogi C jo niche jage insert hogi aur screen pe dikhegi to avoid that function ko
        # yahi se return karo

    # To clear one digit at a time i.e making backspace button fuctioning
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
root.geometry("250x400")
root.config(bg="pink") #Changing root background


# To change it's icon ....the file should be in (.ico) format
root.iconbitmap("image/calicon.ico")

# adding textfield (Here we see all the values when we press button)
# To change height of entry widget we have to increase font size there is no other option (till now)
text = Entry(root, font="lucida 25 bold", justify=CENTER)
text.pack(side=TOP, pady=5, padx=2, fill=X)

# frame is like div container
# creating one frame to put buttons inside that frame
buttonframe = Frame(root,padx=0,pady=1)
buttonframe.pack(side=TOP) #side will decide where to put that frame. TOP (default), BOTTOM, LEFT, or RIGHT.

# Adding buttons in frame(buttonframe)
# By using grid geometry we can devide our root window or frame into rows and columns like excel so that we could put calculator buttons properly.
# In grid we use concept of excel (0,0)th cell (0,1)th cell.....

# Creating 1 to 9 buttons
initial_value = 9
for i in range(0, 3):
    for j in range(2, -1, -1):
        btn = Button(buttonframe, text=initial_value, font=font, width=3, height=2, relief="ridge",
                     activebackground="grey", activeforeground="white",bg="pink")
        btn.grid(row=i, column=j, padx=1, pady=1)

        btn.bind('<Button-1>', clickaction)
        initial_value -= 1
        # Binding 1 to 9 buttons so i could fetch the data in that button
        # Here <Button-1> means when i take my cursor on some button and right click on it it should call some function


# Creating other buttons
Zerobtn = Button(buttonframe, text="0", font=font, width=3, height=2,
                 relief="ridge", activebackground="grey", activeforeground="white",bg="pink")
Zerobtn.grid(row=3, column=1, padx=1, pady=1)

# Creating equal button using one liner code
# when u create one liner code it will create problem while binding so its better to assign it to some variable below code will also work
# Button(buttonframe, text="=", font=font, width=3, height=2,  relief="ridge",
#        activebackground="grey", activeforeground="white").grid(row=3, column=2, padx=2, pady=2)

equalbtn = Button(buttonframe, text="=", font=font, width=3, height=2,  relief="ridge",
                  activebackground="grey", activeforeground="white",bg="pink")
equalbtn.grid(row=3, column=2, padx=1, pady=1)

# Creating dot button
dotbtn = Button(buttonframe, text=".", font=font, width=3, height=2, 
                relief="ridge", activebackground="grey", activeforeground="white",bg="pink")
dotbtn.grid(row=3, column=0, padx=1, pady=1)


# Creating operation buttons +,-,=,/
divisionbtn = Button(buttonframe, text="/", font=font, width=3, height=2, 
                     relief="ridge", activebackground="grey", activeforeground="white",bg="pink")
divisionbtn.grid(row=0, column=3,  padx=1, pady=1)

multiplicationbtn = Button(buttonframe, text="x", font=font, width=3, height=2, 
                           relief="ridge", activebackground="grey", activeforeground="white",bg="pink")
multiplicationbtn.grid(row=1, column=3, padx=1, pady=1)

substractionbtn = Button(buttonframe, text="-", font=font, width=3, height=2, 
                         relief="ridge", activebackground="grey", activeforeground="white",bg="pink")
substractionbtn.grid(row=2, column=3, padx=1, pady=1)

additionbtn = Button(buttonframe, text="+", font=font, width=3, height=2, 
                     relief="ridge", activebackground="grey", activeforeground="white",bg="pink")
additionbtn.grid(row=3, column=3, padx=1, pady=1)

# Creating clear and back button
# To combine 2 columns we can use columnspan=2 in grid
clearbtn = Button(buttonframe, text="⌫", font=font, width=7, height=1, 
                  relief="ridge", activebackground="grey", activeforeground="white",bg="pink")
clearbtn.grid(row=4, column=0, padx=1, pady=1, columnspan=2)

allclearbtn = Button(buttonframe, text="C", font=font, width=7, height=1, 
                     relief="ridge", activebackground="grey", activeforeground="white",bg="pink")
allclearbtn.grid(row=4, column=2, padx=1, pady=1, columnspan=2)

# Binding all remaining buttons
equalbtn.bind('<Button-1>', clickaction)
Zerobtn.bind('<Button-1>', clickaction)
dotbtn.bind('<Button-1>', clickaction)
divisionbtn.bind('<Button-1>', clickaction)
multiplicationbtn.bind('<Button-1>', clickaction)
substractionbtn.bind('<Button-1>', clickaction)
additionbtn.bind('<Button-1>', clickaction)
clearbtn.bind('<Button-1>', clickaction)
allclearbtn.bind('<Button-1>', clickaction)


# ....................Coding for scintific calculator....................

# Creating frame for scintific calculator
sciFrame = Frame(root, padx=0, pady=1)


sqrt = Button(sciFrame, text="√", font=font, width=3, height=2, 
              relief="ridge", activebackground="grey", activeforeground="white",bg="orange")
sqrt.grid(row=0, column=0, padx=1, pady=1)

power = Button(sciFrame, text="^", font=font, width=3, height=2, 
               relief="ridge", activebackground="grey", activeforeground="white",bg="orange")
power.grid(row=0, column=1, padx=1, pady=1)

factorialbtn = Button(sciFrame, text="x!", font=font, width=3, height=2,  relief="ridge",
                      activebackground="grey", activeforeground="white",bg="orange")
factorialbtn.grid(row=0, column=2, padx=1, pady=1)


radbtn = Button(sciFrame, text="Rad", font=font, width=3, height=2,  relief="ridge",
                activebackground="grey", activeforeground="white",bg="orange")
radbtn.grid(row=0, column=3, padx=1, pady=1)

sinbtn = Button(sciFrame, text="sin", font=font, width=3, height=2,  relief="ridge",
                activebackground="grey", activeforeground="white",bg="orange")
sinbtn.grid(row=1, column=0, padx=1, pady=1)

cosbtn = Button(sciFrame, text="cos", font=font, width=3, height=2,  relief="ridge",
                activebackground="grey", activeforeground="white",bg="orange")
cosbtn.grid(row=1, column=1, padx=1, pady=1)

tanbtn = Button(sciFrame, text="tan", font=font, width=3, height=2,  relief="ridge",
                activebackground="grey", activeforeground="white",bg="orange")
tanbtn.grid(row=1, column=2, padx=1, pady=1)

degbtn = Button(sciFrame, text="Deg", font=font, width=3, height=2,  relief="ridge",
                activebackground="grey", activeforeground="white",bg="orange")
degbtn.grid(row=1, column=3, padx=1, pady=1)


# Creating functions ...
# Write functions before binding else it will throw an error NameError: name 'sci_cal' is not defined

def sci_cal(event):
    val = event.widget.cget("text") #To get text value
    # print(val) #(Just for Understanding purpose)
    expression=text.get() #To get value
    # print(expression) #(Just for Understanding purpose)

    if val=="Deg":
        ans=math.degrees(float(expression)) #Storing solution/answer in ans variable
        
    elif val=="Rad":
        ans=math.radians(float(expression[0]),2)

    elif val=="sin":
        ans=math.sin(math.radians(float(expression))) #Sin takes value in rad so we are converting degree into radian
       
    elif val=="cos":
        ans=math.cos(math.radians(float(expression)))
 

    elif val=="tan":
        ans=math.tan(math.radians(float(expression)))

    elif val=="√":
        ans=math.sqrt(float(expression))
       
    elif val=="^":
        text.insert(END, "**") 
        return

    elif val=="=":
        ans=math.pow(float(expression),2)
       
    elif val=="x!":
        ans=math.factorial(float(expression))
    text.delete(0, END)  # It will delete everythin which is on screen
    text.insert(0,ans) #It will insert value of ans at index 0

# Binding all buttons
sqrt.bind('<Button-1>', sci_cal)
power.bind('<Button-1>', sci_cal)
factorialbtn.bind('<Button-1>', sci_cal)
radbtn.bind('<Button-1>', sci_cal)
sinbtn.bind('<Button-1>', sci_cal)
cosbtn.bind('<Button-1>', sci_cal)
tanbtn.bind('<Button-1>', sci_cal)
degbtn.bind('<Button-1>', sci_cal)

#Making keyboard's equal button fuctioning 
def keybrdequalbtn(event):
    getvalue = Event() #Creating event object
    getvalue.widget=equalbtn #Assigning equal button 
    clickaction(getvalue)


text.bind('<Return>',keybrdequalbtn)

#Writing code to shift between normal mode and scientific mode

x = "Normal Mode"

def ScientificCal_click():
    global x
    x = modename.entrycget(0, "label")
    if x == "Normal Mode":
        modename.add_command(label="Scientific Cal",
                             command=ScientificCal_click)  # Adding options
        # concept : self.filemenu2.delete(0) # deletes first item in menu
        modename.delete(0)
        # self.filemenu2.delete("Stop") $ delete item with the label "Stop"
        sciFrame.pack_forget()
        root.geometry("250x400")

    else:
        modename.add_command(label="Normal Mode",
                             command=ScientificCal_click)  # Adding options
        modename.delete(0)
        buttonframe.pack_forget()
        sciFrame.pack(side=TOP)
        buttonframe.pack(side=TOP)
        root.geometry("250x520")


# Adding menubar
menubar = Menu(root, font="lucida 10 bold")  # This line says root ke andar ek menu banao
# Adding options/modes in Menu
# Aur ek menu banao jo menubar be hoga ....tearoff removes dotted line
modename = Menu(menubar, font="lucida 10 bold", tearoff=0)
modename.add_command(label="Scientific Cal",
                     command=ScientificCal_click)  # Adding options
# If u dont cascade it wont show it on screen
menubar.add_cascade(label="Mode", menu=modename)
root.config(menu=menubar)


root.mainloop()



#If you want to convert .py file to .exe file...............
#First install pyinstaller module
#While converting this .py file to .exe use command pyinstaller --onefile main.py (whatever ur filename is ) 
#If you use above command it will convert it into .exe file but when you open that exe file it will open your file along with black console in background 
#To get rid of that console use (-w)...i.e...  pyinstaller --onefile -w main.py   it will solve the problem now it will open only your gui application

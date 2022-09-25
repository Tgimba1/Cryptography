from tkinter import * #Importing all the widgets in the tkinter library(This allows you to use all the widgets without having to import each of the widgets)
from tkinter import messagebox
stem = Tk() #Creating a window
stem.geometry("400x300+10+10") #Defining the size of the window
stem.title("Group 6") #Title of our project

entry = Entry(stem, width=30) #Creating an entry field with the name entry
entry.place(x=200,y=90)

heading = Label(stem,text='PROJECT X',font=('Arial',18)) #Creating a Heading with the inscrition 'PROJECT X'
heading.place(x=150,y=30)

def my_button(): #Defining a function called my_button
     #creating a varaiable s which will handle the values of den as a list with indexes(0,1,2,3,4,5,...X)
    s=[]
    com = pass1.get() #Creating and assigning it the Entry value of the pass1 Variable using get
    den = entry.get() #Creating and assigning it the Entry value of the entry Variable using get

    #Creating an IF ELSE statement to verify whether the KEY/INPUT is empty/incorrect
    if com =='GOBE':
        
        for x in range(0,len(den),2): #Using for loop to iterate through the even indexes using range(e.g 0,2,4)
            s.append(den[x:x+2][::-1]) #This will append and reverse the even indexes of den 


    elif  com=='' or den=='':
        messagebox.showerror('Error','Enter Key/message')
    else:
       messagebox.showerror('Error','Incorrect Key')

    
    
    a = ''.join(s) #This will join the values whilst ommitting the the spaces inbetween them
    label = Label(stem, text = a) 
    #Displaying the codes in a new window
    top = Toplevel()
    msg = Label(top, text=a)
    msg.pack()

note = Label(stem,text="Insert Value here") #Creating a label with the inscription Insert Value here
note.place(x=80,y=90)

encry = Button(stem, text="Encrypt", command= my_button) #Creatung a button and passing the my_button function to it
encry.place(x=80,y=200)

decry = Button(stem, text="Decrypt", command= my_button) #Creatung a button and passing the my_button function to it
decry.place(x=200,y=200)

Pass = Label(stem,text='Enter Secret Key')
Pass.place(x=80,y=150)

pass1 = Entry(stem, width=30,show='*') #Creating an entry field with the name entry
pass1.place(x=200,y=150)

stem.mainloop() #Looping the window(Without this the window will close immediately we run the code)


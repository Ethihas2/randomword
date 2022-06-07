from tkinter import *
import random

root = Tk()
root.title("Random Word")
root.geometry("600x700")
root.configure(background="yellow3")

random_label = Label(root)

def random_genarator():
    alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']   
    random_num1 = random.randint(1,26)
    random_num2 = random.randint(1,26)
    random_num3 = random.randint(1,26)
    random_num4 = random.randint(1,26)
    random_num5 = random.randint(1,26)
    
    random_alpha_1 = alpha_list[random_num1]
    random_alpha_2 = alpha_list[random_num2]
    random_alpha_3 = alpha_list[random_num3]
    random_alpha_4 = alpha_list[random_num4]
    random_alpha_5 = alpha_list[random_num5]
    
    random_label["text"]= random_alpha_1 +random_alpha_2+random_alpha_3+random_alpha_4+random_alpha_5


button1 = Button(root,text="Generate A random word",command=random_genarator,bg="SteelBlue2",fg="White")
button1.place(relx=0.5,rely=0.4,anchor=CENTER)
random_label.place(relx=0.5,rely=0.5,anchor=CENTER)



root.mainloop()
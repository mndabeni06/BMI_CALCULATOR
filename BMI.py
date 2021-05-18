# importing the tkinter module
from tkinter import *

# creating root window
root = Tk()
root.title("Ideal Body Mass Index")
root.geometry("900x700")
root.config(bg="cyan")
header = Label(root, text='Ideal Body Mass Index Calculator', bg='gold', fg='blue', font=30)
header.place(x=250, y=20)

# creating a frame in a root
frame = Frame(root, width=500, height=200, relief='raised', bg='goldenrod')
frame.place(x=200, y=50)

# creating labels in a frame
bmi_weight = Label(frame, text="Weight(kg):", bg='white', fg='green')
bmi_weight.place(x=50, y=20)
bmi_weight_entry = Entry(frame)
bmi_weight_entry.place(x=200, y=20)

bmi_height = Label(frame, text="Height(cm):", bg='white', fg='green')
bmi_height.place(x=45, y=60)
bmi_height_entry = Entry(frame)
bmi_height_entry.place(relx=0.4, rely=0.3)

user_gender = Label(frame, text="Gender:", bg='white', fg='green')
user_gender.place(rely=0.53, relx=0.1)

age = Label(frame, text="Age:", bg='white', fg='green')
age.place(rely=0.8, relx=0.1)
age_entry = Entry(frame, state='readonly')
age_entry.place(rely=0.8, relx=0.4)

options = ['Female...', 'Male']
variable = StringVar(frame)
variable.set(options[0])

# Below is the functions created
def activate(value):
    variable.set(value)
    if value != "Select...":
        age_entry.config(state='normal')
    else:
        age_entry.config(state='readonly')


gender_menu = OptionMenu(frame, variable, *options, command=activate)
gender_menu.place(relx=0.4, rely=0.5)


def bmi_calc():
    try:
        float(bmi_weight_entry.get())
        float(bmi_height_entry.get())
        float(age_entry.get())
        if variable.get() == "Female..":
            raise ValueError
        elif variable.get() == "Male":
            result = ((0.5 * float(bmi_weight_entry.get())) / ((float(bmi_height_entry.get()) / 100) ** 2)) + 11.5
            result = round(result, 1)
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
            result_bmi = float(bmi_weight_entry.get()) / ((float(bmi_height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
        elif variable.get() == "Female":
            result = ((0.5 * float(bmi_weight_entry.get())) / ((float(bmi_height_entry.get()) / 100) ** 2)) + (
                        0.03 * float(age_entry.get())) + 11
            result = round(result, 1)
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
            result_bmi = float(bmi_weight_entry.get()) / ((float(bmi_height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
        if result_bmi < 18.5:
            category.config(text='Underweight')
        elif 18.5 <= result_bmi < 25:
            category.config(text='Healthy')
        elif 25 <= result_bmi < 30:
            category.config(text='Overweight')
        elif result_bmi >= 30:
            category.config(text='Obese')

    except ValueError:
        messagebox.showerror(title=None, message='Gender was not specified or invalid entry was given')
        delete()


calculate = Button(root, text="Calculate your Ideal Body Mass Index", width=50, command=bmi_calc)
calculate.place(rely=0.45, relx=0.2)

bmi = Label(root, text="BMI:", bg='white', fg="green")
bmi.place(rely=0.55, relx=0.1)
bmi_field = Entry(root, state='readonly')
bmi_field.place(rely=0.55, relx=0.2)
ideal_bmi = Label(root, text='Ideal BMI:', bg='white', fg="green")
ideal_bmi.place(rely=0.55, relx=0.5)
ideal_field = Entry(root, state='readonly')
ideal_field.place(rely=0.55, relx=0.65)

# The delete button function
def delete():
    bmi_weight_entry.delete(0, END)
    bmi_height_entry.delete(0, END)
    age_entry.config(state='normal')
    bmi_field.config(state='normal')
    ideal_field.config(state='normal')
    age_entry.delete(0, END)
    bmi_field.delete(0, END)
    ideal_field.delete(0, END)
    age_entry.config(state='readonly')
    bmi_field.config(state='readonly')
    ideal_field.config(state='readonly')
    bmi_weight_entry.focus()
    variable.set(options[0])
    category.config(text='')


category_head = Label(root, text="Category:", bg='orange', fg='white')
category = Label(root, width=20, bg='blue', fg='white')
category.place(relx=0.38, rely=0.72)
category_head.place(relx=0.45, rely=0.67)
clear = Button(root, text='Clear', command=delete)
clear.place(rely=0.85, relx=0.1)
quit = Button(root, text='Exit', command='exit')
quit.place(rely=0.85, relx=0.83)


root.mainloop()

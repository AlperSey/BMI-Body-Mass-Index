from tkinter import *

window = Tk()
window.title("BMI Program")
window.config(padx=30,pady=30)

weight_label = Label(text="Please Enter Weight (kg)")
weight_label.pack()

weight_entry = Entry(width=10)
weight_entry.pack()


height_label = Label(text="Please Enter Height (cm)")
height_label.pack()

height_entry = Entry(width=10)
height_entry.pack()


def calculate():
    weight  = weight_entry.get()
    height  = height_entry.get()
    if weight == "" or height =="":
        print(result_bmi.config(text="Enter Weight and Height"))
    else:
        try:
            bmi = float(format(float(weight) / ((float(height) / 100) ** 2),'.2f'))
            print(result_bmi.config(text=f"Your BMI is : {bmi}"))

            if bmi <= 18.50:    
                print(weight_status.config(text="Your Weight Status :  Underweight"))
            elif bmi > 18.50 and bmi < 25:
                print(weight_status.config(text="Your Weight Status :  Healthy Weight"))
            elif bmi >=25 and bmi < 30 :
                print(weight_status.config(text="Your Weight Status :  Overweight"))
            else:
                print(weight_status.config(text="Your Weight Status :  Obesity"))


        except ValueError:
            print(result_bmi.config(text="Enter a valid number"))
        
        
    

   
       


calculate_button = Button(text="Calculate",command=calculate)
calculate_button.pack()


result_bmi = Label(text="")
result_bmi.pack()

weight_status = Label(text="")
weight_status.pack()



window.mainloop()

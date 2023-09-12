from tkinter import*
from tkinter import ttk
import math

root = Tk()
root.title('Calculator')
root.geometry("356x405")
root.resizable(0,0)
root.configure(bg ="black")

# Display frame
display = LabelFrame(root,bd =0, relief = GROOVE,bg ='black', highlightbackground='white',highlightthickness=1) # highlight background colour use to give color to border  and thickness of the border
display.place (x =0, y=0,width =356, height = 140)

input_label = Label(display, text="", bg='black', fg="white", font=('verdana', 20),anchor ='e') # anchor 'e' use to start display the value from right hand side
input_label.pack(fill='both', expand=True, padx=10, pady=(20, 0))

output_label = Label(display, text="", bg='black', fg="white", font=('verdana', 30, 'bold'),anchor ='e')
output_label.pack(fill='both', expand=True, padx=10, pady=20)

# Button frame
button_frame = LabelFrame(root,bd =3, relief = GROOVE,bg ='black', highlightbackground='white',highlightthickness=1 )
button_frame.place (x =0, y=145,width =356)

btn7 = Button(button_frame,text = '7',bg ='darkgray', fg= 'white',width =5 ,height =2,command=lambda:get_digit(7))
btn7.grid(row =0, column =0)
btn7.config(font=('verdana',14))

btn8 = Button(button_frame,text = '8',bg ='darkgray', fg= 'white',width =5 ,height =2,command=lambda:get_digit(8))
btn8.grid(row =0, column =1)
btn8.config(font=('verdana',14))

btn9 = Button(button_frame,text = '9',bg ='darkgray', fg= 'white',width =5 ,height =2,command=lambda:get_digit(9))
btn9.grid(row =0, column =2)
btn9.config(font=('verdana',14))

# Divide button
btn_div = Button(button_frame,text = '/',bg ='darkgray', fg= 'white',width =5 ,height =2,command=lambda:perform_operation('/'))
btn_div.config(font=('verdana',14))
btn_div.grid(row =0, column =3)

#clear button
btn_clr = Button(button_frame,text = 'C',bg ='brown', fg= 'white',width =5 ,height =2,command=lambda:clear())
btn_clr.grid(row =0, column =4)
btn_clr.config(font=('verdana',14))


btn6 = Button(button_frame,text = '4',bg ='darkgray', fg= 'white',width =5 ,height =2,command=lambda:get_digit(4))
btn6.grid(row =1, column =0)
btn6.config(font=('verdana',14))

btn5 = Button(button_frame,text = '5',bg ='darkgray', fg= 'white',width =5 ,height =2,command=lambda:get_digit(5))
btn5.grid(row =1, column =1)
btn5.config(font=('verdana',14))

btn4 = Button(button_frame,text = '6',bg ='darkgray', fg= 'white',width =5 ,height =2,command=lambda:get_digit(6))
btn4.grid(row =1, column =2)
btn4.config(font=('verdana',14))

# Multiplication button
btn_mul = Button(button_frame,text = 'x',bg ='darkgray', fg= 'white',width =5 ,height =2,command=lambda:perform_operation('*'))
btn_mul.config(font=('verdana',14))
btn_mul.grid(row =1, column =3)

#SQRT button
btn_sqrt = Button(button_frame, text='^', bg='darkgray', fg='white', width=5, height=2, command=lambda: perform_operation('^'))
btn_sqrt.config(font=('verdana', 14))
btn_sqrt.grid(row=1, column=4)

btn3 = Button(button_frame,text = '1',bg ='darkgray', fg= 'white',width =5 ,height =2,command=lambda:get_digit(1))
btn3.grid(row =2, column =0)
btn3.config(font=('verdana',14))

btn2 = Button(button_frame,text = '2',bg ='darkgray', fg= 'white',width =5 ,height =2,command=lambda:get_digit(2))
btn2.grid(row =2, column =1)
btn2.config(font=('verdana',14))

btn1 = Button(button_frame,text = '3',bg ='darkgray', fg= 'white',width =5 ,height =2,command=lambda:get_digit(3))
btn1.grid(row =2, column =2)
btn1.config(font=('verdana',14))

# Subtraction button
btn_sub = Button(button_frame,text = '-',bg ='darkgray', fg= 'white',width =5 ,height =2,command=lambda:perform_operation('-'))
btn_sub.grid(row =2, column =3)
btn_sub.config(font=('verdana',14))

# Power button
btn_power = Button(button_frame, text='√', bg='darkgray', fg='white', width=5, height=2, command=lambda: perform_operation('√'))
btn_power.config(font=('verdana', 14))
btn_power.grid(row=2, column=4)

btn_double_zero = Button(button_frame, text='00', bg='darkgray', fg='white', width=5, height=2, command=lambda: get_digit('00'))
btn_double_zero.grid(row=3, column=0)
btn_double_zero.config(font=('verdana', 14))

btn0 = Button(button_frame,text = '0',bg ='darkgray', fg= 'white',width =5 ,height =2,command=lambda:get_digit(0))
btn0.grid(row =3, column =1)
btn0.config(font=('verdana',14))

# Decimal button
btn_decimal = Button(button_frame, text='.', bg='darkgray', fg='white', width=5, height=2, command=lambda: get_digit('.'))
btn_decimal.grid(row=3, column=2)
btn_decimal.config(font=('verdana', 14))

# Addition Button
btn_add = Button(button_frame,text = '+',bg ='darkgray', fg= 'white',width =5 ,height =2,command=lambda:perform_operation('+'))
btn_add.grid(row =3, column =3)
btn_add.config(font=('verdana',14))

# Equal Button or Evaluate button
btn_equal = Button(button_frame,text = '=',bg ='red', fg= 'white',width =5 ,height =2,command=lambda:calculate_result())
btn_equal.grid(row =3, column =4)
btn_equal.config(font=('verdana',14))


current_input = ""
current_result = ""

#get digit function to display the value in the display frame after pressing the button 
def get_digit(digit):
    global current_input
    if digit == '00':
        current_input += '00'
    elif digit == '.':
        if '.' not in current_input:
            current_input += '.'
    else:
        current_input += str(digit)
    input_label.config(text=current_input)
 
# Clear function to clear both result and current label 
def clear(): 
    global current_input, current_result
    current_input = ""
    current_result = ""
    input_label.config(text=current_input)
    output_label.config(text=current_result)


#  Perform operation function to perform operation on input values
def perform_operation(operator):
    global current_input
    if operator == '√': # To Perform SQRT Operation
        try:
            current_input = str(math.sqrt(float(current_input)))
        except ValueError:
            current_input = "Error"  
    elif operator == '^':     #To Perform exponential function
        current_input += '**'
    else:     # To Perform '+', '-', 'x' and '/' function
        current_input += operator
    input_label.config(text=current_input)

#calculate Function to calculate or evaluate the result 
def calculate_result():
    global current_input, current_result
    try:
        result = eval(current_input)
        current_result = str(eval(current_input))
        output_label.config(text=current_result)
    except Exception as e:
        current_result = "Error"
        output_label.config(text=current_result)
    
 
root.mainloop()


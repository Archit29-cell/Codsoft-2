# Codsoft-2
It is a graphical calculator application built using the Tkinter library in Python. Here's a brief description of the key features and functionality of Calculator:

1. **Graphical User Interface**: The calculator has a graphical user interface (GUI) with a main window that includes a display frame and a button frame.

2. **Display Frame**: The display frame at the top of the window is used to show the current input and the calculated result. It includes two labels: `input_label` for displaying the current input and `output_label` for displaying the result.

3. **Button Frame**: The button frame contains a grid of buttons that users can click to input digits, perform basic arithmetic operations (addition, subtraction, multiplication, division), perform special operations (square root and exponentiation), and clear the input or result.

4. **Button Click Functions**: Each button on the calculator triggers a specific function when clicked. For example, clicking a digit button adds that digit to the current input, clicking an operator button appends the operator to the current input, and clicking the equal button (`=`) evaluates the expression and displays the result.

5. **Mathematical Operations**: Calculator can handle basic arithmetic operations (+, -, *, /) and also includes special operations for square root (√) and exponentiation (^).

6. **Error Handling**: The calculator provides basic error handling. If an invalid expression is entered (e.g., division by zero or an invalid mathematical operation), it displays "Error" in the output label.

7. **Styling**: The GUI is styled with different background colors for the display frame and buttons, as well as font styles for the labels and buttons.

8. **Resizable Window**: The calculator window is not resizable (`root.resizable(0,0)`), meaning users cannot change its size.

Overall,  Calculator provides a user-friendly interface for performing basic mathematical calculations and includes some useful features like square root and exponentiation. It could serve as a starting point for further enhancements, such as additional mathematical functions, memory operations, or keyboard input support.

import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(False, False)
        self.window.title("Calculator")
        
        # Style configuration
        self.style = ttk.Style()
        self.style.configure("Display.TEntry",
                           font=("Arial", 40, "bold"),
                           padding=10,
                           background="#202020",
                           foreground="black")
                           
        # Display
        self.display_frame = ttk.Frame(self.window, padding="10")
        self.display_frame.grid(row=0, column=0, columnspan=4, sticky="nsew")
        
        self.equation = tk.StringVar()
        self.display = ttk.Entry(self.display_frame,
                               textvariable=self.equation,
                               justify="right",
                               style="Display.TEntry")
        self.display.grid(row=0, column=0, sticky="nsew")
        
        # Initialize variables
        self.current_expression = ""
        self.last_was_operator = False
        self.last_was_equals = False
        
        # Create buttons
        self.create_buttons()
        
        # Configure grid
        self.window.grid_columnconfigure(0, weight=1)
        for i in range(6):
            self.window.grid_rowconfigure(i, weight=1)
            
    def create_buttons(self):
        # Button style
        button_style = {
            "font": ("Arial", 20),
            "width": 5,
            "height": 2,
            "bd": 1,
            "relief": "ridge"
        }
        
        # Scientific buttons (row 1)
        scientific_buttons = [
            ("sin", lambda: self.scientific_operation("sin")),
            ("cos", lambda: self.scientific_operation("cos")),
            ("tan", lambda: self.scientific_operation("tan")),
            ("√", lambda: self.scientific_operation("sqrt"))
        ]
        
        # Number pad and operators
        buttons = [
            ("C", self.clear, "#ff9500"),
            ("±", self.toggle_sign, "#ff9500"),
            ("%", lambda: self.add_to_expression("%"), "#ff9500"),
            ("÷", lambda: self.add_to_expression("/"), "#ff9500"),
            ("7", lambda: self.add_to_expression("7"), "#333333"),
            ("8", lambda: self.add_to_expression("8"), "#333333"),
            ("9", lambda: self.add_to_expression("9"), "#333333"),
            ("×", lambda: self.add_to_expression("*"), "#ff9500"),
            ("4", lambda: self.add_to_expression("4"), "#333333"),
            ("5", lambda: self.add_to_expression("5"), "#333333"),
            ("6", lambda: self.add_to_expression("6"), "#333333"),
            ("-", lambda: self.add_to_expression("-"), "#ff9500"),
            ("1", lambda: self.add_to_expression("1"), "#333333"),
            ("2", lambda: self.add_to_expression("2"), "#333333"),
            ("3", lambda: self.add_to_expression("3"), "#333333"),
            ("+", lambda: self.add_to_expression("+"), "#ff9500"),
            ("0", lambda: self.add_to_expression("0"), "#333333"),
            (".", lambda: self.add_to_expression("."), "#333333"),
            ("⌫", self.backspace, "#333333"),
            ("=", self.calculate, "#ff9500")
        ]
        
        # Add scientific buttons
        row = 1
        for i, (text, command) in enumerate(scientific_buttons):
            btn = tk.Button(self.window, text=text, command=command,
                          font=button_style["font"],
                          width=button_style["width"],
                          height=1,
                          bd=button_style["bd"],
                          relief=button_style["relief"],
                          bg="#666666",
                          fg="white")
            btn.grid(row=row, column=i, padx=1, pady=1, sticky="nsew")
            
        # Add number pad and operators
        row = 2
        col = 0
        for text, command, color in buttons:
            btn = tk.Button(self.window, text=text, command=command,
                          font=button_style["font"],
                          width=button_style["width"],
                          height=button_style["height"],
                          bd=button_style["bd"],
                          relief=button_style["relief"],
                          bg=color,
                          fg="white")
            btn.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
                
    def add_to_expression(self, value):
        if self.last_was_equals:
            self.current_expression = ""
            self.last_was_equals = False
            
        if value in "+-*/%":
            if self.last_was_operator:
                self.current_expression = self.current_expression[:-1]
            self.last_was_operator = True
        else:
            self.last_was_operator = False
            
        self.current_expression += value
        self.equation.set(self.current_expression)
        
    def calculate(self):
        try:
            result = eval(self.current_expression)
            self.current_expression = str(result)
            self.equation.set(self.current_expression)
            self.last_was_equals = True
        except:
            self.equation.set("Error")
            self.current_expression = ""
            
    def clear(self):
        self.current_expression = ""
        self.equation.set("")
        self.last_was_operator = False
        self.last_was_equals = False
        
    def toggle_sign(self):
        try:
            if self.current_expression:
                if self.current_expression[0] == "-":
                    self.current_expression = self.current_expression[1:]
                else:
                    self.current_expression = "-" + self.current_expression
                self.equation.set(self.current_expression)
        except:
            pass
            
    def backspace(self):
        self.current_expression = self.current_expression[:-1]
        self.equation.set(self.current_expression)
        
    def scientific_operation(self, operation):
        try:
            num = float(self.current_expression)
            if operation == "sin":
                result = math.sin(math.radians(num))
            elif operation == "cos":
                result = math.cos(math.radians(num))
            elif operation == "tan":
                result = math.tan(math.radians(num))
            elif operation == "sqrt":
                result = math.sqrt(num)
                
            self.current_expression = str(result)
            self.equation.set(self.current_expression)
            self.last_was_equals = True
        except:
            self.equation.set("Error")
            self.current_expression = ""
            
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run() 
# Gets the GUI, design from tkinter
import tkinter as tk
from tkinter import messagebox
import math

# Function for calculating compound interest:
def calculate_compound_interest():
    try:
        principal = float(entry_principal.get())
        interest_rate = float(entry_interest.get()) / 100
        time = float(entry_time.get())

        amount = principal * math.pow((1 + interest_rate), time)
        result = f"The total amount after {time} years: {amount:.2f}"
        label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# Function for calculating simple interest:
def calculate_simple_interest():
    try:
        principal = float(entry_principal.get())
        interest_rate = float(entry_interest.get()) / 100
        time = float(entry_time.get())

        amount = principal * (1 + interest_rate * time)
        result = f"The total amount after {time} years: {amount:.2f}"
        label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# Function for calculating Bond-Repayments:
def calculate_bond_repayments():
    try:
        principal = float(entry_principal.get())
        interest_rate = float(entry_interest.get()) / 100 / 12
        time = float(entry_time.get())

        repayment = (interest_rate * principal) / (1 - math.pow((1 + interest_rate), -time))
        result = f"The monthly repayment amount: {repayment:.2f}"
        label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# Function that clears the entries once calculated
def clear_entries():
    entry_principal.delete(0, tk.END)
    entry_interest.delete(0, tk.END)
    entry_time.delete(0, tk.END)
    label_result.config(text="Result:")

def calculate():
    # Gets the selected calculation type and interest type from the radio buttons
    calculation_type = var.get()
    interest_type = var_interest.get()

    # Perform the corresponding calculation based on the selected types
    if calculation_type == "Bond Repayments":
        # Validate interest type selection
        if interest_type != "Bond Repayments":
            messagebox.showerror("Error", "Invalid interest type for Bond Repayments.")
            return
        calculate_bond_repayments()
    elif calculation_type == "Investment":
        if interest_type == "Simple Interest":
            calculate_simple_interest()
        elif interest_type == "Compound Interest":
            calculate_compound_interest()
    else:
        messagebox.showerror("Error", "Please select a calculation type.")

def toggle_interest_buttons():
    if var.get() == "Bond Repayments":
        button_simple_interest.config(state="disabled")
        button_compound_interest.config(state="disabled")
    else:
        button_simple_interest.config(state="normal")
        button_compound_interest.config(state="normal")

# Create the main window
root = tk.Tk()
root.title("Financial Calculator")
root.configure(background='Teal')

# Configure row and column weights
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Labels for input fields
label_principal = tk.Label(root, text="Principal:", bg='Teal', fg='White')
label_principal.grid(row=0, column=0, padx=10, pady=10)
label_interest = tk.Label(root, text="Interest Rate (%):" , bg='Teal', fg='White')
label_interest.grid(row=1, column=0, padx=10, pady=10)
label_time = tk.Label(root, text="Time:" , bg='Teal', fg='White')
label_time.grid(row=2, column=0, padx=10, pady=10)

# Entry fields for user input
entry_principal = tk.Entry(root)
entry_principal.grid(row=0, column=1, padx=10, pady=10)
entry_interest = tk.Entry(root)
entry_interest.grid(row=1, column=1, padx=10, pady=10)
entry_time = tk.Entry(root)
entry_time.grid(row=2, column=1, padx=10, pady=10)

# Label to display the result
label_result = tk.Label(root, text="Result:" , bg='Teal', fg='White')
label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Variable for calculation type
var = tk.StringVar()
var.set("Bond Repayments")
var.trace("w", lambda *args: toggle_interest_buttons())

# Radio buttons for calculation type
radio_bond_repayments = tk.Radiobutton(root, text="Bond Repayments", variable=var, value="Bond Repayments")
radio_bond_repayments.grid(row=4, column=0, padx=10, pady=10)
radio_investment = tk.Radiobutton(root, text="Investment", variable=var, value="Investment")
radio_investment.grid(row=4, column=1, padx=10, pady=10)

# Variable for interest type
var_interest = tk.StringVar()
var_interest.set("Bond Repayments")

# Buttons for different interest types
button_simple_interest = tk.Button(root, text="Simple Interest", command=lambda: calculate_simple_interest(), state="disabled")
button_simple_interest.grid(row=5, column=0, padx=10, pady=10)
button_compound_interest = tk.Button(root, text="Compound Interest", command=lambda: calculate_compound_interest(), state="disabled")
button_compound_interest.grid(row=5, column=1, padx=10, pady=10)

# Calculate button
button_calculate = tk.Button(root, text="Calculate", command=calculate, bg='Navy', fg='White')
button_calculate.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="n")

# Clear button
button_clear = tk.Button(root, text="Clear", command=clear_entries)
button_clear.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="n")

# Increase font size of all labels and buttons
labels_and_buttons = [label_principal, label_interest, label_time, label_result, radio_bond_repayments,
                      radio_investment, button_simple_interest, button_compound_interest, button_calculate,
                      button_clear]
for item in labels_and_buttons:
    item.config(font=("Arial", 14))

# Increase font size of entry fields
entry_fields = [entry_principal, entry_interest, entry_time]
for item in entry_fields:
    item.config(font=("Arial", 14))

# Start the main event loop
root.mainloop()









from tkinter import *

# Create Window
root = Tk()
root.title('Multiplicatiobn  App✖️')
root.geometry('400x300')

# Add Labels and Entry Widgets
lbl1 = Label(text="Enter First Number")
lbl1.pack()
num1_entry = Entry()
num1_entry.pack()

lbl2 = Label(text="Enter Second Number")
lbl2.pack()
num2_entry = Entry()
num2_entry.pack()

# Function to calculate product
def calculate_product():
    num1 = int(num1_entry.get())
    num2 = int(num2_entry.get())
    text_box.delete(1.0, END)
    text_box.insert(END, f"product: {num1 * num2}")

# Add Button
btn = Button(text="Calculate", command=calculate_product)
btn.pack()

# Add a Text Widget to display result
text_box = Text(height=1)
text_box.pack()

# Run the main event loop
root.mainloop()

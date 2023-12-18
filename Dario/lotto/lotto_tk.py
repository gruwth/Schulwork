# from lotto_6aus49 import *
import tkinter as tk


def on_button_click(button_nr):
    if button_nr not in selected_buttons:
        # Check if there are already 6 selected buttons
        if len(selected_buttons) >= 6:
            # If there are 6 or more selected buttons, deselect the first one
            first_selected = selected_buttons.pop(0)
            buttons[first_selected - 1].config(bg="SystemButtonFace")  # Change the color back to the default

        # Update the list and color the clicked button
        selected_buttons.append(button_nr)
        buttons[button_nr - 1].config(bg="green")

    # If the button is already selected, deselect it
    else:
        selected_buttons.remove(button_nr)
        buttons[button_nr - 1].config(bg="SystemButtonFace")


root = tk.Tk()

label = tk.Label(root, text="Hello, Tkinter!")
label.grid(row=0, column=0, columnspan=7)

buttons = []
selected_buttons = []


for i in range(7):
    for j in range(7):
        button_number = i * 7 + j + 1
        button = tk.Button(root, text=button_number, command=lambda num=button_number: on_button_click(num))
        button.grid(row=i + 2, column=j, sticky="nsew")  # Use sticky to make buttons expand
        buttons.append(button)

# Set a common minsize for all columns and rows to ensure uniform size
for i in range(7):
    root.grid_columnconfigure(i, minsize=50)
    root.grid_rowconfigure(i + 2, minsize=50)

root.mainloop()

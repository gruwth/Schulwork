import random
import tkinter as tk


def update_label_text(label_, text):
    label_.config(text=text)


def button_lock_number(button_nr):
    if button_nr not in selected_winners:
        # Check if there are already 6 selected buttons
        if len(selected_winners) >= 6:
            # If there are 6 or more selected buttons, deselect the first one
            first_selected = selected_winners.pop(0)
            buttons[first_selected - 1].config(bg="SystemButtonFace")  # Change the color back to the default

        # Update the list and color the clicked button
        selected_winners.append(button_nr)
        buttons[button_nr - 1].config(bg="green")

    # If the button is already selected, deselect it
    else:
        selected_winners.remove(button_nr)
        buttons[button_nr - 1].config(bg="SystemButtonFace")

    update_label_text(validate_label, "Choice is valid!" if validate(selected_winners) else "Choice is invalid!")


def button_lock_in():
    if validate(selected_winners):
        amount = sum(1 for i in selected_winners if i in act_winners)
        update_label_text(win_label, f"Du hast {amount} richtig.")


def button_reset():
    global act_winners, sz_winners
    selected_winners.clear()

    for button_ in buttons:
        button_.config(bg="SystemButtonFace")

    act_winners, sz_winners = get_winners()

    while not validate(act_winners):
        act_winners, _ = get_winners()

    update_label_text(win_label, "Board reset!")


def validate(lst):
    return len(lst) == len(set(lst)) and len(set(lst)) == 6


def get_winners():
    regular_numbers = [random.randint(1, 49) for _ in range(6)]
    superzahl = random.randint(1, 10)
    return regular_numbers, superzahl


root = tk.Tk()

label = tk.Label(root, text="Lotto 6 aus 49")
label.grid(row=0, column=0, columnspan=7)

buttons = []
selected_winners = []
selected_sz = []

act_winners, sz_winners = get_winners()

while not validate(act_winners):
    act_winners, _ = get_winners()

for i in range(7):
    for j in range(7):
        button_number = i * 7 + j + 1
        button = tk.Button(root, text=button_number, command=lambda num=button_number: button_lock_number(num))
        button.grid(row=i + 2, column=j, sticky="nsew")  # Use sticky to make buttons expand
        buttons.append(button)

reset_button = tk.Button(root, text="Reset", command=lambda: button_reset())
reset_button.grid(row=12, column=2, columnspan=3, sticky="nsew")

lock_button = tk.Button(root, text="Lock in", command=button_lock_in)
lock_button.grid(row=11, column=0, columnspan=7, sticky="nsew")

validate_label = tk.Label(root, text="")
validate_label.grid(row=10, column=0, columnspan=7)

win_label = tk.Label(root, text="---Result---")
win_label.grid(row=14, column=0, columnspan=7)

# Set a common minsize for all columns and rows to ensure uniform size
for i in range(7):
    root.grid_columnconfigure(i, minsize=50)
    root.grid_rowconfigure(i + 10, minsize=50)

root.mainloop()

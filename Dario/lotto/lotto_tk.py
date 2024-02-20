import random
import tkinter as tk


class Button:
    DEFAULT_COLOR = "SystemButtonFace"
    SELECTED_COLOR = "green"

    def __init__(self, number, config_func):
        self.number = number
        self.is_selected = False
        self.config_func = config_func

    def toggle(self):
        self.is_selected = not self.is_selected
        self.update_color()

    def update_color(self):
        color = self.SELECTED_COLOR if self.is_selected else self.DEFAULT_COLOR
        self.config_func(bg=color)


class Lotto:
    def __init__(self):
        self.selected_winners = []
        self.selected_sz = []
        self.get_winners()

    def get_winners(self):
        self.selected_winners = [random.randint(1, 49) for _ in range(6)]
        self.selected_sz = random.randint(1, 10)
        while not self.validate_winners():
            self.get_winners()

    def validate_winners(self):
        return len(self.selected_winners) == len(set(self.selected_winners)) and len(set(self.selected_winners)) == 6


def button_toggle(buttons_dict, button_nr, toggle_others=False):
    if toggle_others:
        for button in buttons_dict.values():
            if button.is_selected and button.number != button_nr:
                button.toggle()

    button = buttons_dict[button_nr]
    button.toggle()

    valid = validate([b.number for b in buttons_dict.values() if b.is_selected], 7)
    update_label_text(validate_label, "Choice is valid!" if valid else "Choice is invalid!")


def update_label_text(label_, text):
    label_.config(text=text)


def button_lock_in():
    selected_numbers = [b.number for b in buttons.values() if b.is_selected]
    selected_sz = [b.number for b in sz_buttons.values() if b.is_selected]

    if validate(selected_numbers) and len(selected_sz) == 1:
        amount = sum(1 for i in selected_numbers if i in lotto.selected_winners)
        sz_amount = 1 if selected_sz[0] == lotto.selected_sz else 0
        update_label_text(win_label, f"Du hast {amount} + {sz_amount} richtig.")
    else:
        update_label_text(win_label, "Invalid selection.")


def button_reset():
    for button in buttons.values():
        if button.is_selected:
            button.toggle()

    for button in sz_buttons.values():
        if button.is_selected:
            button.toggle()

    lotto.get_winners()

    update_label_text(validate_label, "")
    update_label_text(win_label, "---Reset---")


def validate(selected_numbers, amount=6):
    return len(selected_numbers) == len(set(selected_numbers)) and len(set(selected_numbers)) == amount


root = tk.Tk()
root.title("Lotto")
root.minsize(500, 500)

label = tk.Label(root, text="Lotto 6 aus 49")
label.grid(row=0, column=0, columnspan=9)

lotto = Lotto()

p_button = []
sz_button = []

for i in range(7):
    for j in range(7):
        button_number = i * 7 + j + 1
        button = tk.Button(root, text=button_number, command=lambda num=button_number: button_toggle(buttons, num))
        button.grid(row=i + 3, column=j + 1, sticky="nsew")  # Use sticky to make buttons expand
        p_button.append(button)

buttons = {i: Button(i, p_button[i - 1].config) for i in range(1, len(p_button) + 1)}

for i in range(0, 10):
    button_number = i
    button = tk.Button(root, text=i, command=lambda num=button_number: button_toggle(sz_buttons, num, True))
    button.grid(row=i + 2, column=9, sticky="nsew")
    sz_button.append(button)

sz_buttons = {i: Button(i, sz_button[i].config) for i in range(len(sz_button))}

reset_button = tk.Button(root, text="Reset", command=lambda: button_reset())
reset_button.grid(row=14, column=3, columnspan=3, sticky="nsew")

lock_button = tk.Button(root, text="Lock in", command=button_lock_in)
lock_button.grid(row=13, column=0, columnspan=9, sticky="nsew")

validate_label = tk.Label(root, text="")
validate_label.grid(row=10, column=0, columnspan=9)

win_label = tk.Label(root, text="---Result---")
win_label.grid(row=16, column=0, columnspan=9)

# Set a common minsize for all columns and rows to ensure uniform size
for i in range(10):
    root.grid_columnconfigure(i, minsize=50)
    root.grid_rowconfigure(i + 13, minsize=50)

root.mainloop()

import customtkinter as ctk
import random

# Create the main window
app = ctk.CTk()
app.title("Cee-lo Game")
app.geometry("400x250")

# Dice and message labels
dice_labels = [ctk.CTkLabel(app, text="0", font=('Helvetica', 20)) for _ in range(3)]
for i, label in enumerate(dice_labels):
    label.place(x=50 + 100*i, y=50)

status_label = ctk.CTkLabel(app, text="Roll the Dice!", font=('Helvetica', 14))
status_label.place(x=100, y=200)

# Function to roll dice and update labels
def roll_dice():
    values = [random.randint(1, 6) for _ in range(3)]
    values.sort()  # Sort to make rule checks easier
    for label, value in zip(dice_labels, values):
        label.configure(text=str(value))  # Use .configure to update text correctly
    update_game_status(values)

# Determine the outcome based on dice values
def update_game_status(values):
    if values[0] == values[1] == values[2]:  # All dice are the same
        status_label.configure(text=f"Triple {values[0]}s!")
    elif values[0] == values[1] or values[1] == values[2]:
        if values[0] == values[1]:
            score = values[2]
        else:
            score = values[0]
        status_label.configure(text=f"Pair, score with {score}")
    elif values == [1, 2, 3]:
        status_label.configure(text="1-2-3 Lose!")
    elif values == [4, 5, 6]:
        status_label.configure(text="4-5-6 Win!")
    else:
        status_label.configure(text="Roll again!")

# Roll button
roll_button = ctk.CTkButton(app, text="Roll Dice", command=roll_dice)
roll_button.place(x=140, y=150)

app.mainloop()

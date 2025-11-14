import tkinter as tk
import random

# -----------------------
# Functions
# -----------------------
def start_game():
    global number, attempts
    number = random.randint(1, 100)
    attempts = 5
    update_hearts()
    entry.delete(0, tk.END)
    entry.config(bg="white")
    message_label.config(text="")
    restart_button.pack_forget()
    root.config(bg="#f0f8ff")  

def update_hearts():
    hearts = "❤️" * attempts + "🤍" * (5 - attempts)
    hearts_label.config(text=hearts)

def check_number():
    global attempts

    guess = entry.get()

    if not guess.isdigit():
        message_label.config(text="⚠️ Enter a valid number!", fg="red")
        return

    guess = int(guess)
    difference = abs(number - guess)

    if guess == number:
        entry.config(bg="#b3ffb3")  # green background
        message_label.config(text="🎉 Correct! You guessed it!", fg="green")
        restart_button.pack(pady=10)
        return
    else:
        attempts -= 1
        update_hearts()

        if guess < number:
            if difference > 50:
                msg = "Too low.. Go up!"
            elif difference > 25:
                msg = "Low.. A bit up!"
            elif difference > 10:
                msg = "Slightly low.. Just a bit up!"
            else:
                msg = "Very close! Just a little higher!"
        else:
            if difference > 50:
                msg = "Too high.. Go down!"
            elif difference > 25:
                msg = "High.. A bit down!"
            elif difference > 10:
                msg = "Slightly high.. Just a bit down!"
            else:
                msg = "Very close! Just a little down!"

        message_label.config(text=msg, fg="#333333")

        if attempts == 0:
            entry.config(bg="#ffcccc")  # light red
            message_label.config(
                text=f"❌ No attempts left! Number was {number}",
                fg="red"
            )
            restart_button.pack(pady=10)

def clear_box():
    entry.delete(0, tk.END)
    entry.config(bg="white")
    message_label.config(text="")

# -----------------------
# GUI Window
# -----------------------
root = tk.Tk()
root.title("Guess the Number")
root.geometry("450x450")
root.config(bg="#f0f8ff")  # light blue background

# -----------------------
# Heading
# -----------------------
title = tk.Label(root, text="🎯 Guess the Number between 1 to 100 🎯",
                 font=("Comic Sans MS", 16, "bold"),
                 bg="#f0f8ff", fg="#003366")
title.pack(pady=15)

# -----------------------
# Hearts
# -----------------------
hearts_label = tk.Label(root, text="", font=("Arial", 24), bg="#f0f8ff")
hearts_label.pack(pady=5)

# -----------------------
# Entry Box
# -----------------------
entry = tk.Entry(root, font=("Arial", 14), width=18, justify="center",fg="#333333")
entry.pack(pady=10)

# -----------------------
# Buttons Frame
# -----------------------
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)

clear_btn = tk.Button(button_frame, text="Clear", width=12, bg="#ffcccb", fg="black",
                      font=("Arial", 12, "bold"), command=clear_box)
clear_btn.grid(row=0, column=0, padx=10)

check_btn = tk.Button(button_frame, text="Check", width=12, bg="#b3d9ff", fg="black",
                      font=("Arial", 12, "bold"), command=check_number)
check_btn.grid(row=0, column=1, padx=10)

# -----------------------
# Message Box
# -----------------------
message_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f8ff")
message_label.pack(pady=15)

# -----------------------
# Restart Button
# -----------------------
restart_button = tk.Button(root, text="🔄 Play Again", width=15, bg="#90ee90", fg="black",
                           font=("Arial", 12, "bold"), command=start_game)

# -----------------------
# Start first game
# -----------------------
start_game()

# -----------------------
# Run the GUI
# -----------------------
root.mainloop()
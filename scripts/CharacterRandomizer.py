import tkinter as tk
import random

# Character Randomizer Window function 
def character_randomizer_frame(root, characters, show_main_menu):
    frame = tk.Frame(root)
    
    label = tk.Label(frame, text="Character Randomizer", font=("Arial", 16))
    label.pack(pady=40)

    mode_var = tk.IntVar(value=1) # Default to "Randomize Character"

    def set_mode(n):
        mode_var.set(n)
        for i in range(1, 3):
            result_labels[i].config(text="")

    button_solo = tk.Button(frame, text="Solo", command=lambda: set_mode(1), font=("Arial", 12))
    button_duos = tk.Button(frame, text="Duos", command=lambda: set_mode(2), font=("Arial", 12))
    button_trios = tk.Button(frame, text="Trios", command=lambda: set_mode(3), font=("Arial", 12))
    button_solo.pack(side="left", padx=10, pady=5)
    button_duos.pack(side="left", padx=10, pady=5)
    button_trios.pack(side="left", padx=10, pady=5)

    result_labels = [tk.Label(frame, text="", font=("Arial", 14)) for _ in range(3)]
    for lbl in result_labels:
        lbl.pack(pady=5)

    def on_randomize():
       num_players = mode_var.get()
       if num_players > len(characters):
           chosen = [random.choice(characters) for _ in range(num_players)]
       else:
           chosen = random.sample(characters, num_players)

       for i in range(3):
            if i < num_players:
                result_labels[i].config(text=f"Player {i+1}: {chosen[i]}")
            else:
                result_labels[i].config(text="")

    randomize_button = tk.Button(frame, text="Randomize Character", command=on_randomize)
    randomize_button.pack(pady=20)

    back_button = tk.Button(frame, text="Back to Main Menu", command=show_main_menu)
    back_button.pack(pady=20)

    return frame
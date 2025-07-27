import tkinter as tk
import random

def ShiftingEarths_frame(root, show_main_menu):
    frame = tk.Frame(root)

    label = tk.Label(frame, text="Shifting Earths", font=("Arial", 16))
    label.pack(pady=40)

    shifting_earths = ["None", "Noklateo", "Crater", "Rotten Woods", "Montain Top"]

    result_label = tk.Label(frame, text="", font=("Arial", 14))
    result_label.pack(pady=20)

    def on_randomize():
        chosen = random.choice(shifting_earths)
        result_label.config(text=f"{chosen}")

    randomize_button = tk.Button(frame, text="Randomize Shifting Earths", command=on_randomize)
    randomize_button.pack(pady=20)

    back_button = tk.Button(frame, text="Back to Main Menu", command=show_main_menu)
    back_button.pack(pady=20)

    return frame
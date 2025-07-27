import tkinter as tk
import random

def ShiftingEarthsFrame(root, ShowMainMenu):
    frame = tk.Frame(root)

    label = tk.Label(frame, text="Shifting Earths", font=("Arial", 16))
    label.pack(pady=40)

    # List of Shifting Earths
    ShiftingEarths = ["None", "Noklateo", "Crater", "Rotten Woods", "Montain Top"]

    resultLabel = tk.Label(frame, text="", font=("Arial", 14))
    resultLabel.pack(pady=20)

    # Function to handle randomization
    def OnRandomize():
        chosen = random.choice(ShiftingEarths)
        resultLabel.config(text=f"{chosen}")

    # Randomize Button
    RandomizeBtn = tk.Button(frame, text="Randomize Shifting Earths", command=OnRandomize)
    RandomizeBtn.pack(pady=20)

    # Back to Main Menu Button
    BackBtn = tk.Button(frame, text="Back to Main Menu", command=ShowMainMenu)
    BackBtn.pack(pady=20)

    return frame
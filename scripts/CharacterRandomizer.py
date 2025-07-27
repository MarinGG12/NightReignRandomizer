import tkinter as tk
import random

# Character Randomizer Window function 
def CharacterRandomizerFrame(root, characters, ShowMainMenu):
    frame = tk.Frame(root)
    
    label = tk.Label(frame, text="Character Randomizer", font=("Arial", 16))
    label.pack(pady=40)

    ModeVar = tk.IntVar(value=1) # Default to "Randomize Character"

    def set_mode(n):
        ModeVar.set(n)
        for i in range(1, 3):
            ResultLabels[i].config(text="")

    # Mode Selection Buttons
    ButtonSolo = tk.Button(frame, text="Solo", command=lambda: set_mode(1), font=("Arial", 12))
    ButtonDuos = tk.Button(frame, text="Duos", command=lambda: set_mode(2), font=("Arial", 12))
    ButtonTrios = tk.Button(frame, text="Trios", command=lambda: set_mode(3), font=("Arial", 12))
    ButtonSolo.pack(side="left", padx=10, pady=5)
    ButtonDuos.pack(side="left", padx=10, pady=5)
    ButtonTrios.pack(side="left", padx=10, pady=5)

    # Result Labels for displaying characters
    ResultLabels = [tk.Label(frame, text="", font=("Arial", 14)) for _ in range(3)]
    for lbl in ResultLabels:
        lbl.pack(pady=5)

    # Function to handle randomization
    def on_randomize():
       Players = ModeVar.get()
       if Players > len(characters):
           chosen = [random.choice(characters) for _ in range(Players)]
       else:
           chosen = random.sample(characters, Players)

       for i in range(3):
            if i < Players:
                ResultLabels[i].config(text=f"Player {i+1}: {chosen[i]}")
            else:
                ResultLabels[i].config(text="")

    #Randomize Button
    RandomizeBtn = tk.Button(frame, text="Randomize Character", command=on_randomize)
    RandomizeBtn.pack(pady=20)

    #Returns to main menu
    BackBtn = tk.Button(frame, text="Back to Main Menu", command=show_main_menu)
    BackBtn.pack(pady=20)

    return frame
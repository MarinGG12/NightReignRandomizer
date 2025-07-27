import tkinter as tk
from CharacterRandomizer import CharacterRandomizerFrame
from ShiftingEarths import ShiftingEarthsFrame

def MainMenuFrame(root, show_character_randomizer, show_shifting_earths):
    frame = tk.Frame(root)
    
    # Main Menu Label
    label = tk.Label(frame, text="Main Menu", font=("Arial", 16))
    label.pack(pady=40)
    
    # Button to go to Character Randomizer
    RandomizeBtn = tk.Button(frame, text="Go to Character Randomizer", command=show_character_randomizer)
    RandomizeBtn.pack(pady=20)

    # Button to go to Shifting Earths
    ShiftingEarthBtn = tk.Button(frame, text="Go to Shifting Earths", command=show_shifting_earths)
    ShiftingEarthBtn.pack(pady=20)

    return frame

    return frame

def main():
    root = tk.Tk()
    root.title("NightReign Randomizer")
    root.geometry("600x400") #Resolution of the window

    characters = ["Wylder", "Guardian", "Raider", "Executor", "Ironeye", "Recluse", "Revenant", "Duchess"]

    def ShowMainMenu():
        CharacterRandomizerFrame.pack_forget()
        ShiftingEarthsFrame.pack_forget()
        MainMenuFrame.pack(fill="both", expand=True)

    def ShowCharacterRandomizer():
        MainMenuFrame.pack_forget()
        ShiftingEarthsFrame.pack_forget()
        CharacterRandomizerFrame.pack(fill="both", expand=True)

    def ShowShiftingEarths():
        MainMenuFrame.pack_forget()
        CharacterRandomizerFrame.pack_forget()
        ShiftingEarthsFrame.pack(fill="both", expand=True)

    main_frame = MainMenuFrame(root, ShowCharacterRandomizer, ShowShiftingEarths)
    character_frame = CharacterRandomizerFrame(root, characters, ShowMainMenu)
    shifting_earths_frame = ShiftingEarthsFrame(root, ShowMainMenu)

    main_frame.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
        
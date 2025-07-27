import tkinter as tk
from CharacterRandomizer import character_randomizer_frame
from ShiftingEarths import ShiftingEarths_frame

def main_menu_frame(root, show_character_randomizer, show_shifting_earths):
    frame = tk.Frame(root)
    
    label = tk.Label(frame, text="Main Menu", font=("Arial", 16))
    label.pack(pady=40)
    
    randomizer_button = tk.Button(frame, text="Go to Character Randomizer", command=show_character_randomizer)
    randomizer_button.pack(pady=20)

    shifting_earths_button = tk.Button(frame, text="Go to Shifting Earths", command=show_shifting_earths)
    shifting_earths_button.pack(pady=20)

    return frame

    return frame

def main():
    root = tk.Tk()
    root.title("NightReign Randomizer")
    root.geometry("600x400")

    characters = ["Wylder", "Guardian", "Raider", "Executor", "Ironeye", "Recluse", "Revenant", "Duchess"]

    def show_main_menu():
        character_frame.pack_forget()
        shifting_earths_frame.pack_forget()
        main_frame.pack(fill="both", expand=True)

    def show_character_randomizer():
        main_frame.pack_forget()
        shifting_earths_frame.pack_forget()
        character_frame.pack(fill="both", expand=True)

    def show_shifting_earths():
        main_frame.pack_forget()
        character_frame.pack_forget()
        shifting_earths_frame.pack(fill="both", expand=True)

    main_frame = main_menu_frame(root, show_character_randomizer, show_shifting_earths)
    character_frame = character_randomizer_frame(root, characters, show_main_menu)
    shifting_earths_frame = ShiftingEarths_frame(root, show_main_menu)

    main_frame.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
        
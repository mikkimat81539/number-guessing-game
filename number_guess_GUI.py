import random
import tkinter as tk
from tkinter import font

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        # SCREEN
        master.title("Number Guessing Game")
        master.geometry("300x250")
        master.configure(bg="#fff4cf")

        # TEXT font size
        self.text_size = font.Font(family="Calibri", size=14)

        # Instructions Label
        self.instructions_label = tk.Label(master, text="", bg="#fff4cf", font=self.text_size)
        self.instructions_label.pack(pady=10)

        # TEXT box
        self.text_box = tk.Text(master, bg="white", width=12, height=1, font=self.text_size, wrap=tk.WORD)
        self.text_box.pack(pady=5)

        # BUTTON
        self.btn = tk.Button(master, text='Guess', width=10, height=2, command=self.make_guess)
        self.btn.pack(pady=5)

        # Result Label
        self.result_label = tk.Label(master, text="", bg="#fff4cf", font=self.text_size)
        self.result_label.pack(pady=10)

        # Game Variables
        self.reset_game()

    def make_guess(self):
        try:
            user_input = int(self.text_box.get("1.0", tk.END).strip())
            self.text_box.delete("1.0", tk.END)  # Clear the text box after getting input

            if user_input > self.number:
                self.result_label.config(text="Guess Lower!")
            elif user_input < self.number:
                self.result_label.config(text="Guess Higher!")
            else:
                self.result_label.config(text="You Won!!!")
                self.reset_game()  # Reset game for new round
        except ValueError:
            self.result_label.config(text="That's not a valid number.")

    def reset_game(self):
        self.minimum_number = random.randint(1, 50)
        self.maximum_number = random.randint(51, 100)
        self.number = random.randint(self.minimum_number, self.maximum_number)

        self.instructions_label.config(text=f"Guess a number between {self.minimum_number} and {self.maximum_number}")

# Screen Loop
if __name__ == "__main__":
    screen = tk.Tk()
    game = NumberGuessingGame(screen)
    screen.mainloop()

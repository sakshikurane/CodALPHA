import tkinter as tk
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("456x262")  # Set window size

        # Game setup variables
        self.words = [
            "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
            "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", 
            "watermelon", "xigua", "yam", "zucchini", "almond", "basil", "cinnamon", "dill", "elderflower", "fennel",
            "ginger", "honey", "iceberg", "jalapeno", "kale", "lavender", "mint", "nutmeg", "oregano", "parsley",
            "quinoa", "rosemary", "sage", "thyme", "umbrella", "vinegar", "walnut", "xanthan", "yam", "zatar",
            "avocado", "blackberry", "cantaloupe", "dragonfruit", "eggplant", "fig", "guava", "huckleberry", "indigo", "jackfruit",
            "kumquat", "lime", "melon", "nectarine", "olive", "pineapple", "quince", "radish", "spinach", "tomato",
            "ugli", "vanilla", "watermelon", "xigua", "yam", "zucchini", "artichoke", "broccoli", "carrot", "daikon",
            "endive", "fennel", "garlic", "horseradish", "iceberg", "jicama", "kohlrabi", "leek", "mushroom", "nopales",
            "onion", "parsnip", "quinoa", "rutabaga", "shallot", "turnip", "ume", "violet", "watercress", "xylocarp",
            "yarrow", "zucchini"
        ]

        self.word_to_guess = ""
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.max_attempts = 5

        # Main frames
        self.start_frame = tk.Frame(root)
        self.start_frame.pack(fill=tk.BOTH, expand=True)

        self.game_frame = tk.Frame(root, bg="LightPink")  # Set background color of game frame

        # Starting image and instructions
        self.start_image = tk.PhotoImage(file=r"C:\Users\Sakshi\Pictures\Screenshots\Screenshot (88).png")
        self.background_label = tk.Label(self.start_frame, image=self.start_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.instructions = tk.Label(
            self.start_frame,
            text="Welcome to Hangman!!",
            font=("Times New Roman", 20),  # Medium font size
            justify="left",
            bg="white"
        )
        self.instructions.pack(pady=20)

        self.start_button = tk.Button(
            self.start_frame, text="Start Game", command=self.start_game, font=("Times New Roman", 20)  # Medium font size
        )
        self.start_button.pack(pady=20)

        # Game widgets
        self.word_label = tk.Label(self.game_frame, text="", font=("Times New Roman", 20))  # Medium font size
        self.word_label.pack(pady=20)

        self.guess_entry = tk.Entry(self.game_frame, font=("Times New Roman", 20))  # Medium font size
        self.guess_entry.pack(pady=10)
        self.guess_entry.bind("<Return>", self.make_guess)

        self.feedback_label = tk.Label(self.game_frame, text="", font=("Times New Roman", 20))  # Medium font size
        self.feedback_label.pack(pady=10)

        self.remaining_attempts_label = tk.Label(self.game_frame, text="", font=("Times New Roman", 20))  # Medium font size
        self.remaining_attempts_label.pack(pady=10)

        self.reset_button = tk.Button(
            self.game_frame, text="Reset Game", command=self.reset_game, font=("Times New Roman", 20))  # Medium font size
        self.reset_button.pack(pady=20)

        # Move the 'Next' button to the bottom after the game starts
        self.next_button = tk.Button(
            self.start_frame, text="Next", command=self.start_game, font=("Times New Roman", 20)  # Medium font size
        )
        self.next_button.pack(side=tk.BOTTOM, pady=10)

    def start_game(self):
        self.word_to_guess = random.choice(self.words)
        self.correct_guesses.clear()
        self.incorrect_guesses.clear()
        self.max_attempts = 5

        self.start_frame.pack_forget()
        self.game_frame.pack(fill=tk.BOTH, expand=True)

        # Add hangman image to the game screen when the game starts
        self.hangman_image = tk.PhotoImage(file=r"C:\Users\Sakshi\Pictures\Screenshots\Screenshot (89).png")  # Provide path to your image file
        self.hangman_image_label = tk.Label(self.game_frame, image=self.hangman_image)
        self.hangman_image_label.pack(pady=20)

        # Initialize the word display
        self.word_label.config(text=self.get_display_word())
        self.feedback_label.config(text="")
        self.remaining_attempts_label.config(text=f"Remaining attempts: {self.max_attempts}")

    def get_display_word(self):
        # Return a string with underscores for letters that have not been guessed yet
        return " ".join([letter if letter in self.correct_guesses else "_" for letter in self.word_to_guess])

    def make_guess(self, event):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if not guess.isalpha() or len(guess) != 1:
            self.feedback_label.config(text="Please enter a single letter.")
            return

        if guess in self.correct_guesses or guess in self.incorrect_guesses:
            self.feedback_label.config(text="You already guessed that letter.")
            return

        if guess in self.word_to_guess:
            self.correct_guesses.add(guess)
            self.feedback_label.config(text=f"Good guess! '{guess}' is in the word.")
        else:
            self.incorrect_guesses.add(guess)
            self.max_attempts -= 1
            self.feedback_label.config(text=f"Wrong guess! '{guess}' is not in the word.")

        self.word_label.config(text=self.get_display_word())
        self.remaining_attempts_label.config(text=f"Remaining attempts: {self.max_attempts}")

        self.check_game_over()

    def check_game_over(self):
        if set(self.word_to_guess) == self.correct_guesses:
            self.feedback_label.config(text="Congratulations! You guessed the word!")
            self.disable_input()
        elif self.max_attempts <= 0:
            self.feedback_label.config(text=f"Game Over! The word was '{self.word_to_guess}'.")
            self.disable_input()

    def disable_input(self):
        self.guess_entry.config(state=tk.DISABLED)

    def reset_game(self):
        self.start_frame.pack(fill=tk.BOTH, expand=True)
        self.game_frame.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

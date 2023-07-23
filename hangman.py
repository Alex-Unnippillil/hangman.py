import random
import tkinter as tk
from tkinter import messagebox

def choose_random_word():
    words = ["python", "hangman", "programming", "computer", "apple", "banana", "orange", "watermelon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def on_letter_click(letter):
    if letter not in guessed_letters:
        guessed_letters.append(letter)
        if letter not in word_to_guess:
            attempts_left.set(attempts_left.get() - 1)

    word_display.set(display_word(word_to_guess, guessed_letters))

    if "_" not in word_display.get():
        messagebox.showinfo("Congratulations", "You guessed the word: {}".format(word_to_guess))
        root.destroy()

    if attempts_left.get() == 0:
        messagebox.showinfo("Game Over", "The word was: {}".format(word_to_guess))
        root.destroy()

root = tk.Tk()
root.title("Hangman Game")

word_to_guess = choose_random_word()
guessed_letters = []
attempts_left = tk.IntVar(value=6)
word_display = tk.StringVar(value=display_word(word_to_guess, guessed_letters))

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

attempts_label = tk.Label(frame, text="Attempts left:")
attempts_label.grid(row=0, column=0)

attempts_count = tk.Label(frame, textvariable=attempts_left)
attempts_count.grid(row=0, column=1)

word_label = tk.Label(frame, textvariable=word_display, font=("Courier", 24))
word_label.grid(row=1, column=0, columnspan=2)

letters_frame = tk.Frame(root)
letters_frame.pack(padx=20, pady=10)

for letter in "abcdefghijklmnopqrstuvwxyz":
    tk.Button(letters_frame, text=letter.upper(), width=4, command=lambda l=letter: on_letter_click(l)).pack(side=tk.LEFT, padx=3, pady=3)

root.mainloop()

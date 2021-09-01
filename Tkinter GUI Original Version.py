from tkinter import *
from random import randint

root = Tk()
root.title('Language Flashcards')
root.geometry("410x550")

# Get user input to use in the program
words = []
n = 0
while n <= 10:
    add_card_choice = input("Add card y/n?")
    if add_card_choice == "y":
        untranslated_word = input("Untranslated Word: ")
        translated_word = input("Translated Word: ")
        words.append(untranslated_word)
        words.append(translated_word)
        # convert list into tuple
        lst = tuple(words)
        # print tuple
        print(lst)
    elif add_card_choice == "n":
        break
n += 1

# ERROR Can't get the untranslated or translated words to print as full words onto the GUI

# Get a count of word list
count = len(words)


def next():
    global hinter, hint_count
    # Clear the screen
    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text="")
    # Reset Hint stuff
    hinter = ""
    hint_count = 0

    # Randomly select word for main label
    global random_word
    random_word = randint(0, count-1)
    # Update label with new untranslated word
    untranslated.config(text=lst[random_word][0])


def answer():
    if my_entry.get().capitalize() == lst[random_word][1]:
        answer_label.config(text=f"Correct! {lst[random_word][0]} is {lst[random_word][1]}")
    else:
        answer_label.config(text=f"Incorrect! {lst[random_word][0]} is not {my_entry.get().capitalize()}")


# Track placement in the hint's word
hinter = ""
hint_count = 0


def hint():
    global hint_count
    global hinter

    if hint_count < len(lst[random_word][1]):
        hinter = hinter + lst[random_word][1][hint_count]
        hint_label.config(text=hinter)
        hint_count += 1


# GUI Labels
untranslated = Label(root, text="", font=("Helvetica", 36))
untranslated.pack(pady=50)

answer_label = Label(root, text="")
answer_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

# GUI Buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text="Next", command=next)
next_button.grid(row=0, column=1,)

hint_button = Button(button_frame, text="Hint", command=hint)
hint_button.grid(row=0, column=2, padx=20)

# Hint Text Label
hint_label = Label(root, text="")
hint_label.pack(pady=20)

# Call next function to run on program start
next()

root.mainloop()

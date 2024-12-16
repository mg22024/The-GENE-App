# Program Name: m08_FinalProject_G_M.py.
# Author: MG
# Created: 2024-11-10
# Description: Menu for The Gene App
# IDE: IDLE
# Refrence1: All information and facts were sourced from me. I have a bachelor's in Biology.
# Refrence2: Images were drawn by me or created in Canva.com with permission from my education account. 


# Pseudocode
# Import
# GUI initiating
# User input and menu options
# Menu choice validation
# Genetic Code Function
# Cells Function
# Base Pair Function
# Transciption Function (work in progress)
# Translation Function (incomplete)
# Quiz Function (work in progress)
# Start the program

# Header Banner: 

# Import
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage

# GUI initiating and creation of main window. 
def main_window():
    window = tk.Tk()
    window.geometry("600x600")
    window.title("The GENE App")

  # Change icon picture
    try:
        # My image for icon on corner of the program. 
        icon = PhotoImage(file = 'dna_image.png')
        window.iconphoto(True, icon)
        # If picture does not work, this will show. 
    except Exception:
        print("There was an issue with the image. Imagine a DNA molecule.")
    return window

# User input and menu options
def menu_list(window):
    
    # Creates a list of choices
    user_choice = [
        '1. The Genetic Code',
        '2. Cells',
        '3. DNA Base Pairing',
        '4. Transcription: DNA -> mRNA Converter',
        '5. Translation: mRNA -> Proteins Converter',
        '6. Quiz: Quiz Your Knowledge'
    ]
   # Creates and index and numbers choices in the menu.
    for index, choice in enumerate(user_choice):
        
    # Creates buttons for the menu choices.
        button = tk.Button(window, text=choice, command=lambda idx=index: select_choice(idx + 1))
        button.pack(pady = 8)

# Menu Choice validation. Not sure if I need this, since I use buttons now, but code breaks without it.
def select_choice(choice):
    if choice == 1:
        genetic_code()
    elif choice == 2:
        cells()
    elif choice == 3:
        base_pair()
    elif choice == 4:
        transcription()
    elif choice == 5:
        translation()
    elif choice == 6:
        quiz()
    else:
        print("Please choose a number from the list.")


# Genetic Code Function. Complete page for the Cells button
def genetic_code():
    
    # Create a new window for Genetic Code
    new_window = tk.Toplevel()
    new_window.geometry("1000x900")
    new_window.title("Genetic Code")

    try:
    # Add DNA picture with Genetic Code text.    
        image = PhotoImage(file = "dna.png")
        new_window.image = image
        label = tk.Label(new_window, image = image)
        label.pack(pady = 10)
        
    # If picture does not work, this will show.
    except Exception:
        tk.Label(new_window, text = "There was an issue with the image. Imagine a DNA molecule.").pack(pady = 10)
        
    # Add a question
    tk.Label(new_window, text="The study of inheritance is called? \nA. Cells \nB. Genetics \nC. DNA").pack(pady = 10)
    answer_entry = tk.Entry(new_window, width = 50)
    answer_entry.pack(pady = 5)


    # Function to process the answer and validating loop.
    def process_answer():

    # Validation loop for user input to the question about the genetic code. 
        answer = answer_entry.get().strip().lower()
        if answer == "b":
            result = "Correct!"
        elif answer == "a" or answer == "c":
            result = "Incorrect."
        else:
            result = "Enter A, B, or C."
        text_area.insert(tk.END, f"Your answer: {answer.upper()}\n{result}\n")

    # Submit button
    tk.Button(new_window, text = "Submit", command = process_answer).pack(pady = 10)
    
    # Text area and attributes to display the result
    text_area = tk.Text(new_window, wrap = tk.WORD, height = 3, width = 10)
    text_area.pack(pady = 10)
  
    # Close button
    tk.Button(new_window, text ="Close", command = new_window.destroy).pack(pady = 10)


# Cells Function. Complete page for the Genetic Code button
def cells():

    # Creates a new window for Cells.
    new_window = tk.Toplevel()
    new_window.geometry("1000x900")
    new_window.title("Cells")
    
    # Adds image of cells with text.
    try:
        image = PhotoImage(file = "3cells.png")
        new_window.image = image
        label = tk.Label(new_window, image = image)
        label.pack(pady = 10)

    # If picture does not work, this will show.
    except Exception:
        tk.Label(new_window, text="There was an issue with the image. Imagine 3 cells.").pack( pady = 10)

    # Add a question
    tk.Label(new_window, text="What is the basic unit of the cell? \nA. Cells \nB. Genetics \nC. DNA").pack(pady = 10)

    # User input for question.
    answer_entry = tk.Entry(new_window, width = 50)
    answer_entry.pack(pady = 5)


    # Function to process the answer and validating loop.
    def process_answer():

    #  Validation loop for user input to the question about cells. 
        answer = answer_entry.get().strip().lower()
        if answer == "a":
            result = "Correct!"
        elif answer == "b" or answer == "c":
            result = "Incorrect."
        else:
            result = "Enter A, B, or C."
        text_area.insert(tk.END, f"Your answer: {answer.upper()}\n{result}\n")

    # Submit button
    tk.Button(new_window, text = "Submit", command = process_answer).pack(pady = 10)
    
    # Text area and attributes to display the result
    text_area = tk.Text(new_window, wrap = tk.WORD, height = 3, width = 10)
    text_area.pack(pady = 10)

    # Close button
    tk.Button(new_window, text ="Close", command = new_window.destroy).pack(pady = 10)


# Base Pair Function
def base_pair():

    # Creates new window for this function.
    new_window = tk.Toplevel()
    new_window.geometry("400x400")
    new_window.title("DNA Base Pairing")

    # Creates a label for intructions of the base pair.
    tk.Label(new_window, text="Enter a DNA base pair (A, T, C, G):").pack(pady=10)
    
    # User input for base pair. User will have to choose A,T,C,or G.
    entry = tk.Entry(new_window, width=20)
    entry.pack(pady=5)

    # Process the question
    def process_pair():

    # Aquire user input 
        dna_pair = entry.get().strip().lower()
    # Possible DNA choices
        pairs = {"a": "t", "t": "a", "c": "g", "g": "c"}
    # What letter does the user wish to convert.
        result = pairs.get(dna_pair, "Use A, T, C, G only.")
    # Feedback for user
        text_area.insert(tk.END, f"{dna_pair.upper()} pairs with {result.upper()}\n")

    # Submit Button
    tk.Button(new_window, text="Submit", command=process_pair).pack(pady=10)

    # Text area  and attributes so that user can submit and receive feedback.
    text_area = tk.Text(new_window, wrap=tk.WORD, height=5, width=10)
    text_area.pack(pady=10)

    # Close button
    tk.Button(new_window, text ="Close", command = new_window.destroy).pack(pady = 10)

# Transcription Function: work in progress
def transcription(): pass
"""
# Have this code for transciption, but ran out of time to transfer it to Tkinter. 

    # User input with validation.
    
    transc_converter = entry.get()  
     if transc_converter  == "a":
        print("In DNA, a (Adenine) converts to u (Uracil) in mRNA.")
    elif transc_converter == "t":
        print("In DNA, t (Thymine) converts to a (Adenine) in mRNA.")
    elif transc_converter  == "c":
        print("In DNA, c (Cytosine) converts to g (Guanine) in mRNA.")
    elif transc_converter  == "g":
        print("In DNA, g (Guanine) converts to c (Cytosine) in mRNA.")
    else:
        print("DNA only has 4 base pairs. Please enter a, c, g, or t.")
"""

# translation function: Not started
def translation(): pass


# Quiz function: Where users test their knowledge: Work in progress.
def quiz():
        # Creates new window for this function. This is a work in progress. I think a class might work here. 
    new_window = tk.Toplevel()
    new_window.geometry("400x400")
    new_window.title("Test Your Knowledge!")
    
    # Question 1
    q1 = input("What is study of inheritance called?   A. Genetics  B. Cells  C. DNA" )

    # Question 1 answer validation and feedback.
    if q1 == "b":
        print("Correct!")
    elif q1 == "c":
        print("Incorrect")
    elif q1 == "a":
        print("Incorrect")
    else:
        print("Enter A,B, or C")

    # Question 2 
    q2 = input("What is the basic unit of the cell?   A. Cells  B. Genetics  C. DNA" )
    
    # Question 2 answer validation and feedback.
    if q2 == "a":
        print("Correct!")
    elif q2 == "b":
        print("Incorrect")
    elif q2 == "c":
        print("Incorrect")
    else:
        print("Enter A,B, or C")

    # Question 3
    q3 = input("What is the basic unit of the cell?   A. Cells  B. Genetics  C. DNA" )

    # Question 3 answer validation and feedback.
    if q3 == "c":
        print("Correct!")
    elif q3 == "a":
        print("Incorrect")
    elif q3 == "b":
        print("Incorrect")
    else:
        print("Enter A,B, or C")

# Start the program 
window = main_window()
menu_list(window)
window.mainloop()


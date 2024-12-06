# Program Name: Final_project_The_GENE_App_MG.py.
# Author: MG
# Created: 2024-11-10
# Description: Menu for The Gene App
# IDE: IDLE


# Pseudocode
# import
# GUI initiating
# Prompt the user to make a choice
# Validation for the menu choice
# Genetic code function
# Cells function
# DNA and base pair function
# transcription function
# Translation function
# Quiz function
# Call the functions


# import

import tkinter as tk
from tkinter import *
from tkinter import ttk, PhotoImage



# GUI initiating
window = tk.Tk()  #   instantiate and instance of a window
window.geometry("600x600")
window.title("The GENE App")  
window.configure(bg="black")  # Change the background color

# GUI workings
icon = PhotoImage(file= 'dna_image.png')  # Change icon picture/
window.iconphoto(True, icon)

entry = tk.Entry (window)
entry.config(font = ('Ink Free', 30))
entry.config(bg = "black")
entry.config(fg ="green")
entry.pack()

label_start = ttk.Label(window, text="Welcome to The GENE App: Please select an option.", background ="black", foreground= "green").pack(pady = 8)

# Prompt the user to make a choice.
def menu_list():
    user_choice = [  # Menu list
        '1. The Genetic Code',
        '2. Cells',
        '3. DNA Base Pairing',
        '4. Transcription: DNA -> mRNA Converter',
        '5. Translation: mRNA -> Proteins Converter',
        '6. Quiz: Quiz Your Knowledge'
    ]
    
    for index, choice in enumerate(user_choice):  # Creates an index in tkinter using the menu list.
        button = tk.Button(window, text = choice,background ="black", foreground= "green", command =lambda index = index: select_choice(index + 1))# GUI buttons
        button.pack(pady = 8)
  
# Validation for the menu choice
def select_choice(choice):   #Send choice to global scope.
        user_choice = entry.get()
        if choice == "1":
            genetic_code()
        elif choice == "2":
            cells()
        elif choice == "3":
            base_pair()
        elif choice == "4":
            transcription()
        elif choice == "5":
            translation()
        elif choice == "6":
            quiz()
        else:
            print("Invalid entry: Please choose a number from the list.")

# Genetic code function. Option 1.
def genetic_code():
   with open("genetic_code_text","r") as file:  # reads file about the genetic code.
       genetic_code_text = file.read
       print(genetic_code_text)  # prints the text.
       
# Cells function. Option 2.
def cells():
   with open("ce;;s_text","r") as file:  # reads file about the genetic code.
       cells_text = file.read
       print(cells_text)  # prints the text.
       
# DNA and base pair function. Option 3.
def base_pair():
    dna_pair = entry.get()  # User input
    if dna_pair == "a":
        print("In DNA, a (Adenine) always pairs with t (Thymine).")
    elif dna_pair == "t":
        print("In DNA, t (Thymine) always pairs with a (Adenine).")
    elif dna_pair == "c":
        print("In DNA, c (Cytosine) always pairs with g (Guanine).")
    elif dna_pair == "g":
        print("In DNA, g (Guanine) always pairs with c (Cytosine).")
    else:
        print("DNA only has 4 base pairs. Please enter a, c, g, or t.")
        
# transcription function. Option 4
def transcription():
    transc_converter = entry.get()   # User input
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

# Translation function. Option 5
def translation():
    pass # User input

 # Quiz function. Option 6 
def quiz():
    pass

# Call the functions
menu_list()

window.mainloop()  # Shows the window

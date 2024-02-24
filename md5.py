"""
Name: Collin Nunnally
Class: CSE-111
Comments:
Asking for a file, and checking if the md5 hash matches the file
"""
import tkinter as tk
from tkinter import filedialog, Frame, Label, Button, Entry # Used to create the widget
import hashlib # Uses to hash the file

def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter, a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Hexadecimal MD5 Calculation")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add labels, text entry boxes, and buttons to the main window.
    create_main_window(frm_main)

    # Start the tkinter loop that processes user events such as key presses and mouse button clicks.
    root.mainloop()

#   test_compute_hash_similarity()
    """
    1. summarizes all of the functions
    """

def create_main_window(frm_main):
    global ent_md5_hash #Globals fix an issue where these variables were bot able to be defined
    global lbl_comparison
    lbl_open_file = Label(frm_main, text="Open File:")
    btn_open_file = Button(frm_main, text="Open File", command=open_file)
    lbl_md5_hash = Label(frm_main, text="Hexadecimal MD5 Hash:")
    ent_md5_hash = Entry(frm_main, width=40)
    lbl_comparison = Label(frm_main)
    btn_clear = Button(frm_main, text="Clear", command=clear_window)

#   Update position of functions
    lbl_open_file.grid(row=0, column=0, padx=3, pady=3)
    btn_open_file.grid(row=0, column=1, padx=3, pady=3)
    lbl_md5_hash.grid(row=1, column=0, padx=3, pady=3)
    ent_md5_hash.grid(row=1, column=1, padx=3, pady=3)
    lbl_comparison.grid(row=2, column=0, columnspan=2, padx=3, pady=3)
    btn_clear.grid(row=3, column=0, padx=3, pady=3, columnspan=2, sticky="w")

def open_file():
    global ent_md5_hash
    global lbl_comparison
    # Code that opens a file on computer
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)
    if file_path:
        compute_hash_similarity(file_path) # Updates the similarity once a file is chosen
    return file_path

def compute_hash_similarity(filename):
    global ent_md5_hash
    global lbl_comparison
    file_md5_hash = calculate_md5(filename) # Calculate the MD5 hash of the file
    users_md5_hash = ent_md5_hash.get().strip() # Get the hash provided by the user

    # Compare the two hashes
    if file_md5_hash == users_md5_hash:
        lbl_comparison.config(text="Similarity: Hashes match")
    else:
        lbl_comparison.config(text="Similarity: Hashes do not match")

def calculate_md5(filename):
    global ent_md5_hash
    global lbl_comparison
#   Code needs to take file from btn_open_file and calculates its md5
    with open(filename, "rb") as x:
        md5_hash = hashlib.md5() # Opens given file and hashes it
        while chunk :=x.read(4096): #Reads the file in chunks and updates the hash
            md5_hash.update(chunk)
#    print(md5_hash.hexdigest()) #Used to test hexadecimal
    ent_md5_hash.bind("<KeyRelease>", lambda event: compute_hash_similarity(filename)) # Computes the hash similarity once a md5 hash is entered by the user
    return md5_hash.hexdigest() #Returns the hash in hexadecimal

def clear_window():
    global ent_md5_hash
    global lbl_comparison
    global btn_open_file # added to global since this variable is in the function
    btn_clear.focus()
    ent_md5_hash.clear()
    btn_open_file.clear()
    lbl_comparison.config(text="")
    ent_md5_hash.focus()


    # Bind the clear function to the clear button so that the computer will call the clear function when the user clicks the clear button.
    btn_clear.config(command=clear)

def test_compute_hash_similarity():
    pass
    """
    Test function for compute_hash_similarity()
    """

main()
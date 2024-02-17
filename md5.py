"""
Name: Collin Nunnally
Class: CSE-111
Comments:
Asking for a file, and checking if the md5 hash matches the file
"""
import tkinter as tk
from tkinter import filedialog, Frame, Label, Button # Used to create the widget
import hashlib # Uses to hash the file

def main():
    pass
    """
    1. summarizes all of the functions
    """

def open_file():
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)

root = tk.Tk()
root.title("File Open Example")

btn_open = tk.Button(root, text="Open File", command=open_file)
btn_open.pack(pady=10)

root.mainloop()

def calculate_md5(filename):
    with open(filename, "rb") as _:
        md5_hash = hashlib.md5() # Opens given file and hashes it
    while chunk :=f.read(4096): #Reads the file in chunks and updates the hash
        md5_hash.update(chunk)
    return md5_hash.hexdigest() #Returns the hash in hexadecimal
    """
    Using Hashlib to hash the imported file from choose_file()
    """

def create_main_window():
    
    pass
    """
    Use Wk 12 team activity to create the GUI window for the program
    """

def clear_window():
    pass
    """
    Adding the code to "reset" the GUI window
    """

def compute_hash_similarity():
    pass
    """
    Takes the hash from hash_file() and compares it to the hash given by the user
    """

def test_compute_hash_similarity():
    pass
    """
    Test function for compute_hash_similarity()
    """

# main()
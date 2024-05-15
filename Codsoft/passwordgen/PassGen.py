import random
import string
import hashlib
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def encrypt_password(password):
    encrypted_password = hashlib.sha256(password.encode()).hexdigest()
    return encrypted_password

def save_password(password):
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")

def copy_to_clipboard(password):
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

def generate_and_display_password():
    length = int(entry_length.get())
    if length <= 0:
        messagebox.showerror("Error", "Length must be greater than 0")
        return
    password = generate_password(length)
    encrypted_password = encrypt_password(password)
    save_password(encrypted_password)
    lbl_generated_password.config(text="Generated password: " + password)
    copy_to_clipboard(password)

# Create GUI window
root = tk.Tk()
root.title("Password Generator")

# Create entry field for password length
lbl_length = tk.Label(root, text="Enter password length:")
lbl_length.pack()
entry_length = tk.Entry(root)
entry_length.pack()

# Create button to generate password
btn_generate = tk.Button(root, text="Generate Password", command=generate_and_display_password)
btn_generate.pack()

# Label to display generated password
lbl_generated_password = tk.Label(root, text="")
lbl_generated_password.pack()

root.mainloop()

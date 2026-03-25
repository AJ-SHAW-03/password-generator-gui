import random
import string
import tkinter as tk


def generate_password():
    length = int(entry_length.get())

    characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))

    result_label.config(text=password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x200")

label = tk.Label(root, text="Enter Length:")
label.pack(pady=5)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

generate_btn = tk.Button(root, text="Generate password", command=generate_password)
generate_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial",12))
result_label.pack(pady=10)

root.mainloop()

from tkinter import Tk, Label
from datetime import datetime

window = Tk()
window.title("Digital Clock")
window.geometry("600x300")
# window.configure(bg="steelblue")
# window.configure(bg="blue")

label = Label(window, text="Welcome!",font=("Arial Black",78,"bold"),bg="steelblue")
label.pack(pady=100)

window.mainloop()
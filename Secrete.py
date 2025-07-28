from tkinter import *
from tkinter import messagebox
import base64

# Create main window
screen = Tk()
screen.geometry("460x500")
screen.title("Encryption and Decryption App")
screen.config(bg="#2c3e50")

# Secret key variable
code = StringVar()

# ===== Functions =====
def encrypt():
    password = code.get()
    if password == "1234":
        message = text1.get(1.0, END).strip()
        if message:
            encoded = base64.b64encode(message.encode("ascii")).decode("ascii")
            show_result("Encrypted", encoded)
        else:
            messagebox.showwarning("Warning", "Please enter a message to encrypt.")
    elif password == "":
        messagebox.showerror("Error", "Please enter the secret key!")
    else:
        messagebox.showerror("Oops", "Invalid secret key!")

def decrypt():
    password = code.get()
    if password == "1234":
        message = text1.get(1.0, END).strip()
        if message:
            try:
                decoded = base64.b64decode(message.encode("ascii")).decode("ascii")
                show_result("Decrypted", decoded)
            except Exception:
                messagebox.showerror("Error", "Invalid encrypted message!")
        else:
            messagebox.showwarning("Warning", "Please enter a message to decrypt.")
    elif password == "":
        messagebox.showerror("Error", "Please enter the secret key!")
    else:
        messagebox.showerror("Oops", "Invalid secret key!")

def reset():
    text1.delete(1.0, END)
    code.set("")
    status_label.config(text="")

def show_result(title, message):
    result_window = Toplevel(screen)
    result_window.title(f"{title} Message")
    result_window.geometry("400x250")
    result_window.config(bg="#34495e")

    Label(result_window, text=f"{title} Message:", font="Arial 13 bold", bg="#34495e", fg="white").pack(pady=10)
    text2 = Text(result_window, font="Arial 12", wrap=WORD, bg="white", fg="black")
    text2.pack(padx=10, pady=5, fill=BOTH, expand=True)
    text2.insert(END, message)
    text2.config(state=DISABLED)

    Button(result_window, text="Close", bg="red", fg="white", command=result_window.destroy).pack(pady=10)

def on_exit():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        screen.destroy()

# ===== GUI Layout =====

# Header
Label(screen, text="Encryption & Decryption", font="Impact 20 bold", bg="#2c3e50", fg="white").pack(pady=10)

# Text input
frame1 = Frame(screen, bg="#2c3e50")
frame1.pack(pady=10)

Label(frame1, text="Enter your message:", font="Arial 13", bg="#2c3e50", fg="white").pack(anchor=W)
text1 = Text(frame1, font="Arial 12", height=6, width=50, wrap=WORD, bd=2)
text1.pack()

# Secret key input
frame2 = Frame(screen, bg="#2c3e50")
frame2.pack(pady=15)

Label(frame2, text="Enter Secret Key:", font="Arial 13", bg="#2c3e50", fg="white").pack(anchor=W)
Entry(frame2, textvariable=code, font="Arial 12", bd=3, show="*").pack()

# Buttons
frame3 = Frame(screen, bg="#2c3e50")
frame3.pack(pady=15)

def on_enter(e): e.widget.config(bg="#27ae60")
def on_leave(e): e.widget.config(bg="green")

btn_encrypt = Button(frame3, text="ENCRYPT", font="Arial 12 bold", bg="green", fg="white", command=encrypt, width=12)
btn_encrypt.grid(row=0, column=0, padx=5)
btn_encrypt.bind("<Enter>", on_enter)
btn_encrypt.bind("<Leave>", on_leave)

btn_decrypt = Button(frame3, text="DECRYPT", font="Arial 12 bold", bg="blue", fg="white", command=decrypt, width=12)
btn_decrypt.grid(row=0, column=1, padx=5)

btn_reset = Button(frame3, text="RESET", font="Arial 12 bold", bg="orange", fg="black", command=reset, width=12)
btn_reset.grid(row=0, column=2, padx=5)

# Status Label
status_label = Label(screen, text="", font="Arial 11", bg="#2c3e50", fg="yellow")
status_label.pack(pady=5)

# Exit Button
Button(screen, text="Exit", font="Arial 12 bold", bg="red", fg="white", command=on_exit, width=15).pack(pady=10)

# Run the application
screen.protocol("WM_DELETE_WINDOW", on_exit)
screen.mainloop()

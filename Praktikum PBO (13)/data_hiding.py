import tkinter as tk
from tkinter import messagebox

# Langkah 5
class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Invalid deposit amount!")
        
    def reset_balance(self):
        self.__balance = 0

def add_balance():
    try:
        amount = int(entry_amount.get())
        account.deposit(amount)
        label_balance.config(text=f"Balance: {account.get_balance()}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def reset_account():
    """Fungsi untuk mereset saldo dan input ke kondisi awal."""
    account.reset_balance()
    label_balance.config(text=f"Balance: {account.get_balance()}")
    entry_amount.delete(0, tk.END)

# GUI Tkinter
root = tk.Tk()
root.title("Data Hiding in BankAccount")

# Inisialisasi objek BankAccount
account = BankAccount()

# Label untuk menampilkan saldo
label_balance = tk.Label(root, text=f"Balance: {account.get_balance()}")
label_balance.pack()

# Input untuk jumlah deposit
entry_amount = tk.Entry(root)
entry_amount.pack()

# Tombol untuk menambah saldo
button_deposit = tk.Button(root, text="Deposit", command=add_balance)
button_deposit.pack()

# Tombol untuk mereset saldo dan input
button_reset = tk.Button(root, text="Reset", command=reset_account)
button_reset.pack()

# Menjalankan aplikasi
root.mainloop()

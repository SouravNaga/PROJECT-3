import tkinter as tk
from window2 import MainWindow as mw


def main22():
    root = tk.Tk()
    root.configure(bg="green")
    root.title("Patient Database")
    root.resizable(False,False)
    mw(root).grid()
    root.mainloop()

if __name__ == "__main__":
	main()
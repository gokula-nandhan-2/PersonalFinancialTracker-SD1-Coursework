import tkinter as tk
from tkinter import ttk
import json

class FinanceTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.root.iconbitmap("icon.ico")

        height, width = 600, 800
        display_width = self.root.winfo_screenwidth()
        display_height = self.root.winfo_screenheight()

        left = int((display_width / 2) - (width / 2))
        top = int((display_height / 2) - (height / 2))
        self.root.geometry(f'{width}x{height}+{left}+{top}')
    
        self.create_widgets()
        self.transactions = self.load_transactions("transactions.json")

    def create_widgets(self):
        # Frame for table and scrollbar
        

        # Treeview for displaying transactions
        

        # Scrollbar for the Treeview
        

        # Search bar and button
        self.search_icon = tk.PhotoImage(file="search.ico")
        searchFrame = ttk.Frame(self.root)
        searchFrame.pack(pady=20)
        searchEntry = ttk.Entry(searchFrame, width=40)
        searchEntry.pack(side=tk.LEFT, padx=(0, 10))
        searchButton = ttk.Button(searchFrame, image=self.search_icon, command=self.search_transactions)
        searchButton.pack(side=tk.LEFT)

        pass
        

    def load_transactions(self, filename):
        try:
            
            pass
        except FileNotFoundError:
            return {}

    def display_transactions(self, transactions):
        # Remove existing entries

        # Add transactions to the treeview
        pass

    def search_transactions(self):
        # Placeholder for search functionality
        pass

    def sort_by_column(self, col, reverse):
        # Placeholder for sorting functionality
        pass

def main():
    root = tk.Tk()
    app = FinanceTrackerGUI(root)
    app.display_transactions(app.transactions)
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import ttk
import json

class FinanceTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.root.iconbitmap("icon.ico")

        height, width = 500, 630
        display_width = self.root.winfo_screenwidth()
        display_height = self.root.winfo_screenheight()

        left = int((display_width / 2) - (width / 2))
        top = int((display_height / 2) - (height / 2))
        self.root.geometry(f'{width}x{height}+{left}+{top}')
    
        self.create_widgets()
        self.transactions = self.load_transactions("transactions.json")

    def create_widgets(self):
        # ---------- HEADER ----------
        headerFrame = ttk.Frame(self.root)
        headerFrame.pack(fill="x", pady=20, padx=20)

        # Left side - Expenses label
        expensesLabel = ttk.Label(headerFrame, text="DETAILS OF EXPENSES", font=("Verdana", 20, "bold"))
        expensesLabel.pack(side="top", anchor="center")

        # Search bar and button
        searchFrame = ttk.Frame(self.root)
        searchFrame.pack(pady=0, padx=20)

        searchEntry = ttk.Entry(searchFrame, width=50, font=("Arial", 12))
        searchEntry.pack(side="left", padx=(0,16), ipady=6)

        # Style for button font
        style = ttk.Style()
        style.configure("Search.TButton", font=("Arial", 12, "bold"), padding=(10,2))

        searchButton = ttk.Button(searchFrame, text="Search", command=self.search_transactions, style="Search.TButton")
        searchButton.pack(side="left", ipady=6)
        
        # Frame for table and scrollbar
        tableFrame = ttk.Frame(self.root, width=600, height=350, relief="solid")
        tableFrame.pack(side="bottom", pady=35, padx=20)
        tableFrame.pack_propagate(False)
        

        # Treeview for displaying transactions
        table = ttk.Treeview(tableFrame, columns=("Expense", "Date", "Amount"), show="headings")
        table.heading("Expense", text="Type of Expense")
        table.heading("Date", text="Date")
        table.heading("Amount", text="Amount")

        table.column("Expense", width=200, anchor="w")
        table.column("Date", width=100, anchor="center")
        table.column("Amount", width=150, anchor="e")

        # Change font for the whole Treeview (including headers and rows)
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 10), rowheight=50)           # font for rows
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"),padding=[10,10,10,10])  

        # Scrollbar for the Treeview
        vscrollbar = ttk.Scrollbar(tableFrame, orient="vertical", command=table.yview)
        vscrollbar.pack(side="right", fill="y")
        table.configure(yscrollcommand=vscrollbar.set)
        table.pack(fill="both", expand=True)




        

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

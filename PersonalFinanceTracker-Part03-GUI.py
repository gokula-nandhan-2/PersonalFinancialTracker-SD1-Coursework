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
        # Set the style for the entire application
        self.root.configure(bg="#0E141B")
        # Header frame
        headerFrame = tk.Frame(self.root, bg="#0E141B")
        headerFrame.pack(fill="x", pady=20, padx=20)

        # Left side - Expenses label
        expensesLabel = tk.Label(headerFrame, 
                                 text="DETAILS OF EXPENSES", 
                                 font=("Verdana", 20, "bold"),
                                 bg="#0E141B", 
                                 fg="#4A90E2")
        expensesLabel.pack(side="top", anchor="center")

        # Search bar and button
        searchFrame = tk.Frame(self.root, bg="#0E141B")
        searchFrame.pack(pady=0, padx=20)

        # Style for search entry
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Search.TEntry",
                        fieldbackground="#252535",
                        foreground="white",
                        bordercolor="#4A90E2",
                        insertcolor="white",
                        padding=5,
                        borderwidth=0,
                        lightcolor="#4A90E2",
                        )

        searchEntry = ttk.Entry(searchFrame, width=50, font=("Arial", 12), style="Search.TEntry")
        searchEntry.pack(side="left", padx=(0,16), ipady=3)

        # Style for button font
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Search.TButton", 
                        font=("Arial", 12, "bold"), 
                        padding=(10,2), 
                        background="#4A90E2", 
                        foreground="#FFFFFF", 
                        borderwidth=0)
        style.map("Search.TButton",
              background=[("active", "#357ABD")],
              foreground=[("active", "white")])

        searchButton = ttk.Button(searchFrame, text="Search", command=self.search_transactions, style="Search.TButton")
        searchButton.pack(side="left", ipady=6)
        
        # Frame for table and scrollbar
        tableFrame = tk.Frame(self.root, 
                               width=600, 
                               height=350, 
                               bg="#2E2E42",
                               )
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
        style.configure("Treeview", font=("Arial", 10), rowheight=50) # Font for rows
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

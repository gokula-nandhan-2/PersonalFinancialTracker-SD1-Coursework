import tkinter as tk
from tkinter import ttk
import json

class FinanceTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker") # Set the window title
        self.root.iconbitmap("icon.ico") # Set the window icon (use your own icon file)

        # Define window size
        height, width = 500, 630
        display_width = self.root.winfo_screenwidth() # Get screen width
        display_height = self.root.winfo_screenheight() # Get screen height

        # Calculate coordinates to center the window on the screen
        left = int((display_width / 2) - (width / 2))
        top = int((display_height / 2) - (height / 2))
        
        # Set the window geometry (size and position)
        self.root.geometry(f'{width}x{height}+{left}+{top}')
    
        self.create_widgets() # Create and place all widgets in the window
        self.transactions = self.load_transactions("transactions02.json")  # Load existing transactions from JSON file

    def create_widgets(self):
        # Set background color for the main window
        self.root.configure(bg="#0E141B")  # Dark blue/black background

        # Header frame container for the label
        headerFrame = tk.Frame(self.root, bg="#0E141B")
        headerFrame.pack(fill="x", pady=20, padx=20)  # Pack with padding and fill horizontally

        # Label at the top: "DETAILS OF EXPENSES"
        expensesLabel = tk.Label(headerFrame, 
                                 text="DETAILS OF EXPENSES", 
                                 font=("Verdana", 20, "bold"),
                                 bg="#0E141B", 
                                 fg="white")
        expensesLabel.pack(side="top", anchor="center")

        # Frame for search bar and button below header
        searchFrame = tk.Frame(self.root, bg="#0E141B")
        searchFrame.pack(pady=0, padx=20)

        # Style configuration for the search entry (input box)
        style = ttk.Style()
        style.theme_use("clam")  # Use the 'clam' theme for ttk widgets
        style.configure("Search.TEntry",
                        fieldbackground="#252535", # Dark gray background inside entry
                        foreground="white", # Text color
                        insertcolor="white", # Cursor color
                        padding=5,
                        borderwidth=0, # No border for flat look
                        )

        # Create the search entry box with above style
        self.searchEntry = ttk.Entry(searchFrame, width=50, font=("Arial", 12), style="Search.TEntry")
        self.searchEntry.pack(side="left", padx=(0,16), ipady=3)  # ipady for vertical padding inside entry

        # Style configuration for the Search button
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Search.TButton", 
                        font=("Arial", 12, "bold"), 
                        padding=(10,2), 
                        background="#232858", # Dark blue background
                        foreground="#FFFFFF", # White text
                        borderwidth=0)
        style.map("Search.TButton",
              background=[("active", "#357ABD")], # Change bg color on hover/active
              foreground=[("active", "white")]) # Change text color on active

        # Create Search button next to the entry
        searchButton = ttk.Button(searchFrame, text="Search", command=self.search_transactions, style="Search.TButton")
        searchButton.pack(side="left", ipady=6) # Vertical padding

        # Frame to contain the table and scrollbar
        tableFrame = tk.Frame(self.root, 
                               width=600, 
                               height=350, 
                               bg="#2E2E42",
                               highlightthickness=0,
                               bd=0,
                               borderwidth=0)
        tableFrame.pack(side="bottom", pady=35, padx=20)
        tableFrame.pack_propagate(False)  # Prevent frame from resizing to fit contents

        # Style Treeview (table) with a dark theme and blue accents
        style.configure("Treeview",
                        font=("Arial", 12),
                        background="#1E1E2F", # Dark row background
                        foreground="white", # White text
                        rowheight=50, # Row height for readability
                        padding=2,
                        fieldbackground="#1E1E2F",
                        borderwidth=0,
                        relief="flat")

        # Style Treeview heading (column headers)
        style.configure("Treeview.Heading",
                        font=("Arial", 14, "bold"),
                        background="#2C2C41", # Dark blue header background
                        foreground="white",
                        padding=[10, 10, 10, 10],
                        highlightthickness=0,
                        bordercolor="#1E1E2F",
                        borderwidth=0,
                        relief="flat")
        style.map("Treeview.Heading",
                background=[("active", "#24243B")]) # Header bg on hover/active

        # Create the Treeview widget with three columns (Expense, Date, Amount)
        self.table = ttk.Treeview(tableFrame, columns=("Expense", "Date", "Amount"), show="headings")

        # Set headings with clickable sorting callbacks
        self.table.heading("Expense", text="Type of Expense", command=lambda: self.sort_by_column("Expense", False))
        self.table.heading("Date", text="Date", command=lambda: self.sort_by_column("Date", False))
        self.table.heading("Amount", text="Amount (Rs.)", command=lambda: self.sort_by_column("Amount", False))

        # Define column widths and text alignment
        self.table.column("Expense", width=200, anchor="w")    # Left aligned
        self.table.column("Date", width=100, anchor="center")  # Center aligned
        self.table.column("Amount", width=150, anchor="e")     # Right aligned

        # Update Treeview style for font and row height (for data rows)
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 10), rowheight=50)  # Smaller font for rows
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"), padding=[10,10,10,10])  # Header style

        # Style for vertical scrollbar on table
        style.configure("Vertical.TScrollbar",
            gripcount=0,
            background="#2E2E42",
            darkcolor="#2E2E42",
            lightcolor="#2E2E42",
            troughcolor="#1E1E2F",
            bordercolor="#2E2E42",
            arrowcolor="white"
        )

        # Create vertical scrollbar for the Treeview
        vscrollbar = ttk.Scrollbar(tableFrame, orient="vertical", style="Vertical.TScrollbar", command=self.table.yview)
        vscrollbar.pack(side="right", fill="y")
        self.table.configure(yscrollcommand=vscrollbar.set) # Attach scrollbar to the table
        self.table.pack(fill="both", expand=True) # Expand to fill frame

    def load_transactions(self, filename):
        try:
            with open(filename, 'r') as file:
                transactions = json.load(file)
                return transactions
        except FileNotFoundError:
            # If file not found, print message and return empty dict
            print("No previous transactions found, starting fresh!")
            return {}

    def display_transactions(self, transactions):
        """Display the given transactions in the Treeview table."""
        # Clear any existing rows in the table
        for item in self.table.get_children():
            self.table.delete(item)

        # Insert all transaction rows into the table
        # transactions is a dict with categories as keys, and list of transaction dicts as values
        for category, trans_list in transactions.items():
            for trans in trans_list:
                self.table.insert("", "end", values=(
                    category,
                    trans.get("Date", ""), # Get date or empty string if missing
                    trans.get("Amount", "") # Get amount or empty string if missing
                ))

    def search_transactions(self):
        """Filter transactions based on the search entry text."""
        keyword = self.searchEntry.get().strip().lower()  # Get lowercase keyword from input

        if not keyword:
            # If search box is empty, show all transactions
            self.display_transactions(self.transactions)
            return

        filtered = {}

        # Loop through all transactions and filter those that match the keyword
        for category, trans_list in self.transactions.items():
            filtered_list = []
            for trans in trans_list:
                # Check if keyword in category, date, or amount (converted to string)
                if (keyword in category.lower() or
                    keyword in trans.get("Date", "").lower() or
                    keyword in str(trans.get("Amount", "")).lower()):
                    filtered_list.append(trans)

            if filtered_list:
                filtered[category] = filtered_list

        # Display filtered transactions
        self.display_transactions(filtered)

    def sort_by_column(self, col, reverse):
        """Sort the table rows by the given column."""
        data = []
        for child in self.table.get_children(''):
            value = self.table.set(child, col)
            if col == "Amount":
                value = float(value)  # Convert Amount column to float for numeric sorting
            data.append((value, child))

        # Sort data tuples by the value (ascending or descending)
        data.sort(reverse=reverse)

        # Reorder rows in the table according to sorted data
        for index, item_tuple in enumerate(data):
            self.table.move(item_tuple[1], '', index)

        # Update the heading command to reverse the sorting order on next click
        self.table.heading(col, command=lambda: self.sort_by_column(col, not reverse))


def main():
    root = tk.Tk() # Create root window
    app = FinanceTrackerGUI(root)  # Initialize the app with root window
    app.display_transactions(app.transactions)  # Display loaded transactions
    root.mainloop() # Run the Tkinter event loop

if __name__ == "__main__":
    main()

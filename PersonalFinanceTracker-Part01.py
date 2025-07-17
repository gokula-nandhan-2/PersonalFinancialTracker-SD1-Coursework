import json


# Global list to store transactions
transactions = []

# File handling functions
def load_transactions():
    try:
        with open('transactions.json', 'r') as file:
            global transactions
            transactions = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No previous transactions found. Starting fresh.")
        transactions = []


def save_transactions():
    try:
        with open('transactions.json', 'w') as file:

      
 pass
# Feature implementations
def add_transaction():
 pass
def view_transactions():
 pass
def update_transaction():
 pass
def delete_transaction():
 pass
def display_summary():
 pass
def main_menu():
 pass


if __name__ == "__main__":
 main_menu()
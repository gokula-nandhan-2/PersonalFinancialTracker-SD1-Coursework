import json
from datetime import datetime

class FinanceManager:
    def __init__(self, filename="transactions02.json"):
        self.filename = filename
        self.transactions = {}

    def load_transactions(self):
        try:
            with open(self.filename, "r") as file:
                self.transactions = json.load(file)
            print("Transactions loaded successfully!")
        except FileNotFoundError:
            print("No previous transactions found, starting fresh!")
            self.transactions = {}
        except json.JSONDecodeError:
            print("Error decoding JSON file, starting fresh!")
            self.transactions = {}

    def save_transactions(self):
        try:
            with open(self.filename, "w") as file:
                json.dump(self.transactions, file, indent=4)
            print("Transactions saved successfully!")
        except IOError:
            print("Error saving transactions to file!")

    def add_transaction(self, expense, amount, date):
        if expense not in self.transactions:
            self.transactions[expense] = []
        self.transactions[expense].append({"Amount": amount, "Date": date})
        self.save_transactions()

    def update_transaction_type(self, old_type, new_type):
        if old_type in self.transactions and new_type not in self.transactions:
            self.transactions[new_type] = self.transactions.pop(old_type)
            self.save_transactions()
            return True
        return False

    def update_transaction_amount(self, expense, index, amount):
        try:
            self.transactions[expense][index]["Amount"] = amount
            self.save_transactions()
            return True
        except (IndexError, KeyError):
            return False

    def update_transaction_date(self, expense, index, date):
        try:
            self.transactions[expense][index]["Date"] = date
            self.save_transactions()
            return True
        except (IndexError, KeyError):
            return False

    def delete_transaction(self, expense, index):
        try:
            del self.transactions[expense][index]
            if len(self.transactions[expense]) == 0:
                del self.transactions[expense]  # remove category if empty
            self.save_transactions()
            return True
        except (IndexError, KeyError):
            return False

    def search_transactions(self, keyword):
        keyword = keyword.lower()
        filtered = {}
        for category, trans_list in self.transactions.items():
            filtered_list = []
            for trans in trans_list:
                if (keyword in category.lower() or
                    keyword in trans.get("Date", "").lower() or
                    keyword in str(trans.get("Amount", "")).lower()):
                    filtered_list.append(trans)
            if filtered_list:
                filtered[category] = filtered_list
        return filtered

    def get_summary(self):
        summary = {}
        total_expense = 0
        for category, entries in self.transactions.items():
            category_total = sum(entry["Amount"] for entry in entries)
            summary[category] = {"total": category_total, "count": len(entries)}
            total_expense += category_total
        return summary, total_expense

    def read_bulk_transactions_from_file(self, file_name="transactions02.txt"):
        try:
            with open(file_name, "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(",")
                    if len(parts) != 3:
                        continue
                    transaction_type, amount, date = parts
                    try:
                        transaction_type = transaction_type.strip().capitalize()
                        amount = int(amount)
                        datetime.strptime(date, "%Y-%m-%d")
                    except ValueError:
                        continue
                    if transaction_type not in self.transactions:
                        self.transactions[transaction_type] = []
                    self.transactions[transaction_type].append({"Amount": amount, "Date": date})
            self.save_transactions()
            print("Bulk transactions loaded successfully!")
        except FileNotFoundError:
            print("File not found!")

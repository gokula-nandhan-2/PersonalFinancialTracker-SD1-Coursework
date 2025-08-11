# 💰 Personal Finance Tracker - Multi-Stage Project

### 📌 **Overview**

This project evolves in **three stages**:

1. **List-based tracker** (JSON serialization) - focus on lists, loops, functions.
2. **Dictionary-based tracker** (with bulk file reading) - faster lookups, organized data.
3. **GUI-based tracker** (Tkinter + OOP) - interactive and user-friendly interface.

Each stage adds **new features** and **programming concepts** while keeping the core functionality: CRUD operations, JSON storage, and testing.

---

## 🛠 **Progression Diagram**

```
Stage 1 (Lists + JSON)
        ↓
Stage 2 (Dictionaries + Bulk Import)
        ↓
Stage 3 (GUI + OOP + Search & Sort)
```

---

## 📂 **Stage Details**

### **1️⃣ Stage 1 - List-Based Finance Tracker**

**Goal:** Build a simple finance tracker using **only lists** (no dictionaries).
**Skills:** Lists, loops, functions, JSON I/O, input validation.
**Transaction Scope: Handles both Income and Expense transactions.**
**Data Structure:**

```python
[
    [150, "Groceries", "Expense", "2024-05-10"],
    [1000, "Salary", "Income", "2024-05-01"]
]
```

**Features:**

* Add / View / Update / Delete transactions
* Summary by type/category
* Save & load using JSON
* Input validation for date, amount, and type

---

### **2️⃣ Stage 2 - Dictionary-Based Tracker**

**Goal:** Use **dictionaries** for better data organization and introduce **bulk file reading**.
**Skills:** Dictionaries, file parsing, JSON serialization.
**Transaction Scope: Expense-only** (per assignment input format).
**Data Structure:**

```json
{
    "Groceries": [
        {"amount": 150, "date": "2024-02-03"},
        {"amount": 75, "date": "2024-02-15"}
    ],
    "Salary": [
        {"amount": 1000, "date": "2024-02-01"}
    ]
}
```

**New Feature:** Bulk import transactions from a `.txt` file.

---

### **3️⃣ Stage 3 - GUI-Based Tracker**

**Goal:** Create a **Tkinter GUI** with **OOP** and add **search/sort** features.
**Skills:** Tkinter widgets, Treeview tables, event handling, OOP in Python.
**Transaction Scope: Expense-only** (per assignment input format).
**Features:**

* Load JSON automatically at startup
* Display transactions in a sortable table
* Search transactions by date, category, or amount
* CRUD via buttons and input dialogs
* Sorting by clicking column headers

---

## ⚙ **Installation**

1. Install **Python 3.8+**
2. Ensure **Tkinter** is available (`pip install tk` if needed)
3. Clone or download the repository

---

## ▶ **Running the Program**

**Stage 1 & 2 (Console)**:

```bash
PersonalFinanceTracker_Part01.py
PersonalFinanceTracker_Part02.py
```

**Stage 3 (GUI)**:

```bash
PersonalFinanceTracker_Part03.py
```

---

## Screenshots

### Main Menu

<img src="images/main_menu.png" alt="Main Menu" width="500">

### Transaction Table

<img src="images/transaction_table.png" alt="Transaction Table" width="500">

---



## 📄 **JSON File Format**

* **Stage 1:** Nested list
* **Stage 2 & 3:** Dictionary with categories as keys

---

## 🧪 **Testing**

* CRUD operations
* Bulk file reading (Stage 2)
* GUI search/sort (Stage 3)
* Edge cases for empty data, invalid inputs

---

## 📝 Special Notes

* **Codes are modified after submission for better working purposes.**
* **Assignment-related other documents are available in the `additional-documents` branch.**
* **Transaction scope difference:** Stage 1 supports both **Income and Expense**, while Stage 2 and Stage 3 are **Expense-only** as per the assignment input format.

---


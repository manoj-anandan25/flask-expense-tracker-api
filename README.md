## Flask Expense Tracker API
jfghhhghgkkgjgjj...........................................yythhghagh239847
A simple REST API built with Flask and SQLite to track expenses.  
You can add, view, update, delete, and partially update expense records.

---

 Features
- Add a new expense
- View all expenses
- Get a specific expense by ID
- Update or partially update an expense
- Delete an expense

---

 Project Structure
```

flask-expense-tracker-api/
│── expense\_tracker.py   # Main Flask app
│── expense\_SDK.py       # Python SDK to interact with the API
│── requirements.txt     # Python dependencies
│── README.md            # Documentation
│── data.db              # SQLite database (auto-created)
│── LICENSE              # MIT License

````

---

 Installation (VS Code or PowerShell)

### 1️⃣ Install Python
Make sure Python **3.7+** is installed.  
Check version:
```powershell
python --version
````

### 2️⃣ Clone the Repository

```powershell
git clone https://github.com/<your-username>/flask-expense-tracker-api.git
cd flask-expense-tracker-api
```

### 3️⃣ Create a Virtual Environment

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

### 4️⃣ Install Dependencies

```powershell
pip install -r requirements.txt
```

### 5️⃣ Initialize the Database

In PowerShell or VS Code Terminal:

```powershell
python
```

Then run:

```python
from expense_tracker import db
db.create_all()
exit()
```

### 6️⃣ Run the Application

```powershell
python expense_tracker.py
```

By default, the app runs at:

```
http://127.0.0.1:5000/
```

---

## 🛠 API Endpoints

| Method | Endpoint        | Description                 |
| ------ | --------------- | --------------------------- |
| GET    | `/expense`      | Get all expenses            |
| GET    | `/expense/<id>` | Get expense by ID           |
| POST   | `/expense`      | Add a new expense           |
| PUT    | `/expense/<id>` | Fully update an expense     |
| PATCH  | `/expense/<id>` | Partially update an expense |
| DELETE | `/expense/<id>` | Delete an expense           |

---

## Example: Add a New Expense

```powershell
curl -X POST http://127.0.0.1:5000/expense `
     -H "Content-Type: application/json" `
     -d "{\"amount\":50.5,\"category\":\"Food\",\"date\":\"2025-08-14\",\"notes\":\"Lunch\"}"
```

---

##  Using the Python SDK

You can use `expense_sdk.py` to interact with the API:

```python
from expense_sdk import ExpenseAPI

api = ExpenseAPI()

# Add expense
print(api.add_expense(100, "Travel", "2025-08-14", "Taxi fare"))

# Get all expenses
print(api.get_all_expenses())
```




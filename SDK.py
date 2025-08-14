
import requests

class ExpenseAPI:
    def __init__(self, base_url="http://127.0.0.1:5000"):
        self.base_url = base_url.rstrip('/')

    def get_all_expenses(self):
        return requests.get(f"{self.base_url}/expense").json()

    def get_expense(self, expense_id):
        return requests.get(f"{self.base_url}/expense/{expense_id}").json()

    def add_expense(self, amount, category, date, notes):
        data = {
            "amount": amount,
            "category": category,
            "date": date,
            "notes": notes
        }
        return requests.post(f"{self.base_url}/expense", json=data).json()

    def update_expense(self, expense_id, amount, category, date, notes):
        data = {
            "amount": amount,
            "category": category,
            "date": date,
            "notes": notes
        }
        return requests.put(f"{self.base_url}/expense/{expense_id}", json=data).json()

    def patch_expense(self, expense_id, amount=None, category=None, date=None, notes=None):
        data = {}
        if amount is not None:
            data["amount"] = amount
        if category is not None:
            data["category"] = category
        if date is not None:
            data["date"] = date
        if notes is not None:
            data["notes"] = notes
        return requests.patch(f"{self.base_url}/expense/{expense_id}", json=data).json()

    def delete_expense(self, expense_id):
        return requests.delete(f"{self.base_url}/expense/{expense_id}").json()


if __name__ == "__main__":
    api = ExpenseAPI()
    print(api.add_expense(45.75, "Groceries", "2025-08-14", "Weekly shopping"))
    print(api.get_all_expenses())


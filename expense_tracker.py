from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable = False)
    notes = db.Column(db.Text)

    def __repr__(self):
        return f"<Expense {self.id} | {self.category} | {self.amount}>"
    
@app.route('/')
def home():
    return 'Expense Tracker :)'

@app.route('/expense')
def get_expenses():
    expenses = Expense.query.all()
    output = []
    for expense in expenses:
        expense_data = {"amount":expense.amount,"category":expense.category,"date":expense.date,"notes":expense.notes}
        output.append(expense_data)
    return {"Expense": output}

@app.route('/expense/<id>')
def get_expense(id):
    expense = Expense.query.get(id)
    if expense is None:
        return {"Error":"Not Found"},
    return {"amount":expense.amount,"category":expense.category,"date":expense.date,"notes":expense.notes},200

@app.route('/expense', methods = ['POST'])
def add_expense():
    expense = Expense(amount = request.json['amount'],category=request.json['category'],date=request.json['date'],notes = request.json['notes'])
    db.session.add(expense)
    db.session.commit()
    return {"id":expense.id}

@app.route('/expense/<id>', methods =['DELETE'])
def delete_expense(id):
    expense = Expense.query.get(id)
    if expense is None:
        return {"Error":"Not Found"}
    db.session.delete(expense)
    db.session.commit()
    return {"Message":"Deleted Successfully"}

@app.route('/expense/<id>', methods = ['PUT'])
def update_expense(id):
    expense = Expense.query.get(id)
    if expense is None:
        return {"Error":"Not Found"}
    expense.amount = request.json['amount']
    expense.category = request.json['category']
    expense.date = request.json['date']
    expense.notes = request.json['notes']
    db.session.commit()
    return {"Message":"Updated_Successfully"}

@app.route('/expense/<id>', methods = ['PATCH'])
def patch_expense(id):
    expense = Expense.query.get(id)
    if expense is None:
        return {"Error":"Not Found"}
    if "amount" in request.json:
        expense.amount = request.json['amount']
    if "category" in request.json:
        expense.category = request.json['category']
    if "date" in request.json:
        expense.date = request.json['date']
    if "notes" in request.json:
        expense.notes = request.json['notes']
    db.session.commit()
    return {"Message":"Patched_Successfully"}
    
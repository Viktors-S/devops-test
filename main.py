from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy data for expenses (in reality, you would store this in a database)
expenses = []

# Dummy data for income (in reality, you would store this in a database)
income = 2000

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Dummy authentication (replace with actual authentication logic)
    if username == 'admin' and password == 'password':
        session['username'] = username
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        return redirect(url_for('index'))
    
    total_expenses = sum(expense['amount'] for expense in expenses)
    budget_left = income - total_expenses

    if request.method == 'POST':
        category = request.form['category']
        amount = float(request.form['amount'])
        expenses.append({'category': category, 'amount': amount})
        return redirect(url_for('dashboard'))

    return render_template('dashboard.html', expenses=expenses, income=income, budget_left=budget_left)

if __name__ == '__main__':
    app.run(debug=True)

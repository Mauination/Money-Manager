import sqlite3
from util import accounts, transactions, expenses, income

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('money.db')  # creates a database in memory
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            return conn
        else:
            print("ERROR! cannot create the database connection.")
            return None

def get_total_balance(conn):
    cur = conn.cursor()
    cur.execute("SELECT SUM(account_balance) FROM accounts")
    return cur.fetchone()[0]

def get_total_expenses(conn):
    cur = conn.cursor()
    cur.execute("SELECT SUM(amount) FROM expenses")
    return cur.fetchone()[0]

def get_total_income(conn):
    cur = conn.cursor()
    cur.execute("SELECT SUM(amount) FROM income")
    return cur.fetchone()[0]

def search_accounts(conn, account_name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM accounts WHERE account_name=?", (account_name))
    return cur.fetchall()

def search_transaction(conn, transaction_name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM transactions WHERE transaction_name=?", (transaction_name))
    return cur.fetchall()

def search_expense(conn, expense_name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses WHERE expense_name=?", (expense_name))
    return cur.fetchall()

def search_income(conn, income_name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM income WHERE income_name=?", (income_name))
    return cur.fetchall()

def search_all_accounts(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM accounts")
    return cur.fetchall()

def search_all_transactions(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM transactions")
    return cur.fetchall()

def search_all_expenses(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses")
    return cur.fetchall()

def search_all_income(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM income")
    return cur.fetchall()

def calculate_monthly_pay(rate, frequency):
    # Implementation here

def calculate_annual_pay(rate, frequency):
    # Implementation here

def calculate_next_pay_date(last_pay_date, frequency):
    # Implementation here

def update_pay_dates(account_id, previous_date, current_date, next_date):
    # Implementation here

def calculate_biweekly_expenses(account_id):
    # Implementation here

def calculate_monthly_expenses(account_id):
    # Implementation here

def calculate_yearly_expenses(account_id):
    # Implementation here

def calculate_next_expense_date(last_expense_date, frequency):
    # Implementation here

def update_expense_dates(account_id, previous_date, current_date, next_date):
    # Implementation here

def sort_transactions(field):
    # Implementation here


def main():
    database = r"money.db"

    # create a database connection
    conn = create_connection()

    if conn is not None:
        # create tables
        try:
            accounts.create_table(conn)
            transactions.create_table(conn)
            expenses.create_table(conn)
            income.create_table(conn)
        except Exception as e:
            print("Error while creating tables:", e)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
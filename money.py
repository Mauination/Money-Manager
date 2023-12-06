import sqlite3
from util import accounts, transactions, expenses, income
import datetime

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
    if frequency == "weekly":
        return rate * 4  # Approximate a month as 4 weeks
    elif frequency == "biweekly":
        return rate * 2  # Two biweekly periods in a month
    elif frequency == "monthly":
        return rate  # Already a monthly rate
    elif frequency == "yearly":
        return rate / 12  # Divide the yearly rate by 12 to get the monthly rate
    else:
        raise ValueError("Invalid frequency. Expected 'weekly', 'biweekly', 'monthly', or 'yearly'.")
    
def calculate_annual_pay(rate, frequency):
    if frequency == "weekly":
        return rate * 52  # There are 52 weeks in a year
    elif frequency == "biweekly":
        return rate * 26  # There are 26 biweekly periods in a year
    elif frequency == "monthly":
        return rate * 12  # There are 12 months in a year
    elif frequency == "yearly":
        return rate  # Already a yearly rate
    else:
        raise ValueError("Invalid frequency. Expected 'weekly', 'biweekly', 'monthly', or 'yearly'.")

def calculate_next_pay_date(last_pay_date, frequency):
    if frequency == "weekly":
        return last_pay_date + datetime.timedelta(weeks=1)
    elif frequency == "biweekly":
        return last_pay_date + datetime.timedelta(weeks=2)
    elif frequency == "monthly":
        return last_pay_date + datetime.timedelta(days=30)  # Approximate a month as 30 days
    else:
        raise ValueError("Invalid frequency. Expected 'weekly', 'biweekly', or 'monthly'.")

def update_pay_dates(conn, account_id, previous_date, current_date, next_date):
    sql = ''' UPDATE accounts
              SET previous_pay_date = ?,
                  current_pay_date = ?,
                  next_pay_date = ?
              WHERE account_id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (previous_date, current_date, next_date, account_id))
    conn.commit()

def calculate_biweekly_expenses(conn):
    cur = conn.cursor()
    cur.execute("SELECT SUM(amount) FROM expenses")
    return cur.fetchone()[0] or 0  # Return the sum or 0 if the sum is None

def calculate_monthly_expenses(conn):
    cur = conn.cursor()
    cur.execute("SELECT SUM(amount) FROM expenses")
    return cur.fetchone()[0] or 0  # Return the sum or 0 if the sum is None

def calculate_yearly_expenses(conn):
    cur = conn.cursor()
    cur.execute("SELECT SUM(amount) FROM expenses")
    return cur.fetchone()[0] or 0  # Return the sum or 0 if the sum is None

def calculate_next_expense_date(last_expense_date, frequency):
    if frequency == "weekly":
        return last_expense_date + datetime.timedelta(weeks=1)
    elif frequency == "biweekly":
        return last_expense_date + datetime.timedelta(weeks=2)
    elif frequency == "monthly":
        return last_expense_date + datetime.timedelta(days=30)  # Approximate a month as 30 days
    else:
        raise ValueError("Invalid frequency. Expected 'weekly', 'biweekly', or 'monthly'.")

def update_expense_dates(conn, account_id, previous_date, current_date, next_date):
    sql = ''' UPDATE expenses
              SET previous_date = ?,
                  current_date = ?,
                  next_date = ?
              WHERE account_id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (previous_date, current_date, next_date, account_id))
    conn.commit()

def sort_transactions(conn, field):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM transactions ORDER BY {field}")
    return cur.fetchall()

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
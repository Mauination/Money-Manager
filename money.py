# needs to import files from util/ (account.py, transaction.py, expense.py, income.py)
# needs to create general functions to do math with the various data and functions from the files in util/ (e.g. get total balance, get total expenses, get total income, etc.)
# needs to create a main function that will run the program
# needs a search function related to each of the given database tables (e.g. search for a specific account, search for a specific transaction, etc.)(accounts table, transactions table, expenses table, income table in the money.db)
# needs to connect functionality of all the files in util/ to the main function
# this should all be backend data processing and manipulation front end will be done in a separate file (e.g. run.py)
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
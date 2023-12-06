import sqlite3

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('money.db') # creates a database in memory
        return conn
    except sqlite3.Error as e:
        print(e)

def create_table(conn):
    try:
        sql = '''CREATE TABLE IF NOT EXISTS expenses(
                    id INTEGER PRIMARY KEY,
                    expense_name TEXT NOT NULL,
                    account TEXT,
                    amount REAL,
                    frequency TEXT,
                    paid_status TEXT,
                    previous_payment TEXT,
                    next_payment TEXT,
                    current_payment TEXT
                );'''
        c = conn.cursor()
        c.execute(sql)
    except sqlite3.Error as e:
        print(e)

def add_expense(conn, expense):
    sql = '''INSERT INTO expenses(expense_name, account, amount, frequency, paid_status, previous_payment, next_payment, current_payment) VALUES(?,?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, expense)
    return cur.lastrowid

def edit_expense(conn, expense):
    sql = '''UPDATE expenses SET expense_name = ?, account = ?, amount = ?, frequency = ?, paid_status = ?, previous_payment = ?, next_payment = ?, current_payment = ? WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, expense)
    return cur.rowcount

def delete_expense(conn, id):
    sql = 'DELETE FROM expenses WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    return cur.rowcount

def main():
    # create a database connection
    conn = create_connection()

    if conn is not None:
        # create expenses table
        create_table(conn)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
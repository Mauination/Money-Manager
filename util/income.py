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
        sql = '''CREATE TABLE IF NOT EXISTS income(
                    id INTEGER PRIMARY KEY,
                    income_name TEXT NOT NULL,
                    account TEXT,
                    amount REAL,
                    frequency TEXT,
                    previous_payment TEXT,
                    next_payment TEXT,
                    current_payment TEXT
                );'''
        c = conn.cursor()
        c.execute(sql)
    except sqlite3.Error as e:
        print(e)

def add_income(conn, income):
    sql = '''INSERT INTO income(income_name, account, amount, frequency, previous_payment, next_payment, current_payment) VALUES(?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, income)
    return cur.lastrowid

def edit_income(conn, income):
    sql = '''UPDATE income SET income_name = ?, account = ?, amount = ?, frequency = ?, previous_payment = ?, next_payment = ?, current_payment = ? WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, income)
    return cur.rowcount

def delete_income(conn, id):
    sql = 'DELETE FROM income WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    return cur.rowcount

def main():
    database = r"money.db"

    # create a database connection
    conn = create_connection()

    if conn is not None:
        # create income table
        create_table(conn)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
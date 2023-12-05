import sqlite3

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('money.db') # creates a database in memory
        return conn
    except sqlite3.Error as e:
        print(e)

def create_table(conn):
    try:
        sql = '''CREATE TABLE IF NOT EXISTS transactions(
                    id INTEGER PRIMARY KEY,
                    transaction_name TEXT NOT NULL,
                    account TEXT,
                    amount REAL,
                    category TEXT,
                    tag TEXT,
                    date TEXT,
                    notes TEXT
                );'''
        c = conn.cursor()
        c.execute(sql)
    except sqlite3.Error as e:
        print(e)

def add_transaction(conn, transaction):
    sql = '''INSERT INTO transactions(transaction_name, account, amount, category, tag, date, notes) VALUES(?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, transaction)
    return cur.lastrowid

def edit_transaction(conn, transaction):
    sql = '''UPDATE transactions SET transaction_name = ?, account = ?, amount = ?, category = ?, tag = ?, date = ?, notes = ? WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, transaction)
    return cur.rowcount

def delete_transaction(conn, id):
    sql = 'DELETE FROM transactions WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    return cur.rowcount

def main():
    database = r"money.db"

    # create a database connection
    conn = create_connection()

    if conn is not None:
        # create transactions table
        create_table(conn)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
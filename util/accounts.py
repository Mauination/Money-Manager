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
        sql = '''CREATE TABLE IF NOT EXISTS accounts(
                    id INTEGER PRIMARY KEY,
                    account_name TEXT NOT NULL,
                    account_type TEXT,
                    account_id TEXT UNIQUE,
                    card_id TEXT,
                    account_balance REAL,
                    account_fee REAL,
                    fee_frequency TEXT,
                    account_status TEXT
                );'''
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def add_account(conn, account):
    sql = '''INSERT INTO accounts(account_name, account_type, account_id, card_id, account_balance, account_fee, fee_frequency, account_status) VALUES(?,?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, account)
    conn.commit()
    return cur.lastrowid

def edit_account(conn, account):
    sql = '''UPDATE accounts SET account_name = ?, account_type = ?, account_id = ?, card_id = ?, account_balance = ?, account_fee = ?, fee_frequency = ?, account_status = ? WHERE account_name = ?'''
    cur = conn.cursor()
    cur.execute(sql, account)
    conn.commit()
    return cur.rowcount

def delete_account(conn, account):
    sql = 'DELETE FROM accounts WHERE account_name=?'
    cur = conn.cursor()
    cur.execute(sql, (account,))
    conn.commit()
    return cur.rowcount

def main():

    # create a database connection
    conn = create_connection()

    if conn is not None:
        # create accounts table
        create_table(conn)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
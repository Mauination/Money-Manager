# make a file for displaying and interacting with everything in money.py and the various accounts, transactions, expenses, and income.pyimport money
from util import accounts, transactions, expenses, income
import money 

def display_menu():
    print("1. View total balance")
    print("2. View total expenses")
    print("3. View total income")
    print("4. Search")
    print("5. Manage")
    print("6. Exit")

def display_search_menu():
    print("1. Search accounts")
    print("2. Search transactions")
    print("3. Search expenses")
    print("4. Search income")
    print("5. Search all")
    print("6. Back to main menu")

def display_manage_menu():
    print("1. Manage accounts")
    print("2. Manage transactions")
    print("3. Manage expenses")
    print("4. Manage income")
    print("5. Back to main menu")

def manage_accounts(conn):
    print("1. Add account")
    print("2. Edit account")
    print("3. Remove account")
    print("4. Back to manage menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        account_name = input("Enter account name: ")
        account_type = input("Enter account type: ")
        account_id = input("Enter account id: ")
        card_id = input("Enter card id: ")
        account_balance = input("Enter account balance: ")
        account_fee = input("Enter account fee: ")
        fee_frequency = input("Enter fee frequency: ")
        account_status = input("Enter account status: ")
        account = (account_name, account_type, account_id, card_id, account_balance, account_fee, fee_frequency, account_status)
        accounts.add_account(conn, account)
        print("Account added successfully!")
        input("Press enter to continue...")
    elif choice == "2":
        account_name = input("Enter account name: ")
        accounts.edit_account(conn, account_name)
    elif choice == "3":
        account_name = input("Enter account name: ")
        accounts.delete_account(conn, account_name)
    elif choice == "4":
        return
    else:
        print("Invalid choice. Please try again.")

def manage_transactions(conn):
    print("1. Add transaction")
    print("2. Edit transaction")
    print("3. Remove transaction")
    print("4. Back to manage menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        transactions.add_transaction(conn)
    elif choice == "2":
        transactions.edit_transaction(conn)
    elif choice == "3":
        transactions.delete_transaction(conn)
    elif choice == "4":
        return
    else:
        print("Invalid choice. Please try again.")

def manage_income(conn):
    print("1. Add income")
    print("2. Edit income")
    print("3. Remove income")
    print("4. Back to manage menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        income.add_income(conn)
    elif choice == "2":
        income.edit_income(conn)
    elif choice == "3":
        income.delete_income(conn)
    elif choice == "4":
        return
    else:
        print("Invalid choice. Please try again.")

def manage_expenses(conn):
    print("1. Add expenses")
    print("2. Edit expenses")
    print("3. Remove expenses")
    print("4. Back to manage menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        expenses.add_expense(conn)
    elif choice == "2":
        expenses.edit_expense(conn)
    elif choice == "3":
        expenses.delete_expense(conn)
    elif choice == "4":
        return
    else:
        print("Invalid choice. Please try again.")

def handle_manage(conn):
    while True:
        display_manage_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            manage_accounts(conn)
        elif choice == "2":
            manage_transactions(conn)
        elif choice == "3":
            manage_expenses(conn)
        elif choice == "4":
            manage_income(conn)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def handle_search_all(conn):
    print("All accounts:", money.search_all_accounts(conn))
    print("All transactions:", money.search_all_transactions(conn))
    print("All expenses:", money.search_all_expenses(conn))
    print("All income:", money.search_all_income(conn))

def handle_search(conn):
    while True:
        display_search_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            account_name = input("Enter account name: ")
            print("Account details:", money.search_accounts(conn, (account_name,)))
        elif choice == "2":
            transaction_name = input("Enter transaction name: ")
            print("Transaction details:", money.search_transaction(conn, transaction_name))
        elif choice == "3":
            expense_name = input("Enter expense name: ")
            print("Expense details:", money.search_expense(conn, expense_name))
        elif choice == "4":
            income_name = input("Enter income name: ")
            print("Income details:", money.search_income(conn, income_name))
        elif choice == "5":
            handle_search_all(conn)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        conn = money.create_connection()
        if choice == "1":
            print("Total balance:", money.get_total_balance(conn))
        elif choice == "2":
            print("Total expenses:", money.get_total_expenses(conn))
        elif choice == "3":
            print("Total income:", money.get_total_income(conn))
        elif choice == "4":
            handle_search(conn)
        elif choice == "5":
            handle_manage(conn)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
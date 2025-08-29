from lib.db.database import get_session
from lib.db.services.author_service import add_author, list_authors, delete_author
from lib.db.services.book_service import add_book, list_books, delete_book
from lib.db.services.member_service import add_member, list_members, delete_member
from lib.db.services.loan_service import borrow_book, return_book, list_overdue_loans, list_loans

def validate_choice(prompt, valid_options):
    choice = input(prompt).strip()
    while choice not in valid_options:
        print("Invalid option. Try again.")
        choice = input(prompt).strip()
    return choice

def get_int(prompt):
    while True:
        raw = input(prompt).strip()
        if raw.isdigit():
            return int(raw)
        print("Please enter a valid number.")

def manage_authors(session):
    options = {"1":"Add Author", "2":"List Authors", "3":"Delete Author", "4":"Back"}
    while True:
        print("\n-- Manage Authors --")
        for k,v in options.items():
            print(f"{k}. {v}")
        c = validate_choice("Choose: ", options.keys())
        if c == "1":
            name = input("Author name: ").strip()
            if not name:
                print("Name cannot be empty."); continue
            a = add_author(session, name)
            print(f"Added author #{a.id}: {a.name}")
        elif c == "2":
            authors = list_authors(session)
            if not authors:
                print("No authors."); continue
            for (aid, nm) in authors:
                print(f"[{aid}] {nm}")
        elif c == "3":
            aid = get_int("Author ID to delete: ")
            ok = delete_author(session, aid)
            print("Deleted." if ok else "Author not found.")
        else:
            break

def manage_books(session):
    options = {"1":"Add Book", "2":"List Books", "3":"Delete Book", "4":"Back"}
    while True:
        print("\n-- Manage Books --")
        for k,v in options.items():
            print(f"{k}. {v}")
        c = validate_choice("Choose: ", options.keys())
        if c == "1":
            title = input("Title: ").strip()
            year = get_int("Year (e.g. 2020): ")
            author_id = get_int("Author ID: ")
            try:
                b = add_book(session, title, year, author_id)
                print(f"Added book #{b.id}: {b.title} ({b.year})")
            except ValueError as e:
                print(f"Error: {e}")
        elif c == "2":
            books = list_books(session)
            if not books:
                print("No books."); continue
            for (bid, title, year, aname) in books:
                print(f"[{bid}] {title} ({year}) by {aname}")
        elif c == "3":
            bid = get_int("Book ID to delete: ")
            ok = delete_book(session, bid)
            print("Deleted." if ok else "Book not found.")
        else:
            break

def manage_members(session):
    options = {"1":"Add Member", "2":"List Members", "3":"Delete Member", "4":"Back"}
    while True:
        print("\n-- Manage Members --")
        for k,v in options.items():
            print(f"{k}. {v}")
        c = validate_choice("Choose: ", options.keys())
        if c == "1":
            name = input("Member name: ").strip()
            if not name:
                print("Name cannot be empty."); continue
            m = add_member(session, name)
            print(f"Added member #{m.id}: {m.name}")
        elif c == "2":
            members = list_members(session)
            if not members:
                print("No members."); continue
            for (mid, nm) in members:
                print(f"[{mid}] {nm}")
        elif c == "3":
            mid = get_int("Member ID to delete: ")
            ok = delete_member(session, mid)
            print("Deleted." if ok else "Member not found.")
        else:
            break

def manage_loans(session):
    options = {"1":"Borrow Book", "2":"Return Book", "3":"List Loans", "4":"View Overdue Loans", "5":"Back"}
    while True:
        print("\n-- Loans --")
        for k,v in options.items():
            print(f"{k}. {v}")
        c = validate_choice("Choose: ", options.keys())
        if c == "1":
            member_id = get_int("Member ID: ")
            book_id = get_int("Book ID: ")
            try:
                loan = borrow_book(session, member_id, book_id)
                print(f"Loan #{loan.id} created. Due on {loan.due_date}.")
            except ValueError as e:
                print(f"Error: {e}")
        elif c == "2":
            loan_id = get_int("Loan ID to return: ")
            ok = return_book(session, loan_id)
            print("Returned." if ok else "Loan not found.")
        elif c == "3":
            for (lid, mname, btitle, due, ret) in list_loans(session):
                status = "Returned" if ret else "Borrowed"
                print(f"[{lid}] {btitle} to {mname} | Due {due} | {status}")
        elif c == "4":
            overdue = list_overdue_loans(session)
            if not overdue:
                print("No overdue loans.")
            else:
                for (lid, mname, btitle, due) in overdue:
                    print(f"[{lid}] {btitle} to {mname} | DUE {due}")
        else:
            break

def run_app():
    session = get_session()
    options = {
        "1": ("Manage Authors", manage_authors),
        "2": ("Manage Books", manage_books),
        "3": ("Manage Members", manage_members),
        "4": ("Borrow/Return/View Loans", manage_loans),
        "7": ("Exit", None),
    }
    while True:
        print("\nLibrary Management System ===")
        print("1. Manage Authors")
        print("2. Manage Books")
        print("3. Manage Members")
        print("4. Borrow Book / Return Book / View Loans")
        print("7. Exit")
        choice = validate_choice("Select an option: ", options.keys())
        if choice == "7":
            print("Goodbye!"); break
        _, action = options[choice]
        action(session)

if __name__ == '__main__':
    run_app()
from lib.db.database import get_session
from lib.db.models import Author, Book, Member, Loan
from datetime import date

def manage_authors(session):
    while True:
        print("\n--- Manage Authors ---")
        print("1. Add Author")
        print("2. List Authors")
        print("3. Delete Author")
        print("4. Back")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter author name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            author = Author(name=name)
            session.add(author)
            session.commit()
            print("Author added.")

        elif choice == "2":
            authors = session.query(Author).all()
            for a in authors:
                print(a)

        elif choice == "3":
            id = input("Enter author ID to delete: ")
            author = session.query(Author).get(id)
            if author:
                session.delete(author)
                session.commit()
                print("Author deleted.")
            else:
                print("Author not found.")

        elif choice == "4":
            break

def manage_books(session):
    while True:
        print("\n--- Manage Books ---")
        print("1. Add Book")
        print("2. List Books")
        print("3. Delete Book")
        print("4. Back")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter book title: ").strip()
            year = input("Enter publication year: ")
            author_id = input("Enter author ID: ")
            if not title or not year.isdigit():
                print("Invalid input.")
                continue
            book = Book(title=title, year=int(year), author_id=int(author_id))
            session.add(book)
            session.commit()
            print("Book added.")

        elif choice == "2":
            books = session.query(Book).all()
            for b in books:
                print(b)

        elif choice == "3":
            id = input("Enter book ID to delete: ")
            book = session.query(Book).get(id)
            if book:
                session.delete(book)
                session.commit()
                print("Book deleted.")
            else:
                print("Book not found.")

        elif choice == "4":
            break

def manage_members(session):
    while True:
        print("\n--- Manage Members ---")
        print("1. Add Member")
        print("2. List Members")
        print("3. Delete Member")
        print("4. Back")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter member name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            member = Member(name=name)
            session.add(member)
            session.commit()
            print("Member added.")

        elif choice == "2":
            members = session.query(Member).all()
            for m in members:
                print(m)

        elif choice == "3":
            id = input("Enter member ID to delete: ")
            member = session.query(Member).get(id)
            if member:
                session.delete(member)
                session.commit()
                print("Member deleted.")
            else:
                print("Member not found.")

        elif choice == "4":
            break

def borrow_book(session):
    member_id = input("Enter member ID: ")
    book_id = input("Enter book ID: ")

    member = session.query(Member).get(member_id)
    book = session.query(Book).get(book_id)

    if not member or not book:
        print("Invalid member or book.")
        return

    loan = Loan(member_id=member.id, book_id=book.id)
    session.add(loan)
    session.commit()
    print(f"{member.name} borrowed '{book.title}'.")

def return_book(session):
    loan_id = input("Enter loan ID: ")
    loan = session.query(Loan).get(loan_id)

    if not loan:
        print("Loan not found.")
        return

    loan.returned = True
    session.commit()
    print(f"Book '{loan.book.title}' returned by {loan.member.name}.")

def view_overdue(session):
    overdue = session.query(Loan).filter(
        Loan.returned == False,
        Loan.due_date < date.today()
    ).all()

    if not overdue:
        print("No overdue books.")
    else:
        for loan in overdue:
            print(f"Book '{loan.book.title}' borrowed by {loan.member.name} is overdue since {loan.due_date}.")

def run_app():
    # init_db()
    session = get_session()

    while True:
        print("\n=== Library Management System ===")
        print("1. Manage Authors")
        print("2. Manage Books")
        print("3. Manage Members")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. View Overdue Loans")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            manage_authors(session)
        elif choice == "2":
            manage_books(session)
        elif choice == "3":
            manage_members(session)
        elif choice == "4":
            borrow_book(session)
        elif choice == "5":
            return_book(session)
        elif choice == "6":
            view_overdue(session)
        elif choice == "7":
            print("Goodbye!")
            break

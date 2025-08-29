from faker import Faker
import random
from datetime import timedelta, date


from lib.db.database import get_session
from lib.db.models import Author, Book, Member, Loan

faker = Faker()
session = get_session()


def seed_authors(n=5):
    for _ in range(n):
        author = Author(
            name=faker.name()
        )
        session.add(author)
    session.commit()
    print(f"{n} authors added!")

def seed_books(n=15):
    author_ids = [author.id for author in session.query(Author).all()]
    for _ in range(n):
        book = Book(
            title=faker.sentence(nb_words=3),
            year=int(faker.year()),
            author_id=random.choice(author_ids)
        )
        session.add(book)
    session.commit()
    print(f"{n} books added!")


def seed_members(n=10):
    for _ in range(n):
        member = Member(
            name=faker.name()
        )
        session.add(member)
    session.commit()
    print(f"{n} members added!")


def seed_loans(n=20):
    book_ids = [book.id for book in session.query(Book).all()]
    member_ids = [member.id for member in session.query(Member).all()]

    for _ in range(n):
        borrow_date = faker.date_this_year()
        due_date = borrow_date + timedelta(days=14)

        loan = Loan(
            member_id=random.choice(member_ids),
            book_id=random.choice(book_ids),
            due_date=due_date,
            returned=random.choice([True, False]) 
        )
        session.add(loan)
    session.commit()
    print(f"{n} loans added!")


if __name__ == "__main__":
    seed_authors(5)
    seed_books(15)
    seed_members(10)
    seed_loans(20)
    print("Database seeded with authors, books, members, and loans!")

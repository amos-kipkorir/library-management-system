from faker import Faker
import random
from datetime import timedelta, date
from lib.db.database import get_session, Base, engine
from lib.db.models import Author, Book, Member, Loan

faker = Faker()
session = get_session()

def seed_authors(n=8):
    for _ in range(n):
        session.add(Author(name=faker.name()))
    session.commit()

def seed_books(n=20):
    author_ids = [a.id for a in session.query(Author).all()]
    for _ in range(n):
        session.add(Book(title=faker.sentence(nb_words=3), year=int(faker.year()), author_id=random.choice(author_ids)))
    session.commit()

def seed_members(n=12):
    for _ in range(n):
        session.add(Member(name=faker.name()))
    session.commit()

def seed_loans(n=25):
    book_ids = [b.id for b in session.query(Book).all()]
    member_ids = [m.id for m in session.query(Member).all()]
    for _ in range(n):
        loan = Loan(member_id=random.choice(member_ids), book_id=random.choice(book_ids))
        # 50% overdue & not returned to test overdue view
        if random.random() < 0.5:
            loan.due_date = date.today() - timedelta(days=random.randint(1, 20))
            loan.returned = False
        else:
            loan.returned = random.random() < 0.6
        session.add(loan)
    session.commit()

def create_db_and_seed():
    Base.metadata.create_all(bind=engine)
    seed_authors()
    seed_members()
    seed_books()
    seed_loans()
    print("Seeding complete.")

if __name__ == '__main__':
    create_db_and_seed()
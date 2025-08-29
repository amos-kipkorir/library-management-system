from typing import List, Tuple
from sqlalchemy.orm import Session
from lib.db.models import Book, Author

def add_book(session: Session, title: str, year: int, author_id: int) -> Book:
    if not session.get(Author, author_id):
        raise ValueError("Author does not exist.")
    book = Book(title=title.strip(), year=int(year), author_id=author_id)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

def list_books(session: Session) -> List[Tuple[int, str, int, str]]:
    rows = (
        session.query(Book)
        .join(Author)
        .with_entities(Book.id, Book.title, Book.year, Author.name)
        .order_by(Book.title)
        .all()
    )
    return [(id, title, year, author_name) for (id, title, year, author_name) in rows]

def delete_book(session: Session, book_id: int) -> bool:
    book = session.get(Book, book_id)
    if not book:
        return False
    session.delete(book)
    session.commit()
    return True
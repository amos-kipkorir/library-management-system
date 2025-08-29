from typing import List, Tuple
from sqlalchemy.orm import Session
from lib.db.models import Author

def add_author(session: Session, name: str) -> Author:
    author = Author(name=name.strip())
    session.add(author)
    session.commit()
    session.refresh(author)
    return author

def list_authors(session: Session) -> List[Tuple[int, str]]:
    return [(a.id, a.name) for a in session.query(Author).order_by(Author.name).all()]

def delete_author(session: Session, author_id: int) -> bool:
    author = session.get(Author, author_id)
    if not author:
        return False
    session.delete(author)
    session.commit()
    return True
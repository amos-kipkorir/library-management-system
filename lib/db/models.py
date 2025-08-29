from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from datetime import date, timedelta
from lib.db.database import Base

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}')>"

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)

    author = relationship("Author", back_populates="books")
    loans = relationship("Loan", back_populates="book", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', year={self.year})>"

class Member(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    loans = relationship("Loan", back_populates="member", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Member(id={self.id}, name='{self.name}')>"

class Loan(Base):
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey("members.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    due_date = Column(Date, default=lambda: date.today() + timedelta(days=14))
    returned = Column(Boolean, default=False)

    member = relationship("Member", back_populates="loans")
    book = relationship("Book", back_populates="loans")

    def __repr__(self):
        return f"<Loan(id={self.id}, member_id={self.member_id}, book_id={self.book_id}, due_date={self.due_date}, returned={self.returned})>"

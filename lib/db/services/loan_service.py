from typing import List, Tuple
from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy import and_
from lib.db.models import Loan, Member, Book

def borrow_book(session: Session, member_id: int, book_id: int) -> Loan:
    if not session.get(Member, member_id):
        raise ValueError("Member does not exist.")
    if not session.get(Book, book_id):
        raise ValueError("Book does not exist.")
    loan = Loan(member_id=member_id, book_id=book_id)
    session.add(loan)
    session.commit()
    session.refresh(loan)
    return loan

def return_book(session: Session, loan_id: int) -> bool:
    loan = session.get(Loan, loan_id)
    if not loan:
        return False
    loan.returned = True
    session.commit()
    return True

def list_overdue_loans(session: Session) -> List[Tuple[int, str, str, str]]:
    rows = (
        session.query(Loan, Member, Book)
        .join(Member, Loan.member_id == Member.id)
        .join(Book, Loan.book_id == Book.id)
        .filter(and_(Loan.returned == False, Loan.due_date < date.today()))
        .with_entities(Loan.id, Member.name, Book.title, Loan.due_date)
        .order_by(Loan.due_date.asc())
        .all()
    )
    return [(lid, mname, btitle, due) for (lid, mname, btitle, due) in rows]

def list_loans(session: Session) -> List[Tuple[int, str, str, str, bool]]:
    rows = (
        session.query(Loan, Member, Book)
        .join(Member, Loan.member_id == Member.id)
        .join(Book, Loan.book_id == Book.id)
        .with_entities(Loan.id, Member.name, Book.title, Loan.due_date, Loan.returned)
        .order_by(Loan.id.desc())
        .all()
    )
    return [(lid, mname, btitle, due, ret) for (lid, mname, btitle, due, ret) in rows]
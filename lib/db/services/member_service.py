from typing import List, Tuple
from sqlalchemy.orm import Session
from lib.db.models import Member

def add_member(session: Session, name: str) -> Member:
    member = Member(name=name.strip())
    session.add(member)
    session.commit()
    session.refresh(member)
    return member

def list_members(session: Session) -> List[Tuple[int, str]]:
    return [(m.id, m.name) for m in session.query(Member).order_by(Member.name).all()]

def delete_member(session: Session, member_id: int) -> bool:
    member = session.get(Member, member_id)
    if not member:
        return False
    session.delete(member)
    session.commit()
    return True
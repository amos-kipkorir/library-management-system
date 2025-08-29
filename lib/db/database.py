from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base




engine = create_engine("sqlite:///library.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()





def get_session():
    return Session()

# db.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


class DB:
    def __init__(self) -> None:
        Base.metadata.create_all(engine)

    def insert_data(self):
        with Session() as session:
            # Clear existing data for demonstration purposes
            session.query(User).delete()
            session.add_all([
                User(name="Alice", email="alice@example.com"),
                User(name="Bob", email="bob@example.com"),
                User(name="Charlie", email="charlie@example.com")
            ])
            session.commit()

    def fetch_users(self):
        with Session() as session:
            return session.query(User).all()

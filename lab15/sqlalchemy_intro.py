from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, or_
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, Date, DateTime
from sqlalchemy.orm import sessionmaker

# Declare a base using declarative_base
Base = declarative_base()

# Create an engine
engine = create_engine('sqlite:///python_course.db')
# Create a session
Session = sessionmaker(bind=engine)
session = Session()


# Define the User class inheriting from Base
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# Create the tables in the database
Base.metadata.create_all(engine)

def insert_data():
    data = [
        {"name": "Iv0", "age": 35},
        {"name": "Mario", "age": 12},
        {"name": "Asen", "age": 50}
    ]

    # Iterate over the list of dictionaries and add each record to the session
    for entry in data:
        new_user = User(name=entry['name'], age=entry['age'])
        session.add(new_user)

    # Commit the session to persist the changes
    session.commit()


def get_data():
    # Query all users
    # q = session.query(User).filter(User.age>=30).filter(User.name.like('I%'))
    q = session.query(User).filter( or_(User.age>=30, User.name.like('I%')))
    users = q.all()

    for user in users:
        print(f'{user.name}, {user.age}')

def update_name(old_name, new_name):
    user = session.query(User).filter_by(name=old_name).first()
    if user:
        print(user.name)
        user.name = new_name

    # Commit the session to persist the changes
    session.commit()

def delete_user(name):
    q = session.query(User).filter_by(name=name)
    if q:
        q.delete()

    session.commit()

if __name__ == "__main__":
    # insert_data()
    # update_name('new_name', 'Ivo')
    delete_user('Ivo')
    # get_data()

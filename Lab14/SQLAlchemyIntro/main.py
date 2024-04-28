from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Text


# Create an engine (connect to db + ...)
engine = create_engine('sqlite:///python_course.db')

# Declare a base using declarative_base
Base = declarative_base()

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Define the Employee class inheriting from Base
class Employee(Base):
    __tablename__ = 'employees2'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    position = Column(Text, nullable=False)
    office = Column(String, nullable=True)
    age = Column(Integer)
    start_date = Column(String, nullable=True)

    def __str__(self):
        return f'{self.name}, {self.position}, {self.age} '

def create_table():
    """ Create all tables"""
    # Create the tables in the database
    Base.metadata.create_all(engine)
    print('employees2 is created')

def insert_row():
    # Create a new user instance
    new_user = Employee()
    # Add the new user to the session
    session.add(new_user)
    # Commit the session to persist the changes
    session.commit()

def insert_many(rows):
    for row in rows:
        employee = Employee(
            **row
        )
        session.add(employee)
        session.commit()

def select_rows():
    rows = session.query(Employee).filter(
        Employee.age >=30, Employee.name.like('%an%')
    ).all()
    for row in rows:
        print(row)

if __name__ == "__main__":
    # create_table()
    # insert_data()

    rows = (
        {
            'name':'Ivan',
            'age':30,
            'office':'Sofia',
            'position':'Python Dev'
        },
        {
            'name':'Maria',
            'age':34,
            'office':'Sofia',
            'position':'JS Dev',
            'start_date':'2022-01-01'
        }
    )

    # insert_many(rows)
    select_rows()
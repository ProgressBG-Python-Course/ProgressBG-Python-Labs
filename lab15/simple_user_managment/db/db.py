from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base class for our class definitions
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'  # Define the table name

    # Define the columns of the table
    id = Column(Integer, primary_key=True)  # Primary key column
    name = Column(String, nullable=False)   # Name cannot be null
    age = Column(Integer, nullable=False)   # Age cannot be null

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"

class Database:
    def __init__(self, db_url='sqlite:///example.db'):
        """Initializes database connection and sessionmaker."""
        self.engine = create_engine(db_url)

        # Creates all tables defined in the Base subclass
        Base.metadata.create_all(self.engine)

        # Creates session to handle queries
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()


    def add_user(self, name, age):
        """Add a new user to the database."""
        new_user = User(name=name, age=age)
        # Add the new user to the session
        self.session.add(new_user)
        # Commit all pending transactions to the database
        self.session.commit()

    def get_users(self):
        """Retrieve all users from the database."""
        return self.session.query(User).all()

    def update_user(self, user_id, name, age):
        """Update a user's information in the database."""
        # Retrieve specific user by ID
        user = self.session.query(User).filter(User.id == user_id).one()
         # Update name and age
        user.name = name
        user.age = age
        # Commit all pending transactions to the database
        self.session.commit()

    def delete_user(self, user_id):
        """Delete a user from the database."""
        # Find the user to be deleted
        user = self.session.query(User).filter(User.id == user_id).one()
        # Delete the user from the session
        self.session.delete(user)
        # Commit all pending transactions to the database
        self.session.commit()

    def __del__(self):
        """Close the session when the object is deleted to free resources."""
        self.session.close()

# Example usage
if __name__ == "__main__":
    db = Database()

    # Add users to the database
    db.add_user('Ivan', 30)
    db.add_user('Maria', 25)

    # Print all users in the database
    print(db.get_users())

    # Update Ivan's details
    db.update_user(1, 'Ivan Petrov', 31)

    # Delete Maria from the database
    db.delete_user(2)

    print(db.get_users())
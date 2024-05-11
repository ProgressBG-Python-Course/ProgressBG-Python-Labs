from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Base

class Database:
    def __init__(self, db_url='sqlite:///example.db'):
        """Initializes database connection and sessionmaker."""
        # Create engine ties our app with SQLAlchemy ORM to a specific database. Echo set to True to log all SQL queries
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
        try:
            user = self.session.query(User).filter(User.id == user_id).one()
            # Delete the user from the session
            if user:
                self.session.delete(user)
            # Commit all pending transactions to the database
            self.session.commit()
        except:
            print('Ups, something went wrong!')


    def __del__(self):
        """Close the session when the object is deleted to free resources."""
        self.session.close()

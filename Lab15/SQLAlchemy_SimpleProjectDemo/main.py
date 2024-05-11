# Lab15/SQLAlchemy_SimpleProjectDemo/main.py
from db import Database


# Example usage
if __name__ == "__main__":
    db = Database()

    # # Add users to the database
    db.add_user('Ivan', 30)
    db.add_user('Maria', 25)

    # # Print all users in the database
    print(db.get_users())

    # # Update Ivan's details
    # db.update_user(1, 'Ivan Petrov', 31)

    # # Delete Maria from the database
    db.delete_user(2)

    # print(db.get_users())
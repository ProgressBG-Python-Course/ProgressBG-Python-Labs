# from db.db_sqlite import SQLiteDB
from db.db import Database

def input_user_data():
    """Get user data

    Returns:
        _type_: list of lists

        users = [
            ['Pier',  40 ],
            ['John', 25],
            ['Sara', 45],
            ['Mary', 30],
            ['Bob',  35 ],
        ]
    """
    users = []

    while True:
        name = input('Enter your name: ')
        age = int(input('Enter age'))

        users.append([name, age])

        user_choice = input('Enter more?[y/n]')
        if user_choice.lower()!='y':
            break

    print(users)
    return users


if __name__=="__main__":
    db = Database('sqlite:///python_course.db')


    # Add users to the database
    users = input_user_data()
    for user in users:
        db.add_user(*user)


from user import User
from privileges import Privileges


class Admin(User):
    """class inherited of user"""

    def __init__(self, first_name, last_name, username, age, email):
        super().__init__(first_name, last_name, username, age, email)
        self.privileges = Privileges()

from user import User
from privileges import Privileges
from admin import Admin

user = Admin('karla', 'raro', 'cdkarlaroaro', 34, 'cdkarlaroaro@gmail.com')
user.privileges.show_privileges()

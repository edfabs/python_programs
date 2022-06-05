from admin import Admin


my_admin_user = Admin('Fabian', 'suchett', 'edfabs',
                      33, 'fabian.suchett@edfabs.com')

my_admin_user.descriptive_user()
my_admin_user.privileges.show_privileges()

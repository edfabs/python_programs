from cgi import print_form
from http.client import PROXY_AUTHENTICATION_REQUIRED


rows = 5
columns = 9

for row in range(rows):
    for space in range((row)):
        print(" ", end=" ")
    for column in range(columns - (row)*2):           
        print("*",end=" ")           
    print("\r")
"""
Realize a function-decorator , which is checking an access according to USERNAME
All USERNAMEs are saved as global in the List USERS
If User is agree for authorisation - he should input his username (saved as global)
Funktion should use two decorators: one for checking of authorisation, second - for check of access
"""

USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yesno = input(""" Input Y if you want to authorisate yourself or iput N if you want to work as an anonyme User """)

auth = yesno == "Y"



def is_auth(func):
    def wrapper():
        if auth:
            print("User is authorised")
            func()
        else:
            print("User is not authorised. Function will not performed")
    return wrapper




if auth:
    username = input("Input your username:")


###:

def has_access(func):
    def wrapper():
        if username in USERS:
            print("Authorised as", username)
            func()
        else:
            print("Access for user", username, "don't allowed")
    return wrapper
    

@is_auth
@has_access
def from_db():
    print("some data from database")

from_db()




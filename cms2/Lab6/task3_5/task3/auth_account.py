"""Task3_lab6"""
from auth import *

authenticator = Authenticator()
authorizor = Authorizor(authenticator)

# add users
try:
    authenticator.add_user('user1', 'passw0rd')
    authenticator.add_user('user2', 'passw0rd')
    authenticator.add_user('user3', 'passw0rd')
    authenticator.add_user('user4', 'passw0rd')
except AuthException as e:
    print(e)

# check authorisation of user
print(authenticator.login('user1', 'passw0rd'))
print(authenticator.login('user2', 'passw0rd'))
print(authenticator.login('user3', 'passw0rd'))
print(authenticator.login('user4', 'passw0rd'))

# add posibilities to users
try:
    authorizor.add_permission('paint')
    authorizor.add_permission('draw')
    authorizor.permit_user('paint', 'user1')
    authorizor.permit_user('draw', 'user2')
    authorizor.permit_user('draw', 'user3')
except AuthException as e:
    print(e)

# check users posibilities
try:
    authorizor.check_permission('paint', 'user1')
    # authorizor.check_permission('draw', 'user1') #Error exeption \
    # "User 'user1' does not have permission 'draw'"
    # authorizor.check_permission('paint', 'user2') #Error exeption  (User does not have permission)
    authorizor.check_permission('draw', 'user2')
    # authorizor.check_permission('paint', 'user3') #Error exeption  (User does not have permission)
    authorizor.check_permission('draw', 'user3')
    # authorizor.check_permission('paint', 'user4')#Error exeption   (User does not have permission)
    # authorizor.check_permission('draw', 'user4')#Error exeption    (User does not have permission)
except AuthException as e:
    print(e)

from models.user import UserModel

### commenting the below code because we are now working with data.db database (sqlite)
# users = [
#     User(1, 'vaibhav', 'asd'),
#     User(2, 'saurabh', 'asd')
# ]
#
#
# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}


# the below two functions will be user to authenticate and identify the user
# authenticate user
def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user


# identity function - takes payload (content of jwt token) - we are going to extract user id from payload
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)


auth_users = {}

def signup(username, password):
    if username in auth_users:
        return False
    auth_users[username] = password
    return True

def login(username, password):
    return auth_users.get(username) == password

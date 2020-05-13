"""存储用户数据"""

import json


def get_stored_username():
    file_name = 'username.json'
    try:
        with open(file_name, 'r') as file_obj:
            username = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input('what is your name?')
    file_name = 'username.json'
    with open(file_name,'w') as file_obj:
        json.dump(username, file_obj)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print('welcome back, ' + username)
    else:
        username = get_new_username()
        print('we will remenber you when you come back, ' + username + '!')


greet_user()

import pytest 
import subprocess

from hr import users 

password = '$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/'
user_dict = {
    'name':'kevin',
    'groups': ['wheel','dev'],
    'password': password
}

def test_users_add(mocker):
    """
    Given a user dictionary. 'user.add(...)' should
    create a user with the password and groups using 
    'useradd' linux command.
    """
    mocker.patch('subprocess.call')
    users.add(user_dict)
    subprocess.call.assert_called_with([
        'useradd',
        '-p',
        password,
        '-G',
        'wheel,dev',
        'kevin',
    ])

def test_users_remove(mocker): 
    """
    Given a user dictionary. 'user.remove(...)' should
    remove a user from the system using the 'userdel' linux command.
    """
    mocker.patch('subprocess.call')
    users.remove(user_dict)
    subprocess.call.assert_called_with([
        'userdel',
        '-r',
        'kevin',
    ])

def test_users_update(mocker):
    """
    Given a user dictionary. 'user.update(...)' should 
    update a user on the system using the 'usermod' linux command.
    """
    mocker.patch('subprocess.call')
    users.update(user_dict)
    subprocess.call.assert_called_with([
        'usermod',
        '-p',
        password,
        '-G',
        'wheel,dev',
        'kevin',
    ])

def test_users_sync(mocker):
    """
    Given a list of user dictionaries, 'users.sync(...)' should
    create missing users, remove extra non-system users, and update 
    existing users. A list of existing usernames can be passed in or default users
    will be used.
    """
    existing_user_names = ['kevin', 'bob']
    users_info = [
        user_dict, 
        {
            'name': 'john',
            'groups': ['wheel'],
            'password': password
        }
    ] 
    mocker.patch('subprocess.call')
    users.sync(user_info, existing_user_names) 

    subprocess.call.assert_has_calls([
        moker.call([
            'usermod',
            '-p', 
            password,
            '-G'
            'wheel,dev',
            'kevin',
        ]),
        mocker.call([
            'useradd',
            '-p',
            password,
            '-G',
            'wheel',
            'john',
        ]),
        mocker.call([
            'userdel',
            '-r',
            'bob',
        ]),
    ])
import pwd
import subprocess
import sys

def add(user_info):
    try:
        print(f"Adding user: {user_info['name']}")
        subprocess.run([
            "useradd",
            "-p", 
            user_info['password'],
            "-G",
            user_info['groups'],
            #_groups_str(user_info),
            user_info['name'],
        ])
    except: 
        print(f"Unable to add the user: {user_name['name']} to the system.")
        sys.exit(1)

def remove(user_info):
    try: 
        print(f"Removing user: {user_info['name']}")
        subprocess.run([
            "userdel",
            "-r",
            user_info['name',]
        ])
    except:
        print(f"Unable to remove the user: {user_name['name']} from the system.")
        sys.exit(1)

def update(user_info): 
    try: 
        print(f"Updating user: {user_info['name']}")
        subprocess.run([
            "usermod",
            "-p", 
            user_info['password'], 
            '-G',
            user_info['groups'], 
            #_groups_str(user_info),
            user_info['name'],
        ])
    except: 
        print(f"Unable to update the user: {user_info['name']}")
        sys.exit(1)

def sync(users, existing_user_names=None):
    existing_user_names = (existing_user_names or _user_names())
    user_names = [user['name'] for user in users]
    for user in users:
        if user['name'] not in existing_user_names: 
            add(user)
        elif user['name'] in existing_user_names:
            update(user)
    for user_name in existing_user_names: 
        if not user_name in user_names:
            remove({'name': user_name})


def _user_names():
    return [user.pw_name for user in pwd.getpwall()
            if user.pw_uid >= 1000 and 'home' in user.pw_dir]
#def _groups_str(user_info):
#    return ','.join(user_info['groups'] or [])
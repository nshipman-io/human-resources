import json
import grp 
import pwd
import spwd 
import sys

def load(inventory): 
    try: 
        print(f"Loading Inventory file: {inventory}")
        inventory = open(inventory)
        users = json.load(inventory)
    except ValueError: 
        print(f"Error loading '{inventory}'. File must be in JSON format.")
        sys.exit(1)
    else:
        return users 

def export(inventory): 
    users = []
    for p in pwd.getpwall():
        if p.pw_uid > 1000:
            name = p.pw_name
            groups = grp.getgrgid(p.pw_gid)[0]
            password = spwd.getspnam(name)[1]
            user = {
                "name": name,
                "groups": groups,
                "password": password
            }
            users.append(user)
    with open(inventory,'w',encoding='utf-8') as f:
        json.dump(users, f)
    print(f"System state exported to: {inventory}")
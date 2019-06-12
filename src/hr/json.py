import json
import grp 
import pwd
import spwd 
import sys

def load_inventory(inventory): 
    try: 
        print(f"Loading Inventory file: {inventory}")
        users = json.load(inventory)
    except ValueError: 
        print(f"Error loading '{inventory}'. File must be in JSON format.")
        sys.exit(1)
    else:
        return users 

def export_inventory(): 
    users = []
    for p in pwd.getpwall():
        if p.pw_uid > 1000:
            name = p.pw_name
            groups = grp.getgrgid(p.pw_gid)
            password = spwd.getspnam(name).sp_pwdp
            user = {
                "name": name,
                "groups": groups,
                "password": password
            }
            users.append(user)
    print(users)

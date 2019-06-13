import argparse

def create_parser(): 

    parser = argparse.ArgumentParser(description='Takes in path to inventory json file.')
    parser.add_argument('inventory', help='Path to the inventory json file')
    parser.add_argument('--export','-e',
            help='Exports json data to specified location. Default value is False',
            action='store_true'
            )
    return parser 

def main():
    from hr import inventory, users

    args = create_parser().parse_args()
    
    if args.export:
        print(f"Creating system state inventory file to {args.inventory}")
        inventory.export(args.inventory)
    else:
        print(f"Syncing system to desired state using: {args.inventory}")
        users_data = inventory.load(args.inventory)
        users.sync(users_data)

import argparse

def create_parser(): 

    parser = argparse.ArgumentParser(description='Takes in path to inventory json file.')
    parser.add_argument('inventory', help='Path to the inventory json file')
    parser.add_argument('--export','-e',
            help='Exports json data to specified location. Default value is False',
            action='store_true'
            )
    return parser
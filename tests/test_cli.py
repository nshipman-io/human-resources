import pytest

from hr import cli

inventory = "/path/to/inv.json"

@pytest.fixture
def parser():
    return cli.create_parser()

def test_parser_without_inventory(parser): 
    """
    Parser will fail with no arguments passed
    """
    with pytest.raises(SystemExit):
        parser.parse_args([])

def test_parser_with_inventory(parser): 
    """
    Parser will not exit if inventory file is provided
    """
    args = parser.parse_args([inventory])

    assert args.inventory == '/path/to/inv.json'

def test_parser_with_export_flag(parser):
    """
    Parser will set export value to 'True' if export flag is given
    """
    args = parser.parse_args([inventory])
    assert args.export == False

    args = parser.parse_args([inventory,'--export'])
    assert args.export == True


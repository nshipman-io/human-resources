import pytest
import tempfile 

from hr import inventory

users = [
    {
        "name": "kevin",
        "groups": ["wheel","dev"], 
        "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
    },
    {
        "name": "lisa",
        "groups": ["wheel"],
        "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
    },
    {
        "name": "jim",
        "groups": [],
        "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
    }
] 

def test_load_inventory(): 
    """
    `inventory.load` takes a path to a file and parses it as JSON.
    """
    inv_file = tempfile.NamedTemporaryFile(delete=False)
    inv_file.write(b"""
    [
        {
            "name": "kevin",
            "groups": ["wheel","dev"], 
            "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
        },
        {
            "name": "lisa",
            "groups": ["wheel"],
            "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
        },
        {
            "name": "jim",
            "groups": [],
            "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
        }
    ]
    """) 
    inv_file.close()
    users_list = inventory.load(inv_file.name)
    assert users_list[0] == {
        "name": "kevin",
        "groups": ["wheel","dev"], 
        "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
    }
    assert users_list[1] == {
        "name": "lisa",
        "groups": ["wheel"],
        "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
    }
    assert users_list[2] == {
        "name": "jim",
        "groups": [],
        "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
    }

def test_inventory_dump(mocker): 
    """
    `inventory.dump` takes a destination oath and optional list of users to export then exports the existing user information.
    """
    #spwd.getspanm can't be used by non-root user normally.
    mocker.patch('spwd.getspnam', return_value=mocker.Mock(sp_pwd='password'))
    
    #grp.getgrall will return the values from th test machine. 
    # For consistency results will be mocked.
    mocker.patch('grp.getgrall', return_value=[
        mocker.Mock(gr_name='super', gr_mem=['bob']),
        mocker.Mock(gr_name='other', gr_mem=[]),
        mocker.Mock(gr_name='wheel', gr_mem=['bob', 'kevin']),
    ])

    inventory.dump(dest_file.name, ['kevin', 'bob'])

    with open(dest_filename.name) as f: 
        assert f.read() == """[{"name": "kevin", "groups": ["wheel"], "password": "password"}, {"name": "bob", "groups": ["super", "wheel"], "password": "password"}]"""
hr - Human Resources tool for your UNIX system
== 

CLI tool to manage the user state on your system. 

WARNING
-------
Use this tool at your own discretion. This tool is for learning purposes
and is advised that you do not run it on your home system or a production system. 

Preparing the Development 
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed. 
2. Clone repository: ``git clone https://github.com/nshipman-io/human-resources.git`` 
3. ``cd`` into the repository. 
4. Fetch development dependencies ``make install`` 
5. Activate virtualenv: ``pipenv shell`` 

Usage
-----

Pass in a path an inventory file. Inventory file must be json. Pass the export flag to build an inventory file based on your system's state.

Warning: root access is required to run this tool. 

Base Example: 

:: 

  $ sudo hr inventory.json 

Export Example: 

:: 

  $ sudo hr --export inventory.json

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active: 

:: 

    $ make 

If virtualenv is not active then use: 

:: 

    $ pipenv run make
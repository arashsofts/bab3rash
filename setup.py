from distutils.core import setup
import py2exe 

setup(
    console=['sheeba.py'],
    options = {
        'py2exe' = {
            'packages': ['getpass']
        }
    }
)

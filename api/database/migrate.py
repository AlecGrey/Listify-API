# THIS FILE WILL ONLY EVER BE EXECUTED ON ITS OWN AS '__main__'
# THEREFORE WE NEED TO FIX THE PATH TO CONSIDER ALL DEPENDENCY MODULES
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# FIX PATH TO MATCH EVERY OTHER FILE!
if __name__ == '__main__':
    import sys
    from pathlib import Path # if you haven't already done so
    file = Path(__file__).resolve()
    parent, root = file.parent, file.parents[2]
    sys.path.append(str(root))
    # Additionally remove the current file's directory from sys.path
    try:
        sys.path.remove(str(parent))
    except ValueError: # Already removed
        pass
# DIRECTORY-BASED IMPORTS
from api import app, db
from api.database import models

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from app import app, db

# Manager, to run command line commands
manager = Manager(app)

# Set MigrateCommand, sub-manager
migrate = Migrate(app, db)

# Add it to the manager, so we can run it's commands
manager.add_command('db', MigrateCommand)

# Run manager that will read command line arguments, if main
if __name__ == '__main__':
    manager.run()

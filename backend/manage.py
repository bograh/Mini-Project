from create_app import create_app, db
from flask_migrate import MigrateCommand
from flask_script import Manager

app = create_app()
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
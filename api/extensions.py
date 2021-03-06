from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy


db: SQLAlchemy = SQLAlchemy()
migrate: Migrate = Migrate()
cors = CORS()

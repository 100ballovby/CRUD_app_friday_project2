from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)  # привязываем к сайту БД
migrate = Migrate(app, db)  # указываем, что миграции с базой будет совершать сайт

from routes import *
from models import *


if __name__ == '__main__':
    app.run()

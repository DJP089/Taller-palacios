from flask import Flask
from routes.main.site import site
from routes.admin.dash import dash
from flask_sqlalchemy import SQLAlchemy
from database.db import db
from database.loginManagerService import login_manager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate



app = Flask(__name__)


app.register_blueprint(site)
app.register_blueprint(dash)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)
Bcrypt(app)
Migrate(app, db)
login_manager.init_app(app)
print (app.config)

with app.app_context():
    db.create_all()
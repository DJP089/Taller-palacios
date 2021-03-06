from flask_login import LoginManager
from models.contact import Contactos

login_manager = LoginManager()
login_manager.login_view = "site.login"


@login_manager.user_loader
def load_user(user_id):
    contacto = Contactos.query.filter_by(id=user_id).first()
    return contacto 

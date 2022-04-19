from database.db import db
from flask_login import UserMixin
class Contactos(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(10), nullable=False)
    dui = db.Column(db.String(1000), nullable=False)
    rank = db.Column(db.String(1000), nullable=False)
    
    
    def __init__(self, nombres, apellidos, telefono, dui,):
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono
        self.dui = dui
        self.rank = "user"
    
    def __repr__(self) -> str:
        return f"Contactos({self.id}, '{self.nombres}', '{self.apellidos}', '{self.telefono}', '{self.dui}','{self.rank}')"
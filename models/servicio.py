from database.db import db


class Servicios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    n_contacto = db.Column(db.Integer, db.ForeignKey("contactos.id"))
    n_carro = db.Column(db.Integer, db.ForeignKey("carros.id"))
    costo_total = db.Column(db.Integer, nullable=True)
    
    def __init__(self, n_contacto, n_carro, costo_total):
        self.n_contacto = n_contacto
        self.n_carro = n_carro
        self.costo_total = costo_total
    
    def __repr__(self) -> str:
        return f"Servicios('{self.costo_total}')"    
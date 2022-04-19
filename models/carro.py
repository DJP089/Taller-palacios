from database.db import db


class Carros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    n_contacto = db.Column(db.Integer, db.ForeignKey("contactos.id"))
    placa = db.Column(db.Integer, nullable=False)
    marca = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    version = db.Column(db.String(50), nullable=False)
    neumatico = db.Column(db.Float, nullable=False)
    color = db.Column(db.String(50))
    anno = db.Column(db.Integer)
    

    def __init__(self, placa, contacto, marca, modelo, version, neumatico, color, anno,):
        self.placa = placa
        self.contacto = contacto
        self.marca = marca
        self.modelo = modelo
        self.version = version
        self.neumatico = neumatico
        self.color = color
        self.anno = anno
       
    def __repr__(self) -> str:
        return f"Carro('{self.placa}', '{self.contacto}',{self.marca}',{self.modelo}', '{self.version}', '{self.neumatico}', '{self.color}', '{self.anno}')"
            
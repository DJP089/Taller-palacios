from database.db import db


class Detalles(db.Model):
    id_detalle = db.Column(db.Integer, primary_key=True)
    id_servicio = db.Column(db.Integer, db.ForeignKey("servicios.id"))
    id_estado = db.Column(db.Integer, db.ForeignKey("estados.id"))
    id_tipo = db.Column(db.Integer, db.ForeignKey("tipos.id"))
    fecha = db.Column(db.DateTime,)
    fecha_prox = db.Column(db.DateTime)
    costo = db.Column(db.Integer,)
    cantidad = db.Column(db.Integer,)
    costo_total = db.Column(db.Integer, nullable=True)
    
    
    
    def __init__(self, fecha, fecha_prox, costo,costo_total, cantidad):
        self.fecha = fecha
        self.fecha_prox = fecha_prox
        self.costo = costo
        self.cantidad = cantidad
        self.costo_total = costo_total
    
    def repr(self) -> str:
        return f"Detalles({self.id_detalle}, {self.fecha}, '{self.fecha_prox}', '{self.costo}','{self.costo_total}','{self.cantidad}')"
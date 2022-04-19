from database.db import db

#impedir nulo
class Tipos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    n_tipo = db.Column(db.String(200), nullable=False)
    
    
    def __init__(self, n_tipo):
        self.n_tipo = n_tipo
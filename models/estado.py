from database.db import db

#en todos quitar el id
#inpedir nulo
class Estados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    n_estado = db.Column(db.String(40), nullable=False)
    
    def __init__(self, n_estado):
        self.n_estado = n_estado
        
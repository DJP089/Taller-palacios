import pandas as pd
from models.estado import Estados
from database.db import db
from os.path import relpath

import os
def get_estados_from_file():
    current_dir = os.getcwd()
    data_frame = pd.read_csv( relpath('./estados.csv'), sep=";")
    for desc, _ in data_frame.values:
        estado = Estados(desc)
        db.session.add(estado)
        db.session.commit() 
        
import pandas as pd
from models.estado import Estados
from database.db import db
from os.path import relpath

import os
def get_estados_from_file():
    current_dir = os.getcwd()
    print(current_dir)
    data_frame = pd.read_csv( relpath('./database/estados.csv'), sep=";")
    for desc, _ in data_frame.values:
        estado = Estados(desc)
        db.session.add(estado)
        db.session.commit() 
        
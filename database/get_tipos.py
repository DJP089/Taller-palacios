import pandas as pd
from models.tipo import Tipos
from database.db import db
from os.path import relpath
import os
def get_tipos_from_file():
    current_dir = os.getcwd()
    
    data_frame = pd.read_csv( relpath('./database/tipos.csv'), sep=";")
    for desc, _ in data_frame.values:
        tipo = Tipos(desc)
        db.session.add(tipo)
        db.session.commit() 
        
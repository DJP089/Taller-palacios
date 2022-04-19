from turtle import ondrag
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from models.carro import Carros
from models.contact import Contactos


class carroCreateform(FlaskForm):
    placa = StringField(
        validators=[
            InputRequired(),
            Length(min=1, max=7),
        ],
        render_kw={"placehalder": "Placa"},
    )
    

    
    marca = StringField(
        validators=[
            InputRequired(),
            
        ], 
        render_kw={"placeholder": "Marca"},
    )
    
    modelo = StringField(
        validators=[
            InputRequired(),
            
        ],
        render_kw={"placeholder": "Modelo"},
    )
    
    
    version = StringField(
        validators=[
            InputRequired(),
            
        ],
        render_kw={"placeholder": "Version"},
    )
    
    neumatico = StringField(
        validators=[
            InputRequired(),
            
        ],
        render_kw={"placeholder": "Neumaticos"},
    )
    
    color = StringField(
        validators=[
            InputRequired(),
            
        ],
        render_kw={"placeholder": "Color"},
    )
    
    anno = IntegerField(
        validators=[
            InputRequired(),
            
        ],
        render_kw={"placeholder": "anno"},
    )

    submit = SubmitField("create")




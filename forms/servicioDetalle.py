from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length
from models.servicio import Servicios

class OrderCreateform(FlaskForm):
    costo_total = IntegerField(
        validators=[
            InputRequired(),
            
        ],
        render_kw={"placehalder": "orderId"},
    )
    
    cantidad = IntegerField(
        validators=[
            InputRequired(),

        ],
        render_kw={"placeholder": "cantidad"},
    )
    
    descripcion = StringField(
        validators=[
            InputRequired(),
            Length(min=1, max=50),    
        ],
        render_kw={"placeholder": "descripcion"},
    )
    
    costoUnitario = IntegerField(
        validators=[
            InputRequired(),          
        ],
        render_kw={"placeholder": "costoUnitario"},
    )
    
    
    
    
    submit = SubmitField("create")






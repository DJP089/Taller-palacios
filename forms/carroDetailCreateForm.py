from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateTimeField
from wtforms.validators import InputRequired, Length
from models.detalle import Detalles

class OrderCreateform(FlaskForm):
    fecha = DateTimeField(
        validators=[
            InputRequired(),
            
        ],
        render_kw={"placehalder": "Fecha"},
    )
    
    fecha_prox = DateTimeField(
        validators=[
            InputRequired(),
            
        ],
        render_kw={"placehalder": "Fecha proxima"},
    )
    
    cantidad = IntegerField(
        validators=[
            InputRequired(),

        ],
        render_kw={"placeholder": "Cantidad"},
    )
    
    costo = IntegerField(
        validators=[
            InputRequired(),
                
        ],
        render_kw={"placeholder": "Costo"},
    )
    
    costo_total = IntegerField(
        validators=[
            InputRequired(),          
        ],
        render_kw={"placeholder": "Costo total"},
    )
    
    
    
    
    submit = SubmitField("crear")






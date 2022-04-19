from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from models.contact import Contactos


class RegisterForm(FlaskForm):
    nombres = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=100),
        ],
        render_kw={"placeholder": "Nombres"},
    )
    
    
    apellidos = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=100),
        ],
        render_kw={"placeholder": "Apellidos"},
    )
    
    telefono = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=100),
        ],
        render_kw={"placeholder": "Telefono"},
    )
    
    dui = PasswordField(
        validators=[
            InputRequired(),
            Length(min=4, max=100),
        ],
        render_kw={"placeholder": "DUI"},
    )
    

    submit = SubmitField("Registrarse")

    def validate_username(self, nombres):
        currentUser = Contactos.query.filter_by(nombres=nombres).first()
        if currentUser:
            raise ValidationError("Este usuario o contraseña ya existen")

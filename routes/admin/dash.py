from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from forms.carroCreateForm import carroCreateform
from datetime import date
from models.contact import Contactos
from models.carro import Carros
from database.db import db




#lo que pogamos en el url sera la ruta unica que solo el admin puede tener
dash = Blueprint("dash", __name__, url_prefix="/admin")

#Esta parte es para que el dueño pueda meter su usuario y contraseña, asi sera mas seguro y solo el podra entrar
@dash.route("/")
@login_required
def home():
    print(f"current_user: {current_user}")
    return render_template("admin/dashboard.html", contacto=current_user)



##todos los registros de los clientes
@dash.route("/dashboard")
@login_required
def dashboard():
    listado = Carros.query.filter_by(contacto=current_user.id)
    return render_template("admin/dashboard.html", listado=listado)

##crear registro de un carro de
@dash.route("/carro", methods=["GET", "POST"])
@login_required
def carro():
    form = carroCreateform()
    print(form)
    if form.validate_on_submit():
        placa = form.placa.data
        contacto = current_user.id
        marca = form.marca.data
        modelo = form.modelo.data
        version = form.version.data
        neumatico = form.neumatico.data
        color = form.color.data
        anno = form.anno.data
        nuevocarro =Carros(placa, contacto, marca, modelo, version, neumatico, color, anno)
        db.session.add(nuevocarro)
        db.session.commit()
        return redirect(url_for("dash.home"))
    return render_template("admin/carro.html",form=form)


## ver los carros de un cliente 
@dash.route("/garage")
@login_required
def garage():
    garage = Carros.query.filter_by(contacto=current_user.id)
    return render_template("admin/garage.html", carros=garage)

##agregar un servicio 

##agregar servicio detalles 

##modificar estados

##modificar Tipos


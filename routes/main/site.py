#AQUI SE MANEJAN LAS RUTAS DEL SITIO PRINCIPAL
from flask import Blueprint, render_template,redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from forms.registerForm import RegisterForm
from forms.loginForm import LoginForm

from models.contact import Contactos
from database.bcryptService import bcrypt
from models.tipo import Tipos
from models.estado import Estados
from database.db import db
from database.get_tipos import get_tipos_from_file
from database.get_estados import get_estados_from_file

site = Blueprint("site", __name__, url_prefix="/")

# esta pagina sera la pricipal 
@site.route("/")
def home():
    if not Estados.query.all():
        get_estados_from_file()
        
    if not Tipos.query.all():
        get_tipos_from_file()
    return render_template("main/home_main.html")



##ruta para registro
@site.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        nombres = form.nombres.data
        apellidos = form.apellidos.data
        telefono = form.telefono.data
        dui = form.dui.data
        hashed_password = bcrypt.generate_password_hash(dui)
        newUser = Contactos(nombres, apellidos, telefono, hashed_password)
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for("site.login"))
    return render_template("register.html", form=form)


##ruta para login
@site.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        nombres = form.nombres.data
        dui = form.dui.data
        currentUser = Contactos.query.filter_by(nombres=nombres).first()
        if currentUser:
            if bcrypt.check_password_hash(currentUser.dui, dui):
                login_user(currentUser)
                if currentUser.rank == "admin":
                    return redirect(url_for("dash.dashboard"))
                return redirect(url_for("site.home2"))
    return render_template("login.html", form=form)
    
@site.route("/home2")
@login_required
def home2():
    if not Estados.query.all():
        get_estados_from_file()
        
    if not Tipos.query.all():
        get_tipos_from_file()
    print(f"current_user: {current_user}")
    return render_template("main/home_login.html", contacto=current_user)
       



##ruta para logout
@site.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("site.login"))


##ruta para about
@site.route("/about")
def about():
    return render_template("about.html")


##ruta para contacto
@site.route("/contact")
def contact():
    return render_template("contact.html")

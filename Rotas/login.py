from flask import Blueprint, Flask, render_template, session
import os
from Models.Bd import get_db_connection
from Models.Usuario import Usuario

bp_usuario = Blueprint('usuario', __name__, template_folder='../templates')

@login.route("/Login", methods=['GET', 'POST'])
def login():
    return render_template ("/htmllogin.html")






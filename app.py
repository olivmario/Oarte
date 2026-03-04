from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify

from Models.Bd import get_db_connection

app = Flask(__name__)



@app.route("/")
def home():
    return render_template ("/Home.html")

@app.route("/usuarios")
def listar_usuarios():

    con = get_db_connection()
    cursor = con.cursor(dictionary=True)
    cursor.execute("Select * from usuarios")
    lista_usuarios = cursor.fetchall()

    cursor.close()
    con.close()

    return jsonify(lista_usuarios)

if __name__ == "__main__":
    app.run(debug=True)
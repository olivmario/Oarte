from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify

from Models.Bd import get_db_connection

app = Flask(__name__)



@app.route("/")
def home():
    return render_template ("/Home.html")


if __name__ == "__main__":
    app.run(debug=True)
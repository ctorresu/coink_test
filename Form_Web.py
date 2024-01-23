import Database_Manager as DM
import sqlite3
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/customers.db'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/create_user", methods=["POST"])
def create_register():
    
    name = request.form['name'].upper()
    email = request.form['email']
    city = request.form['city'].upper()
    
    DB = sqlite3.connect('database/customers.db')
    cursor = DB.cursor()
    cursor.execute('SELECT * FROM table_customer WHERE name=? AND email=? AND city=?', (name, email, city))
    existing_data = cursor.fetchone()

    if name=="" or email=="" or city=="":
        message = "Error al enviar: No has registrado todos los campos, no fue posible hacer el registro"
        return f'<script>alert("{message}"); window.history.back();</script>'

    if existing_data==None:
        DM.insertRow(name=name, email=email, city=city)
        message = "Los datos han sido correctamente registrados"
        return f'<script>alert("{message}"); window.history.back();</script>'
    else:
        message = "Los datos que ingresaste ya se encuentran en la base de datos"
        return f'<script>alert("{message}"); window.history.back();</script>'

@app.route('/Database')
def sendtodatabase():
    DB = sqlite3.connect('database/customers.db')
    cursor = DB.cursor()
    cursor.execute('SELECT * FROM table_customer')
    dates = cursor.fetchall()
    DB.close()

    return render_template("show_database.html", dates=dates)

if __name__=="__main__":
    app.run(debug=True)


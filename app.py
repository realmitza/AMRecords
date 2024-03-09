import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Angajat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nume = db.Column(db.String(100), nullable=False)
    prenume = db.Column(db.String(100), nullable=False)
    calificari = db.Column(db.Text)
    functie_id = db.Column(db.Integer, db.ForeignKey('functie.id'), nullable=False)

    def __repr__(self):
        return f'{self.nume}, {self.prenume}'

class Functie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    functia = db.Column(db.String(200), nullable=False)
    responsabilitati = db.Column(db.Text)
    angajati = db.relationship('Angajat', backref='functie', lazy=True)
    servicii = db.relationship('Serviciu', backref='functie', lazy=True)

    def __repr__(self):
        return f'{self.functia}'

class Serviciu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nume = db.Column(db.String(100), nullable=False)
    pret = db.Column(db.String(200), nullable=False)
    descriere = db.Column(db.Text)
    functie_id = db.Column(db.Integer, db.ForeignKey('functie.id'), nullable=False)

    def __repr__(self):
        return f'{self.nume}'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/servicii/<int:id>')
def serviciu(id):
    serviciu = Serviciu.query.get_or_404(id)
    return render_template('serviciu.html', serviciu=serviciu)
@app.route('/servicii')
def servicii():
    servicii = Serviciu.query.all()
    return render_template('servicii.html', servicii=servicii)

@app.route('/despre_noi')
def despre_noi():
    angajati = Angajat.query.all()
    return render_template('despre_noi.html', angajati=angajati)

@app.route('/angajati/<int:id>')
def angajat(id):
    angajat = Angajat.query.get_or_404(id)
    return render_template('angajat.html', angajat=angajat)
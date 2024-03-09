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

class Firma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nume = db.Column(db.String(100), nullable=False)
    domeniu_activitate = db.Column(db.String(100), nullable=False)
    adresa = db.Column(db.String(255))
    angajati = db.relationship('Angajat', backref='firma', lazy=True)
    functii = db.relationship('Functie', backref='firma', lazy=True)
    despre_noi = db.Column(db.Text)

    def __repr__(self):
        return f'<Firma {self.nume}>'

class Angajat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nume = db.Column(db.String(100), nullable=False)
    prenume = db.Column(db.String(100), nullable=False)
    calificari = db.Column(db.Text)
    firma_id = db.Column(db.Integer, db.ForeignKey('firma.id'), nullable=False)
    functie_id = db.Column(db.Integer, db.ForeignKey('functie.id'), nullable=False)

    def __repr__(self):
        return f'<Angajat {self.nume}, {self.prenume}>'

class Functie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    functia = db.Column(db.String(200), nullable=False)
    responsabilitati = db.Column(db.Text)
    firma_id = db.Column(db.Integer, db.ForeignKey('firma.id'), nullable=False)
    angajati = db.relationship('Angajat', backref='functie', lazy=True)

    def __repr__(self):
        return f'<Functie {self.functia}>'

@app.route('/')
def index():
    return 'Test'

from app import app
from flask import render_template
from models.angajat import Angajat
from models.functie import Functie
from models.serviciu import Serviciu

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

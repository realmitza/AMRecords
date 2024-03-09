from app import db

class Functie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    functia = db.Column(db.String(200), nullable=False)
    responsabilitati = db.Column(db.Text)
    angajati = db.relationship('Angajat', backref='functie', lazy=True)
    servicii = db.relationship('Serviciu', backref='functie', lazy=True)

    def __repr__(self):
        return f'{self.functia}'

from app import db

class Serviciu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nume = db.Column(db.String(100), nullable=False)
    pret = db.Column(db.String(200), nullable=False)
    descriere = db.Column(db.Text)
    functie_id = db.Column(db.Integer, db.ForeignKey('functie.id'), nullable=False)

    def __repr__(self):
        return f'{self.nume}'

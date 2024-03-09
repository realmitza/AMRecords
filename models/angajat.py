from app import db

class Angajat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nume = db.Column(db.String(100), nullable=False)
    prenume = db.Column(db.String(100), nullable=False)
    calificari = db.Column(db.Text)
    functie_id = db.Column(db.Integer, db.ForeignKey('functie.id'), nullable=False)

    def __repr__(self):
        return f'{self.nume}, {self.prenume}'

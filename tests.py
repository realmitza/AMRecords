import unittest
from app import app, db
from models.angajat import Angajat
from models.functie import Functie
from models.serviciu import Serviciu

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

        # Populăm baza de date cu date de test
        functie = Functie(functia="Fotograf", responsabilitati="Realizarea fotografiilor")
        db.session.add(functie)
        angajat = Angajat(nume="Popescu", prenume="Ana", calificari="Calificare X", functie=functie)
        db.session.add(angajat)
        serviciu = Serviciu(nume="Sedinta foto", pret="100 RON", descriere="O sedinta foto profesionala")
        db.session.add(serviciu)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_servicii(self):
        response = self.app.get('/servicii')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sedinta foto', response.data)

    def test_angajat(self):
        response = self.app.get('/angajati/1')  # Assume the first employee ID is 1
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Popescu, Ana', response.data)

if __name__ == '__main__':
    unittest.main()

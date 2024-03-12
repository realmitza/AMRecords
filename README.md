# Prezentare firma AMRecords

## Instructiuni instalare

### Clonare repertoriu

git clone https://github.com/realmitza/AMRecords.git

### Setare mediu virtual python

Navigati in directorul AMRecords si creati on mediu virtual
 `python -m venv venv`

Activati mediul virtual
- Windows `venv\Scripts activate`
- MacOS / Linux `source venv/bin/activate`

### Instalare dependente

`pip install -r requirements.txt`

### Baza de date
Baza de date este inclusa in aplicatie si nu necesita initializare.

### Rulare applicatie
`flask run`

Deschideti applicatie in browser `http://127.0.0.1:5000/`
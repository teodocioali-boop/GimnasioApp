from flask import Flask
from gymapp.extensions import db
from gymapp import models 
from config import SECRET_KEY, SQLALCHEMY_DATABASE_URI

print(f"🔍 CONECTANDO A LA BASE DE DATOS: {SQLALCHEMY_DATABASE_URI}")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db.init_app(app)

with app.app_context():
    # Esto nos dirá si Python está leyendo tus modelos
    tablas = list(db.metadata.tables.keys())
    print(f"📊 TABLAS ENCONTRADAS POR PYTHON: {tablas}")
    
    if len(tablas) == 0:
        print("⚠️ ERROR: Python no ve las tablas. Revisa que models.py tenga código.")
    else:
        db.create_all()
        print("✅ ¡PROCESO TERMINADO!")
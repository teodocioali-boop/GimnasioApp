from flask import Flask
from gymapp.extensions import db, appbuilder
from gymapp import models
from gymapp import views

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)

# ¡ESTA ES LA MAGIA! Le decimos a Flask que "empuje" el contexto
with app.app_context():
    appbuilder.init_app(app, db.session)
    
    # Registramos las vistas
    appbuilder.add_view(views.DisciplinaView, "Disciplinas", category="Gestión")
    appbuilder.add_view(views.EntrenadorView, "Entrenadores", category="Gestión")
    appbuilder.add_view(views.SocioView, "Socios", category="Gestión")
    appbuilder.add_view(views.HorarioView, "Horarios", category="Gestión")
    appbuilder.add_view(views.ReservaView, "Reservas", category="Gestión")
    appbuilder.add_view(views.HistorialEntrenamientoView, "Historial e IA", category="Gestión")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
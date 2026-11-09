from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Disciplina, Entrenador, Socio, Horario, Reserva, HistorialEntrenamiento
from .ia_utils import analizar_sentimiento

class DisciplinaView(ModelView):
    datamodel = SQLAInterface(Disciplina)

class EntrenadorView(ModelView):
    datamodel = SQLAInterface(Entrenador)

class SocioView(ModelView):
    datamodel = SQLAInterface(Socio)

class HorarioView(ModelView):
    datamodel = SQLAInterface(Horario)

class ReservaView(ModelView):
    datamodel = SQLAInterface(Reserva)

class HistorialEntrenamientoView(ModelView):
    datamodel = SQLAInterface(HistorialEntrenamiento)
    list_columns = ['socio', 'fecha', 'peso_actual', 'sentimiento']

    def pre_add(self, item):
        item.sentimiento = analizar_sentimiento(item.comentarios_objetivo)

    def pre_update(self, item):
        item.sentimiento = analizar_sentimiento(item.comentarios_objetivo)
from .extensions import db
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Text, Float
from sqlalchemy.orm import relationship
from datetime import datetime

class Disciplina(db.Model):
    __tablename__ = 'disciplina'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(Text)
    horarios = relationship('Horario', back_populates='disciplina')

class Entrenador(db.Model):
    __tablename__ = 'entrenador'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    especialidad = Column(String(100))
    horarios = relationship('Horario', back_populates='entrenador')

class Socio(db.Model):
    __tablename__ = 'socio'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    telefono = Column(String(20))
    fecha_alta = Column(Date, default=datetime.utcnow)
    reservas = relationship('Reserva', back_populates='socio')
    historial = relationship('HistorialEntrenamiento', back_populates='socio')

class Horario(db.Model):
    __tablename__ = 'horario'
    id = Column(Integer, primary_key=True)
    dia_semana = Column(String(20), nullable=False)
    hora_inicio = Column(DateTime, nullable=False)
    cupo_maximo = Column(Integer, default=20)
    disciplina_id = Column(Integer, ForeignKey('disciplina.id'), nullable=False)
    disciplina = relationship('Disciplina', back_populates='horarios')
    entrenador_id = Column(Integer, ForeignKey('entrenador.id'), nullable=False)
    entrenador = relationship('Entrenador', back_populates='horarios')
    reservas = relationship('Reserva', back_populates='horario')

class Reserva(db.Model):
    __tablename__ = 'reserva'
    id = Column(Integer, primary_key=True)
    fecha_reserva = Column(DateTime, default=datetime.utcnow)
    estado = Column(String(20), default='Confirmada')
    socio_id = Column(Integer, ForeignKey('socio.id'), nullable=False)
    socio = relationship('Socio', back_populates='reservas')
    horario_id = Column(Integer, ForeignKey('horario.id'), nullable=False)
    horario = relationship('Horario', back_populates='reservas')

class HistorialEntrenamiento(db.Model):
    __tablename__ = 'historial_entrenamiento'
    id = Column(Integer, primary_key=True)
    fecha = Column(DateTime, default=datetime.utcnow)
    peso_actual = Column(Float)
    comentarios_objetivo = Column(Text)
    sentimiento = Column(String(20))
    socio_id = Column(Integer, ForeignKey('socio.id'), nullable=False)
    socio = relationship('Socio', back_populates='historial')
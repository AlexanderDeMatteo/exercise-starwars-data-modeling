import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(60), nullable=False)
    apellido = Column(String(60), nullable=False)
    correo = Column(String(30), nullable=False)
    direccion = Column(String(250), nullable=True)
    telefono = Column(String(20), nullable=False)
    fecha_de_creacion = Column(String(50), nullable=False)

class Planeta(Base):
    __tablename__ = 'planeta'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(60), nullable=False)
    ubicacion = Column(String(250), nullable=False)
    dimencion = Column(String(30), nullable=False)
    peso = Column(String(250), nullable=True)
    fauna = Column(String(250), nullable=False)
    raza = Column(String(50), nullable=False)

class Personaje(Base):
    __tablename__ = 'personaje'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(60), nullable=False)
    apellido = Column(String(250), nullable=False)
    faccion = Column(String(30), nullable=False)
    clase = Column(String(250), nullable=False)
    clase = Column(String(250), nullable=False)
    raza = Column(String (50), nullable=False)

class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=False)
    usuario = relationship(Usuario)
    planeta = relationship(Planeta)
    personaje = relationship(Personaje)



# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     user = relationship(user)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
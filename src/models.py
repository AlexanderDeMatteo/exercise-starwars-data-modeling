import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Numeric, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('role.id'))
    # user_profile = Column(Integer, ForeignKey('person.id'))
    email = Column(String(250))
    password = Column(String(250))
    is_psicologo = Column(Boolean(), nullable = True)
    is_active = Column(Boolean(), nullable = True)
    is_online = Column(Boolean(), nullable = True)
    salt = Column(String(250), unique=True) 

class Role(Base):
    __tablename__ = 'role'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(250))
    permission = Column(Integer, ForeignKey('permission.id'))

class Permission(Base):
    __tablename__ = 'permission'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(250))

class Psicology_profile(Base):
    __tablename__ = 'psicology_profile'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('role.id'))
    name = Column(String(250), nullable=True)
    last_name = Column(String(250), nullable=True)
    profile_picture = Column(String(250), nullable=True)
    dni = Column(Numeric(20), unique=True, nullable=False)
    fpv_number = Column(Numeric(20), unique=True, nullable=False)
    gender= Column(String(20), nullable=True)
    monto_consulta = Column(Numeric(20), nullable=True)
    phone_number = Column(Numeric(20), nullable=True)
    specialty_area = Column(String(250))
    city = Column(String(250), nullable=True)
    state = Column(String(250), nullable=True)
    twitter = Column(String(250), nullable=True)
    facebook = Column(String(250), nullable=True)
    instagram = Column(String(250), nullable=True)
    education = Column(String(250), nullable=True)
    motivo_consulta = Column(String(250), nullable=True)
    psych_strategies = Column(String(250), nullable=True)
    PsychExperiences = Column(String(250), nullable=True)

class Client_Profile(Base):
    __tablename__ = 'client_profile'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('role.id'))
    name = Column(String(250), nullable=True)
    last_name = Column(String(250), nullable=True)
    profile_picture = Column(String(250), nullable=True)
    dni = Column(Numeric(20), unique=True, nullable=False)
    gender= Column(String(20), nullable=True)
    phone_number = Column(Numeric(20), nullable=True)
    city = Column(String(250), nullable=True)
    state = Column(String(250), nullable=True)

class Client_task(Base):
    __tablename__ = 'client_task'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('role.id'))
    description = Column(String(250))
    completed = Column(Boolean(), nullable = True)

class Session(Base):
    __tablename__ = 'session'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('role.id'))
    start_time = Column(String(250), nullable=True)
    end_time = Column(String(250), nullable=True)
    duration_time = Column(String(250), nullable=True)
    reserved = Column(Boolean(), nullable = True)
    calendar_date = Column(Date(), nullable = True)
    room_number = Column(String(250), nullable=True)

class Mi_psicologo(Base):
    __tablename__ = "mi_psicologo"
    id = Column(Integer, primary_key=True)   
    role_id = Column(Integer, ForeignKey('role.id'))

class Payment_acount(Base):
    __tablename__ = "payment_acount"
    id = Column(Integer, primary_key=True)   
    psiology_profile_id = Column(Integer, ForeignKey(Psicology_profile.id))
    zell_email = Column(String(250), nullable=True)
    binance_route = Column(Numeric(30), nullable=True)
    paypal_user = Column(String(250), nullable=True)
    paypal_name = Column(String(250), nullable=True)
    paypal_email = Column(String(250), nullable=True)
    pagomovil_bank = Column(Numeric(20), nullable=True)
    pagomovil_ci = Column(Numeric(20), nullable=True)
    pagomovil_phone = Column(Numeric(20), nullable=True)

class Phrase(Base):
    __tablename__ = "phrase"
    id = Column(Integer, primary_key=True) 
    phrase = Column(String(250), nullable=True)
    author = Column(String(20), nullable=True)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)






## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
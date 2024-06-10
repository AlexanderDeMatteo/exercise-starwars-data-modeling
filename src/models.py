import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Numeric, Date, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

association_table = Table(
    "association_table",
    Base.metadata,
    Column('role_id', Integer, ForeignKey('role.id'), primary_key=True),
    Column('permission_id', Integer, ForeignKey('permission.id'), primary_key=True ),
)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    # user_profile = Column(Integer, ForeignKey('person.id'))
    name = Column(String(250), nullable=True)
    last_name = Column(String(250), nullable=True)
    profile_picture = Column(String(250), nullable=True)
    dni = Column(Numeric(20), unique=True, nullable=False)
    gender= Column(String(20), nullable=True)
    phone_number = Column(Numeric(20), nullable=True)
    email = Column(String(250))
    motivo_consulta = Column(String(250), nullable=True)
    password = Column(String(250))
    is_psicologo = Column(Boolean(), nullable = True)
    is_active = Column(Boolean(), nullable = True)
    is_online = Column(Boolean(), nullable = True)
    salt = Column(String(250), unique=True)
    role_id = Column(Integer, ForeignKey('role.id'))
    user_address = Column(Integer, ForeignKey('address.id'))
    Psicology_profile = Column(Integer, ForeignKey('psicology_profile.id'))
    marketplace = Column(Integer, ForeignKey('marketplace.id'))

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

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    city = Column(String(250), nullable=True)
    state = Column(String(250), nullable=True)

class Psicology_profile(Base):
    __tablename__ = 'psicology_profile'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    fpv_number = Column(Numeric(20), unique=True, nullable=False)
    monto_consulta = Column(Numeric(20), nullable=True)
    specialty_area = Column(String(250))
    psych_strategies = Column(String(250), nullable=True)
    PsychExperiences = Column(String(250), nullable=True)
    socialNetwork_id = Column(Integer, ForeignKey('socialnetwork.id'))

class SocialNetwork(Base):
    __tablename__ = 'socialnetwork'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    url = Column(String(250), nullable=True)
    icon = Column(String(250), nullable=True)

class client_List(Base):
    __tablename__ = "client_list"
    id = Column(Integer, primary_key=True)   
    client_id = Column(Integer, ForeignKey('user.id'))

class Client_task(Base):
    __tablename__ = 'client_task'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    psychologist_id = Column(Integer, ForeignKey('user.id'))
    client_id = Column(Integer, ForeignKey('user.id'))

class Session(Base):
    __tablename__ = 'session'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    start_time = Column(String(250), nullable=True)
    end_time = Column(String(250), nullable=True)
    duration_time = Column(String(250), nullable=True)
    reserved = Column(Boolean(), nullable = True)
    calendar_date = Column(Date(), nullable = True)
    room_number = Column(String(250), nullable=True)
    psychologist_session_id = Column(Integer, ForeignKey('user.id'))
    client_session_id = Column(Integer, ForeignKey('user.id'))
    session_type = Column(Integer, ForeignKey('session_type.id'))

class Session_type(Base):
    __tablename__ = "session_type"
    id = Column(Integer, primary_key=True)
    type_of_session = Column(String(250), nullable=True)

class Payment_acount(Base):
    __tablename__ = "payment_acount"
    id = Column(Integer, primary_key=True)   
    zell_email = Column(String(250), nullable=True)
    binance_route = Column(Numeric(30), nullable=True)
    paypal_user = Column(String(250), nullable=True)
    paypal_name = Column(String(250), nullable=True)
    paypal_email = Column(String(250), nullable=True)
    pagomovil_bank = Column(Numeric(20), nullable=True)
    pagomovil_ci = Column(Numeric(20), nullable=True)
    pagomovil_phone = Column(Numeric(20), nullable=True)
    Psicology_profile_id = Column(Integer, ForeignKey('psicology_profile.id'))

class Phrase(Base):
    __tablename__ = "phrase"
    id = Column(Integer, primary_key=True) 
    phrase = Column(String(250), nullable=True)
    author = Column(String(20), nullable=True)

class MarketPlace(Base):
    __tablename__ = "marketplace"
    id = Column(Integer, primary_key=True) 
    product = Column(String(250), nullable=True)
    description = Column(String(20), nullable=True)
    status = Column(Boolean(), nullable=True)
    cost = Column(String(20), nullable=True)

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
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True) 
    username = Column(String(100), nullable = False)
    email = Column(String(50), nullable = False)
    password = Column(String(500), nullable = False)
    favorite = relationship("favorite") 


class People(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key = True)
    name = Column(String(150), nullable = False)
    height = Column(Integer, nullable = False)
    mass = Column(Integer, nullable = False)
    hair_color = Column(String(100), nullable = False)
    skin_color = Column(String(100), nullable = False)
    eye_color = Column(String(100), nullable = False)
    brth_year = Column(Date, nullable = False)
    create = Column(Date, nullable = False)
    edited = Column(Date, nullable = False)
    homeworld = Column(String(100), nullable = False)
    url = Column(String(200), nullable = False)
    description = Column(Text, nullable = False)
    favorite = relationship("favorite")

class Planet(Base):
    __tablename__ = "planet"

    id = Column(Integer, primary_key = True)
    diameter = Column(Integer, nullable = False)
    rotation_period = Column(Integer, nullable = False)
    orbital_period = Column(Integer, nullable = False)
    gravity = Column(Integer, nullable = False)
    population = Column(Integer, nullable = False )
    climate = Column(String(100), nullable = False )
    terrain = Column(String(100), nullable = False)
    surface_water = Column(String(100), nullable = False)
    creted = Column(Date, nullable = False)
    edited = Column(Date, nullable = False)
    name = Column(String(150), nullable = False)
    url = Column(String(150), nullable = False)
    description = Column(Text, nullable = False)
    favorite = relationship("favorite")

class Vehicle(Base):
    __tablename__ = "vehicle"

    id = Column(Integer, primary_key = True)
    model = Column(String(200), nullable = False)
    vehicle_cLass = Column(String(200), nullable = False)
    manufacturer = Column(String(150), nullable = False)
    cost_in_credits = Column(Integer, nullable = False)
    length = Column(Integer, nullable = False)
    crew = Column(Integer, nullable = False)
    passangers = Column(Integer, nullable = False)
    max_atmosphering_speed = Column(Integer, nullable = False )
    cargo_capacity = Column(Integer, nullable = False)
    consumables = Column(String(150), nullable = False)
    creted = Column(Date, nullable = False)
    edited = Column(Date, nullable = False)
    name = Column (String(200), nullable = False)
    favorite = relationship("favorite")


class Favorite(Base):
    __tablename__ = "favorite"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False)
    people_id = Column(Integer, ForeignKey("people.id"), nullable = False)
    planet_id = Column(Integer, ForeignKey("planet.id"), nullable = False)
    vehicle_id = Column(Integer,ForeignKey("vehicle.id"), nullable = False)

## Draw from SQLAlchemy base
render_er(Base, 'uml.png')

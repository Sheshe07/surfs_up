9.5
#import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy

#import sqlalchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#Flask dependency
from flask import Flask

#SQLAlchemy Create Engine
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#Create a New Flask App
app = Flask(__name__)

#Create Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world'


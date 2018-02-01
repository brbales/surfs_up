import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


engine = create_engine("sqlite:///hawaii.db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# assign base class variables
Measurement = Base.classes.Measurement
Station = Base.classes.Station

# start our session from Python to the DB
session = Session(engine)

# flask setup
app = Flask(__name__)

# set routes


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Avalable Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"

        f"/api/v1.0/stations<br/>"

        f"/api/v1.0/tobs<br/>"

        f"/api/v1.0/&ltstart_date&gt" 
        f" - Start Date (Y%-m%-d%)<br/>" 

        f"/api/v1.0/&ltstart_date&gt/&ltend_date&gt" 
        f" - Start Date & End Date (Y%-m%-d%)<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precip():
    # Create a list of dicts reporting precipitation by date for year prior to trip
    results = session.query(Measurement.date, Measurement.prcp).\
            group_by(Measurement.date).having(Measurement.date.like('2016%')).all()

    # Convert list of tuples into normal list
    precip_list = list(np.ravel(results))

    return jsonify(precip_list)


@app.route("/api/v1.0/stations")
def stations():
    # list of weather stations
    results = session.query(Measurement.station, Station.name).\
                group_by(Measurement.station).\
                order_by(func.count(Measurement.tobs).desc()).all()

    
    station_list = []
    for result in results:
        row = {}
        row["Station"] = result[0]
        row["Name"] = result[1]
        station_list.append(row)

    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def temps():
    # Create a list of dicts reporting station and tobs
    results = session.query(Measurement.station, Measurement.date, Measurement.tobs).\
                order_by((Measurement.date).desc()).all()
    
    temp_list = list(np.ravel(results))

    return jsonify(temp_list)

@app.route("/api/v1.0/<start_date>")
@app.route("/api/v1.0/<start_date>/<end_date>")
def dates(start_date, end_date="2017-08-23"):
    # return a list of min, max, and avg temp for given date range
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
                            filter(Measurement.date >= start_date, Measurement.date <= end_date).all()

    calc_temp_list = []
    for result in results:
        row = {}
        row["TempMin"] = float(result[0])
        row["TempMax"] = float(result[1])
        row["TempAvg"] = float(result[2])
        calc_temp_list.append(row)

    return jsonify(calc_temp_list)



if __name__ == '__main__':
    app.run()

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br>"
        f"<b>/api/v1.0/precipitation</b><br>"
        f"Returns last 12 months of precipitation data<br><br>"
        f"<b>/api/v1.0/stations</b><br>"
        f"Returns a list of stations from the dataset<br><br>"
        f"<b>/api/v1.0/tobs</b><br>"
        f"Returns temperature obervatons over the last 12 months<br><br>"
        f"<b>/api/v1.0/<i>yyyy-mm-dd</i></b><br>"
        f"Returns min, max, and avg temperature obervatons on and after the start date input<br><br>"
        f"<b>/api/v1.0/<i>yyyy-mm-dd/yyyy-mm-dd</i></b><br>"
        f"Returns min, max, and avg temperature obervatons within the start/end date range input"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
	last_date = session.query(Measurement.date).\
	order_by(Measurement.date.desc()).first()
	
	last_date = last_date[0]
	
	time_frame = dt.datetime.strptime(last_date, "%Y-%m-%d") - dt.timedelta(days=365)
	
	prcp_query = session.query(Measurement.date, Measurement.prcp).\
	filter(Measurement.date >= time_frame).all()
	
	prcp_dict = dict(prcp_query)
	
	return jsonify(prcp_dict)

@app.route("/api/v1.0/stations")
def stations():

	station_query = session.query(func.distinct(Measurement.station)).all()

	station_list = list(np.ravel(station_query))

	return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():

	last_date = session.query(Measurement.date).\
	order_by(Measurement.date.desc()).first()
	
	last_date = last_date[0]
	
	time_frame = dt.datetime.strptime(last_date, "%Y-%m-%d") - dt.timedelta(days=365)

	tobs_query = session.query(Measurement.date, Measurement.tobs).\
	filter(Measurement.date >= time_frame).all()

	tobs_dict = dict(tobs_query)

	return jsonify(tobs_dict)

@app.route("/api/v1.0/<start>")
def start(start):

	start_date = session.query(Measurement.date, func.min(Measurement.tobs),\
	func.max(Measurement.tobs),\
	func.avg(Measurement.tobs)).\
	filter(Measurement.date >= start).\
	group_by(Measurement.date).all()
	
	return jsonify(start_date)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):

	date_range = session.query(Measurement.date, func.min(Measurement.tobs),\
	func.max(Measurement.tobs),\
	func.avg(Measurement.tobs)).\
	filter(Measurement.date >= start).\
	filter(Measurement.date <= end).\
	group_by(Measurement.date).all()

	return jsonify(date_range)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import Scrape_Mars

app = Flask(__name__)

mongo = PyMongo(app)

@app.route('/')
def index():
    mars_data = mongo.db.mars.find_one()
    return render_template('index.html', mars_data=mars_data)

@app.route('/scrape')
def scrape():
    mars_data = mongo.db.mars_data
    data = Scrape_Mars.scrape()
    mars_data.update({}, data, upsert=True)
    return redirect('/', code=302)

if __name__ == '__main__':
    app.run(debug=True)


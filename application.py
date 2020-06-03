from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime
import os
# from geopy.geocoders import Nominatim
# from GPSPhoto import gpsphoto
# from selenium import webdriver
from picture_locator import JpgPicFinder, Picture

app = Flask('__name__')
app.secret_key = 'aa3049cb37add30e0d4b9ebd5f2ca349'
path = '/Users/marcin94/PycharmProjects/Jpg_flask/pics'
app.config['IMAGE_UPLOADS'] = path
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'
db = SQLAlchemy(app)


# class Picture(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200), nullable=False)
#     # location = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # def __repr__(self):
    #     return '<Pic %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if request.files:
            pic = request.files['image']

            pic.save(os.path.join(app.config['IMAGE_UPLOADS'], pic.filename))

            data = JpgPicFinder.get_coords(os.path.join(app.config['IMAGE_UPLOADS'], pic.filename))
            coords = (data['Latitude'], data['Longitude'])
            print(coords)

            location = JpgPicFinder.search_location(coords)
            print(location)
            # Picture.google_maps_search(keys=location)

            # new_pic = Picture(name=pic.filename)
            # try:
            #     db.session.add(new_pic)
            #     db.session.commit()
            #     return redirect('/')
            # except:
            #     return 'There was an issue adding your task'

            return render_template('update.html', location=location, coords=coords, filename=pic.filename)

    return render_template('update.html')


@app.route('/show', methods=['POST', 'GET'])
def show_on_map():
    location = 'new york'
    # Picture.google_maps_search(keys=location)
    return redirect(Picture.google_maps_search(keys=location))


if __name__ == '__main__':
    app.run(debug=True)

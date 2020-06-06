from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request, redirect, flash
import os
from picture_locator import JpgPicFinder, Picture
from flask_sqlalchemy import SQLAlchemy

app = Flask('__name__')
path = '/Users/marcin94/PycharmProjects/Jpg_flask/pics'
app.config['SECRET_KEY'] = 'ZOMn8n1Jt8KTfXPwbcZ3tw'
app.config['IMAGE_UPLOADS'] = path


@app.route('/', methods=['POST', 'GET'])
def index():
    global coords
    if request.method == 'POST':
        if request.files:
            pic = request.files['image']
            try:
                pic.save(os.path.join(app.config['IMAGE_UPLOADS'], pic.filename))
                data = JpgPicFinder.get_coords(os.path.join(app.config['IMAGE_UPLOADS'], pic.filename))
                coords = (data['Latitude'], data['Longitude'])
                location = JpgPicFinder.search_location(coords)
                return render_template('update.html', location=location, coords=coords, filename=pic.filename)
            except:
                flash('Something went wrong', 'error')
    return render_template('update.html')


@app.route('/show', methods=['GET'])
def show_on_map():
    return redirect(Picture.google_maps_search(keys=str(coords)))


if __name__ == '__main__':
    app.run(debug=True)

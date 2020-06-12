from flask import Flask, render_template, url_for, request, redirect, flash, session
import os
from picture_locator import JpgPicFinder, Picture
from helpers import convertToStr
from errors import NoCoord

app = Flask('__name__')
path = '/Users/marcin94/PycharmProjects/Jpg_flask/pics'
app.config['SECRET_KEY'] = 'ZOMn8n1Jt8KTfXPwbcZ3tw'
app.config['IMAGE_UPLOADS'] = path


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if request.files:
            pic = request.files['image']
            try:
                pic.save(os.path.join(app.config['IMAGE_UPLOADS'], pic.filename))
                data = JpgPicFinder.get_coords(os.path.join(app.config['IMAGE_UPLOADS'], pic.filename))
                if data == {}:
                    raise NoCoord
                else:
                    coords = (round(data['Latitude'], 7), round(data['Longitude'], 7))
                    location = JpgPicFinder.search_location(coords)
                    session['coords'] = coords
                    return render_template('update.html', location=location, coords=coords, filename=pic.filename)
            except IsADirectoryError:
                flash("Ups! Forgot to add a file didn't you?", 'error')
            except NoCoord:
                flash('No gps data available for current picture!', 'error')

    return render_template('update.html')


@app.route('/show', methods=['GET'])
def show_on_map():
    my_cor = session.get('coords')
    return redirect(Picture.google_maps_search(keys=convertToStr(my_cor)))


if __name__ == '__main__':
    app.run(debug=True)

from app import app
from flask import render_template, request, redirect, flash, session
import os
from app.picture_locator import JpgPicFinder
from app.helpers import convertToStr
from app.errors import NoCoord


@app.route('/', methods=['POST', 'GET'])
def index() :
    if request.method == 'POST' :
        if request.files :
            pic = request.files ['image']
            try :
                pic.save(os.path.join(app.config ['IMAGE_UPLOADS'], pic.filename))
                data = JpgPicFinder.get_coords(os.path.join(app.config ['IMAGE_UPLOADS'], pic.filename))
                if data == {} :
                    raise NoCoord
                else :
                    coords = (round(data ['Latitude'], 7), round(data ['Longitude'], 7))
                    location = JpgPicFinder.search_location(coords)
                    session ['coords'] = coords
                    return render_template('update.html', location=location, coords=coords, filename=pic.filename)
            except IsADirectoryError :
                flash("Ups! Forgot to add a file didn't you?", 'error')
            except NoCoord :
                flash('No gps data available for current picture!', 'error')

    return render_template('update.html')


@app.route('/show', methods=['GET'])
def show_on_map() :
    # return render_template('map.html')
    my_cor = session.get('coords')
    return redirect('https://www.google.com/maps/' + 'search/?api=1&query=' + convertToStr(my_cor))

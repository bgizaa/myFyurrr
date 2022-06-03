import json
from xmlrpc.client import boolean
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from sqlalchemy import ForeignKey
from forms import *



app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    num_upcoming_shows = db.Column(db.Integer)
    genres = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_talent = boolean
    seeking_description = db.Column(db.String(120))
    shows = db.relationship('Show',
      backref=db.backref('veneues', lazy=True))


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    shows = db.relationship('Show',
      backref=db.backref('artists', lazy=True))


class Show(db.Model):
    __tablename__ = 'Show'

    db.Column('artist_id', db.Integer, db.ForeignKey('artist.id'), primary_key=True)
    db.Column('venue_id', db.Integer, db.ForeignKey('venue.id'), primary_key=True)
    date = db.Column(db.String)


def format_datetime(value, format='medium'):
    date = dateutil.parser.parse(value)
    if format == 'full':
        format = "EEEE MMMM, d, y 'at' h:mma"
    elif format == 'medium':
        format = "EE MM, dd, y h:mma"
    return babel.dates.format_datetime(date, format, locale='en')


app.jinja_env.filters['datetime'] = format_datetime


@app.route('/')
def index():
    return render_template('pages/home.html')


@app.route('/venues')
def venues():

    data = []
    return render_template('pages/venues.html', data=Venue.query.all())


@app.route('/venues/search', methods=['POST'])
def search_venues():
    response = {}
    return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))


@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
    data1 = {}
    data2 = {}
    data3 = {}
    data = list(filter(lambda d: d['id'] ==
                venue_id, [data1, data2, data3]))[0]
    return render_template('pages/show_venue.html', venue=data)


@app.route('/venues/create', methods=['GET'])
def create_venue_form():
    form = VenueForm()
    return render_template('forms/new_venue.html', form=form)


@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
    flash('Venue ' + request.form['name'] + ' was successfully listed!')
    return render_template('pages/home.html')


@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):

    return None


@app.route('/artists')
def artists():
    data = [{}, {}, {}]
    return render_template('pages/artists.html', data=Artist.query.all())


@app.route('/artists/search', methods=['POST'])
def search_artists():

    response = {
        "count": 1,
        "data": [{
        }]
    }
    return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))


@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):

    data1 = {}
    data2 = {}
    data3 = {}

    data = list(filter(lambda d: d['id'] ==
                artist_id, [data1, data2, data3]))[0]
    return render_template('pages/show_artist.html', artist=data)


@ app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
    form = ArtistForm()
    artist = {

    }

    return render_template('forms/edit_artist.html', form=form, artist=artist)


@ app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):

    return redirect(url_for('show_artist', artist_id=artist_id))


@ app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
    form = VenueForm()
    venue = {}

    return render_template('forms/edit_venue.html', form=form, venue=venue)


@ app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):

    return redirect(url_for('show_venue', venue_id=venue_id))


@ app.route('/artists/create', methods=['GET'])
def create_artist_form():
    form = ArtistForm()
    return render_template('forms/new_artist.html', form=form)


@ app.route('/artists/create', methods=['POST'])
def create_artist_submission():

    flash('Artist ' + request.form['name'] + ' was successfully listed!')

    return render_template('pages/home.html')


@ app.route('/shows')
def shows():

    data = [{
    }, {

    }, {

    }, {

    }, {

    }]
    return render_template('pages/shows.html', data=Show.query.all())


@ app.route('/shows/create')
def create_shows():

    form = ShowForm()
    return render_template('forms/new_show.html', form=form)


@ app.route('/shows/create', methods=['POST'])
def create_show_submission():
    artist_id = request.form['artist_id']
    venue_id = request.form['venue_id']
    start_time = request.form['start_time']
    artist = Artist(artist_id=artist_id)
    venue = Artist(venue_id=venue_id)
    time = Artist(start_time_id=start_time)
    db.session.add(artist, venue, time)
    db.session.commit()

    flash('Show was successfully listed!')

    return render_template('pages/home.html', data=Show.query.all())


@ app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@ app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')


if __name__ == '__main__':
    app.run()


'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''

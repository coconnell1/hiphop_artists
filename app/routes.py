from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Cobi'}

    return render_template('/index.html', title="Home", user=user)

@app.route('/artistList')
def artist_list():
    artists = [
        {
            'artist': 'Kendrick Lamar'
        },
        {
            'artist': 'Tupac'
        },
        {
            'artist': 'Nas'
        },
        {
            'artist': 'Eminem'
        },
        {
            'artist': 'Joey Bada$$'
        },
        {
            'artist': 'XXXTentacion'
        },
        {
            'artist': 'Childish Gambino'
        }
        ]

    return render_template('/artistList.html', title="List of Artists", artists=artists)

@app.route('/artistPage')
def artist_page():

    return render_template('/artistPage.html', title="Artist Page")

@app.route('/createArtist')
def create_artist():

    return render_template('/createArtist.html', title="Create New Artist")


from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import CreateArtist


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
    info = [
        {
            'artistName': 'Kendrick Lamar',
            'birth': 'Kendrick Lamar was born on June 17th, 1987 in Compton, California.',
            'music': 'He is known to be one of the best lyricists, and story-tellers in all of hip-hop.',
            'events': ' He is currently on tour, and his next concert is on September 14th in Denver, Colorado.'

        }

    ]

    return render_template('/artistPage.html', title="Artist Page", info=info)


@app.route('/createArtist', methods=['GET', 'POST'])
def create_artist():
    create = CreateArtist()
    if create.validate_on_submit():
        info = [
            {
                'artistName': create.name.data,

                'birth': create.birth.data,

                'music': create.music.data,

                'events': create.events.data

            }

        ]
        flash('New Artist Created:'.format(create.name.data, create.birth.data, create.music.data, create.events.data))

        return render_template('/artistPage.html', title="Artist Page", info=info)

    return render_template('/createArtist.html', title="Create New Artist", create=create)



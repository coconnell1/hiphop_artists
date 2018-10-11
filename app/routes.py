from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import CreateArtist
from app.models import Artist, Venue, Event, ArtistToEvent


@app.route('/')
@app.route('/index')
def index():

    return render_template('/index.html', title="Home")


@app.route('/artistList')
def artist_list():
    artists = Artist.query.all()

    return render_template('/artistList.html', title="List of Artists", artists=artists)


@app.route('/artistPage/<stagename>')
def artist_page(stagename):
    a = Artist.query.filter(Artist.stagename == stagename).first()
    if a is None:
        flash("Artist {} is not found.", format(stagename))
        return redirect(url_for("artist_list"))
    else:
        event_list = []
        for a2e in a.events:
            event_list.append(a2e.event)
        return render_template("artistPage.html", artist=a, event_list=event_list)


@app.route('/createArtist', methods=['GET', 'POST'])
def create_artist():
    createForm = CreateArtist()
    if createForm.validate_on_submit():
        art1 = Artist(stagename=createForm.name.data, birthday=createForm.birth.data, hometown=createForm.hometown.data, description=createForm.description.data)
        db.session.add(art1)
        db.session.commit()
        flash('New Artist Created!')
        return redirect(url_for("artist_list"))
    return render_template('/createArtist.html', title="Create New Artist", createForm=createForm)


@app.route('/reset_db')
def reset_db():
   flash("Resetting database: deleting old data and repopulating with dummy data")
   meta = db.metadata
   for table in reversed(meta.sorted_tables):
       print('Clear table {}'.format(table))
       db.session.execute(table.delete())
   db.session.commit()
   art = [Artist(stagename='Kendrick Lamar', birthday='June 7, 1987', hometown='Compton', description='Great lyricist'),
        Artist(stagename='Joey Bada$$', birthday='January 20, 1995', hometown='Brooklyn', description='Great rapper'),
        Artist(stagename='Childish Gambino', birthday='September 25, 1983', hometown='Edwards Base', description='talented'),
        Artist(stagename='Eminem', birthday='October 17th, 1972', hometown='Detroit', description='great storyteller')]

   for a in art:
       db.session.add(a)
       db.session.commit()

   ven = Venue(venuename='Ithaca Commons', address='123', city='Ithaca', state='NY')
   ven1 = Venue(venuename='Staples Center', address='456', city='Las Angeles', state='CA')
   ven2 = Venue(venuename='Madison Square Garden', address='789', city='NYC', state='NY')
   db.session.add(ven)
   db.session.add(ven1)
   db.session.add(ven2)
   db.session.commit()

   even = [Event(eventname='Ithaca Festival', capacity='20000', venue_venueid='1'),
        Event(eventname='New York State Festival', capacity='30000', venue_venueid='2')]

   for c in even:
       db.session.add(c)
       db.session.commit()

   arttoeven = [ArtistToEvent(artist_artistid='1', event_eventid='1'),
        ArtistToEvent(artist_artistid='2', event_eventid='1'),
        ArtistToEvent(artist_artistid='2', event_eventid='2')]

   for d in arttoeven:
       db.session.add(d)
       db.session.commit()

   return render_template('/index.html', title="Home")





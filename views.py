import flask
import redis
import datetime
from app import db
from flask import render_template
import models
red = redis.StrictRedis()

def event_stream(channel_name):
    pubsub = red.pubsub()
    pubsub.subscribe(channel_name)
    for message in pubsub.listen():
        print message
        yield 'data: %s\n\n' % message['data']


def login():
    if flask.request.method == 'POST':
        flask.session['user'] = flask.request.form['user']
        u = models.User(nickname=flask.request.form['user'])
        db.session.add(u)
        db.session.commit()
        return flask.redirect('/')
    return render_template('login.html')


def post(channel_name):
    message = flask.request.form['message']
    user = flask.session.get('user', 'anonymous')
    now = datetime.datetime.now().replace(microsecond=0).time()
    red.publish(channel_name, u'[%s] %s: %s' % (now.isoformat(), user, message))
    return flask.Response(status=204)


def stream(channel_name):
    return flask.Response(event_stream(channel_name),
                          mimetype="text/event-stream")

def index():
    if 'user' not in flask.session:
        return flask.redirect('/login')
    channels = models.Channel.query.all()
    return render_template("index.html", channels = channels)


def channel(channel_name):
    channels = models.Channel.query.all()
    return render_template("channel.html", channels = channels, user = flask.session['user'], channel_name = channel_name)   


def add_channel():
    channel_name = flask.request.form['channel_name']
    db.session.add(models.Channel(channel_name = channel_name))
    db.session.commit()
    return flask.redirect('/channel/' + channel_name)


def unsubscribe(channel_name):
    pubsub = red.pubsub()
    pubsub.unsubscribe(channel_name)
    return flask.redirect("/")


def search_channel():
    requested_name = flask.request.form['search_channel']
    channels = models.Channel.query.filter(requested_name == models.Channel.channel_name).all()
    return render_template("index.html", channels = channels)
















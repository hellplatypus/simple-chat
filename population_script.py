from app import db
import models

db.session.add(models.User(nickname='user1'))
db.session.add(models.User(nickname='user2'))
db.session.add(models.User(nickname='user3'))


db.session.add(models.Channel(channel_name='channel1'))
db.session.add(models.Channel(channel_name='channel2'))
db.session.add(models.Channel(channel_name='channel3'))

db.session.commit()

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    
    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Channel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    channel_name = db.Column(db.String(64), index = True, unique = True)

    def __repr__(self):
        return '<Channel %r>' % (self.channel_name)

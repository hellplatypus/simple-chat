from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'asd'
db = SQLAlchemy(app)
app.config.from_object('config')


import views 
import models 


app.add_url_rule('/login', view_func=views.login, methods = ['GET', 'POST'])
app.add_url_rule('/post/<channel_name>', view_func=views.post, methods = ['POST'])
app.add_url_rule('/stream/<channel_name>', view_func=views.stream)
app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/channel/<channel_name>', view_func=views.channel, methods = ['GET', 'POST'])
app.add_url_rule('/add_channel', view_func=views.add_channel, methods = ['POST'])
app.add_url_rule('/unsubscribe/<channel_name>', view_func=views.unsubscribe, methods = ['POST'])
app.add_url_rule('/search_channel', view_func=views.search_channel, methods = ['POST'])

if __name__ == '__main__': 
    app.debug = True
    app.run()


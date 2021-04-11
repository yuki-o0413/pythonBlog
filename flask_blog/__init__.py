from flask import Flask
#flaskを使う

app = Flask(__name__)
app.config.from_object('flask_blog.config')

import flask_blog.views
#処理命令をvies.pyに受けわたす
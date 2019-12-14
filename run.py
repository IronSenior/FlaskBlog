from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
from flask_login import current_user

import uuid
import os
from .forms import PostForm
from flask_login import LoginManager


from .src.user.repository.userRepository import UserRepository

from .src.user.application.auth import auth
from .src.post.application.post import post
from .src.comment.application.comment import comment

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]

app.register_blueprint(auth)
app.register_blueprint(post)
app.register_blueprint(comment)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    userRepository = UserRepository()
    return userRepository.getById(user_id)


@app.route('/', methods=['GET'])
def index():
    if current_user.is_authenticated:
        return redirect("/post/index/")
    return render_template('index.html')

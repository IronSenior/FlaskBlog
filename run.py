from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
import uuid
import os
from .forms import PostForm
from flask_login import LoginManager

from .src.user.model.user import User
from .src.user.model.username import Username
from .src.user.model.fullname import Fullname
from .src.user.model.usermail import UserMail
from .src.user.model.userId import UserId
from .src.user.repository.userRepository import UserRepository

from .src.user.application.auth import auth

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]

app.register_blueprint(auth)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    userRepository = UserRepository()
    return userRepository.getById(user_id)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/newPost', methods=['GET'])
def newPost():
    return render_template("post_form.html", form=PostForm())

@app.route('/newPost/send/', methods=['POST'])
def newPostSend():
    form = PostForm()
    if form.validate_on_submit():
        data = get_post_data(form)
        #TODO
        return redirect(url_for('index'))
    return render_template('post_form.html', form=form)


def get_post_data(form: PostForm):
    return {
        'title' : form.title.data,
        'title_slug' : form.title_slug.data,
        'content' : form.content.data
    }
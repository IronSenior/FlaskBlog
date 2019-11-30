from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
import uuid
import os
from .forms import SignupForm, PostForm


from .src.user.model.user import User
from .src.user.model.username import Username
from .src.user.model.fullname import Fullname
from .src.user.model.usermail import UserMail
from .src.user.model.userId import UserId
from .src.user.repository.userRepository import UserRepository

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/signup/', methods=['GET'])
def signup():
    return render_template('signup_form.html', form=SignupForm())


@app.route('/signup/send/', methods=['POST'])
def signupSend():
    form = SignupForm()
    if form.validate_on_submit():
        data = get_user_data(form)
        user = User(UserId(uuid.uuid4()), Username.fromString(data["name"]), UserMail.fromString(data["email"]), Fullname.fromString(data.get("fullname", "NO Name")))
        repository = UserRepository()
        repository.add(user)
        return redirect(url_for('index'))

    return render_template('signup_form.html', form=form)

def get_user_data(form: SignupForm):
    return {
        'name': form.name.data,
        'email': form.email.data,
        'password': form.password.data,
    }


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
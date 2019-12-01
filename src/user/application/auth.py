from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user 


import uuid

from .forms import SignupForm
from .forms import LoginForm

from ..model.user import User
from ..model.usermail import UserMail
from ..model.username import Username
from ..model.userId import UserId
from ..model.fullname import Fullname
from ..model.password import Password
from ..repository.userRepository import UserRepository


auth = Blueprint('auth', __name__, url_prefix="/auth", template_folder='templates')


@auth.route('/signup/', methods=['GET'])
def signup():
    return render_template('signup_form.html', form=SignupForm())


@auth.route('/signup/send/', methods=['POST'])
def signupSend():
    form = SignupForm()
    userRepository = UserRepository()

    if not form.validate_on_submit():
        # TODO Redirect to GET method
        return render_template('signup_form.html', form=form)
    
    user = get_user_from_data(form)
    userRepository.add(user)

    return redirect(url_for('index'))

    
def get_user_from_data(form: SignupForm):
    user = User(
        userid = UserId(uuid.uuid4()),
        username = Username.fromString(form.username.data),
        userMail = UserMail.fromString(form.email.data),
        userFullname = Fullname.fromString(form.fullname.data),
        password = Password.fromString(form.password.data)
    )
    return user


@auth.route('/login/', methods=['GET'])
def login():
    return render_template('login_form.html', form=LoginForm())


@auth.route('/login/send/', methods=['POST'])
def loginSend():
    form = LoginForm()
    userRepository = UserRepository()

    if not form.validate_on_submit():
        #TODO Redirect to GET method
        return render_template('login_form.html', form=form)
    
    user = userRepository.getByEmail(UserMail.fromString(form.email.data))

    if not user:
        return render_template('login_form.html', form=form)

    if not user.verifyPassword(form.password.data):
        return render_template('login_form.html', form=form)

    login_user(user)
    return redirect(url_for("index"))


@auth.route('/logout/', methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
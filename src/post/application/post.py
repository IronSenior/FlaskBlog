from flask import Blueprint
from flask import render_template
from flask import url_for
from flask import redirect
from flask import abort

from flask_login import current_user
from flask_login import login_required

import uuid
from uuid import UUID

from .forms import NewPostForm
from ..repository.postRepository import PostRepository

from ..model.post import Post
from ..model.postId import PostId
from ..model.postTitle import PostTitle
from ..model.postSubtitle import PostSubtitle
from ..model.postContent import PostContent

from ...user.model.userId import UserId
from ...user.repository.userRepository import UserRepository


post = Blueprint('post', __name__, url_prefix="/post", template_folder='templates')


@post.route('/new/', methods=["GET"])
@login_required
def new():
    return render_template('newPost_form.html', form=NewPostForm())


@post.route('/new/send/', methods=["POST"])
@login_required
def newSend():
    form = NewPostForm()
    postRepository = PostRepository()

    if not form.validate_on_submit():
        # TODO Redirect to GET method
        return render_template('signup_form.html', form=form)
    
    post = get_post_from_data(form)
    postRepository.add(post)

    return redirect(url_for('index'))

def get_post_from_data(form: NewPostForm):
    post = Post(
        postid=PostId(uuid.uuid4()),
        userid=UserId(current_user.userId),
        title=PostTitle.fromString(form.title.data),
        subtitle=PostSubtitle.fromString(form.subtitle.data),
        content=PostContent.fromString(form.content.data)
    )
    return post


@post.route('/index/', methods=["GET"])
def postIndex():
    postRepository = PostRepository()
    posts = postRepository.getAll() or []

    return render_template('postIndex.html', posts=posts)


@post.route('/<postid>/', methods=["GET"])
def getPost(postid: str):
    checkId(postid)
    postRepository = PostRepository()
    userRepository = UserRepository()
    post = postRepository.getById(UUID(postid))

    if not post:
        abort(404)

    author = userRepository.getById(post.userid)
    return render_template('postPage.html', post=post, author=author)

def checkId(parameterId: str):
    try:
        UUID(parameterId)
    except:
        abort(404)


@post.route('/user/<userid>/', methods=["GET"])
def userPosts(userid: str):
    checkId(userid)
    postRepository = PostRepository()
    userRepository = UserRepository()

    posts = postRepository.getByUserId(UUID(userid)) or []
    author = userRepository.getById(UUID(userid))

    if not author:
        abort(404)

    return render_template('userPosts.html', posts=posts, author=author)
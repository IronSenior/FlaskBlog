from flask import Blueprint
from flask import redirect
from flask import abort
from flask_login import current_user

import uuid
from uuid import UUID

from ..repository.commentRepository import CommentRepository
from ..model.comment import Comment
from ..model.commentId import CommentId
from ..model.commentContent import CommentContent

from ...user.model.userId import UserId
from ...user.model.username import Username
from ...post.model.postId import PostId

from .forms import NewCommentForm


comment = Blueprint('comment', __name__, url_prefix="/comment", template_folder="template")

@comment.route("/new/<postid>", methods=["POST"])
def newComment(postid):
    checkId(postid)
    form = NewCommentForm()
    commentRepository = CommentRepository()

    if not form.validate_on_submit():
        return redirect("/post/%s" %(postid))
    
    comment = get_comment_from_data(form, postid)
    commentRepository.add(comment)
    return redirect("/post/%s" %(postid))


@comment.route("/new/<postid>/<parentid>", methods=["POST"])
def newChildComment(postid, parentid):
    checkId(parentid)
    checkId(postid)
    form = NewCommentForm()
    commentRepository = CommentRepository()

    if not form.validate_on_submit():
        return redirect("/post/%s" %(postid))
    
    comment = get_comment_from_data(form, postid, parentid)
    commentRepository.add(comment)
    return redirect("/post/%s" %(postid))


def checkId(parameterId: str):
    try:
        UUID(parameterId)
    except:
        abort(404)


def get_comment_from_data(form: NewCommentForm, postid: str, parentid: str = None):
    return Comment(
        commentid=CommentId(uuid.uuid4()),
        userid=UserId(current_user.userId),
        postid=PostId.fromString(postid),
        username=Username.fromString(current_user.username),
        content=CommentContent.fromString(form.content.data),
        parentid = CommentId.fromString(parentid) if parentid else None
    )



from flask import jsonify, Response

from oasis import app, db
from oasis.models import Post
from oasis.schamas import post_schema


@app.get('/api/post/list')
def get_post_list() -> Response:
    posts = db.session.query(Post).\
        order_by(Post.updated_at.desc()).\
        all()
    return jsonify(posts=post_schema.dump(posts, many=True))


@app.post('/api/post/save')
def save_post() -> dict:
    return {}


@app.post('/api/post/delete')
def delete_post() -> dict:
    return {}

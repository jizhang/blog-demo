from typing import List

from flask import jsonify, Response

from nasa import app, db
from nasa.models import User


@app.get('/api/user/list')
def get_user_list() -> Response:
    users: List[User] = db.session.query(User).all()
    return jsonify(users=users)

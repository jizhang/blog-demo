from flask import jsonify, Response

from nasa import app, db
from nasa.models import User


@app.get('/api/user/list')
def get_user_list() -> Response:
    rows = db.session.query(User).all()
    return jsonify(users=rows)

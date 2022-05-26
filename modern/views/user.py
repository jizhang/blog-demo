from flask import current_app, jsonify, Response


@current_app.get('/api/user/list')
def get_user_list() -> Response:
    return jsonify(users=[])

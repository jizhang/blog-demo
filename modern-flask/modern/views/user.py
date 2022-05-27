import logging

from flask import current_app, jsonify, Response

from modern.services import user as user_svc

logger = logging.getLogger(__name__)


@current_app.get('/api/user/list')
def get_user_list() -> Response:
    logger.info('Get user list in view.')

    user_list = user_svc.get_user_list()
    users = []
    for user in user_list:
        users.append({
            'id': user.id,
            'username': user.username,
        })

    return jsonify(users=users)

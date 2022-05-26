import logging

from flask import current_app, jsonify, Response

logger = logging.getLogger(__name__)


@current_app.get('/api/user/list')
def get_user_list() -> Response:
    logger.info('Get user list')
    return jsonify(users=[])

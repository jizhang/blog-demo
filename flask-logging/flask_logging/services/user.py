import logging
from typing import List

from flask_logging import db
from flask_logging.models.user import User

logger = logging.getLogger(__name__)


def get_user_list() -> List[User]:
    logger.info('Get user list in service.')
    return db.session.query(User).all()

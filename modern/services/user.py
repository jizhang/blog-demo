import logging
from typing import List

from modern import db
from modern.models.user import User

logger = logging.getLogger(__name__)


def get_user_list() -> List[User]:
    logger.info('Get user list in service.')
    return db.session.query(User).all()

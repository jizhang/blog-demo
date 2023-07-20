import logging

from flask import current_app

from flask_logging import db
from flask_logging.models.user import User

logger = logging.getLogger(__name__)


@current_app.cli.command('user_count')
def run():
    """Get user count."""
    count = db.session.query(User).count()
    logger.info(f'Result: {count}')

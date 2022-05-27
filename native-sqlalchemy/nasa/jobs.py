from nasa import app, db
from nasa.models import User


@app.cli.command('user_count')
def user_count():
    """Get user count."""
    result = db.session.query(User).count()
    app.logger.info(f'Result: {result}')

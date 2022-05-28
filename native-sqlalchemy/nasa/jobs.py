from flask.cli import AppGroup

from nasa import app, db
from nasa.models import User

job_cli = AppGroup('job', help='Run jobs.')
app.cli.add_command(job_cli)


@job_cli.command('user_count')
def user_count():
    """Get user count."""
    result = db.session.query(User).count()
    app.logger.info(f'Result: {result}')

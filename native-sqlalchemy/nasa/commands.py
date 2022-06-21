from nasa import app, db
from nasa.models import Base, User


@app.cli.command()
def init_db():
    """Initialize database."""
    Base.metadata.create_all(db.session.get_bind())


@app.cli.command()
def user_count():
    """Get user count."""
    result = db.session.query(User).count()
    app.logger.info(f'User count: {result}')

from nasa import app, db, db_multi
from nasa.models import Base, User


@app.cli.command()
def init_db() -> None:
    """Initialize database."""
    Base.metadata.create_all(db.session.get_bind())


@app.cli.command()
def user_count() -> None:
    """Get user count."""
    result = db.session.query(User).count()
    app.logger.info(f'User count: {result}')


@app.cli.command()
def product_db() -> None:
    """Access product database."""
    row = db_multi.session('product_db').execute('PRAGMA database_list').fetchone()
    app.logger.info(f'Current database file: {row.file}')

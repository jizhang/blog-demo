from nasa import app, db, db_multi, db_alpha
from nasa.models import Base, User

from sqlalchemy import text


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
    db_file = db_multi.get_session('product_db').execute(
        text("""
        SELECT `file` FROM pragma_database_list
        WHERE `name` = :name
        """),
        {
            'name': 'main',
        }
    ).scalar()
    app.logger.info(f'Database file: {db_file}')


@app.cli.command()
def use_alpha() -> None:
    """Test alpha extension."""
    user_count = db_alpha.engine.execute('SELECT COUNT(*) FROM `user`').scalar_one()
    app.logger.info(f'User count: {user_count}')

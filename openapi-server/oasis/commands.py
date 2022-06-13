from oasis import app, db


@app.cli.command()
def init_db():
    """Initialize database."""
    import oasis.models
    db.create_all()

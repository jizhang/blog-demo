from apipydantic import app


@app.get('/')
def index() -> str:
    return 'hello world'

from apipydantic import app


@app.get('/')
def index() -> str:
    return 'hello world'


from . import article, spectree_demo, sqlmodel_demo, user

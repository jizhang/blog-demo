from oasis import app


@app.get('/api/ping')
def ping() -> str:
    return 'pong'

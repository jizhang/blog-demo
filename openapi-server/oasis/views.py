from oasis import app


@app.get('/api/post/list')
def get_post_list() -> dict:
    return {}


@app.post('/api/post/save')
def save_post() -> dict:
    return {}


@app.post('/api/post/delete')
def delete_post() -> dict:
    return {}

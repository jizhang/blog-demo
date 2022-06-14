from flask import jsonify, Response

from oasis import app, db
from oasis.models import Post
from oasis.schemas import post_schema


@app.get('/api/post/list')
def get_post_list() -> Response:
    """
    ---
    get:
      summary: Get post list.
      tags: [post]
      x-swagger-router-controller: oasis.views
      operationId: get_post_list
      parameters:
        - in: query
          name: page
          schema:
            type: integer
            minimum: 1
        - in: query
          name: sort
          schema:
            type: string
            enum: [asc, desc]
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                properties:
                  posts:
                    type: array
                    items:
                      $ref: '#/components/schemas/Post'
    """
    posts = db.session.query(Post).\
        order_by(Post.updated_at.desc()).\
        all()
    return jsonify(posts=post_schema.dump(posts, many=True))


@app.post('/api/post/save')
def save_post() -> dict:
    return {}


@app.post('/api/post/delete')
def delete_post() -> dict:
    return {}

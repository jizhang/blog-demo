from flask import request, jsonify, Response
from marshmallow import ValidationError

from oasis import app, db, AppError
from oasis.models import Post
from oasis.schemas import post_schema

PAGE_SIZE = 10


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
    page = int(request.args.get('page', '1'))
    sort = request.args.get('sort', 'desc')

    query = db.session.query(Post)
    if sort == 'desc':
        query = query.order_by(Post.updated_at.desc())

    query = query.offset((page - 1) * PAGE_SIZE).limit(PAGE_SIZE)
    posts = query.all()
    return jsonify(posts=post_schema.dump(posts, many=True))


@app.post('/api/post/save')
def save_post() -> dict:
    """
    ---
    post:
      summary: Save post
      tags: [post]
      x-swagger-router-controller: oasis.views
      operationId: save_post
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Post'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
    """
    try:
        post_form = post_schema.load(request.form)
    except ValidationError as e:
        raise AppError(e.messages)

    post = Post(**post_form)
    post = db.session.merge(post)
    db.session.commit()
    return jsonify({'id': post.id})


@app.post('/api/post/delete')
def delete_post() -> dict:
    return {}

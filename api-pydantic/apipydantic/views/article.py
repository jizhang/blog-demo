from datetime import datetime
from decimal import Decimal
from enum import Enum, IntEnum
from pprint import pprint
from typing import Annotated, Optional
from uuid import uuid4

from flask import request, url_for
from pydantic import BaseModel, BeforeValidator, Field, PrivateAttr, computed_field

from apipydantic import app


class Article(BaseModel):
    id: int
    title: str
    category_id: int

    _categories: dict[int, str] = PrivateAttr(default_factory=dict)

    @computed_field  # type: ignore[misc]
    @property
    def link(self) -> str:
        return url_for('article', id=self.id)

    @computed_field  # type: ignore[misc]
    @property
    def category_name(self) -> str:
        return self._categories.get(self.category_id, 'N/A')


class ArticleListResponse(BaseModel):
    articles: list[Article]


@app.get('/article/list')
def article_list() -> dict:
    article = Article(id=1, title='Python Static Type Check', category_id=2)
    article._categories = {
        1: 'Big Data',
        2: 'Programming',
    }
    response = ArticleListResponse(articles=[article])
    return response.model_dump(mode='json')


@app.get('/article/<int:id>')
def article(id: int) -> dict:
    article = Article(id=1, title='Python Static Type Check', category_id=2)
    return article.model_dump(mode='json')


def parse_tags(tags: str) -> list[str]:
    return tags.split(',')


TagList = Annotated[list[str], BeforeValidator(parse_tags)]

class OrderBy(str, Enum):
    ASC = 'asc'
    DESC = 'desc'

class Category(IntEnum):
    BIG_DATA = 1
    PROGRAMMING = 2

class SearchForm(BaseModel):
    keyword: Optional[str] = Field(default=None)

    tags: TagList = Field(default_factory=list)
    create_time: datetime = Field(default_factory=datetime.now)
    uuid: str = Field(default_factory=lambda: uuid4().hex)

    order_by: OrderBy
    category: Category

    # @field_validator('tags', mode='before')
    # @classmethod
    # def validate_tags(cls, value: str) -> list[str]:
    #     return value.split(',')

    # @model_validator(mode='before')
    # @classmethod
    # def validate_model(cls, data: dict[str, Any]) -> dict[str, Any]:
    #     if not data['keyword'].strip():
    #         data['keyword'] = None
    #     return data


@app.get('/article/search')
def article_search() -> dict:
    pprint(request.args)
    form = SearchForm.model_validate(request.args.to_dict())
    print(form.order_by == OrderBy.ASC)
    print(form.category == Category.PROGRAMMING)
    return form.model_dump(mode='json')


class ConversionForm(BaseModel):
    int_value: int
    decimal_value: Decimal
    bool_value: bool
    datetime_value: datetime
    array_value: list[int]
    object_value: dict[str, int]


@app.get('/article/demo')
def article_demo() -> dict:
    # form = ConversionForm(
    #     int_value='10',
    #     decimal_value='10.24',
    #     bool_value='true',
    #     datetime_value='2024-01-27 17:02:00',
    #     array_value=(1, '2'),
    #     object_value={'key': False},
    # )
    form = ConversionForm.model_validate({
        'int_value': '10',
        'decimal_value': '10.24',
        'bool_value': 'true',
        'datetime_value': '2024-01-27 17:02:00',
        'array_value': [1, '2'],
        'object_value': {'key': '10'},
    })
    return form.model_dump(mode='json')

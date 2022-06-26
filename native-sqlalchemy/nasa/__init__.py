from flask import Flask

from . import default_settings
from .custom_encoder import CustomEncoder
from .sqlalchemy import SQLAlchemy
from .sqlalchemy_multi import SQLAlchemyMulti
from .sqlalchemy_alpha import SQLAlchemyAlpha

app = Flask(__name__)
app.config.from_object(default_settings)
app.json_encoder = CustomEncoder

db = SQLAlchemy(app)
db_multi = SQLAlchemyMulti(app)
db_alpha = SQLAlchemyAlpha(app)

from . import views, commands

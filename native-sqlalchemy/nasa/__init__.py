from flask import Flask

from . import default_settings
from .custom_encoder import CustomEncoder
from .sqlalchemy import SQLAlchemy
from .sqlalchemy_multi import SQLAlchemyMulti

app = Flask(__name__)
app.config.from_object(default_settings)
app.json_encoder = CustomEncoder

db = SQLAlchemy(app)
db_multi = SQLAlchemyMulti(app)

from . import views, commands

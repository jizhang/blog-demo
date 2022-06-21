from flask import Flask

from . import default_settings
from .custom_encoder import CustomEncoder
from .sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(default_settings)
app.json_encoder = CustomEncoder
db = SQLAlchemy(app)

from . import views, commands

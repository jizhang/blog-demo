from flask import Flask

from . import default_settings
from .sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(default_settings)
db = SQLAlchemy(app)


from . import views, commands

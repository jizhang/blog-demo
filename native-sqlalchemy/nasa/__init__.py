from flask import Flask

from . import config
from .sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


from . import views, jobs

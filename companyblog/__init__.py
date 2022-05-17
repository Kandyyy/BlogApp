from flask import Flask

app = Flask(__name__)

from companyblog.core.views import core
from companyblog.core.error_pages.handlers import error
app.register_blueprint(core)
app.register_blueprint(error)
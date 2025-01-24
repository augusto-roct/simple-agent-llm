from flask_api import FlaskAPI
from flasgger import Swagger

from app.routes import agent_blueprint


app = FlaskAPI(__name__)

app.register_blueprint(agent_blueprint, url_prefix="/api/v1/agent")

swagger = Swagger(app)

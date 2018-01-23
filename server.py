from algorithm_services.config import config
from algorithm_services.app import create_app

app = create_app(__name__, config)
app.run()

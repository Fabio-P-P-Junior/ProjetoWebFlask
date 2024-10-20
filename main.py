from flask import Flask
from routes.home import home_route

#inicializacao do flash
app = Flask(__name__)

app.register_blueprint(home_route)

app.run(debug=True)
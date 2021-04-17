import flask
import mongoengine
import controllers

# Creating the flask app
app = flask.Flask(__name__)

# Conencting the database
mongoengine.connect( "weekly", host="localhost", port=27017 )

# Registering routes
controllers.TaskController.register_routes(app)


if __name__ == "__main__":
    app.run( "localhost", 5000 )
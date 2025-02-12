from flask import Flask
from views import views  # Import the Blueprint

app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask server

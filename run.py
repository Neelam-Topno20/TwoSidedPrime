from flask import Flask


def create_app():
    # creating a flask app
    app = Flask(__name__)

    # embedding the app name with the uri
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/pyrestapi')

    return app


# Launching the application
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

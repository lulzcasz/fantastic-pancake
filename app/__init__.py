from flask import Flask

from .blog import blog as blog_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(blog_bp)

    return app

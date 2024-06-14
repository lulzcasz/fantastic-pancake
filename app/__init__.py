from flask import Flask

def create_app():
    app = Flask(__name__)

    from .blog import blog as blog_bp
    app.register_blueprint(blog_bp)

    return app

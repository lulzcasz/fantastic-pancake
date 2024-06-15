from flask import render_template, request, abort

from . import blog

@blog.route('', methods = ['GET'])
def index():
    return render_template('blog/index.html')

@blog.route('world', methods = ['GET'])
def world():
    if not 'HX-Request' in request.headers: return abort(404)

    return render_template('blog/partials/world.html')

from flask import Blueprint


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return "Please, go to '/admin' endpoint."

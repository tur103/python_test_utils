from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route('/', methods=["GET"])
    def hello_world():
        return "hello world"

    return app


def function_to_test(number: int) -> int:
    if number == 0:
        raise ValueError
    else:
        return number

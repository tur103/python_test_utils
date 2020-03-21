from typing import Callable
from flask import Flask
from flask.testing import FlaskClient

from api.flask_app.api_validation import ApiValidation


def create_app_client(app_factory: Callable[[], Flask]) -> FlaskClient:
    """
    Create a client for the accepted flask app in order to test it.
    :param app_factory: The factory that creates the app we want to test.
    :return: A client for the tested app.
    """
    app = app_factory()
    app.testing = True
    app_client = app.test_client()
    return app_client


def create_api_validation(app_factory: Callable[[], Flask]) -> ApiValidation:
    """
    Create an api validation object that can be used to validate a flask api.
    :param app_factory: The factory that creates the app we want to test.
    :return: An ApiValidation object to validate the flask api.
    """
    app_client = create_app_client(app_factory)
    api_validation = ApiValidation(app_client=app_client)
    return api_validation

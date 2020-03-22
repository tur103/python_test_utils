from api.flask_api.flask_api_validation import FlaskApiValidation
from mock.mocker import Mocker
from test_examples.create_flask_app import create_app
from flask import Response


def test_example_using_mock():
    mocking_maps = [('flask.testing.FlaskClient.get', Response(status=200))]
    with Mocker(patchers=mocking_maps) as mocks:
        api = FlaskApiValidation.create_api_validation(app_factory=create_app)
        api.validate_route_existence(request_method_type="GET", url_prefix="/not_existing_route")

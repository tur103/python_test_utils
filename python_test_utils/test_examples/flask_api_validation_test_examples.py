from python_test_utils.test_examples.create_flask_app import create_app
from python_test_utils.api.flask_api.flask_api_validation import FlaskApiValidation


def test_example_validate_route_existence():
    api = FlaskApiValidation.create_api_validation(app_factory=create_app)
    api.validate_route_existence(request_method_type="GET", url_prefix="/")


def test_example_validate_response_from_request():
    api = FlaskApiValidation.create_api_validation(app_factory=create_app)
    api.validate_response_from_request(request_method_type="GET", url_prefix="/", response_expected_status_code=200,
                                       response_expected_body="hello world")

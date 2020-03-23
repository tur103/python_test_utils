from python_test_utils.test_examples.utils_for_test_examples import create_app
from python_test_utils.test_expansion import TestExpansion


class TestExampleFlaskApiValidation(TestExpansion):
    def test_example_validate_route_existence(self):
        api = self.flask_api_validation.create_api_validation(app_factory=create_app)
        api.validate_route_existence(request_method_type="GET", url_prefix="/")

    def test_example_validate_response_from_request(self):
        api = self.flask_api_validation.create_api_validation(app_factory=create_app)
        api.validate_response_from_request(request_method_type="GET", url_prefix="/", response_expected_status_code=200,
                                           response_expected_body="hello world")

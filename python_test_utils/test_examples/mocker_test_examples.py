from flask import Response

from python_test_utils.test_examples.utils_for_test_examples import create_app
from python_test_utils.test_expansion import TestExpansion


class TestExampleMocker(TestExpansion):
    def test_example_using_mock(self):
        mocking_maps = [('flask.testing.FlaskClient.get', Response(status=200))]
        with self.mocker(patchers=mocking_maps) as mocks:
            api = self.flask_api_validation.create_api_validation(app_factory=create_app)
            api.validate_route_existence(request_method_type="GET", url_prefix="/not_existing_route")

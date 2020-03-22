from flask.testing import FlaskClient
from typing import Callable
from flask import Flask


class FlaskApiValidation:
    """
    Validation tests for the flask api.
    The validation can validate that the api controllers are exist
    or that the requests to the api controllers response the desired result.
    """
    def __init__(self, app_client: FlaskClient):
        self.client = app_client
        self.request_methods_map = {"GET": self.client.get, "POST": self.client.post, "OPTIONS": self.client.options,
                                    "DELETE": self.client.delete, "PUT": self.client.put, "HEAD": self.client.head,
                                    "TRACE": self.client.trace, "PATCH": self.client.patch}
        self.not_exists_status_codes = [404, 405]

    def validate_route_existence(self, request_method_type: str, url_prefix: str):
        """
        Validation for an existence of a single route.
        :param request_method_type: The method type of the route
        :param url_prefix: The url prefix for the controller.
        """
        if request_method_type not in self.request_methods_map:
            raise ValueError("The request method type is invalid\n"
                             "Use GET, POST, OPTIONS, DELETE, PUT, HEAD, TRACE or PATCH")

        request_method = self.request_methods_map[request_method_type]
        response = request_method(path=url_prefix)

        assert response.status_code not in self.not_exists_status_codes

    def validate_response_from_request(self, request_method_type: str, url_prefix: str,
                                       response_expected_status_code: int, request_body=None,
                                       response_expected_body=None):
        """
        Validate that the accepted request to the app returns the expected response.
        :param request_method_type: The method type of the route
        :param url_prefix: The url prefix for the controller.
        :param response_expected_status_code: The expected status code of the returns response.
        :param request_body: The body to send with the request to the app.
        :param response_expected_body: The expected returned body from the request.
        """
        self.validate_route_existence(request_method_type=request_method_type, url_prefix=url_prefix)

        request_method = self.request_methods_map[request_method_type]
        response = request_method(path=url_prefix, data=request_body)

        response_decoded_body = response.get_json() if response.get_json() else response.get_data().decode(encoding="utf-8")

        assert response.status_code == response_expected_status_code and response_decoded_body == response_expected_body

    @staticmethod
    def create_app_client(app_factory: Callable[[], Flask]) -> FlaskClient:
        """
        Create a client for the accepted flask app in order to test_examples it.
        :param app_factory: The factory that creates the app we want to test_examples.
        :return: A client for the tested app.
        """
        app = app_factory()
        app.testing = True
        app_client = app.test_client()
        return app_client

    @staticmethod
    def create_api_validation(app_factory: Callable[[], Flask]):
        """
        Create an api validation object that can be used to validate a flask api.
        :param app_factory: The factory that creates the app we want to test_examples.
        :return: An ApiValidation object to validate the flask api.
        """
        app_client = FlaskApiValidation.create_app_client(app_factory=app_factory)
        api_validation = FlaskApiValidation(app_client=app_client)
        return api_validation

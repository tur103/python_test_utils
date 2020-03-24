import pytest
from typing import Type, Callable, List

from python_test_utils.api.flask_api.flask_api_validation import FlaskApiValidation
from python_test_utils.mock.mocker import Mocker
from python_test_utils.database.neo4j.neo4j_graph_validation import Neo4jGraphValidation
from python_test_utils.database.sql.sql_database_validation import SqlDatabaseValidation


class TestExpansion:
    """
    The test utils expansion that a new test class should inherit in order to get all the helpers.
    """
    @property
    def flask_api_validation(self) -> Type[FlaskApiValidation]:
        """
        A validation utils for a flask api.
        """
        return FlaskApiValidation

    @property
    def mocker(self) -> Type[Mocker]:
        """
        A utils for mocking objects.
        """
        return Mocker

    @property
    def neo4j_graph_validation(self) -> Type[Neo4jGraphValidation]:
        """
        A validation utils for running neo4j queries.
        """
        return Neo4jGraphValidation

    @property
    def sql_database_validation(self) -> Type[SqlDatabaseValidation]:
        """
        A validation utils for running sql queries.
        """
        return SqlDatabaseValidation

    @staticmethod
    def validate_function_result(function: Callable, arguments_list: List[dict], expected_result_list: list):
        """
        Helper for testing a function with given arguments for the expected result.
        :param function: THe function that we want to test.
        :param arguments_list: The list of arguments map to call the function with.
        :param expected_result_list: The list of expected results corresponding to the arguments list.
        """
        for arguments, expected_result in zip(arguments_list, expected_result_list):
            result = function(**arguments)
            assert expected_result == result

    @staticmethod
    def validate_function_exception(function: Callable, arguments_list: List[dict],
                                    expected_exception_list: List[Type[Exception]]):
        """
        Helper for testing a function with given arguments and expecting for an exception to be raised.
        :param function: THe function that we want to test.
        :param arguments_list: The list of arguments map to call the function with.
        :param expected_exception_list: The list of expected exceptions corresponding to the arguments list.
        """
        for arguments, expected_exception in zip(arguments_list, expected_exception_list):
            with pytest.raises(expected_exception=expected_exception):
                function(**arguments)

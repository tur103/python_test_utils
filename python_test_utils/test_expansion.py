from typing import Type

from python_test_utils.api.flask_api.flask_api_validation import FlaskApiValidation
from python_test_utils.mock.mocker import Mocker
from python_test_utils.database.neo4j.neo4j_graph_validation import Neo4jGraphValidation


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

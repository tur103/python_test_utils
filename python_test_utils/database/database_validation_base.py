from abc import ABC, abstractmethod


class DatabaseValidationBase(ABC):
    """
    Base class for defining a database validation utils behavior
    """
    def __init__(self, connector):
        self.connector = connector

    @abstractmethod
    def __enter__(self):
        """
        Setup functionality to occur at the initiation of the session to the database.
        """
        raise NotImplementedError

    @abstractmethod
    def setup_objects(self, setup_objects: list):
        """
        Create all the accepted objects in the database.
        :param setup_objects: All the object to setup in the database prior to the test.
        """
        raise NotImplementedError

    @abstractmethod
    def run_query_on_database(self, query: str):
        """
        Helper for running a query on the database.
        :param query: The query to run on the database.
        """
        raise NotImplementedError

    def add_objects(self, objects_to_add: list):
        """
        Add accepted objects to the database.
        :param objects_to_add: The objects to add to the database.
        """
        self.setup_objects(setup_objects=objects_to_add)

    @abstractmethod
    def remove_objects(self, objects_to_remove: list):
        """
        Remove accepted objects from the database.
        :param objects_to_remove: The objects to remove from the database.
        """
        raise NotImplementedError

    @abstractmethod
    def validate_expected_objects(self, expected_objects: list):
        """
        Validation that the expected objects to be in the database after the running of the test are truly there.
        :param expected_objects: The expected objects to be in the database after the running of the test.
        """
        raise NotImplementedError

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Teardown functionality to occur at the end of the session to the database.
        """
        raise NotImplementedError

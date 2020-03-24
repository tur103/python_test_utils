from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.base import Engine

from python_test_utils.database.database_validation_base import DatabaseValidationBase


class SqlDatabaseValidation(DatabaseValidationBase):
    """
    Test utils for testing an sql database.
    """
    def __init__(self, engine: Engine):
        super().__init__(connector=engine)
        self.session = None

    def __enter__(self):
        """
        Create a session to the database and clear the database at the initiation of the test.
        :return: The sql database validation instance of the database.
        """
        session = sessionmaker(bind=self.connector)
        self.session = session()
        self.session.query().delete()
        self.session.commit()
        return self

    def setup_objects(self, setup_objects: list):
        """
        Create all the accepted objects in the database.
        :param setup_objects: All the object to setup in the database prior to the test.
        """
        self.session.add_all(instances=setup_objects)
        self.session.commit()

    def run_query_on_database(self, sql_query: str):
        """
        Helper for running an sql query on the database.
        :param sql_query: The sql query to run on the database.
        """
        self.session.execute(clause=sql_query)
        self.session.commit()

    def remove_objects(self, objects_to_remove: list):
        """
        Remove accepted objects from the database.
        :param objects_to_remove: The objects to remove from the database.
        """
        self.session.query(objects_to_remove).delete()
        self.session.commit()

    def validate_expected_objects(self, expected_objects: list):
        """
        Validation that the expected objects to be in the database after the running of the test are truly there.
        :param expected_objects: The expected objects to be in the database after the running of the test.
        """
        assert self.session.query() == expected_objects

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Clear the database and close the session at the end of the test.
        """
        self.session.query().delete()
        self.session.commit()
        self.session.close()

    @staticmethod
    def create_engine(database_connection_details: str) -> Engine:
        """
        Create an sql database engine that is connected to the given database connection details.
        :param database_connection_details: The connection details to the desired database.
        :return: The engine that is connected to the sql database.
        """
        engine = create_engine(database_connection_details)
        return engine

    @staticmethod
    def create_sql_database_validation(database_connection_details: str):
        """
        Create an sql database validation for util helpers with testing sql database.
        :param database_connection_details: The connection details to the desired database.
        :return: The sql database validation object.
        """
        engine = SqlDatabaseValidation.create_engine(database_connection_details=database_connection_details)
        return SqlDatabaseValidation(engine=engine)

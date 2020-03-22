from py2neo import Graph, Node, Relationship
from typing import List, Union


class Neo4jGraphValidation:
    """
    Test utils for testing a noe4j graph.
    """
    def __init__(self, graph: Graph):
        self.graph = graph

    def __enter__(self):
        """
        Clear the graph at the initiation of the test.
        :return: The neo4j graph validation instance of the database.
        """
        self.graph.delete_all()
        return self

    def setup_objects(self, setup_objects: List[Union[Node, Relationship]]):
        """
        Create all the accepted objects in the graph.
        :param setup_objects: All the object to setup in the graph prior to the test.
        """
        self.graph.create(subgraph=setup_objects)

    def run_query_on_graph(self, cypher_query: str):
        """
        Helper for running a cypher query on the graph.
        :param cypher_query: The cypher query to run on the graph.
        """
        self.graph.run(cypher=cypher_query)

    def add_objects(self, objects_to_add: List[Union[Node, Relationship]]):
        """
        Add accepted objects to the graph.
        :param objects_to_add: The objects to add to the graph.
        """
        self.setup_objects(setup_objects=objects_to_add)

    def remove_objects(self, objects_to_remove: List[Union[Node, Relationship]]):
        """
        Remove accepted objects from the graph
        :param objects_to_remove: The objects to remove from the graph.
        """
        self.graph.delete(subgraph=objects_to_remove)

    def validate_expected_objects(self, expected_objects: List[Union[Node, Relationship]]):
        """
        Validation that the expected objects to be in the graph after the running of the test are truly there.
        :param expected_objects: The expected objects to be in the graph after the running of the test.
        """
        assert self.graph.exists(subgraph=expected_objects)
        assert len(self.graph.nodes) + len(self.graph.relationships) == len(expected_objects)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Clear the graph at the end of the test.
        """
        self.graph.delete_all()

    @staticmethod
    def create_graph(host: str, port: int, username: str, password: str) -> Graph:
        """
        Create a neo4j graph instance that is connected to the given server details
        :param host: The host of the server.
        :param port: The port of the server.
        :param username: The username that is used to connect to the server.
        :param password: The password that is used to connect to the server.
        :return: The graph instance that is connected to the neo4j server.
        """
        return Graph(host=host, port=port, auth=(username, password))

    @staticmethod
    def create_neo4j_graph_validation(host: str, port: int, username: str, password: str):
        """
        Create a neo4j graph validation for util helpers with testing neo4j graph database.
        :param host: The host of the server.
        :param port: The port of the server.
        :param username: The username that is used to connect to the server.
        :param password: The password that is used to connect to the server.
        :return: The neo4j graph validation object.
        """
        graph = Neo4jGraphValidation.create_graph(host=host, port=port, username=username, password=password)
        return Neo4jGraphValidation(graph=graph)

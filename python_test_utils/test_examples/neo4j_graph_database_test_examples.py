from python_test_utils.test_expansion import TestExpansion


class TestExampleNeo4jGraphDatabase(TestExpansion):
    def test_example_validate_graph_correctness(self):
        with self.neo4j_graph_validation.create_neo4j_graph_validation(host="localhost", port=7474, username="neo4j",
                                                                       password="neo4j") as neo4j_graph_validation:
            setup_objects = []
            neo4j_graph_validation.setup_objects(setup_objects=setup_objects)

            # Run your changes to the graph here

            expected_objects = setup_objects + []
            neo4j_graph_validation.validate_expected_objects(expected_objects=expected_objects)

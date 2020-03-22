from python_test_utils.database.neo4j.neo4j_graph_validation import Neo4jGraphValidation


def test_example_validate_graph_correctness():
    with Neo4jGraphValidation.create_neo4j_graph_validation(host="localhost", port=7474, username="neo4j",
                                                            password="neo4j") as neo4j_graph_validation:
        setup_objects = []
        neo4j_graph_validation.setup_objects(setup_objects=setup_objects)

        # Run your changes to the graph here

        expected_objects = setup_objects + []
        neo4j_graph_validation.validate_expected_objects(expected_objects=expected_objects)

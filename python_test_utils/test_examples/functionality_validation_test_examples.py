from python_test_utils.test_expansion import TestExpansion
from python_test_utils.test_examples.utils_for_test_examples import function_to_test


class TestExampleFunctionalityValidation(TestExpansion):
    def test_example_expected_result_from_function(self):
        TestExampleFunctionalityValidation.validate_function_result(function=function_to_test,
                                                                    arguments_list=[{"number": 1}],
                                                                    expected_result_list=[1])

    def test_example_expected_exception_from_function(self):
        TestExampleFunctionalityValidation.validate_function_exception(function=function_to_test,
                                                                       arguments_list=[{"number": 0}],
                                                                       expected_exception_list=[ValueError])

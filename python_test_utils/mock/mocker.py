from unittest.mock import patch, MagicMock
from typing import List, Tuple, Any


class Mocker:
    """
    A mocker object that exports some mocking utilities for tests.
    """
    def __init__(self, patchers: List[Tuple[str, Any]]):
        self.patchers = Mocker.create_patchers(patchers=patchers)

    @staticmethod
    def create_patchers(patchers: List[Tuple[str, Any]]) -> List[Tuple[patch, Any]]:
        """
        Creating a patch objects from the given functions to mock.
        :param patchers: A list of callable functions to mock with their desired return value.
        :return: A list of tuples of patches and their desired return value.
        """
        mock_patchers = []
        for patcher in patchers:
            mock_patchers.append((patch(patcher[0]), patcher[1]))

        return mock_patchers

    def __enter__(self) -> List[MagicMock]:
        """
        Starts the mocking on all the patchers with their return value.
        :return: List of all the mocks.
        """
        mock_patchers = []
        for patcher in self.patchers:
            mock_patcher = patcher[0].start()
            mock_patcher.return_value = patcher[1]
            mock_patchers.append(mock_patcher)

        return mock_patchers

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Stop the mocking on the patchers.
        """
        for patcher in self.patchers:
            patcher[0].stop()

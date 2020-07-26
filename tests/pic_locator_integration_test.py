from app.picture_locator import JpgPicFinder
import tempfile
import os
import pytest
from unittest.mock import patch


def test_list_files(provide_test_file):
    test_jpg, test_file = provide_test_file
    result_files = test_jpg.list_jpg_files()

    assert test_file.name in result_files
    assert result_files == [test_file.name]


@pytest.fixture
def provide_test_file():
    with tempfile.NamedTemporaryFile(suffix='.jpg') as fp:
        test_jpg = JpgPicFinder(os.path.dirname(fp.name))
        yield test_jpg, fp


@patch("app.picture_locator.gpsphoto.getGPSData")
def test_get_coords(mock_getGPS, provide_test_file):
    test_jpg, test_file = provide_test_file
    JpgPicFinder.get_coords(test_file.name)
    mock_getGPS.assert_called_once_with(test_file.name)

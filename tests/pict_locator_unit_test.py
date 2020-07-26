from pytest import raises
from app.picture_locator import JpgPicFinder, Picture
from unittest.mock import patch, MagicMock

def test_jpg_find_init():
    test_jpg = JpgPicFinder(path_in='/this/is/tes/path')
    assert test_jpg.path_in == '/this/is/tes/path'


def test_list_jpg_files():
    with raises(FileNotFoundError):
        test_jpg = JpgPicFinder(path_in='/this/is/tes/path')
        assert test_jpg.list_jpg_files()


@patch("app.picture_locator.gpsphoto.getGPSData", return_value={"key", "value"})
def test_get_coords(mock_gpsphoto: MagicMock):
    test_file = "/test/file.jpg"
    print(mock_gpsphoto(test_file))
    mock_gpsphoto.assert_called_with(test_file)


@patch("app.picture_locator.Nominatim.reverse")
def test_search_location(mock_Nominatim):
    test_point = (12, 45)
    JpgPicFinder.search_location(test_point)
    mock_Nominatim.asset_called_with(test_point)
    mock_Nominatim.asset_called_once_with(test_point)


def test_pic_init():
    test_pic = Picture(name='test_name', location='/test/location')
    assert test_pic.name == 'test_name'
    assert test_pic.location == '/test/location'

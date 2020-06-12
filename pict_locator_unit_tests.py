from pytest import raises
import picture_locator


def test_jpg_find_init():
    test_jpg = picture_locator.JpgPicFinder(path_in='/this/is/tes/path')
    assert test_jpg.path_in == '/this/is/tes/path'


def test_list_jpg_files():
    with raises(FileNotFoundError):
        test_jpg = picture_locator.JpgPicFinder(path_in='/this/is/tes/path')
        assert test_jpg.list_jpg_files()


def test_list_ok():
    test_jpg = picture_locator.JpgPicFinder(path_in='/Users/marcin94/Desktop/my_files')
    assert type(test_jpg.list_jpg_files()) is list
    assert len(test_jpg.list_jpg_files()) == 2


def test_get_coords():
    # test_jpg = picture_locator.JpgPicFinder(path_in='/Users/marcin94/Desktop/my_files')
    result = picture_locator.JpgPicFinder.get_coords(filename='/Users/marcin94/Desktop/my_files/test_img.jpg')
    assert type(result) is dict
    assert result['Latitude'] == 37.014630555555556
    assert result['Longitude'] == -7.934463888888889


def test_search_location():

    data = picture_locator.JpgPicFinder.get_coords(filename='/Users/marcin94/Desktop/my_files/test_img.jpg')
    coords = (data['Latitude'], data['Longitude'])
    assert picture_locator.JpgPicFinder.search_location(
        coords) == 'Rua Domingos Guieiro, Sé, Faro, Algarve, 8000-250 FARO, Portugal'


def test_pic_init():
    test_pic = picture_locator.Picture(name='test_name', location='/test/location')
    assert test_pic.name == 'test_name'
    assert test_pic.location == '/test/location'


def test_google_maps_search():
    test_pic = picture_locator.Picture(name='test_name', location='New york')
    assert '@40.6971494,-74.2598656,10z/' in test_pic.google_maps_search(keys="New york")

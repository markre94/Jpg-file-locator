from time import sleep


def test_example(app_browser):
    response = app_browser.get('http://127.0.0.1:8080/"')
    assert response.status_code == 200


def test_title(app_browser_main):
    app_browser_main.get("http://127.0.0.1:5000/")
    title = 'Picture locator'
    assert app_browser_main.title == title

    upload_button = app_browser_main.find_element_by_xpath('//*[@id="inputGroupFileAddon03"]')
    upload_button.click()
    sleep(3)
    warning = app_browser_main.find_element_by_xpath('/html/body/div/h3')
    text_warning = "Ups! Forgot to add a file didn't you?"
    assert text_warning == warning.text


def test_browse(app_browser_main):

    app_browser_main.get("http://127.0.0.1:5000/")
    sleep(3)
    browse_button = app_browser_main.find_element_by_xpath('//*[@id="inputGroupFile03"]')
    browse_button.send_keys('/Users/marcin94/Desktop/my_files/poznan.jpg')
    sleep(5)

    file_label = app_browser_main.find_element_by_xpath('/html/body/div/div/form/div/div[2]/label')
    name = 'poznan.jpg'
    assert name == file_label.text

    upload = app_browser_main.find_element_by_xpath('//*[@id="inputGroupFileAddon03"]')
    upload.click()
    sleep(5)

    # Check if table appears
    app_browser_main.find_element_by_xpath('/html/body/div/div[1]/table')

    # Test if picture location is correct
    test_location = "44, Stary Rynek, Garbary, Chwaliszewo, Stare Miasto, Poznań, województwo wielkopolskie, 61-772, Polska"
    app_location = app_browser_main.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr/td[2]')
    assert test_location == app_location.text

    # Test if picture Coordinates are correct
    app_coords = app_browser_main.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr/td[3]')
    test_coords = "(52.4081944, 16.9346694)"

    assert test_coords == app_coords.text

    # Google redirect testing

    show_test = app_browser_main.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr/td[4]/a[2]')
    show_test.click()
    sleep(5)

    tabs_qty = 2
    assert tabs_qty == len(app_browser_main.window_handles)

    # Switching tabs
    app_browser_main.switch_to.window(app_browser_main.window_handles[1])

    assert 'https://www.google.com/maps/place/' in app_browser_main.current_url
    sleep(2)

    test_loc = app_browser_main.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[8]/div/div[1]/span[3]/span[3]')
    assert 'Woźna 45, 61-779 Poznań' == test_loc.text


def test_browse_fail(app_browser_main):
    app_browser_main.get("http://127.0.0.1:5000/")
    sleep(3)
    browse_button = app_browser_main.find_element_by_xpath('//*[@id="inputGroupFile03"]')
    browse_button.send_keys('/Users/marcin94/Desktop/my_pics/IMG_5934.jpg')
    sleep(5)

    upload = app_browser_main.find_element_by_xpath('//*[@id="inputGroupFileAddon03"]')
    upload.click()
    sleep(5)

    text_warning = "No gps data available for current picture!"
    location_error = app_browser_main.find_element_by_xpath('/html/body/div/h3')
    sleep(1)
    assert text_warning == location_error.text


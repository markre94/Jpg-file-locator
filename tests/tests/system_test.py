# -*- coding: utf-8 -*-
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from tests.pages.main_page import MainPage


def test_title(app_browser_main):
    start_page = MainPage(app_browser_main)

    start_page.load_page()

    title_data = 'Picture locator'
    assert app_browser_main.title == title_data
    assert app_browser_main.current_url == "http://127.0.0.1:5000/"
    sleep(5)

    app_browser_main.find_element_by_xpath('/html/body/div/div/form/div/div[2]/input').click()
    sleep(5)


def test_upload_button(app_browser_main):
    start_page = MainPage(app_browser_main)
    start_page.load_page()

    # start_page.test_button()

    app_browser_main.find_element_by_xpath('/html/body/div/div/form/div/div[1]/button').click()

    sleep(5)
    # upload_button = app_browser_main.find_element_by_xpath('//*[@id="inputGroupFileAddon03"]')
    # upload_button.click()
    # warning = app_browser_main.find_element_by_xpath('/html/body/div/h3')
    # text_warning = "Ups! Forgot to add a file didn't you?"
    # assert text_warning == warning.text


def test_browse(app_browser_main):
    app_browser_main.get("http://127.0.0.1:5000/")
    browse_button = app_browser_main.find_element_by_xpath('//*[@id="inputGroupFile03"]')
    browse_button.send_keys('/Users/marcin94/Desktop/my_files/poznan.jpg')

    file_label = app_browser_main.find_element_by_xpath('/html/body/div/div/form/div/div[2]/label')
    name = 'poznan.jpg'
    assert name == file_label.text

    upload = app_browser_main.find_element_by_xpath('//*[@id="inputGroupFileAddon03"]')
    upload.click()

    try:
        WebDriverWait(app_browser_main, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/table"))
        )
    except NoSuchElementException:
        print("The element does not exsits!")
    # app_browser_main.find_element_by_xpath('/html/body/div/div[1]/table')

    # Test if picture location is correct
    test_location = "44, Stary Rynek, Garbary, Chwaliszewo, Stare Miasto, Poznań, województwo wielkopolskie, " \
                    "61-772, Polska"
    app_location = app_browser_main.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr/td[2]')
    assert test_location == app_location.text

    # Test if picture Coordinates are correct
    app_coords = app_browser_main.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr/td[3]')
    test_coords = "(52.4081944, 16.9346694)"

    assert test_coords == app_coords.text

    # Google redirect testing

    show_test = app_browser_main.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr/td[4]/a[2]')
    show_test.click()

    tabs_qty = 2
    assert tabs_qty == len(app_browser_main.window_handles)

    # Switching tabs
    app_browser_main.switch_to.window(app_browser_main.window_handles[1])

    sleep(5)
    assert 'https://www.google.com/maps/place/' in app_browser_main.current_url

    test_loc = app_browser_main.find_element_by_xpath(
        '//*[@id="pane"]/div/div[1]/div/div/div[8]/div/div[1]/span[3]/span[3]')
    assert 'Woźna 45, 61-779 Poznań' == test_loc.text


def test_browse_fail(app_browser_main):
    app_browser_main.get("http://127.0.0.1:5000/")
    browse_button = app_browser_main.find_element_by_xpath('//*[@id="inputGroupFile03"]')
    browse_button.send_keys('/Users/marcin94/Desktop/my_pics/IMG_5934.jpg')

    upload = app_browser_main.find_element_by_xpath('//*[@id="inputGroupFileAddon03"]')
    upload.click()

    text_warning = "No gps data available for current picture!"
    location_error = app_browser_main.find_element_by_xpath('/html/body/div/h3')
    assert text_warning == location_error.text

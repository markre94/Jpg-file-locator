import os
from typing import List
from geopy.geocoders import Nominatim
from GPSPhoto import gpsphoto
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class JpgPicFinder:
    def __init__(self, path_in: str):
        self.path_in = path_in

    def list_jpg_files(self):
        x = []
        for filename in os.listdir(self.path_in):
            if filename.endswith('.jpg'):
                x.append(os.path.join(self.path_in, filename))
        return x

    @staticmethod
    def get_coords(filename: str):
        return gpsphoto.getGPSData(filename)

    @staticmethod
    def search_location(point: tuple):
        geolocator = Nominatim(user_agent='my-application')
        location = geolocator.reverse(point)
        return location.address


class Picture:

    def __init__(self, name: str, location: str):
        self.location = location
        self.name = name
    @staticmethod
    def google_maps_search(keys):
        chrome_options=Options()
        chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(options=chrome_options)
        browser.get('https://www.google.com/maps/')
        browser.find_element_by_id('searchboxinput').send_keys(keys)
        browser.find_element_by_id("searchbox-searchbutton").click()
        time.sleep(5)
        return browser.current_url



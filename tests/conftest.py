import pytest
from selenium import webdriver
import subprocess
from app import app


@pytest.fixture()
def app_browser_main() -> webdriver.Chrome :
    print("Starting server...")
    proc = subprocess.Popen('export FLASK_APP=run.py;flask run', shell=True)
    print("Server stared...")
    # run flask
    # run selenium with proper url
    browser = webdriver.Chrome()
    yield browser
    print("Killing")
    browser.close()
    proc.kill()
    print("Killed")
    # if needed - clean up (close webdriver etc)


@pytest.fixture()
def app_browser() :
    app.config['TESTING'] = True
    with app.test_client() as client :
        yield client

    print('Shutting down tests')

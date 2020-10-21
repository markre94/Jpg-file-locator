import tempfile, os
from app.picture_locator import JpgPicFinder
import pytest
from selenium import webdriver
import subprocess


@pytest.fixture()
def app_browser_main() -> webdriver.Chrome:

    proc = subprocess.Popen('cd ..;export FLASK_APP=run.py;flask run', shell=True)
    print("Server stared...")
    # run flask
    # run selenium with proper url
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("Killing")
    proc.kill()
    browser.quit()

    p = subprocess.run("lsof -i -n -P | grep 5000", capture_output=True, shell=True, encoding="utf8")
    print(p.stdout)
    x = [elem for elem in p.stdout.split()]
    if x[0] == 'Python':
        subprocess.run(f'kill {x[1]}', shell=True)
    print("Killed")


@pytest.fixture
def provide_test_file():
    with tempfile.NamedTemporaryFile(suffix='.jpg') as fp:
        test_jpg = JpgPicFinder(os.path.dirname(fp.name))
        yield test_jpg, fp

import pytest
from selenium import webdriver
import subprocess


@pytest.fixture()
def app_browser_main() -> webdriver.Chrome :
    print("Starting server...")
    subprocess.Popen('pkill flask', shell=True)
    proc = subprocess.Popen('cd ..;export FLASK_APP=run.py;flask run', shell=True)
    assert not proc.stderr
    print(proc.stderr)
    print("Server stared...")
    # run flask
    # run selenium with proper url
    browser = webdriver.Chrome()
    yield browser
    print("Killing")
    proc.kill()
    browser.close()
    p = subprocess.run("lsof -i -n -P | grep 5000", capture_output=True, shell=True, encoding="utf8")
    print(p.stdout)
    x = [elem for elem in p.stdout.split()]
    if x[0] == 'Python':
        subprocess.run(f'kill {x[1]}', shell=True)
    print("Killed")


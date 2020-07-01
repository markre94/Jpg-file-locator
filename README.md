# Jpg_flask

### Functionality

This web app provides a valid information about a uploaded picture in .jpg format. The informations consist of a address of where the picture was taken along with it geographical coordinates.

The app has got a feature which allows user to see the location of the picture on the map by redirecting a web page to the Google Maps application.

### File structure
The Jpg_flask consist the following files:
- run.py _runs an application_
- requirements.txt _contains the required packages for the project._


- app/ configuration of the aplication along with all backend.
- pics/ a directory where uploaded pictures are being saved.
- static/ is a folder which contains static assets for the frontend: CSS style sheets, images, etc.
- templates/ is a folder which contains html templates to be rendered.

The test files are located in the test/ folder. There unit tests along with the system tests were written with the use of pytest and selenium.

### Presentation

![Zrzut ekranu 2020-07-1 o 22 28 29](https://user-images.githubusercontent.com/54006852/86289083-579f7c80-bbeb-11ea-9968-ffa8646ce33a.png)


![Zrzut ekranu 2020-07-1 o 22 29 25](https://user-images.githubusercontent.com/54006852/86289694-6cc8db00-bbec-11ea-9e4b-efff4b7857c5.png)


![Zrzut ekranu 2020-07-1 o 22 29 39](https://user-images.githubusercontent.com/54006852/86289969-e660c900-bbec-11ea-9ea7-6235276c8b10.png)


### System tests

With the combination of the Selenium and Pytest the fully functional tests were writen. The whole idea of writting the automated tests e.g. end to end tests was to contruct a optimal fixture that would set up a flask application server and killed it after the tests have ended. The fixture file is located in the test/conftest.py file. 

```import pytest
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
```

from flask import Flask

app = Flask('__name__')
path = 'pics'
app.config ['SECRET_KEY'] = 'ZOMn8n1Jt8KTfXPwbcZ3tw'
app.config ['IMAGE_UPLOADS'] = path

from app import views

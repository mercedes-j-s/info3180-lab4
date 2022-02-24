from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
from app import views

USERNAME = 'admin'
PASSWORD = 'Password123'
UPLOAD_FOLDER = './uploads'
SECRET_KEY= 'Som3$ec5etK*y'

allowed_uploads = ['png', 'jpg', 'jpeg']
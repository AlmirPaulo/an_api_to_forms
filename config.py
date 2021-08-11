from pathlib import Path

BASE_DIR = Path('.')

URL = 'http://localhost:8000/'

METHOD = 'POST' #POST, GET, PUT, etc...

DATA = {}

# directly from Flask-Mail documentation. 
# https://pythonhosted.org/Flask-Mail/
MAIL_SERVER = 'smtp-relay.gmail.com'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'ap.freelas@gmail.com'
MAIL_PASSWORD = open('../passwords', 'r').read()
MAIL_DEFAULT_SENDER = 'ap.freelas@gmail.com'
MAIL_MAX_EMAILS = None
MAIL_ASCII_ATTACHMENTS = False


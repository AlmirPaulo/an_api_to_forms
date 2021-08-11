from pathlib import Path

BASE_DIR = Path('.')


HOMEPAGE = ...  #In order to redirect back when data was processed. 

URL = ...

METHOD = ... #POST, GET, PUT, etc...

DATA = {}

# directly from Flask-Mail documentation. Change it to fit your needs. 
# https://pythonhosted.org/Flask-Mail/
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = None
MAIL_PASSWORD = None
MAIL_DEFAULT_SENDER = None
MAIL_MAX_EMAILS = None
MAIL_ASCII_ATTACHMENTS = False


URL = 'http://localhost:8000'

METHOD = 'POST' #POST, GET, PUT, etc...

DATA = {'a':[1], 'b':[2] 'c':[3]}

# directly from Flask-Mail documentation. 
# https://pythonhosted.org/Flask-Mail/
MAIL_SERVER = ... #default ‘localhost’
MAIL_PORT = ... #default 25
MAIL_USE_TLS = ... # default False
MAIL_USE_SSL = ... #default False
MAIL_USERNAME = ...
MAIL_PASSWORD = ...
MAIL_DEFAULT_SENDER = ...
MAIL_MAX_EMAILS = ...
MAIL_ASCII_ATTACHMENTS = ... #default False


from flask import Flask, request, render_template
from flask_mail import Mail, Message
import logging, config, pdb


logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, template_folder='.')
mail = Mail()

@app.route('/form')
def tests():
    logging.debug('hit')
    return render_template('index.html')

# @app.route('/')
# def endpoint():
#     if request.method == config.METHOD and request.url_root == config.URL:
#         for i in config.DATA.items():
#             config.DATA[i[0]].append(request.form.get(i[1][0]))
#     else:
#         return "I'm sorry, I can't help you."
        
@app.route('/email', methods=['POST'])
def email():
    if request.method == config.METHOD and request.url_root == config.URL:
        #Getting data
        email = request.form.get('email')
        subject = request.form.get('subject')
        text = request.form.get('text')
        #Sending email
        msg = Message(text)
        msg.recipients = [config.MAIL_DEFAULT_SENDER]
        mail.send(msg)
        logging.debug('email sent')


    else:
        logging.debug(request.url_root)
        return "I'm sorry, I can't help you."







#Factorization
#Configuration
app.config['SECRET_KEY'] = '...'
app.config['MAIL_SERVER'] = config.MAIL_SERVER
app.config['MAIL_PORT'] = config.MAIL_PORT
app.config['MAIL_USE_TLS'] = config.MAIL_USE_TLS
app.config['MAIL_USE_SSL'] = config.MAIL_USE_SSL
app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = config.MAIL_DEFAULT_SENDER
app.config['MAIL_MAX_EMAILS'] = config.MAIL_MAX_EMAILS
app.config['MAIL_ASCII_ATTACHMENTS'] = config.MAIL_ASCII_ATTACHMENTS

#Initializations
mail.init_app(app) 





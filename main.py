from flask import Flask, request
from flask_mail import Mail, Message
import logging, config, pdb

app = Flask(__name__)
mail = Mail()

@app.route('/')
def endpoint():
    if request.method == config.METHOD and request.url_root == config.URL:
        for i in config.DATA.items():
            config.DATA[i[0]].append(request.form.get(i[1][0]))
    else:
        return "I'm sorry, I can't help you."
        
@app.route('/email')
def email():
    if request.method == config.METHOD and request.url_root == config.URL:
        #Getting data
        email = request.form.get('email')
        subject = request.form.get('subject')
        text = request.form.get('text')
        #Sending email
        msg = Message(text)
        msg.recipients = [msg.sender]
        mail.send(msg)


    else:
        return "I'm sorry, I can't help you."







#Factory
def create_app():
    #Configuration
    app.config['SECRET_KEY'] = '...'
    app.config['MAIL_SERVER'] = config.MAIL_SERVER
    app.config['MAIL_PORT'] = config.MAIL_PORT
    app.config['MAIL_USE_TLS'] = config.MAIL_USE_TLS
    app.config['MAUL_USE_SSL'] = config.MAIL_USE_SSL
    app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
    app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD
    app.config['MAIL_DEFAULT_SENDER'] = config.MAIL_DEFAULT_SENDER
    app.config['MAIL_MAX_EMAILS'] = config.MAIL_MAX_EMAILS
    app.config['MAIL_ASCII_ATTACHMENTS'] = config.MAIL_ASCII_ATTACHMENTS
    
    #Initializations
    mail.init_app(app)




    return app

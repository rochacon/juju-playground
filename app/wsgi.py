from flask import Flask

application = Flask(__name__)

@application.route('/')
def testing():
    return 'Hello <a href="https://juju.ubuntu.com">JuJu</a>!!'



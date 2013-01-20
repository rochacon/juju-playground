from flask import Flask

application = Flask(__name__)

@application.route('/')
def testing():
    return 'Hello <a href="https://juju.ubuntu.com">JuJu</a>!!'


@application.route('/works')
def it_works():
    return 'JuJu powered server w/ charm upgrading.', 202


import os

from flask import Flask
from flask import render_template
from flask import request

STATUS = " "

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     SECRET_KEY = os.urandom(24),
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def mainmenu():
        return render_template('mainmenu.html')

    @app.route('/quiz', methods=['POST'])
    def quiz():
        return render_template('quiz.html')

    @app.route('/materials', methods=['POST'])
    def levelselection():
        return render_template('materials.html')

    @app.route('/wordlist', methods=['POST'])
    def wordlist():
        return render_template('wordlist.html')

    return app

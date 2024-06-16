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

    @app.route('/materials', methods=['POST'])
    def materials():
        STATUS = request.form['button'] # quiz or word_list
        PREV_STATUS = request.form['prev-status']
        # MATERIAL_STATUS = request.form['material_status']
        print("STATUS           = " + STATUS)
        print("PREV_STATUS      = " + PREV_STATUS)
        # print("MATERIAL_STATUS  = " + MATERIAL_STATUS)
        if PREV_STATUS == 'mainmenu':
            return render_template('materials.html')
        elif PREV_STATUS == 'materials':
            if STATUS == quiz:
                return render_template('quiz.html')
            elif STATUS == word_list:
                return render_template('wordlist.html')
        else:
            print('Unknown choice selected')

    @app.route('/quiz', methods=['POST'])
    def quiz():
        # MATERIAL_STATUS = request.from['material_status']
        return render_template('quiz.html')

    @app.route('/wordlist', methods=['POST'])
    def wordlist():
        return render_template('wordlist.html')

    # @app.route('back', methods=['POST'])
    # def back():
    #     PREV_STATUS = request.form['prev-status']

    return app

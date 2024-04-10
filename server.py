from flask import Flask
from data import db_session
from services import dict, home_page
from flask_font_awesome import FontAwesome


app = Flask(__name__)
font_awesome = FontAwesome(app)
app.config['SECRET_KEY'] = 'dictionary_secret_key'


def main():
    db_session.global_init("db/dictionary.db")
    app.register_blueprint(home_page.blueprint)
    app.register_blueprint(dict.blueprint)
    app.run()


if __name__ == '__main__':
    main()

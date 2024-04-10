from flask import Blueprint, render_template, request
from data import db_session
from data.word import Word


blueprint = Blueprint(
    'dict_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/dict')
def dictionary():
    db_sess = db_session.create_session()
    words = db_sess.query(Word).all()

    return render_template('dictionary.html', words=words, title='Словарь')


@blueprint.route('/dict/search', methods=['POST', 'GET'])
def search():
    db_sess = db_session.create_session()
    query = request.form['query']
    words = db_sess.query(Word).filter(Word.word.like(f'%{query}%')).all()
    return render_template('dictionary.html', words=words, title='Словарь')

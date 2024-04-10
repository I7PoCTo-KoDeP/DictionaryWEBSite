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

    w = Word(word='ЛИВАТЬ', information='несов. [англ. leave – оставить] – бросать, валить, оставлять, покидать, сваливать, удаляться, уходить.', accent=3)
    w1 = Word(word='МЕМ', information='мема, м. [англ. meme – мем (единица значимой для культуры информации) <= др. греч. mimema – подобие] – прикол, соль, суть, шутка.', accent=1)
    w2 = Word(word='ОК/ОКЕЙ', information='[англ. OK – хорошо] – ладно, понятно, хорошо, ясно.', accent=5)
    db_sess.add(w)
    db_sess.add(w1)
    db_sess.add(w2)
    db_sess.commit()

    return render_template('dictionary.html', words=words, title='Dictionary')


@blueprint.route('/dict/search', methods=['POST', 'GET'])
def search():
    db_sess = db_session.create_session()
    query = request.form['query']
    words = db_sess.query(Word).filter(Word.word.like(f'%{query}%')).all()
    return render_template('dictionary.html', words=words, title='Dictionary')

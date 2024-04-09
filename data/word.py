import sqlalchemy
from .db_session import SqlAlchemyBase


class Word(SqlAlchemyBase):
    __tablename__ = 'words'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    word = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    information = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    accent = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

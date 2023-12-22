# models.py

from config import db
from config import ma

class Game(db.Model):
    __tablename__ = "game"
    id = db.Column(db.Integer, primary_key=True)
    courtname = db.Column(db.String(32), unique=True)
    team1 = db.Column(db.String(32))
    team2 = db.Column(db.String(32))
    score1 = db.Column(db.Integer)
    score2 = db.Column(db.Integer)
    gamenum = db.Column(db.Integer)

class GameSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Game
        load_instance = True
        sqla_session = db.session

game_schema = GameSchema()
games_schema = GameSchema(many=True)
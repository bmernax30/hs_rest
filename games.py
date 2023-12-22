# games.py
from flask import abort, make_response
from config import db
from models import Game, games_schema, game_schema

def read_all():
    games = Game.query.all()
    return games_schema.dump(games)

def create(game):
    courtname = game.get("courtname")
    existing_game = Game.query.filter(Game.courtname == courtname).one_or_none()

    if existing_game is NONE:
        new_game = game_schema.load(game, session=db.session)
        db.session.add(new_game)
        db.session.commit()
        return game_schema.dump(new_game), 201
    else:
        abort(404 ,f"Game with courtname {courtname} already exists")

def read_one(courtname):
    game = Game.query.filter(Game.courtname == courtname).one_or_none()
    if game is not None:
        return game_schema.dump(game)
    else:
        abort(404, f"Game with courtname {courtname} not found")
        
def update(courtname, game):
    existing_game = Game.query.filter(Game.courtname == courtname).one_or_none()
    if existing_game:
        update_game = game_schema.load(game, session=db.session)
        existing_game.password = update_game.password
        db.session.merge(existing_game)
        db.session.commit()
        return game_schema.dump(existing_game), 201

    else:
        abort(
            404,
            f"Game with courtname {courtname} not found"
        )

def delete(courtname):
    existing_game = Game.query.filter(Game.courtname == courtname).one_or_none()
    if existing_game:
        db.session.delete(existing_game)
        db.session.commit()
        return make_response(f"{courtname} successfully deleted", 200)
    else:
        abort(404,f"Game with courtname {courtname} not found")

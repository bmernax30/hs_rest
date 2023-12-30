from flask import render_template
import config
from models import Game

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

@app.route("/")
def home():
	games = Game.query.all()
	print(games)
	return render_template("home.html", games=games)


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=9000, debug=True)
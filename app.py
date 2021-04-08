from flask import Flask,render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index')
def home():
    return render_template("index.html")


@app.route('/movie')
def showmovie():
    datalist = []
    conn = sqlite3.connect("movie.db")
    cur = conn.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)

    cur.close()
    conn.close()
    return render_template("movie.html", datalist=datalist)

@app.route('/score')
def showscore():
    return render_template("score.html")

@app.route('/team')
def showteam():
    return render_template("team.html")

if __name__ == '__main__':
    app.run()

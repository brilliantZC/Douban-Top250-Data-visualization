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
    score = [] # 评分
    num = []   # 评分的电影数
    conn = sqlite3.connect("movie.db")
    cur = conn.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        num.append(item[1])
    cur.close()
    conn.close()
    return render_template("score.html", score=score, num=num)

@app.route('/word')
def showword():
    return render_template("word.html")

@app.route('/team')
def showteam():
    return render_template("team.html")

if __name__ == '__main__':
    app.run()

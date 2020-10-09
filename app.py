from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_movie():
    return render_template('movie.html')


@app.route('/addmovie', methods=['POST', 'GET'])
def addmovie():
    if request.method == 'POST':
        try:
            release = request.form['Release Year']
            title = request.form['Title']
            origin_eth = request.form['Origin/Ethnicity']
            director = request.form['Director']
            cast = request.form['Cast']
            genre = request.form['Genre']
            wiki = request.form['Wiki Page']
            plot = request.form['Plot']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("""INSERT INTO Movies(ReleaseYear, Title, OriginEthnicity, Director, Cast, Genre, WikiPage, Plot)
                            VALUES(?, ?, ?, ?, ?, ?, ?, ?)""", (release, title, origin_eth, director, cast, genre, wiki, plot))

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from Movies")

    rows = cur.fetchall()
    return render_template("list.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)

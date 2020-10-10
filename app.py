from flask import Flask, request, jsonify
import sqlite3 as sql
app = Flask(__name__)


@app.route('/addmovie', methods=['POST', 'GET'])
def addmovie():
    if request.method == 'POST':
        try:
            movie = request.get_json()
            release = movie['ReleaseYear']
            title = movie['Title']
            origin_eth = movie['OriginEthnicity']
            director = movie['Director']
            cast = movie['Cast']
            genre = movie['Genre']
            wiki = movie['WikiPage']
            plot = movie['Plot']

            new_movie = request.get_json()
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("""INSERT INTO Movies(ReleaseYear, Title, OriginEthnicity, Director, Cast, Genre, WikiPage, Plot)
                            VALUES(?, ?, ?, ?, ?, ?, ?, ?)""", (release, title, origin_eth, director, cast, genre, wiki, plot))

                con.commit()
                return new_movie, 201
        except:
            con.rollback()
            return 'Error', 500
        finally:
            con.close()


@app.route('/all')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from Movies")

    rows = cur.fetchall()
    movies = []

    for row in rows:
        movies.append({
            'ReleaseYear': row['ReleaseYear'],
            'Title': row['Title'],
            'OriginEthnicity': row['OriginEthnicity'],
            'Director': row['Director'],
            'Cast': row['Cast'],
            'Genre': row['Genre'],
            'WikiPage': row['WikiPage'],
            'Plot': row['Plot'],
        })

    return jsonify({'movies': movies})


if __name__ == '__main__':
    app.run(debug=True)

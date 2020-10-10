from flask import Flask, request, jsonify
import sqlite3 as sql
import os
import pandas as pd
from sqlalchemy import create_engine
app = Flask(__name__)

# Parse csv using pandas.  Clean up column names.
data_frame = pd.read_csv('./data/movie_plots.csv')
updated_df = data_frame.rename(columns={"Release Year": "ReleaseYear",
                                        "Origin/Ethnicity": "OriginEthnicity",
                                        "Wiki Page": "WikiPage"
                                        })

# Clear db if exists so data is fresh every time app restarts
if os.path.exists('database.db'):
    os.remove('database.db')

engine = create_engine('sqlite:///database.db', echo=True)
sql_connection = engine.connect()

# Load table
updated_df.to_sql('Movies', sql_connection)
sql_connection.row_factory = sql.Row
sql_connection.close()


@app.route('/addmovie', methods=['POST'])
def addmovie():
    if request.method == 'POST':
        # TODO generate id for Index column
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


@app.route('/movies/<movie_id>', methods=['PUT'])
def updatemovie(movie_id):
    if request.method == 'PUT':
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
            updated_movie = request.get_json()

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("UPDATE Movies SET ReleaseYear=?, Title=?, OriginEthnicity=?, Director=?, Cast=?, Genre=?, WikiPage=?, Plot=? WHERE `Index`=?",
                            (release, title, origin_eth, director, cast, genre, wiki, plot, movie_id))
                con.commit()
            return updated_movie, 200
        except:
            con.rollback()
            return 'Error', 500
        finally:
            con.close()


@app.route('/movies/<movie_id>', methods=['DELETE'])
def deletemovie(movie_id):
    if request.method == 'DELETE':
        # TODO Delete does not work for movie_ids that are 2 digits.  ex movie_id = 1 works; movie_id=10 does not
        try:
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("DELETE FROM Movies WHERE `Index`=?", (movie_id))
                con.commit()
            return 'Done', 200
        except:
            con.rollback()
            return 'Error', 500
        finally:
            con.close()


@ app.route('/all')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from Movies")

    rows = cur.fetchall()
    movies = []
    for row in rows:
        movies.append({
            'id': row['Index'],
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

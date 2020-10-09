import os
import pandas as pd
import sqlite3
from sqlalchemy import create_engine


def load_data():
    data_frame = pd.read_csv('./data/movie_plots.csv')
    updated_df = data_frame.rename(columns={"Release Year": "ReleaseYear",
                                            "Origin/Ethnicity": "OriginEthnicity", "Wiki Page": "WikiPage"})

    # Clear db if exists so data is fresh
    if os.path.exists('database.db'):
        os.remove('database.db')

    engine = create_engine('sqlite:///database.db', echo=True)
    sql_connection = engine.connect()
    updated_df.to_sql('Movies', sql_connection)

    sql_connection.row_factory = sqlite3.Row
    sql_connection.close()

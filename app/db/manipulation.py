import sqlalchemy
import pymysql
from sqlalchemy import insert
import json
from datetime import date
import os
import pandas as pd
import tabulate

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:inyourfootsteps@35.246.2.66')
conn = engine.connect()


def get_nearest_ten(lat, lng):
    query = f"SELECT story_id, startlat, startlng, SQRT(POW(69.1 * (startlat - {lat}), 2) + POW(69.1 * ({lng} - startlng) * COS(startlat / 57.3), 2)) AS distance  FROM `footsteps_db`.`story` ORDER BY distance LIMIT 0, 10;"
    return pd.read_sql(query, engine)

def get_profile_data(username):
    query = f"SELECT * FROM `footsteps_db`.`profile` LEFT JOIN `story` ON `profile`.`user_id`=`story`.`user_id` WHERE `profile`.`username`='{username}' UNION SELECT * FROM `footsteps_db`.`profile` RIGHT JOIN `story` ON `profile`.`user_id`=`story`.`user_id` WHERE `profile`.`username`='{username}';"
    result = engine.execute(query)

def search_by_title(title):
    query = f"SELECT * FROM `footsteps_db`.`story` WHERE `title`='{title}'"
    return pd.read_sql(query, engine)

def search_by_theme(title):
    print('here')
    query = f"SELECT * FROM `footsteps_db`.`story` WHERE `title`='{title}'"
    return pd.read_sql(query, engine)

def upvote(story_id):
    query = f"UPDATE `footsteps_db`.`story` SET ranking = ranking + 1 WHERE story_id ={story_id}"
    return pd.read_sql(query, engine)

def downvote(story_id):
    query = f"UPDATE `footsteps_db`.`story` SET ranking = ranking + 1 WHERE story_id ={story_id}"
    return pd.read_sql(query,engine)


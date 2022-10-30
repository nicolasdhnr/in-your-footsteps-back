import sqlalchemy
import pymysql
from sqlalchemy import insert
import json
from datetime import date
import os
import pandas as pd

pwd = os.getenv('DB_PASS')
user = os.getenv('DB_USER')
ip = os.getenv('DB_IP')
engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:inyourfootsteps@35.246.2.66')
conn = engine.connect()


def get_nearest_ten(lat, lng):
    query = f"SELECT story_id, startlat, startlng, SQRT(POW(69.1 * (startlat - {lat}), 2) + POW(69.1 * ({lng} - startlng) * COS(startlat / 57.3), 2)) AS distance  FROM story ORDER BY distance LIMIT 0, 10;"
    engine.execute(query)
    for i in result:
        print(i['path_id'])

def get_profile_data(username):
    query = f"SELECT * FROM `profile`LEFT JOIN `story` ON `profile`.`user_id`=`story`.`user_id` WHERE `profile`.`username`='{username}' UNION SELECT * FROM `profile` RIGHT JOIN `story` ON `profile`.`user_id`=`story`.`user_id` WHERE `profile`.`username`='{username}';"
    result = engine.execute(query)

def search_by_title(title):
    query = f"SELECT * FROM `story` WHERE `title`='{title}'"
    result = engine.execute(query)
    for i in result:
        print(i['title'])

def search_by_theme(title):
    query = f"SELECT * FROM `story` WHERE `title`='{title}'"
    result = engine.execute(query)

def upvote(story_id):
    query = f"UPDATE story SET ranking = ranking + 1 WHERE story_id ={story_id}"
    result = engine.execute(query)

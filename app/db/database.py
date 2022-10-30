import sqlalchemy
import pymysql
from sqlalchemy import insert
import json
from datetime import date
import os
import pandas as pd


engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:inyourfootsteps@35.246.2.66')

def send_to_db(table, json_file):
    data = json.load(json_file)
    for i in data:
        values = list(i.values())
        if table == 'authentication':
            return pd.read_sql(insert_auth(values), engine)
        elif table == 'profile':
            return pd.read_sql(insert_profile(values), engine)
        elif table == 'story':
            return pd.read_sql(insert_story(values), engine)
        elif table == 'path':
            return pd.read_sql(insert_path(values), engine)
        elif table == 'voice':
            return pd.read_sql(insert_voice(values), engine)

def insert_auth(data):
    return f"INSERT INTO footsteps_db.authentication (userUID, identifier, provider, created, signed_in) VALUES({str(data[0])}, '{data[1]}', '{data[2]}', {str(data[3])}, {str(data[4])})"

def insert_profile(data):
    return f"INSERT INTO footsteps_db.profile (user_id, userUID, username) VALUES ({str(data[0])}, {str(data[1])}, {data[2]})"

def insert_story(data):
    return f"INSERT INTO footsteps_db.story (story_id, user_id, title, ranking, theme) VALUES ({str(data[0])}, {str(data[1])}, '{data[2]}', '{data[3]}', '{data[4]}')"

def insert_path(data):
    return f"INSERT INTO footsteps_data.path (path_id, story_id, latitude, longitude, timestamp) VALUES ({str(data[0])}, {str(data[1])}, {str(data[2])}, {str(data[3])}, {str(data[4])})"

def insert_voice(data):
    return f"INSERT INTO footsteps_data.voice(voice_id, story_id, order, text, start, end) VALUES ({str(data[0])}, {str(data[1])}, {str(data[2])}, '{data[3]}', {str(data[4])}, {str(data[5])})"


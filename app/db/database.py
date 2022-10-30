import sqlalchemy
import pymysql
from sqlalchemy import insert
import json
from datetime import date
import os

class data_to_db():
    def __init__(self):
        self.establish_connection()

    def establish_connection(self):
        pwd = os.getenv('DB_PASS')
        user = os.getenv('DB_USER')
        ip = os.getenv('DB_IP')
        engine = sqlalchemy.create_engine(f'mysql+pymysql://root:{pwd}@{ip}')

    def send_to_db(self,table, json_file):
        data = json.load(json_file)
        for i in data:
            values = list(i.values())
            if table == 'authentication':
                engine.execute(self.insert_auth(values))
            elif table == 'profile':
                engine.execute(self.insert_profile(values))
            elif table == 'story':
                engine.execute(self.insert_story(values))
            elif table == 'path':
                engine.execute(self.insert_path(values))
            elif table == 'voice':
                engine.execute(self.insert_voice(values))

    def insert_auth(self,data):
        return f"INSERT INTO footsteps_db.authentication (userUID, identifier, provider, created, signed_in) VALUES({str(data[0])}, '{data[1]}', '{data[2]}', {str(data[3])}, {str(data[4])})"

    def insert_profile(self,data):
        return f"INSERT INTO footsteps_db.profile (user_id, userUID, username) VALUES ({str(data[0])}, {str(data[1])}, {data[2]})"

    def insert_story(self,data):
        return f"INSERT INTO footsteps_db.story (story_id, user_id, title, ranking, theme) VALUES ({str(data[0])}, {str(data[1])}, '{data[2]}', '{data[3]}', '{data[4]}')"

    def insert_path(self,data):
        return f"INSERT INTO footsteps_data.path (path_id, story_id, latitude, longitude, timestamp) VALUES ({str(data[0])}, {str(data[1])}, {str(data[2])}, {str(data[3])}, {str(data[4])})"

    def insert_voice(self,data):
        return f"INSERT INTO footsteps_data.voice(voice_id, story_id, order, text, start, end) VALUES ({str(data[0])}, {str(data[1])}, {str(data[2])}, '{data[3]}', {str(data[4])}, {str(data[5])})"

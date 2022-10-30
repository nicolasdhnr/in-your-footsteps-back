import sqlalchemy
import pymysql
from sqlalchemy import insert
import json
from datetime import date
import os
import pandas as pd
from app.models.data_transfer_models import Story
from app.models.data_transfer_models import HandshakeOut, HandshakeIn, StoryIn, StoryOut, Recording, StoryStartOut

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:inyourfootsteps@35.246.2.66')
conn = engine.connect()


def get_nearest(lat, lng):
    query = f"SELECT *, SQRT(POW(69.1 * (startlat - {lat}), 2) + POW(69.1 * ({lng} - startlng) * COS(startlat / 57.3), 2)) AS distance  FROM `footsteps_db`.`story` ORDER BY likes ASC LIMIT 0, 30;"
    df = pd.read_sql(query, engine)
    df.columns = ['story_id', 'story_user_id', "likes", 'title', 'theme', 'startlat', 'startlng', 'endlat',
                  'endlng', "description", 'distance']
    # parse df into a list of StoryIn Objects

    out = []
    for idx, row in df.iterrows():
        out.append(
            Story(story_id=row['story_id'], story_user_id=row['story_user_id'], likes=row['likes'], title=row['title'],
                  theme=row['theme'], startlat=row['startlat'], startlng=row['startlng'],
                  endlat=row['endlat'], endlng=row['endlng'], description=row['description'],
                  distance=row['distance']).dict())

    return HandshakeOut(stories=out)


def get_profile_data(username):
    query = f"SELECT * FROM `footsteps_db`.`profile` LEFT JOIN `story` ON `profile`.`user_id`=`story`.`user_id` WHERE `profile`.`username`='{username}' UNION SELECT * FROM `footsteps_db`.`profile` RIGHT JOIN `story` ON `profile`.`user_id`=`story`.`user_id` WHERE `profile`.`username`='{username}';"
    result = engine.execute(query)


def search_by_title(title):
    query = f"SELECT * FROM `footsteps_db`.`story` WHERE `title`='{title}'"
    df = pd.read_sql(query, engine)
    df.columns = ['story_id', 'story_user_id', "likes", 'title', 'theme', 'startlat', 'startlng', 'endlat', 'endlng',
                  "description"]
    out = []
    for idx, row in df.iterrows():
        out.append(
            Story(story_id=row['story_id'], story_user_id=row['story_user_id'], likes=row['likes'], title=row['title'],
                  theme=row['theme'], startlat=row['startlat'], startlng=row['startlng'],
                  endlat=row['endlat'], endlng=row['endlng'], description=row['description']).dict())

    return HandshakeOut(stories=out)


def search_by_theme(theme):
    print('here')
    query = f"SELECT * FROM `footsteps_db`.`story` WHERE `theme`='{theme}' ORDER BY likes ASC LIMIT 0, 30;"
    df = pd.read_sql(query, engine)
    df.columns = ['story_id', 'story_user_id', "likes", 'title', 'theme', 'startlat', 'startlng', 'endlat', 'endlng',
                  "description"]
    out = []
    for idx, row in df.iterrows():
        out.append(
            Story(story_id=row['story_id'], story_user_id=row['story_user_id'], likes=row['likes'], title=row['title'],
                  theme=row['theme'], startlat=row['startlat'], startlng=row['startlng'],
                  endlat=row['endlat'], endlng=row['endlng'], description=row['description']).dict())

    return HandshakeOut(stories=out)


def upvote(story_id):
    query = f"UPDATE `footsteps_db`.`story` SET ranking = ranking + 1 WHERE story_id ={story_id}"
    engine.execute(query)


def downvote(story_id):
    query = f"UPDATE `footsteps_db`.`story` SET ranking = ranking + 1 WHERE story_id ={story_id}"
    engine.execute(query)


def recordings_per_story(story_id):
    query = f"SELECT recording_id, start_lat FROM `footsteps_db`.`recordings` INNER JOIN story on story_id=story_id WHERE `story_id`='{story_id}'"
    df = pd.read_sql(query, engine)
    df.columns = ['recording_id', 'start_lat']
    out = []
    for idx, row in df.iterrows():
        out.append(Recording(recording_id=row['recording_id'], start_lat=row['start_lat']).dict())
    return StoryStartOut(stories=out)


def insert_new_story(story: StoryIn):
    query = f"INSERT INTO `footsteps_db`.`story` (`story_id`, `story_user_id`, `title`, `startlat`, `startlng`, `description`) " \
            f"VALUES ({story.story_id}, '{story.story_user_id}', '{story.title}', '{story.startlng}', '{story.description}');"
    engine.execute(query)


if __name__ == "__main__":
    print(get_nearest(1.1, 1.1))


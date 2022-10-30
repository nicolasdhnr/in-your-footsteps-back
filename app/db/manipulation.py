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

    def get_nearest_ten(self, lat, lng):
        query = f'SELECT path_id, latitude, longitude, SQRT(POW(69.1 * (latitude - {lat}), 2) + POW(69.1 * ({lng} - longitude) * COS(latitude / 57.3), 2)) AS distance  FROM path ORDER BY distance LIMIT 0, 1000'
        # TODO: Also needs to order by ranking within those 1000.
        engine.execute(query)



def get_recommended_paths(lat, lng):
    #
    pass

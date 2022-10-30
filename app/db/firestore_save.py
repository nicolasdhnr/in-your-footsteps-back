"""
This script saves the path data to Firestore.Once it has been received.


TODOS:
- Use the REST API indtead to read from DATABASE from the fastAPI heroku-deployed app.

"""

import firebase_admin
from firebase_admin import firestore
from google.cloud import storage
import firebase_admin
from firebase_admin import credentials



cred = credentials.Certificate("/Users/nico/Code/secret.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# TODO: Actually here we just need to read the data from the database and save it to Firestore.
collection = db.collection('in-your-footsteps-paths')
doc = collection.document('testtt')
res = doc.get().to_dict()
print(res)  # Nice - works


def get_path_data(path_id):
    """Get path data from database."""

    # Return in a jsonable format
    pass

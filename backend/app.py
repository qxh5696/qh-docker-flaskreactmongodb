from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

username = 'admin'
password = 'password'
mongoClient = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))

db = mongoClient.get_database('test')
col = db.get_collection('fremp_test_app1_col')

# $ mongo
# $ use fremp_test_app1_db
# $ db.fremp_test_app1_col.insertOne({'data': 'Hello World from MongoDB'})

@app.route('/api/get/')
def getdata():
    data = ''
    if col.find({}):
        for data in col.find({}):
            import pdb; pdb.set_trace()
            data = data['data']
    return {'data': data}

if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
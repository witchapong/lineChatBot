import json
import os

from flask import Flask
from flask import request
from flask import make_response

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("mr-spock-25e2d-firebase-adminsdk-npk8u-34c04c79cf.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():

    req = request.get_json(silent=True, force=True)
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):

    # Parsing the POST request body into a dictionary for easy access.
    req_dict = json.loads(request.data)

    # Accessing the fields on the POST request boduy of API.ai invocation of the webhook
    intent = req_dict["queryResult"]["intent"]["displayName"]

    if intent == 'ถามหนังน่าดู':

        doc_ref = db.collection(u'movies').document(u'zuzqMHTmffFOLl0vUhZc')
        doc = doc_ref.get().to_dict()
        print(doc)

        movie_name = doc['movie_name']
        rel_date = doc['release_date']
        speech = f'ตอนนี้มีเรื่อง {movie_name} เข้าโรงวันที่ {rel_date}'

    else:

        speech = "ผมไม่เข้าใจ คุณต้องการอะไร"

    res = makeWebhookResult(speech)

    return res

def makeWebhookResult(speech):

    return {
  "fulfillmentText": speech
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)

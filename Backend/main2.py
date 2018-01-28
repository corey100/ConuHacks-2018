from flask import Flask, request
import json

from tf_stuff import retrain_model
import google_search

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    pass

@app.route('/retrain', methods=['POST'])
def retrain():
    retrain_model()
    # Twilio API should go here

@app.route('/findJobPage', methods=['GET'])
def findJobPage():
    query = request.args.get('company')
    job_results = google_search.search("%s internships" % (query,))

    company_results = google_search.search(query)

    if len(job_results) > 0 and len(company_results) > 0:
        return json.dumps({
            'link': job_results[0].get('link'),
            'desc': company_results[0].get('desc')
        })
    return json.dumps({
        'error': 'There was an exception when trying to find the job page.'
    })

if __name__ == "__main__":
    app.run(host= '0.0.0.0')

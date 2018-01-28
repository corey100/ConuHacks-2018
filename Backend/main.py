from flask import Flask, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename

import subprocess
import os
import re
import json

import google_search

UPLOAD_FOLDER = '/Users/jasonle/Projects/CONUHacks/CONUHACKSLASTMINUTE/Backend/uploads'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

PAT = r'(\n)?([a-z]*) 0.'


def match(filename):
	result = subprocess.check_output(['python3','tensorflow/tensorflow/examples/label_image/label_image.py','--graph=/tmp/output_graph.pb','--labels=/tmp/output_labels.txt','--input_layer=Mul','--output_layer=final_result','--input_mean=128','--input_std=128','--image=/Users/jasonle/Projects/CONUHacks/CONUHACKSLASTMINUTE/Backend/uploads/%s' % filename])
	print(result)
	company = re.search(PAT, str(result))
	if company is not None:
		return company.group()
	return None

@app.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		if 'file' in request.files:
			file = request.files['file']
			if file:
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				company_name = match(filename)
				link = google_search.search(company_name) if company_name is not None else None
				return json.dumps({
					'company': match(filename),
					'link': link,
				})

	return render_template('index.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0')

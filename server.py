from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def portfolio():
	return render_template('index.html')


@app.route('/<string:pagename>')
def about(pagename):
	return render_template(pagename)


def write_file(data):
	email=data['email']
	subject=data['subject']
	message=data['Message']
	with open('database.csv', 'a', newline='') as csvfile:
		file=csv.writer(csvfile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		file.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method=='POST':
		data = request.form.to_dict()
		write_file(data)
		return redirect('/thank_you.html')
	else:
		return 'Not Working'

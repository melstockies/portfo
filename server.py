from flask import Flask, render_template, url_for
import os
from flask import send_from_directory
from flask import request
from flask import redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def index():
    page_name = 'index.html'
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data.get("email", "")
        subject = data.get("subject", "")
        message = data.get("message", "")   
        file = database.write(f'\n : {email} : {subject} : {message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data.get("email", "")
        subject = data.get("subject", "")
        message = data.get("message", "")   
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something when wrong , try again'



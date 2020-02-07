from flask import Flask,request,render_template
app = Flask('app')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
import main
from os import system

@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

@app.route('/')
def hello_world():
  return render_template("index.html", display="none")

@app.route('/single_year', methods=['POST'])
def single_year():
  main.selectIndividualYear(request.form['year'])
  return render_template("index.html", path="images/individualYear.png", scroll="visualization", display="block")

@app.route('/year_range', methods=['POST'])
def year_range():
  main.selectYearRange(int(request.form['year-start']),int(request.form['year-end']))
  return render_template("index.html", path="images/selectYearRange.png", scroll="visualization", display="block")

#system("pkill -9 python")
app.run(host='0.0.0.0', port=8080, threaded=True)
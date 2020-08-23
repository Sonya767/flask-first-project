
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/page2')
def hobby_page():
    return render_template('index2.html')
@app.route('/page3')
def skills_page():
    return render_template('index3.html')
app.run(debug=True)

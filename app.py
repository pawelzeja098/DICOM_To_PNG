from flask import Flask, render_template
from flask_restx import Resource, Api
from flask_cors import CORS

app = Flask(__name__)

app.secret_key = "Mnc_erJqCbYeRxfuVrszxw"
app.config['UPLOAD_FOLDER'] = './tmp'


CORS(app)

from webapi import blueprint as bp

app.register_blueprint(bp)


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=False)

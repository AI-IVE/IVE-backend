from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import boto3
import io
import pandas as pd
from configparser import ConfigParser

app = Flask(__name__)

def load_config(filename='config.properties'):
    parser = ConfigParser()
    parser.read(filename)
    return parser

config = load_config()

AWS_ACCESS_KEY = config.get('Secrets', 'AWS_ACCESS_KEY')
AWS_SECRET_KEY = config.get('Secrets', 'AWS_SECRET_KEY')
BUCKET_NAME = config.get('Secrets', 'BUCKET_NAME')

@app.route('/')
def home():
    return render_template('upload_form.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
 
@app.route('/read/file', methods=['POST'])
def readFile():

    s3 = boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

    obj = s3.get_object(Bucket=bucket_name, Key='data3.parquet')
    result = pd.read_parquet(io.BytesIO(obj['Body'].read()))
    print(result)

    return 'No file uploaded'
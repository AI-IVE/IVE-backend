from flask import Flask, render_template, request
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('upload_form.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

    
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' in request.files:
        file = request.files['file']
        filename = secure_filename(file.filename)
        # Here you should save the file
        # file.save(path_to_save_file)
        return 'File uploaded successfully'

    return 'No file uploaded'
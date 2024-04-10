from flask import Blueprint

upload = Blueprint('upload', __name__)

@upload.route("/file/upload", methods=['GET'])
def upload_file():
    return "Upload page"


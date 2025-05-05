from flask import Flask, request, jsonify
from src.constants import ALLOWED_EXTENSIONS
from src.classifier import classify_file
from src.errors import error_response
import src.error_types as et

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/classify_file', methods=['POST'])
def classify_file_route():

    if 'file' not in request.files:
        return error_response(et.FILE_PART)

    file = request.files['file']
    if file.filename == '':
        return error_response(et.FILE_NAME)
    
    if not allowed_file(file.filename):
        return error_response(et.FILE_TYPE)

    try: 
        file_class = classify_file(file)
    except Exception:
        return error_response(et.CLASSIFICATION)
    
    return jsonify({"file_class": file_class}), 200


if __name__ == '__main__':
    app.run(debug=True)

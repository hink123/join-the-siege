from flask import jsonify

def error_response(error):
    message, code = error
    return jsonify({"error": message}), code
import json
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['POST'])
def create_ppt():
    text = json.loads(request.data)
    print(text["test"])
    return "OK"


app.run()

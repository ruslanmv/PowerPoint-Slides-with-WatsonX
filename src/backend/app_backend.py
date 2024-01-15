import json
from flask import Flask, request, jsonify
from slides_generator import PowerPoint
app = Flask(__name__)


@app.route('/', methods=['POST'])
def create_ppt():
    text = json.loads(request.data).get("text")
    print("""--- Text Received ---""")
    print(text)

    if text:
        """ppt = PowerPoint()
        ppt.slides(text)"""
        return "OK", 200

    return "Bad Input", 400


app.run()

from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route('/time')
def hello_world():
    return str(datetime.now().time())


app.run(host='0.0.0.0',
        port=8080,
        debug=True)

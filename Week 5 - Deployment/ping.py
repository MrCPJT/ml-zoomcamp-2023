# Web service example script

# Importing Flask
from flask import Flask

app = Flask('ping')

# Decorator
@app.route('/ping', methods=['GET'])
def ping():
    return "PONG"

# Running the webservice
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
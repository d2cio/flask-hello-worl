import os
import socket
from flask import Flask

app = Flask(__name__)
port = os.getenv('PORT', '8000')
hostname = socket.gethostname()

@app.route('/')
def hello():
	return 'Hello world from Python!<br>Server listening port ' + port + ' on host: ' + hostname

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))

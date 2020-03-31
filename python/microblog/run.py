#!flask/bin/python
from app import app
app.run(debug = True, host='192.168.56.101', port=5001)

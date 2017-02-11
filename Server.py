import socketio
import eventlet
import eventlet.wsgi
from flask import Flask, render_template
import os

controllerData = {}

sio = socketio.Server()
template_dir = os.path.abspath('.')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
    """Serve the client-side application."""
    return render_template('index.html')

@sio.on('connect')
def connect(sid, environ):
    print("connect ", sid, environ)

@sio.on('controllerDataFromBrowser')
def message(sid, data):
    global controllerData
    #print("controller: ", data)
    controllerData = data
    #sio.emit('reply')

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)


def startServer():
	global app
	global sio
	app = socketio.Middleware(sio, app)
	eventlet.wsgi.server(eventlet.listen(('', 8000)), app)

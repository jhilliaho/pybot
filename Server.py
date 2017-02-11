import socketio
import eventlet
import eventlet.wsgi
from flask import Flask, render_template
import os


class Server:

	def __init__(self):


	self.sio = socketio.Server()

	template_dir = os.path.abspath('.')
	self.app = Flask(__name__, template_folder=template_dir)

    self.app = socketio.Middleware(self.sio, self.app)

    eventlet.wsgi.server(eventlet.listen(('', 8000)), self.app)

	@self.app.route('/')
	def index(self):
	    """Serve the client-side application."""
	    return render_template('index.html')

	@self.sio.on('connect')
	def connect(self, sid, environ):
	    print("connect ", sid, environ)

	@self.sio.on('controllerDataFromBrowser')
	def message(self, sid, data):
	    print("message ", data)
	    #sio.emit('reply')

	@self.sio.on('disconnect')
	def disconnect(self, sid):
	    print('disconnect ', sid)

if __name__ == '__main__':
	ser = Server()
	
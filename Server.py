import socketio
import eventlet
import eventlet.wsgi
from flask import Flask, render_template
import os



	sio = socketio.Server()

	template_dir = os.path.abspath('.')
	app = Flask(__name__, template_folder=template_dir)

	app = socketio.Middleware(sio, app)

	eventlet.wsgi.server(eventlet.listen(('', 8000)), app)

	@app.route('/')
	def index():
	    """Serve the client-side application."""
	    return render_template('index.html')

	@sio.on('connect')
	def connect(sid, environ):
	    print("connect ", sid, environ)

	@sio.on('controllerDataFromBrowser')
	def message(sid, data):
	    print("message ", data)
	    #sio.emit('reply')

	@sio.on('disconnect')
	def disconnect(sid):
	    print('disconnect ', sid)

if __name__ == '__main__':
	ser = Server()

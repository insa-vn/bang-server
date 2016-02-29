from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('hoang sida')
def handle_message(args):
    print('Message from client : ' + args['message'])
    return 'Positive'

if __name__ == '__main__':
    socketio.run(app)

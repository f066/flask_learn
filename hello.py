#use "pip install flask-script" command before run this hello.py

from flask import Flask
from flask import request
from flask_script import Manager
app = Flask(__name__)

manager = Manager(app)

#@app.route('/')
#def index():
#    user_agent = request.headers.get('User-Agent')
#    return '<h1>hello world!</h1><p> your browser is %s!</p>' % user_agent
#
#@app.route('/user/<name>')
#def user(name):
#    return '<h1>hello, %s!</h1>' % name

if __name__ == '__main__':
#    app.run(debug=True)
    manager.run()



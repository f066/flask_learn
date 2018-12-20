#use "pip install flask-bootstrap" command before run this hello.py

from flask import Flask,render_template
#from flask import request
from flask_script import Manager
from flask_bootstrap import Bootstrap
app = Flask(__name__)

bootstrap = Bootstrap(app)
#manager = Manager(app)

@app.route('/')
def index():
    return render_template('index.html')
#    user_agent = request.headers.get('User-Agent')
#    return '<h1>hello world!</h1><p> your browser is %s!</p>' % user_agent
#

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
#    return '<h1>hello, %s!</h1>' % name

@app.route('/test')
def test():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)



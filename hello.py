#use "pip install flask-wtf" command before run this hello.py

from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask import Flask,render_template
#from flask import request
from flask_script import Manager
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to gusess string'

bootstrap = Bootstrap(app)
moment = Moment(app)
#manager = Manager(app)

class NameForm(Form):
    name = StringField('what is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template('index.html', form=form, name=name)
#    user_agent = request.headers.get('User-Agent')
#    return '<h1>hello world!</h1><p> your browser is %s!</p>' % user_agent
#

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
#    return '<h1>hello, %s!</h1>' % name

@app.route('/test')
def test():
    return render_template('test.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)



from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
# app.config['']
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = ''
        form.name.data = 'hello'
    flash('Looks like you have changed your name!')
    return render_template('index.html', form=form, name=name)

app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/time', methods=['GET', 'POST'])
def time():
    return render_template('time.html', current_time=datetime.utcnow())

if __name__ == '__main__':
    app.run()
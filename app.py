"""
Routes and views for the flask application.
"""
import os
import eventloader, eventhandler, materialisedview
from datetime import datetime
from flask import render_template, flash, request, Flask
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '03717357'

class ReusableForm(Form):
    name = TextField('File Path:',validators=[validators.input_required()])

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    """Renders the home page."""
    form = ReusableForm(request.form)
    if request.method == 'POST':
        name=request.form['name']
        if form.validate() and os.path.isfile(name): # check what was entered in form was actually a file
            # Save the comment here.
            msg = ''
            msg = eventloader.loadeventsfrompath(name)
            if 'Error' in msg:
                pass
            else:
                msg += ' and ' + eventhandler.processQueue()
            flash(msg)
        else:
            flash('Error: Please enter a valid file path ')
        return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        form=form,
        rec = materialisedview.getRecQuery(),
        shot = materialisedview.getShotQuery(),
        trc = materialisedview.getTrcQuery(),
        matv = materialisedview.getSummary()
        )
    elif request.method == 'GET':
        return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        form=form,
        rec = materialisedview.getRecQuery(),
        shot = materialisedview.getShotQuery(),
        trc = materialisedview.getTrcQuery(),
        matv = materialisedview.getSummary()
        )
    

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact Info',
        year=datetime.now().year,
        message='03717357 Gregory Ollivierre'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='Assignment 2 details',
        year=datetime.now().year,
        message=''
    )

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

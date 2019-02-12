from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators, DateField
from wtforms.validators import Required


bp = Blueprint('entryPoint', __name__)

# straight from the wtforms docs:
class HostForm(FlaskForm):
    fullName = TextField('Host IP/Name', [validators.required()])

class ExampleForm(FlaskForm):
    # subforms
    new_Host = FormField(HostForm)
    submit_button = SubmitField('Run')


@bp.route('/', methods=('GET', 'POST'))
def index():
    """TODO"""
    form = ExampleForm()
    form.validate_on_submit()  # to get error messages to the browser
    return render_template('entryPoint/index.html', form=form)

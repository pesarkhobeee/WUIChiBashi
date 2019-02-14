from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators, DateField
from wtforms.validators import Required

from flask_simplelogin import login_required

import uuid
import json
import subprocess
from shlex import quote
from pathlib import Path

bp = Blueprint('entryPoint', __name__)

# straight from the wtforms docs:
class HostForm(FlaskForm):
    fullName = TextField('Host IP/Name', [validators.required()])

class ExampleForm(FlaskForm):
    # subforms
    new_Host = FormField(HostForm)
    submit_button = SubmitField('Run')


@bp.route('/', methods=('GET', 'POST'))
@login_required  # < --- simple decorator
def index():
    """TODO"""
    form = ExampleForm()
    runningProgramID = ''
    if form.validate_on_submit():
        host = form.new_Host.fullName.data
        flash('Requested for {}'. format(host))
        tmpFileName = str(uuid.uuid4())
        if runCommand(host, tmpFileName) == 0:
            runningProgramID = tmpFileName
        else :
            flash('Some Errors happend!', 'error')
    else :
        if form.errors:
            print(form.errors)
    return render_template('entryPoint/index.html', form=form,
     runningProgramID=runningProgramID)

@bp.route('/checkStatus/<string:id>')
@login_required
def checkStatus(id):
    """TODO"""
    fileFullAddress = "/tmp/" + id
    file = open(fileFullAddress, "r")
    content = file.read()
    result = {}
    result['content'] = content
    path = Path(fileFullAddress + ".finished")
    if path.exists():
        result["status"] = "finished"
    else :
        result["status"] = "running"
    return json.dumps(result)

def runCommand(host, tmpFileName):
    """TODO"""
    #Attention: Sanitizing inputs MUST be done
    host = quote(host)

    path = str(Path().absolute())
    cmd = 'python ' + path + '/worker.py ' + host + ' ' + tmpFileName

    return subprocess.call(cmd.split())

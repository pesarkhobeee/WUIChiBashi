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
        flash('Requested for {}'.
        format(form.new_Host.fullName.data))
        runningProgramID = runCommand()
    else :
        if form.errors:
            print(form.errors)
    return render_template('entryPoint/index.html', form=form,
     runningProgramID=runningProgramID)

@bp.route('/runningProgram/<string:id>')
@login_required
def runningProgram(id):
    file = open("/tmp/" + id, "r")
    content = file.read()
    result = {}
    result["status"] = "ok"
    result['content'] = content
    import json
    return json.dumps(result)

def runCommand():
    import uuid
    tmpFileName = str(uuid.uuid4())
    import subprocess
    cmd = 'free -m > ' + "/tmp/" + tmpFileName
    print(cmd)
    proc = subprocess.Popen(cmd,
    shell=True, stdin=None ,stdout=None,stderr=subprocess.PIPE, close_fds=True)
    stderr = proc.communicate()
    if stderr[0] is not None:
        return str(stderr)
    else :
        return tmpFileName

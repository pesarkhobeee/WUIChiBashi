WUIChiBashi
==========================

WUIChiBashi is a simple python Web Interface example based on Flask framework to run command line programs.

# How to Run:

You can run the web interface for development purposes only the by help of:
At the very beginning, you have to initial virtual environment with this:

```
sudo apt-get install -y python3-venv
pyvenv env
```

And then every time that you want to run it:

```
source env/bin/activate
python -m pip install -r requirements.txt
FLASK_ENV=development FLASK_APP=webUI flask run
```

For production you can use docker and docker-compose:  

```
docker-compose up -d
```

# Debugging guidelines:

[TODO]

# Security guidelines:

[TODO]

# Coding style and general guidelines:

[TODO]

### License:

MIT

### Resources:

* https://github.com/rochacbruno/flask_simplelogin
* https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xix-deployment-on-docker-containers
* https://pythonhosted.org/Flask-Bootstrap/forms.html

### Looking for a more comprehensive solution? look at below link:

https://github.com/wooey/Wooey

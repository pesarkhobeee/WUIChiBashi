WUIChiBashi
==========================

WUIChiBashi is a simple python Web Interface example based on Flask framework to run command line programs.

![ScreenShot](https://raw.github.com/pesarkhobeee/WUIChiBashi/master/screenshot.png)

The main aim of this project is creating a minimal Web User Interface which can promise an easy way to understand and change.
Yes, I know the **WebSocket** technology is out there but I believe that having a fancy technology which you don't have enough resource to maintain it is nonsense.   

# How to Run:

### Development Environment

At the very beginning, you have to initial a virtual environment with this:

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

You should know the default username and password for the development environment are **admin**

### Production Environment

For production you can use docker and docker-compose, but before running it you change below variables inside of **web-application.cfg**

```
SECRET_KEY='changeThis'
SIMPLELOGIN_USERNAME='changeThis'
SIMPLELOGIN_PASSWORD='changeThis'
```  

After that, you can easily set up your docker container with help of :

```
docker-compose up -d
```

# Security guidelines:

Although we are using a none root user inside a docker container and also sanitizing input by `shlex.quote` you should consider that **worker.pay** using **subprocess.Popen** with `shell=True` which means you should be very careful about that:
https://docs.python.org/3/library/subprocess.html#security-considerations

# Coding style and General guidelines:

[TODO]

# Tests and Debugging guidelines:

[TODO]

### License:

MIT

### Resources:

* https://github.com/rochacbruno/flask_simplelogin
* https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xix-deployment-on-docker-containers
* https://pythonhosted.org/Flask-Bootstrap/forms.html

### Looking for a more comprehensive solution? look at below link:

https://github.com/wooey/Wooey

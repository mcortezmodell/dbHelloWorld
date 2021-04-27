# dbHelloWorld
Flask application that creates a simple webapp and connects to a sqlite database.


# Install 

Create a virtualenv and active it: 
```
$ python3 -m venv venv
$ .venv/bin/activate 
```

Or on Windows cmd: 
```
$ py -3 -m venv venv
$ venv\Scripts\activate.bat
```

# Run 
```
$ export FLASK_APP=application.py
$ export FLASK_ENV=development
$ flask run
```
Or on Windows cmd: 
```
$ set FLASK_APP=application.py
$ set FLASK_ENV=development
$ flask run
```

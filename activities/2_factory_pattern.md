TODO: Modify to remove the config class code and instead move this to the config activity.

# Apply the Factory pattern to a Flask app

In this activity we will cover an architectural pattern used in Flask apps:

- [Application Factory](https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/)

## Application Factory

To date we have seen the application object created in `app.py` where are also defined the routes.

If we move the creation of the Flask object into a function, we can then create multiple instances of this app later.

The advantages of this approach are:

- Testing. You can have instances of the application with different settings to test every case.
- Multiple instances. Imagine you want to run different versions of the same application. You can have multiple
  instances of the same application running in the same application process which can be handy.

For this course (COMP0034), the main purpose is to support testing. It is also a convenient way to configure and enable
a number of the Flask extensions that we will be using in the project such as Flask-Login, Flask-SQLAlchemy and
Flask-WTF.

To use this approach you will define a function called `create_app`. For this example we are going to create it in
the `__init__.py` for `my_flask_app` (or whatever you renamed this directory to).

### Create a new function in `my_flask_app/__init__.py`

We are going to create the function and inside the function create an instance of the Flask app.

Your Python code might look something like this:

```python
from flask import Flask


def create_app():
    """
    Initialise the Flask application.
    :rtype: Returns a configured Flask object
    """
    app = Flask(__name__)

    return app
```

We now need to call the function to create the app. For now we will do this in app.py with the following code:

```python

from my_flask_app import create_app

app = create_app()


@app.route('/')
def index():
    return 'This is the home page for my_flask_app'


if __name__ == '__main__':
    app.run(debug=True)

```

Run app.py and check that you can access it at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

Note: for convenience the examples in class use the app.run() method to run the app whereas
the [Flask documentation](https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/#run-the-application) uses a
command line approach. You can use either approach though please make it clear in your README.md how your app should be run.

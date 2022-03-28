# Lab 6: Configure your Flask app for the coursework

## Create coursework repository

You may continue using the same repo as for coursework 1. 

If you wish to create a new repo then please do so using the relevant links in the Moodle assessment section.

You will need to add your Dash app files, including data set, to the new repository.

Make sure you 'add' the files, 'commit' them and 'push' them back to GitHub so your teammates can 'pull' the changes to
their local development environments.

## Create the Flask app directory structure for coursework 2

**Only one person per group will need to create this**, however it is strongly recommended that you use pair programming
or at a minimum peer review the structure.

Create an appropriate directory structure (see activity 1 - create Flask app for guidance). For example (replace
`my_flask_app` with an appropriate name for your app!):

```
/yourapplication
    flask_db.sqlite
    /my_flask_app
        __init__.py
        app.py
        /static
            ... css will go here
        /templates
            ... html files will go here
    /my_dash_app
        __init__.py
        /assets
            ... dash css here
        /data
            ... dataset will go here
        my_dash_app.py
    /venv
    .gitignore
    README.md
    setup.py
    MANIFEST.in
```

Remember to add, commit and push your changes to GitHub so the rest of the group can pull them.

## Install additional libraries in your venv and update requirements.txt

**Everyone in a group** needs to install the following in their venv (if not already installed) flask, Flask-SQLAlchemy,
Flask-Login, Flask-WTF, pandas, dash, Plotly, dash_bootstrap_components.

**One person per group** should update requirements.txt. You can either manually type in the packages or in the terminal
use the following which will overwrite your existing requirements.txt file.

```terminal
pip freeze > requirements.txt
```

## Create the Flask app using the Flask factory pattern

**Only one person per group** should do this.

Use the 2_factory_pattern.md activity to help you with this.

The code will go in `/my_flask_app/__init__.py` e.g.

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

We now need to call the function to create the app. Edit `app.py` e.g.

```python
from my_flask_app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
```

Make sure you push the changes back to GitHub so you team mates can 'pull' the changes to their local development
environments.

## Configure your Flask app

**Only one person per group** should do this. 

Decide which approach you will use to configure your Flask app. Read 3_configure_flask_app.md for guidance.

The minimum that you will need to configure is: 

- SECRET_KEY
- SQLALCHEMY_DATABASE_URI
- SQLALCHEMY_TRACK_MODIFICATIONS = False

You may need to add other parameters, for example `SQLALCHEMY_ECHO = True` can be useful when you are testing and debugging interactions with your SQLite database.

Make sure you push the changes back to GitHub so you team mates can 'pull' the changes to their local development
environments.

## Using Blueprints to define modules in your app

At this stage you haven't created any routes. However, you may wish to work through the 4_blueprints.md activity and
decide whether to use any in your coursework.

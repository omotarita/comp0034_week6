# Create a new Flask app project and modify the file and folder structure

The following gives instructions using PyCharm Professional and VS Code. It is likely that similar functions exist in
other IDEs though you will need to refer to their documentation.

## Create a new project with a basic Flask app

In PyCharm Professional (not available in the community edition), when you select the menu option File > New project
there is an option to create a new Flask project and this will install Flask and any dependencies and create the basic
folder structure and app.py.
The [PyCharm documentation is here](https://www.jetbrains.com/help/pycharm/creating-flask-project.html).

In VS Code follow the [instructions here](https://code.visualstudio.com/docs/python/tutorial-flask) to create a new
project, create a venv and install Flask.

For other IDEs follow the [installation instructions](https://flask.palletsprojects.com/en/2.0.x/installation/) in the
Flask documentation. You will then need to create the following two subdirectories in your Flask project
directory: `/static` and `/templates`.

## Add a README.md

Create a new file called README.md.

You will need to use markdown to edit the file.

For now you can copy the following into README.md:

```markdown
# COMP0034 Week 6

## Flask app example with a basic structure

A minimal app to demonstrate how to structure and configure a Flask app.
```

## Create a requirements.txt

Open the Terminal in PyCharm (or open a command line and navigate to your venv).

Enter `pip freeze > requirements.txt`

This will generate a requirements.txt file with the package dependencies for the project. Note: if you add more
dependency packages to your project you will need to either add these to requirements.txt or run the command again and
replace the existing file.

## Add a .gitignore file

If you are using PyCharm and have installed and enabled the .ignore plug in then you should be able to
select `File | New | .ignore file | .gitignore`. If you search for 'python' you should find and select the JetBrains and
the Python templates and create the .ignore.

If you are using VSCode you may want to
install [this extension](https://marketplace.visualstudio.com/items?itemName=codezombiech.gitignore) which allows you to
create a .gitignore file by choosing templates for Python.

Alternatively you can copy a `.gitignore` from one of your earlier projects into this project directory.

## Create a new python package for the app

In PyCharm this is File | New | Package. You can call it `my_first_app` or any name you wish.

For other IDEs, or if you create a directory from a command line, then inside the directory you need to create a blank
python file called `__init__.py` (in Pycharm this is created when you select the Python Package option for the new file)
.

## Move the `static` and `templates` folders and app.py into the python package you just created

If you are working in an IDE then you should use refactoring to move files so that any references to them in other files
are updated. In PyCharm you can use Refactor | Move (though dragging to another folder within PyCharm refactors by
default).

## [OPTIONAL] Create setup.py and MANIFEST.in

You do not need to create the following, this is only for those who wish to create a distributable package.

Read [Making the project installable](https://flask.palletsprojects.com/en/1.1.x/tutorial/install/) and then create
a `setup.py` and `MANIFEST.in` for your project.

The setup.py file describes your project and the files that belong to it. It might look like this:

```python
# setup.py

from setuptools import find_packages, setup

setup(
    name='my_app',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
```

The `install_requires` lists packages that are required, you may think this is the same as `requirements.txt` however
their uses are slightly different and you should read
the [documentation](https://packaging.python.org/discussions/install-requires-vs-requirements/).

To include other files, such as the static and templates directories, include_package_data is set. Python needs another
file named MANIFEST.in to tell what this other data is. It might look like this:

```text
# MANIFEST.in

graft my_app/static
graft my_app/templates
global-exclude *.pyc
```

## Check your structure

You should now have something like this:

```
/yourapplication
    /my_app
        __init__.py
        app.py
        /static
            ... css will go here
        /templates
            ... html files will go here
    /venv
    .gitignore
    README.md
    setup.py
    MANIFEST.in
```

## Create a basic Flask app

If you are using PyCharm Professional and used the 'New Flask Project' method then you will already have a file
called `app.py`. Use the menu option File | Refactor and move it to the `/my_fist_app` package.

If you are using any other IDE then in the `/my_first_app` directory create a file called `app.py` with the following
code:

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
```

Run the Flask app and check that it launches.

See [Flask structure recommendations](https://flask.palletsprojects.com/en/2.0.x/patterns/packages/) for more guidance.

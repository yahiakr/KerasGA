# KerasGA

A simple and easy-to-use implementation of Genetic Algorithm for Keras NN models in Python.

## Features

* Preconfigured setup for [Travis CI](https://travis-ci.org/), [Coveralls](https://coveralls.io/), and [Scrutinizer](https://scrutinizer-ci.com/)
* `pyproject.toml` for managing dependencies and package metadata
* `Makefile` for automating common [development tasks](https://github.com/jacebrowning/template-python/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/CONTRIBUTING.md):
    - Installing dependencies with `poetry`
    - Automatic formatting with `isort` and `black`
    - Static analysis with `pylint`
    - Type checking with `mypy`
    - Docstring styling with `pydocstyle`
    - Running tests with `pytest`
    - Building documentation with `mkdocs`
    - Publishing to PyPI using `poetry`
    
If you are instead looking for a [Python application](https://caremad.io/posts/2013/07/setup-vs-requirement/) template, check out one of the sibling projects:

* [jacebrowning/template-django](https://github.com/jacebrowning/template-django)
* [jacebrowning/template-flask](https://github.com/jacebrowning/template-flask)

## Examples

Here are a few projects based on this package:

* [yahiakr/FlappyAI](https://github.com/yahiakr/FlappyAI)
* [yahiakr/SnakeAI](https://github.com/yahiakr/SnakeAI)

## Usage

Install `cookiecutter` and generate a project:

```
$ pip install cookiecutter
$ cookiecutter gh:jacebrowning/template-python -f
```

Cookiecutter will ask you for some basic info (your name, project name, python package name, etc.) and generate a base Python project for you.

If you still need to use legacy Python or `nose` as the test runner, older versions of this template are available on branches:

```
$ cookiecutter gh:jacebrowning/template-python -f --checkout=python2

$ cookiecutter gh:jacebrowning/template-python -f --checkout=nose
```

## Updates

Checkout the appropriate branch of [template-python-demo](https://github.com/jacebrowning/template-python-demo) and manually merge changes into your project.

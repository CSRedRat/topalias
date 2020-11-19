# How to contribute

topalias developed in PyCharm, pienv (earlier Anaconda) with Python 3.8. Package will run on Python 3.6-3.9.

## Dependencies

```bash
pip3 install -r requirements-dev.txt
pip3 install -r requirements.txt
#pip freeze > requirements-freeze.txt # for freeze current env req
```

Add git hooks:

```bash
pre-commit install -t pre-commit
pre-commit install -t pre-push
```

If you use conda:

```bash
conda install --yes --file requirements-dev.txt
conda install --yes --file requirements.txt
conda install -c conda-forge pre-commit  # work only in Linux
```

You can use [poetry](https://github.com/python-poetry/poetry) to manage the dependencies.

To install them you would need to run `install` command:

```bash
poetry install
```

To activate your `virtualenv` run `poetry shell`.

You can use [pipfile](https://github.com/pypa/pipfile) to manage the dependencies.

To install them you would need to run `pipenv install` command:

```bash
pipenv install --dev
#pipenv lock # if need update Pipfile.lock
```

Setup pre-commit and pre-push hooks:

```bash
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## Local package build

Install from sources:

```bash
python3 setup.py install
```

Build wheel-package:

```bash
pip3 install -U --user twine wheel setuptools
python3 setup.py sdist bdist_wheel
#twine upload -r testpypi dist/* # upload package to test.pypi.org
```

## One magic command

Run `make test` to run everything we have!

## Tests

We use `pytest` and `flake8` for quality control.
We also use [wemake_python_styleguide](https://github.com/wemake-services/wemake-python-styleguide) to enforce the code quality.

To run all tests:

```bash
pytest
```

To run linting:

```bash
flake8 .
```

Keep in mind: default virtual environment folder excluded by flake8 style checking is `.venv`.
If you want to customize this parameter, you should do this in `setup.cfg`.
These steps are mandatory during the CI.

## Submitting your code

We use [trunk based](https://trunkbaseddevelopment.com/)
development (we also sometimes call it `wemake-git-flow`).

What the point of this method?

1. We use protected `master` branch,
   so the only way to push your code is via pull request
2. We use issue branches: to implement a new feature or to fix a bug
   create a new branch named `issue-$TASKNUMBER`
3. Then create a pull request to `master` branch
4. We use `git tag`s to make releases, so we can track what has changed
   since the latest release

So, this way we achieve an easy and scalable development process
which frees us from merging hell and long-living branches.

In this method, the latest version of the app is always in the `master` branch.

### Before submitting

Before submitting your code please do the following steps:

1. Run `pytest` to make sure everything was working before
2. Add any changes you want
3. Add tests for the new changes
4. Edit documentation if you have changed something significant
5. Update `CHANGELOG.md` with a quick summary of your changes
6. Run `pytest` again to make sure it is still working
7. Run `flake8` to ensure that style is correct
8. Run `doc8` to ensure that docs are correct

## Get Started!

Ready to contribute? Here's how to set up `topalias` for local development.

1. Fork the `topalias` repo on GitHub.
2. Clone your fork locally::

    \$ git clone git@github.com:your_name_here/topalias.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv topalias
    $ cd topalias/
    \$ python setup.py develop

4. Create a branch for local development::

    \$ git checkout -b name-of-your-bugfix-or-feature

    Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox::

    $ flake8 topalias tests
    $ python setup.py test or pytest
    \$ tox

    To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    \$ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

### Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.md.
3. The pull request should work for Python 3.5, 3.6, 3.7, 3.8 and 3.9, and for PyPy. Check
   https://travis-ci.com/CSRedRat/topalias/pull_requests
   and make sure that the tests pass for all supported Python versions.

## Other help

You can contribute by spreading a word about this library.
It would also be a huge contribution to write
a short article on how you are using this project.
You can also share your best practices with us.

### Report Bugs

Report bugs at https://github.com/CSRedRat/topalias/issues.

If you are reporting a bug, please include:

-   Your operating system name and version.
-   Any details about your local setup that might be helpful in troubleshooting.
-   Detailed steps to reproduce the bug.

## Deploying

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in CHANGELOG.md).
Then run::

    $ bump2version patch  # possible: major / minor / patch
    $ git push
    $ git push --tags

Travis will then deploy to PyPI if tests pass.

## Add to contributors

Comment on an issue or pull request with:
@all-contributors please add @CSRedRat for code, infra, tests, ideas, maintenance, platform, mentoring and example ✨

# Future Proof Your Python

## Tools

* pyenv - install whatever versions of Python you want to test against
* tox
* unittest, nose, py.test, etc

## Pyenv installation

* [Show web page](https://github.com/yyuu/pyenv)
* Install with homebrew if possible (`brew install pyenv`)
* Otherwise, use [the installer](https://github.com/yyuu/pyenv-installer)
* Install Python versions
  `pyenv install 2.7.9`
  `pyenv install 3.4.1`
* Set global/local order
  `pyenv global 3.4.1 2.7.9`
  `pyenv local 3.4.1 2.7.9`
* Whatever you set here will be your "default" Python

## What's tox?

* Runs tests under multiple configurations. Multiple versions of Python, or Django, or whatever
* Show basic tox.ini

## py.test

* Alternative to `unittest`
* Easier to use with `tox` so that's what we're doing

## Live coding!

* Show current files
* Show current tests
* Run tests, show fails

* Add `# -*- coding: utf-8 -*-`
* Add `(object)` to classes
* Fix `super()`
* Add `from __future__ import unicode_literals` so everything is unicode
* Fix Unicode `.encode('utf-8').decode('utf-8')`
* Add `try` and `except` blocks for Unicode
* Add `from __future__ import division` to fix `dog_years`
* Add `from __future__ import print_function` to fix printing

## Other useful things

* Iterators (use `list`)
* Exceptions (use `as`)
* bytes vs strings
* six
* futurize
* modernize
* python2 -3
* python3 -b

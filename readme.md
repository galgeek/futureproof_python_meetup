# Treehouse

## Future Proof Your Python

Meetup on May 20, 2015. Presented by Kenneth Love.

### Getting Started

You'll need to install [pyenv](https://github.com/yyuu/pyenv) and [tox](http://tox.readthedocs.org/en/latest/).

Then you'll want to install multiple version of Python, at least the latest 2.7 and 3.4. You'll do this with:

```
$ pyenv install 2.7.9 && pyenv install 3.4.2
```

Of course, if newer versions are out, feel free to use them.

Then run the test suite against both Pythons by running `tox`. Tests will fail! Fix code until the tests don't fail!


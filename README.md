<pre><code>8""""8                           8""""8
8      eeeee eeeee eeeee eeee    8      eeeee e    e e     eeee
8eeeee   8   8   8   8   8       8eeeee   8   8    8 8     8
    88   8e  8eee8   8e  8eee        88   8e  8eeee8 8e    8eee
e   88   88  88  8   88  88      e   88   88    88   88    88
8eee88   88  88  8   88  88ee    8eee88   88    88   88eee 88ee </code></pre>

A Python library that standardizes the names of U.S. states

[![Build Status](https://travis-ci.org/datadesk/latimes-statestyle.png?branch=master)](https://travis-ci.org/datadesk/latimes-statestyle)
[![PyPI version](https://badge.fury.io/py/latimes-statestyle.png)](http://badge.fury.io/py/latimes-statestyle)
[![Coverage Status](https://coveralls.io/repos/datadesk/latimes-statestyle/badge.png?branch=master)](https://coveralls.io/r/datadesk/latimes-statestyle?branch=master)

* Issues: [https://github.com/datadesk/latimes-statestyle/issues](https://github.com/datadesk/latimes-statestyle/issues)
* Packaging: [https://pypi.python.org/pypi/latimes-statestyle](https://pypi.python.org/pypi/latimes-statestyle)
* Testing: [https://travis-ci.org/datadesk/latimes-statestyle](https://travis-ci.org/datadesk/latimes-statestyle)
* Coverage: [https://coveralls.io/r/datadesk/latimes-statestyle](https://coveralls.io/r/datadesk/latimes-statestyle)

Features
--------

-   Submit a state’s name, postal code or Associated Press abbreviation or [FIPS
    code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards)
    and receive a clean object with all other formats as attributes.
-   State objects also provide the “stateface” code for [ProPublica’s
    web font of state shapes](http://propublica.github.com/stateface/)

Getting started
---------------

Getting started is as easy as…

```bash
$ pip install latimes-statestyle
```

Then start feeding it your data.

```python
>>> import statestyle
# Get by postal code
>>> obj = statestyle.get('CA')
```

If there is a match you can access the clean, standardized attributes.

```python
# Here's the full name of the state
>>> print obj.name
California
# The U.S. postal code
>>> print obj.postal
CA
# The Associated Press style abbreviation
>>> print obj.ap
Calif.
# The FIPS ID code
>>> print obj.fips
6
# The type of geographic area
>>> print obj.type
state
# The ProPublic stateface code
>>> obj.stateface
"E"
```

You can pass in any of the attributes for a match.

```python
# Like the FIPS code
>>> obj = statestyle.get(6)
# And the same attributes available
>>> print obj.name
California
```

Here's what happens when you submit something that doesn't have a match.

```python
>>> statestyle.get("foo")
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "statestyle/__init__.py", line 27, in get
    raise ValueError("The state you requested does not exist")
ValueError: The state you requested does not exist
```

And here's a couple ways you can convert the object it returns to a dictionary.

```python
>>> o = statestyle.get("CA")
>>> dict(o)
{'name': 'California', 'ap': 'Calif.', 'fips': '6', 'postal': 'CA', 'type': 'state', 'stateface': 'E'}
>>> o.to_dict()
{'name': 'California', 'ap': 'Calif.', 'fips': '6', 'postal': 'CA', 'type': 'state', 'stateface': 'E'}
# You can also access the attributes as dictionary keys if you want
>>> o['name']
'California'
```

Contributing
------------

If you would like to add another feature or change existing data, edit
`statestyle/data.csv` and then run `python build.py`, which will remake
the data file imported by the library.

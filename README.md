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

Then start feeding it your data:

```python
>>> import statestyle
# Get by postal code
>>> obj = statestyle.get('CA')
# Fiddle with the clean attributes
>>> print obj.name
California
>>> print obj.postal
CA
>>> print obj.ap
Calif.
# Get by FIPS code
>>> obj = statestyle.get(6)
# Same attributes available
>>> print obj.name
California
>>> obj.stateface
"E"
# Here's what happens when you submit something that doesn have a match
>>> statestyle.get("foo")
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "statestyle/__init__.py", line 27, in get
    raise ValueError("The state you requested does not exist")
ValueError: The state you requested does not exist</code>
```

Contributing
------------

If you would like to add another feature or change existing data, edit
`statestyle/data.csv` and then run `python build.py`, which will remake
the data file imported by the library.

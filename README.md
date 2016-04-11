# system-programming [<img src="https://travis-ci.org/saravanakumar-periyasamy/system-programming.svg?branch=master">](https://travis-ci.org/saravanakumar-periyasamy/system-programming)

## Requirements

* Python 2.7
* virtualenvwrapper

## Install

1. Install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)
2. Create a virtualenv `$ mkvirtualenv system-programming`
3. Install library and requirements `pip install -r requirements.txt`
4. Run the tests `python -m unittest test_diskusage`


## Usage

```python diskusage.py <<directory/mount point>>```

```eg., python diskusage.py /tmp```

And sample output will look like this

```json
{
    "files": [
        {
            "name": "/tmp/123",
            "size": 23
        },
        {
            "name": "/tmp/abc/123",
            "size": 56
        }
    ]
}
```
   
## Build

This repo is hooked to Travis CI, and it runs through the unit test cases for every commit. Refer `.travis.yml` for more information.
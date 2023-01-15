[![](https://img.shields.io/pypi/pyversions/python-imageutil.svg?color=blue&logo=python&logoColor=white)](https://www.python.org/)
[![](https://img.shields.io/pypi/v/python-imageutil.svg?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/python-imageutil/)
[![](https://pepy.tech/badge/python-imageutil/month)](https://pepy.tech/project/python-imageutil)
[![](https://img.shields.io/github/stars/fabiocaccamo/python-imageutil?logo=github)](https://github.com/fabiocaccamo/python-imageutil/)
[![](https://img.shields.io/pypi/l/python-imageutil.svg?color=blue)](https://github.com/fabiocaccamo/python-imageutil/blob/main/LICENSE.txt)

[![](https://results.pre-commit.ci/badge/github/fabiocaccamo/python-imageutil/main.svg)](https://results.pre-commit.ci/latest/github/fabiocaccamo/python-imageutil/main)
[![](https://img.shields.io/github/actions/workflow/status/fabiocaccamo/python-imageutil/test-package.yml?branch=main&label=build&logo=github)](https://github.com/fabiocaccamo/python-imageutil)
[![](https://img.shields.io/codecov/c/gh/fabiocaccamo/python-imageutil?logo=codecov)](https://codecov.io/gh/fabiocaccamo/python-imageutil)
[![](https://img.shields.io/codacy/grade/e387a301748f4877b30dc4443bcadc00?logo=codacy)](https://www.codacy.com/app/fabiocaccamo/python-imageutil)
[![](https://img.shields.io/codeclimate/maintainability/fabiocaccamo/python-imageutil?logo=code-climate)](https://codeclimate.com/github/fabiocaccamo/python-imageutil/)
[![](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# python-imageutil
🎩 elegant image operations on top of `Pillow`.

## Installation
```bash
pip install python-imageutil
```

## Testing
```bash
# clone repository
git clone https://github.com/fabiocaccamo/python-imageutil.git && cd python-imageutil

# create virtualenv and activate it
python -m venv venv && . venv/bin/activate

# upgrade pip
python -m pip install --upgrade pip

# install requirements
pip install -r requirements.txt -r requirements-test.txt

# run tests using tox
tox

# or run tests using unittest
python -m unittest
```

## License
Released under [MIT License](LICENSE.txt).

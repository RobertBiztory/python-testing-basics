# Readme for thething

## Folder structure, packaging, imports

src/your-module-name -> the source code  
tests/ -> tests for your code  

Pyproject.toml -> packages the code and makes it installable  

```sh
# this installs your python code in development mode
pip install -e .

```

The reason you do this is so you do not have to mess around with relative imports.

```py

# in src/thething/main.py
from thething.module import whatever

# in tests/whatever.py
from thething.module import whatever

# in src/nested/nested/nested/nested/etc.py
from thething.module import whatever
```

Sucks a little bit to get it up and running, but you never have to do these kinds of gymnastics:

```py

# file1.py
from module.thing import function

#subfolder/anotherone/ohboy/file.py
from ....module.thing import function_hopefully

>> ImportError: attempted relative import with no known parent package

```


## Tests
Using pytest, will autodiscover tests inside of the tests/ subfolder and find files that start or end with a "test" prefix or suffix.

```sh

pytest

================================== test session starts ===================================
platform darwin -- Python 3.11.9, pytest-8.3.3, pluggy-1.5.0 -- /Users/robert/Documents/python-testing/.venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/robert/Documents/python-testing
configfile: pyproject.toml
collected 8 items                                                                        

tests/test_module.py::test_f1_output PASSED                                        [ 12%]
tests/test_module.py::test_f2_output PASSED                                        [ 25%]
tests/test_module.py::test_f3_output PASSED                                        [ 37%]
tests/test_module.py::test_f4_output[1-1-2] PASSED                                 [ 50%]
tests/test_module.py::test_f4_output[2-1-3_0] PASSED                               [ 62%]
tests/test_module.py::test_f4_output[2-1-3_1] PASSED                               [ 75%]
tests/test_module.py::test_f4_exception PASSED                                     [ 87%]
tests/test_nested.py::test_nested_module PASSED                                    [100%]

=================================== 8 passed in 0.01s ====================================



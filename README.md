# Python-C/C++ examples

Examples of interaction between Python and C/C++.


## PyBind Examples

We need to clone and install [pybind](https://pybind11.readthedocs.io/) to run the examples.

To get it as a submodule:

```
git submodule init
git submodule update
cd pybind11/
pip install .
```

Then, run pybind example:

```
cd pybind_examples/02_type_conversions
cmake .
make
python example.py
```

**Note**: Examples `00_sum` and `01_objects` use plain Makefiles instead of cmake. 

all:
		g++ -O3 -Wall -shared -std=c++11 -fPIC `python -m pybind11 --includes` example.cpp -o example`python-config --extension-suffix`
clean:
		rm example`python-config --extension-suffix`

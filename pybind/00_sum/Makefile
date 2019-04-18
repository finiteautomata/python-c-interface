CFLAGS := -O3 -Wall -std=c++11 $(shell python -m pybind11 --includes)

all:
		g++ -shared -fPIC $(CFLAGS) example.cpp -o example`python-config --extension-suffix`
clean:
		rm example`python-config --extension-suffix`

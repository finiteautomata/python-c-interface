INCLUDE_DIR=/home/jmperez/.pyenv/versions/3.6.5/include/python3.6m
CC=g++
CFLAGS=-Wall -I $(INCLUDE_DIR)
SOURCES=$(wildcard *.c)
OBJECTS=$(SOURCES:.c=.o)


all: libstringtools.so

libstringtools.so: string_tools.o
	$(CC) -shared $< -o $@

%.o: %.c
	$(CC) $(CFLAGS) -c -fPIC -o $@ $<

clean:
	rm libstringtools.so
	rm *.o

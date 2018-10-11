INCLUDE_DIR=/home/jmperez/.pyenv/versions/3.6.5/include/python3.6m
CC=gcc
CFLAGS=-Wall -I $(INCLUDE_DIR)
SOURCES=$(wildcard *.c)
OBJECTS=$(SOURCES:.c=.o)


all: libspam.so

libspam.so: spam.o
	$(CC) -shared spam.o -o libspam.so

%.o: %.c
	$(CC) $(CFLAGS) -c -fPIC -o $@ $<

clean:
	rm libspam.so
	rm *.o

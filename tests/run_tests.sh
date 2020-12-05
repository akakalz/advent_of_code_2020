#!/bin/sh

export PYTHONPATH=/src

flake8 --ignore E24,W504,E501 .
flakeExit=$?

if [ $flakeExit -ne 0 ]; then
    echo "flake error"
    exit $flakeExit
fi

pytest
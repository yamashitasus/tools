#!/bin/bash

pip install termcolor
echo ${0%/*}/init.py
${0%/*}/../init.py

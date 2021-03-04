#! /bin/bash
PATH="/usr/local/bin:/usr/bin:/bin"

cd /Users/andrei/french
pipenv run python verbedujour.py >> log.txt

#! /bin/bash

# activate virtualenv
cd /Users/andrei/french
source fr-venv/bin/activate

# virtualenv now active
python verbedujour.py >> log.txt

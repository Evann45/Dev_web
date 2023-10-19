#!/bin/bash

pip install -r requirements.txt
echo " "
flask initdb
flask run
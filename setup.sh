#!/bin/sh

VENV_NAME=slideshow_venv

virtualenv ${VENV_NAME}

source ${VENV_NAME}/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
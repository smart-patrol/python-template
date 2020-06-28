#!/usr/bin/env/python3
from logging import config

import yaml

# source
# https://dev.to/martinheinz/ultimate-guide-to-python-debugging-1739
with open("config.yaml", "rt") as f:
    config_data = yaml.safe_load(f.read())
    config.dictConfig(config_data)

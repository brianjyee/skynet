#!/bin/bash
env FLASK_CONFIG='skynet.settings.test.TestingConfig' python -m unittest discover

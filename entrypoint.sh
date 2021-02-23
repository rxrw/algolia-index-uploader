#!/bin/sh

pip install algoliasearch

python3 /main.py ${GITHUB_WORKSPACE}/${INDEX_PATH}

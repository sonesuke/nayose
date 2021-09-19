#!/bin/bash

set -eu

# change version
if [ $# != 1 ]
then
  echo "bash build.sh <version-number>"
  exit 1
fi
sed -e "s/__version__ = \".*\"/__version__ = \"${1}\"/" -i /app/nayose/__init__.py
poetry version ${1}
sed -e "s/assert __version__ == \".*\"/assert __version__ == \"${1}\"/" -i /app/tests/test_nayose.py

# install libraries
poetry install

# test
pysen run lint
pytest

# build and publish
poetry config http-basic.pypi "__token__" "${PYPI_API_TOKEN}"
poetry build
poetry publish


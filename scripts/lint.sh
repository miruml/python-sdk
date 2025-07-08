#!/usr/bin/env bash

set -ex

mypy miru
ruff check miru
ruff format --check miru

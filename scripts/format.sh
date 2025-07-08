#!/bin/sh -e
set -x

ruff check --fix miru
ruff format miru

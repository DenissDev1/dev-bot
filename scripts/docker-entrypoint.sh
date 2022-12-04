#!/bin/sh

set -e

# if [ -n "${RUN_MIGRATIONS}" ]; then
# exec alembic upgrade head
# fi

exec python -O -m app
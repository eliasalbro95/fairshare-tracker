#!/bin/bash
set -e

# Your additional setup commands go here
# For example, start PostgreSQL
if [ "$1" = 'start_postgres' ]; then
    exec postgres --port=57352
fi

# exec 
# ---------- Python Intializtion ----------

# exec gunicorn core.wsgi:application --bind '0.0.0.0:$PORT'

# Run the default command (e.g., Gunicorn)
# WORKDIR /app

# COPY requirments.txt .

# RUN pip install -r requirments.txt 
# COPY . .
# # EXPOSE 8000
# EXPOSE $PORT
exec "$@"
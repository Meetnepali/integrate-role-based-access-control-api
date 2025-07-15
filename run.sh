#!/bin/bash
set -e
bash install.sh
source venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000

#!/bin/bash
bash refresh_data.sh
python3 load.py search.html roster.db

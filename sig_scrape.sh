#!/bin/sh
cd services/
python scrape_services.py
python parse_services.py
cd ../
find . -name '*.xml' -type f -delete

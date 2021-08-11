#! /bin/bash
echo "starting now"
cd ~/repos/stock-scraper/.env
source bin/activate

python3 ~/repos/stock-scraper/main.py >> ~/repos/stock-scraper/log 2>&1

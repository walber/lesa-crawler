#!/bin/bash
docker-compose down || true
docker rmi scrapyd:1.0 || true
docker rmi splash:1.0 || true
su -c 'rm -rf kibana/data/* elasticsearch/data/* crawler/items/ crawler/logs/ crawler/dbs/ crawler/twistd.pip crawler/lesaticket/__pycache__/ crawler/lesaticket/spiders/__pycache__/'

#!/bin/bash
docker-compose down &&
docker rmi scrapyd:1.0 &&
docker rmi splash:1.0 &&
su -c 'rm -rf kibana/data/* elasticsearch/data/* crawler/items/ crawler/logs/ crawler/dbs/ crawler/twistd.pip crawler/lesaticket/__pycache__/ crawler/lesaticket/spiders/__pycache__/'

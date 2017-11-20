# LESA Crawler

A web crawler that uses the Elasticsearch, Kibana, Scrapy framework, Splash javascript rendering service on top of a Docker containerized application archtecture that aims to retrieve data from LESA tickets.

## Getting Started

Since current LESA doesn't provide any sort of REST API to retrieve data from tickets, I've started developping a web crawler that aquire data through Xpath queries. All data retrieved is stored in an Elasticsearch index where it can be visualized through Kibana.

### Prerequisites

To run this app you will need to install:
* Docker (version 17.09.0+)
* docker-compose (version 1.16.1+)

## Configuration

1. Clone this project.
2. Replace the **SCREEN_NAME** and **TIME_ZONE** values with your LESA screen name and time zone:
```python
# lesa-crawler/crawler/lesaticket/lesa.py
SCREEN_NAME = "screen.name"
TIME_ZONE = "<your time zone>" # Where "+0000" means GMT time zone.
```
3. You can also change the start mark of date range and region of the query:
```python
# lesa-crawler/crawler/lesaticket/lesa.py
START_MONTH = ...
START_DAY = ...
START_YEAR = ...
REGION_ID = ...
``` 
4. Encode your **email:password** using a base64 enconder. (Your LESA site credentials).
5. Replace the authorization hash code with yours: 
```python
# lesa-crawler/crawler/lesaticket/settings.py
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml, ...',
   'Accept-Language': 'en',
   'Authorization': 'Basic c2NyZWVuLm5hbWVAbGlmZXJheS5jb20=',
}
```
6. Set the time zone of scrapyd and splash Dockerfiles.

## Deployment

1. Run the following command to build the containers and startup the aplication.  
```
$ docker-compose --file <path to>/lesa-crawler/docker-compose.yml up --build
```
Or go to *lesa-crawler* directory and just enter:
```
$ docker-compose up --build
```
2. When it finishes its initialization, you are able to access the following URLs:
* http://localhost:9200 (user: elastic, password: changeme)
* http://localhost:5601 (same as above)
* http://localhost:6800 (The scrapyd web interface)
* http://localhost:8050 (The splash web interface)
3. If don't want to wait the application start crawling, execute the following command:
```
curl http://localhost:6800/schedule.json -d project=default -d spider=ticket
```

## Built With

* [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/5.5/docker.html) - An open-source full-text search and analytics engine.
* [Kibana](https://www.elastic.co/guide/en/kibana/5.5/_configuring_kibana_on_docker.html) - An open source visualization platform designed to work with Elasticsearch.
* [Scrapyd](https://hub.docker.com/r/vimagick/scrapyd/) - A service to run Scrapy spiders.
* [Splash](https://hub.docker.com/r/scrapinghub/splash/) - Lightweight, scriptable browser as a service with an HTTP API.

# LESA Crawler

TODO

## Getting Started

TODO

### Prerequisites

To run this app you will need to install:
* Docker (version 17.09.0+)
* docker-compose (version 1.16.1+)

## Configuration

1. Clone this project.
2. Replace the **SCREEN_NAME** value with your screen name:
```python
# lesa-crawler/crawler/lesaticket/lesa.py
SCREEN_NAME = "screen.name"
```
3. Encode your **screen.name:password** using a base64 enconder.
4. Replace the authorization hash code with yours: 
```python
# lesa-crawler/crawler/lesaticket/settings.py
DEFAULT_REQUEST_HEADERS = {
'Accept': 'text/html,application/xhtml+xml, ...',
'Accept-Language': 'en',
'Authorization': 'Basic c2NyZWVuLm5hbWU6cGFzc3dvcmQ=',
}
```

## Deployment

1. Run the following command to build the containers and startup the aplication.  
```
docker-compose up --build
``` 
2. When it finish its initialization, you are able to access the following URLs:
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
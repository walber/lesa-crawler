# LESA Crawler

TODO

## Getting Started

TODO

### Prerequisites

To run this app you will need to install:
Docker (version 17.09.0+)
docker-compose (version 1.16.1+)

## Deployment

1. Clone this project.
2. Encode your **screen.name:password** using a base64 enconder.
3. Replace the **SCREEN_NAME** value with your screen name:
```python
# lesa-crawler/crawler/lesaticket/lesa.py
SCREEN_NAME = "screen.name"
```
4. Replace the authorization hash code with yours: 
```python
# lesa-crawler/crawler/lesaticket/settings.py
DEFAULT_REQUEST_HEADERS = {
...

'Authorization': 'Basic c2NyZWVuLm5hbWU6cGFzc3dvcmQ=',
}
```
5. Run the following command to build the containers and startup the aplication.  
```
docker-compose up --build
``` 
TODO


## Built With

* [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/5.5/docker.html) - An open-source full-text search and analytics engine.
* [Kibana](https://www.elastic.co/guide/en/kibana/5.5/_configuring_kibana_on_docker.html) - An open source visualization platform designed to work with Elasticsearch.
* [Scrapyd](https://hub.docker.com/r/vimagick/scrapyd/) - A service to run Scrapy spiders.
* [Splash](https://hub.docker.com/r/scrapinghub/splash/) - Lightweight, scriptable browser as a service with an HTTP API.
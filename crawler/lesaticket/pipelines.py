# -*- coding: utf-8 -*-
import datetime
from elasticsearch_dsl import DocType, Index, Date, Byte, Keyword
from elasticsearch_dsl.connections import connections
from elasticsearch.exceptions import ConnectionError
from lesaticket.elastic_settings import ELASTICSEARCH_HOST, ELASTICSEARCH_PORT, ELASTICSEARCH_USER, ELASTICSEARCH_PASSWD
from lesaticket.lesa import TIME_ZONE

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

def to_datetime(date_str):

    parts = date_str.split()
    date_wout_tz = " ".join(parts[:-1])
    date_with_tz = "{} {}".format(date_wout_tz, TIME_ZONE)

    # Example: February 7, 2017 2:28:18 AM -0300
    # Date format: "%B %d, %Y %I:%M:%S %p %z"
    return datetime.datetime.strptime(date_with_tz, "%B %d, %Y %I:%M:%S %p %z")


def sla_datetime(created_date, severity):

    if severity == "Minor":
        return created_date + datetime.timedelta(weeks = 3)

    elif severity == "Major":
        return created_date + datetime.timedelta(weeks = 2)

    elif severity == "Critical":
        return created_date + datetime.timedelta(weeks = 1)

    else:
        raise ValueError("Unknown severity value: {}".format(severity))


class ElasticSearchIndexerPipeline(object):

    instance = connections.create_connection(
        host = ELASTICSEARCH_HOST,
        port = ELASTICSEARCH_PORT,
        http_auth=(ELASTICSEARCH_USER, ELASTICSEARCH_PASSWD)
    )

    index = Index("support")

    def __init__(self):
        try:
            self.is_connected = ElasticSearchIndexerPipeline.instance.ping()
            index = ElasticSearchIndexerPipeline.index
            if not index.exists():
                index.doc_type(Ticket)
                index.create()

            Ticket.init()
        except ConnectionError as ex:
            raise ValueError("Connection Failed.")


    def save(self, ** kwargs):
        return super(Ticket, self).save(** kwargs)


    def process_item(self, item, spider):
        if self.is_connected:
            id = item._values.pop("id", None)
            item._values["id"] = id
            created_date = item._values.pop("created_date", None)
            last_update = item._values.pop("last_update", None)
            due_date = item._values.pop("due_date", None)

            if created_date is None:
                item._values["created_date"] = "N/A"
                item._values["sla_date"] = "N/A"
            else:
                item._values["created_date"] = to_datetime(created_date)
                item._values["sla_date"] = sla_datetime(item._values["created_date"], item._values["severity"])

            if last_update is None:
                item._values["last_update"] = "N/A"
            else:
                item._values["last_update"] = to_datetime(last_update)

            if due_date is None:
                item._values["due_date"] = "N/A"
            else:
                item._values["due_date"] = to_datetime(due_date)

            if "feedback" in item._values:
                if item._values["feedback"] == "Yes":
                    item._values["feedback_value"] = 100
                else:
                    item._values["feedback_value"] = 0
            else:
                item._values["feedback"] = "N/A"

            if "cas" not in item._values:
                item._values["cas"] = "N/A"                

            ticket = Ticket(meta={"id": id}, ** item._values)
            ticket.save()

        return item

@ElasticSearchIndexerPipeline.index.doc_type
class Ticket(DocType):
    id = Keyword()
    severity = Keyword()
    escalation = Keyword()
    status = Keyword()
    resolution = Keyword()
    feedback = Keyword()
    feedback_value = Byte()
    project_name = Keyword()
    support_response = Keyword()
    environment = Keyword()
    language = Keyword()
    project_response = Keyword()
    created_date = Date()
    last_update = Date()
    due_date = Date()
    sla_date = Date()
    reporter = Keyword()
    assignee = Keyword()
    cas = Keyword()
    sales = Keyword()
    portal_version = Keyword()
    os = Keyword()
    application_server = Keyword()
    jvm = Keyword()
    database = Keyword()

    class Meta:
        index = "support"


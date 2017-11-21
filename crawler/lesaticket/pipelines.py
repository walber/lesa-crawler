# -*- coding: utf-8 -*-
from elasticsearch_dsl import DocType, Index, Date, Byte, Keyword
from elasticsearch_dsl.connections import connections
from elasticsearch.exceptions import ConnectionError
from lesaticket.custom_settings import INDEX_NAME, ELASTICSEARCH_HOST, ELASTICSEARCH_PORT, ELASTICSEARCH_USER, ELASTICSEARCH_PASSWD
from lesaticket.liferay_jira import LiferayJira

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
class ElasticsearchPipeline(object):

    instance = connections.create_connection(
        host = ELASTICSEARCH_HOST,
        port = ELASTICSEARCH_PORT,
        http_auth=(ELASTICSEARCH_USER, ELASTICSEARCH_PASSWD)
    )

    index = Index(INDEX_NAME)

    def __init__(self):
        liferay_jira = LiferayJira()
        self.issues = liferay_jira.issues()
        self.issues.update(liferay_jira.expired_sla_issues())
    
        try:
            self.is_connected = ElasticsearchPipeline.instance.ping()
            index = ElasticsearchPipeline.index
            if not index.exists():
                index.doc_type(Ticket)
                index.create()

            Ticket.init()
        except ConnectionError as ex:
            raise ValueError('Connection Failed.')


    def save(self, ** kwargs):
        return super(Ticket, self).save(** kwargs)


    def process_item(self, item, spider):
    
        if self.is_connected:
            
            buff = {}
            ticket_id = item._values['ticket_id']
            buff.update(self.issues.pop(ticket_id, {}))

            if 'feedback' in item._values:
                if item._values['feedback'] == 'Yes':
                    buff['feedback_value'] = 100
                else:
                    buff['feedback_value'] = 0
            else:
                buff['feedback'] = 'N/A'

            if 'cas' not in item._values:
                buff['cas'] = 'N/A'            

            item._values.update(buff)            
            ticket = Ticket(meta={'id': ticket_id}, ** item._values)
            ticket.save()

        return item
        

@ElasticsearchPipeline.index.doc_type
class Ticket(DocType):

    ticket_id = Keyword()
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
    reporter = Keyword()
    assignee = Keyword()
    cas = Keyword()
    sales = Keyword()
    portal_version = Keyword()
    os = Keyword()
    application_server = Keyword()
    jvm = Keyword()
    database = Keyword()
    components = Keyword()
    resolution_date = Date()
    expired_sla = Keyword()
    resolution_date = Date()
    components = Keyword()

    class Meta:
        index = INDEX_NAME
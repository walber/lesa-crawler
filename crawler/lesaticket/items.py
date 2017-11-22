# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import datetime
from scrapy import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
from lesaticket.custom_settings import TIME_ZONE


def str_trim(value):
    return value.strip()


def remove_parentesis(value):
    return str_trim(value).strip('()')


def coma_sepated_to_list(value):
    return map(str_trim, value.split(','))


def datetime_lesa(date_str):

    parts = date_str.split()
    date_wout_tz = ' '.join(parts[:-1])
    date_with_tz = '{} {}'.format(date_wout_tz, TIME_ZONE)

    # Example: February 7, 2017 2:28:18 AM -0300
    return datetime.datetime.strptime(date_with_tz, '%B %d, %Y %I:%M:%S %p %z')


def datetime_jira(date_str):

    # Example: 2017-09-04T15:43:17.000-0700
    return datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.000%z')


class LesaticketItem(Item):

    # Header info
    ticket_id = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    severity = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    pending = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    escalation = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    status = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    resolution = Field(
        input_processor = MapCompose(remove_parentesis),
        output_processor = TakeFirst()
    )
    feedback = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    feedback_value = Field()

    # Sidebar
    # Account detail
    project_name = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    support_response = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    environment = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    language = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    project_response = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )

    # Ticket details
    created_date = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    last_update = Field(
        input_processor = MapCompose(str_trim, datetime_lesa)
    )
    due_date = Field(
        input_processor = MapCompose(str_trim, datetime_lesa)
    )
    reporter = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    assignee = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    cas = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    sales = Field(
        input_processor = MapCompose(coma_sepated_to_list)
    )

    # Environment details
    portal_version = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    os = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    application_server = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    jvm = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    database = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    
    # From JIRA
    sla = Field()
    components = Field()
    resolution_date = Field(
        input_processor = MapCompose(datetime_jira)
    )

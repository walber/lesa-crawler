# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst


def str_trim(value):
    return value.strip()

def remove_parentesis(value):
    return str_trim(value).strip("()")

def coma_sepated_to_list(value):
    return map(str_trim, value.split(','))

class LesaticketItem(Item):

    # Header info
    id = Field(
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
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    due_date = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
    )
    sla_date = Field(
        input_processor = MapCompose(str_trim),
        output_processor = TakeFirst()
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

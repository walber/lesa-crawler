# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from scrapy.loader import ItemLoader
from lesaticket.items import LesaticketItem
from lesaticket.lesa import URLManager
from scrapy_splash import SplashRequest

class TicketSpider(Spider):

    name = "ticket"
    allowed_domains = ["liferay.com"]

    custom_settings = {
        'URL_MANAGER': URLManager()
    }

    def goto_page(self, page_num = 1):
        url = self.settings["URL_MANAGER"].get_url(page_num)
        return SplashRequest(url, callback=self.parse, endpoint='render.html',
            args={
                'resource_timeout': 60.0,
                'wait': 15.0,
                'images': 0,
                'render_all': 1
            },
            meta={
                'cookiejar': 'TicketSpider',
                'current_page': page_num,
            })


    def start_requests(self):
        yield self.goto_page()


    def parse(self, response):

        ticket_urls = response.css("div.results-table div.ticket-column a::attr(href)").extract()
        for url in ticket_urls:
            yield Request(url, callback=self.parse_ticket)

        self.logger.debug("URLS: {}".format(len(ticket_urls)))

        next_page_link = response.css('div.page-links a.next').extract_first()
        if next_page_link is not None:
            next_page = response.meta['current_page'] + 1
            self.logger.debug("GO TO PAGE: {}".format(next_page))
            yield self.goto_page(page_num = next_page)


    def parse_ticket(self, response):
        loader = ItemLoader(item = LesaticketItem(), response = response)

        # Header info
        loader.add_xpath("id", """//*[@id="_2_WAR_osbportlet_ticketDisplayId"]/a/text()""")
        loader.add_xpath("severity", """//*[@id="_2_WAR_osbportlet_severityDisplay"]/span/text()""")
        loader.add_xpath("pending", """//*[@id="_2_WAR_osbportlet_pendingDisplay"]/span/text()""")
        loader.add_xpath("escalation", """//*[@id="_2_WAR_osbportlet_ticketHeader"]/descendant::span[contains(text(),"Escalation:")]/span/text()""")
        loader.add_xpath("status", """//*[@id="_2_WAR_osbportlet_statusLabel"]/text()""")
        loader.add_xpath("resolution", """//*[@id="_2_WAR_osbportlet_resolutionLabel"]/text()""")
        loader.add_xpath("feedback", """//*[@id="_2_WAR_osbportlet_feedback"]/descendant::div[@class="aui-w50 content-column"]/descendant::div[@class="double-indent"]/text()""")

        # Sidebar
        # Account detail
        loader.add_xpath("project_name", """//*[@id="_2_WAR_osbportlet_accountEntryName"]/text()""")
        loader.add_xpath("support_response", """//*[@id="_2_WAR_osbportlet_supportResponseName"]/text()""")
        loader.add_xpath("environment", """//*[@id="_2_WAR_osbportlet_productEntryName"]/text()""")
        loader.add_xpath("language", """//div[@class="sidebar-account-detail section"]/div[4]/text()""")
        loader.add_xpath("project_response", """//div[@class="sidebar-account-detail section"]/div[5]/text()""")

        # Ticket details
        loader.add_xpath("created_date", """//div[@class="sidebar"]/div[@class="section last"]/descendant::div[contains(text(), " Created: ")]/span/@title""")
        loader.add_xpath("last_update", """//div[@class="sidebar"]/div[@class="section last"]/descendant::div[contains(text(), " Updated: ")]/span/@title""")
        loader.add_xpath("due_date", """//div[@class="sidebar"]/div[@class="section last"]/descendant::div[contains(text(), " Due: ")]/span/@title""")
        loader.add_xpath("reporter", """//*[@id="_2_WAR_osbportlet_reportedByUserName"]/text()""")
        loader.add_xpath("assignee", """//div[@class="sidebar"]/div[@class="section last"]/div[@class="sub-section"]/descendant::div[contains(text(), " Assignee: ")]/span/text()""")
        loader.add_xpath("cas", """//div[@class="sidebar"]/div[@class="section last"]/div[@class="sub-section"]/descendant::div[contains(text(), " CAS: ")]/span/text()""")
        loader.add_xpath("sales", """//div[@class="sidebar"]/div[@class="section last"]/div[@class="sub-section"]/descendant::div[contains(text(), " Sales: ")]/span/text()""")

        # Environment details
        loader.add_xpath("portal_version", """//div[@class="sidebar"]/div[@class="section last"]/div[@class="sub-section last"]/div[1]/span[2]/text()""")
        loader.add_xpath("os", """//div[@class="sidebar"]/div[@class="section last"]/div[@class="sub-section last"]/div[2]/span[2]/text()""")
        loader.add_xpath("application_server", """//div[@class="sidebar"]/div[@class="section last"]/div[@class="sub-section last"]/div[3]/span[2]/text()""")
        loader.add_xpath("jvm", """//div[@class="sidebar"]/div[@class="section last"]/div[@class="sub-section last"]/div[4]/span[2]/text()""")
        loader.add_xpath("database", """//div[@class="sidebar"]/div[@class="section last"]/div[@class="sub-section last"]/div[5]/span[2]/text()""")

        return loader.load_item()

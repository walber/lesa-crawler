# -*- coding: utf-8 -*-
from jira import JIRA
from lesaticket.custom_settings import LIFERAY_ISSUES_AUTORIZATION_HEADER, EXPIRED_SLA_SIT_ISSUES, SIT_ISSUES, SIT_FIELDS


JIRA.DEFAULT_OPTIONS['headers'].update(LIFERAY_ISSUES_AUTORIZATION_HEADER)

class LiferayJira(JIRA):


    def __init__(self):
        super(LiferayJira, self).__init__(server='http://issues.liferay.com')


    def exec_query(self, jql_query, fields):
        result = []
        offset = 0
        buff = self.search_issues(jql_query, json_result=True, maxResults=1000, startAt=offset, fields=fields)

        result.extend(buff['issues'])
        while len(buff['issues']) == 1000:
            buff['issues'][:] = []
            offset += 1000
            buff = self.search_issues(jql_query, json_result=True, maxResults=1000, startAt=offset, fields=fields)
            result.extend(buff['issues'])

        return result


    def issues(self):

        result = self.exec_query(SIT_ISSUES, SIT_FIELDS)
        issues = {}

        for issue in result:
            fields = issue['fields']
            ticket_id = list(map(str.strip, fields['summary'].split('|')))[0]

            issues[ticket_id] = {
                'components': [comp['name'] for comp in fields['components']],
                'expired_sla': 'N/A'
            }
            
            if fields['resolutiondate'] is not None:
                issues[ticket_id].update({'resolution_date': fields['resolutiondate']})

        return issues


    def expired_sla_issues(self):

        result = self.exec_query(EXPIRED_SLA_SIT_ISSUES, ['summary'])
        issues = {}

        for issue in result:
            fields = issue['fields']
            ticket_id = fields['summary']

            issues[ticket_id] = {
                'expired_sla': 'yes' 
            }

        return issues

######################################################
################ Elasticsearch settings ##############
######################################################
INDEX_NAME = 'support'
ELASTICSEARCH_HOST = 'elasticsearch'
ELASTICSEARCH_PORT = '9200'
ELASTICSEARCH_USER = 'elastic'
ELASTICSEARCH_PASSWD = 'changeme'


######################################################
#################### LESA settings ###################
######################################################

# LESA user info
SCREEN_NAME = 'screen.name'
TIME_ZONE = '-0300'

# Search parameters
START_MONTH = 0 # January == 0
START_DAY = 1
START_YEAR = 2017

#
# Sets the LESA region ID 
#
# American code:    42356488
# Australian code:  42442481
# Brazilian code:   42356516
# Chineese code:    42356502
# Global code:      70917309
# Hungarian code:   42356493
# Indian code:      42356498
# Japaneese code:   45637701
# N/A code:         78237012
# Spanish code:     42356507
REGION_ID = 42356516

######################################################
#################### JIRA settings ###################
###################################################### 

#
# Sets the support office.
# Available values:
# - APAC
# - Brazil
# - EU
# - Global
# - India
# - Japan
# - Spain
# - US
#
SUPPORT_OFFICE = 'Brazil'

#
# JIRA Authorization header.
# Enconde your 'user.name:password' in base64
#
LIFERAY_ISSUES_AUTORIZATION_HEADER = {
    'Authorization': 'Basic c2NyZWVuLm5hbWU6cGFzc3dvcmQ='
}

#
# Fetch all ticket in the same range configured by
# START_MONTH, START_DAY, START_YEAR in 'leasticket/lesa.py'
#
SIT_ISSUES = """
    project = SIT
    AND 'Support Office' = {}
    AND created >= '{}/{}/{} 00:00'
    """.format(SUPPORT_OFFICE, START_YEAR, (START_MONTH + 1), START_DAY)

#
# Fields to retrive from SIT issues.
#
SIT_FIELDS = ['component', 'resolutiondate', 'summary']

#
# Fetches all expired SLA open tickets.
#
EXPIRED_SLA_SIT_ISSUES = """
    (created <= -21d AND priority = Minor
    OR created <= -14d AND priority = Major
    OR created <= -7d AND priority = Critical)
    AND project = SIT
    AND 'Support Office' = {}
    AND NOT status IN (Closed, Reopened, Resolved, 'Resolved in Production', 'Solution Delivered')
    AND status WAS NOT IN (Closed, Reopened, Resolved, 'Resolved in Production', 'Solution Delivered')
    """.format(SUPPORT_OFFICE)
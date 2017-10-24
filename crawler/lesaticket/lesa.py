from datetime import date

# LESA user info
SCREEN_NAME = "screen.name"

# Search parameters
START_MONTH = 0 # January == 0
START_DAY = 1
START_YEAR = 2017
REGION_ID = 42356516 # Brazilian code
# American code:		42356488
# Australian code:  42442481
# Brazilian code:		42356516
# Chineese code:		42356502
# Global code:			70917309
# Hungarian code:		42356493
# Indian code:			42356498
# Japaneese code:		45637701
# N/A code:         78237012
# Spanish code:			42356507

class URLManager(object):

    def get_url(self, page=1):
        today = date.today()
        current_month = today.month - 1
        current_day = today.day
        current_year = today.year

        url = "https://web.liferay.com/web/{}/support?".format(SCREEN_NAME)
        params = {
            "&p_p_id=": "2_WAR_osbportlet",
            "&p_p_lifecycle=" : 0,
            "&p_p_state=" : "normal",
            "&p_p_mode=" : "view",
            "&p_p_col_id=" : "column-1",
            "&p_p_col_count=" : 1,
            "&_2_WAR_osbportlet_mvcPath=" : """%2Fsupport%2F2%2Fadvanced_search.jsp""",
            "&_2_WAR_osbportlet_searchTab=" : "tickets",
            "&_2_WAR_osbportlet_cur=" : page,
            "&_2_WAR_osbportlet_orderByCol=" : "create-date",
            "&_2_WAR_osbportlet_orderByType=" : "asc",
            "&_2_WAR_osbportlet_createDateGTMonth=" : START_MONTH,
            "&_2_WAR_osbportlet_createDateGTDay=" : START_DAY,
            "&_2_WAR_osbportlet_createDateGTYear=" : START_YEAR,
            "&_2_WAR_osbportlet_createDateLTMonth=" : current_month,
            "&_2_WAR_osbportlet_createDateLTDay=" : current_day,
            "&_2_WAR_osbportlet_createDateLTYear=" : current_year,
            "&_2_WAR_osbportlet_closedDateGTMonth=" : 0,
            "&_2_WAR_osbportlet_closedDateLTMonth=" : 0,
            "&_2_WAR_osbportlet_supportRegionIds=" : REGION_ID,
            "&_2_WAR_osbportlet_feedbackAvailable=" : "false"
        }

        url_params = ''.join(["{}{}".format(k, v) for k, v in params.items()])
        return "{}{}".format(url, url_params)


if __name__ == "__main__":
    print(URLManager().get_url())

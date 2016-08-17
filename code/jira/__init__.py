'''
Connect to Jira
'''
import json
from urllib2 import urlopen, Request
from urllib import quote

class Jira:

    def __init__(self, url, jql, authentication_string):
        self.query_url = url.rstrip('\r\n')
        self.authentication_string = authentication_string.rstrip('\r\n')
        self.jql = quote(jql.rstrip('\r\n'))
        self.data = {}
        self.critical_ticket = False

    def request(self):
        try:
            q = Request(self.query_url + self.jql)
            q.add_header('Authorization', self.authentication_string)
            page = urlopen(q ).read()
            page = page.decode('utf-8')
            self.data = json.loads(page)
            self.critical_tickets_check()
        except:
            self.data["total"] = 0
        
        
    def total_tickets(self):
        return int(self.data['total'])

    def critical_tickets_check(self):
        """(nul) -> bool
           returns True if there are any Critical tickets in the returned filter
        """
        self.critical_ticket = False
        for ticket in self.data["issues"]:
            if "priority" in ticket["fields"]:
                if ticket["fields"]["priority"]["name"] =="Critical":
                    self.critical_ticket = True
                    break


        

    def critical_tickets(self):
        return self.critical_ticket

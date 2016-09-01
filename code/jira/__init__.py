'''
Connect to Jira
'''
import json, urllib2
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
            q = urllib2.Request(self.query_url + self.jql)
            q.add_header('Authorization', 'Basic ' + self.authentication_string)
            page = urllib2.urlopen(q).read()
        except urllib2.HTTPError, e:
			print e.code
			print e.read()
			self.data["total"] = -1
        except:
			self.data["total"] = -2
				
        try:
            page = page.decode('utf-8')
        except:
			print("not UTF-8")
			
        try:
            self.data = json.loads(page)
        except:
			print("could not load data, error decoding")
			self.data["total"] = -2
			
        try:
            self.critical_tickets_check()
        except:
			print('Error checking for critical')
        
        
    def total_tickets(self):
        return int(self.data['total'])

    def critical_tickets_check(self):
        """(nul) -> bool
           returns True if there are any Critical tickets in the returned filter
        """
        self.critical_ticket = False
        if "issues" in self.data:
			for ticket in self.data["issues"]:
				if "priority" in ticket["fields"] and "name" in ticket["fields"]["priority"] and ticket["fields"]["priority"]["name"] == "Critical":
					self.critical_ticket = True
					break



        

    def critical_tickets(self):
        return self.critical_ticket
